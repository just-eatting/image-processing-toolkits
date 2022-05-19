from math import floor
import os
import cv2

from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import pyqtSlot
from enum import Enum

import numpy as np
from ui.Ui_idphotogen import Ui_IdPhotoGen

from utils import mat2qimage, show_img_on_label, show_tips, generate_imagename, check_img_empty


class BgColor(Enum):
    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)


class IdPhotoGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self._ui = Ui_IdPhotoGen()
        self._ui.setupUi(self)

        self._input_img = None
        self._output_img = None
        self._bgcolor = BgColor.white

    @pyqtSlot()
    def on_idPhotoGenShowInputButton_clicked(self):
        # 选择图片路径
        imgpath, _ = QFileDialog.getOpenFileName(
            self, "打开图片", "./data", "Image Files(*.jpg *.png *.jpeg)")

        if len(imgpath) > 0:
            img = cv2.imread(imgpath)
            if check_img_empty(self, img):
                return

            # 调整图片适应窗口大小
            img_width = img.shape[1]
            img_height = img.shape[0]
            max_width = self._ui.idPhotoGenShowInputImgScrollAreaWidgetContents.width(
            )
            max_height = self._ui.idPhotoGenShowInputImgScrollAreaWidgetContents.height(
            )
            scale = img_height / max_height if img_height > max_height else 1.0
            scale = img_width / max_width if img_width / scale > max_width else scale
            new_width = floor(img_width / scale)
            new_height = floor(img_height / scale)

            img = cv2.resize(img, (new_width, new_height))

            # 转为RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # 显示图片
            qimg = mat2qimage(img)
            show_img_on_label(self._ui.idPhotoGenShowInputImgLabel, qimg)
            self._ui.idPhotoGenShowInputImgScrollAreaWidgetContents.adjustSize(
            )

            # 保存一下图片
            self._input_img = img

    @pyqtSlot()
    def on_idPhotoGenShowOutputButton_clicked(self):
        if check_img_empty(self, self._output_img):
            return

        # 生成图片名并获取保存图片的路径
        imagepath = os.path.join(os.curdir, generate_imagename())
        abs_img_path, _ = QFileDialog.getSaveFileName(
            self, "保存图片", imagepath, "Image Files(*.jpg *.png *.jpeg)")

        # 将mat类型的图片转为Qimage并保存
        img = mat2qimage(self._output_img)
        if img.save(abs_img_path):
            show_tips(self, "保存图片成功：{}".format(abs_img_path))
        else:
            show_tips(self, "图片保存失败：{}".format(abs_img_path))

    @pyqtSlot()
    def on_idPhotoGenParamsOptionalSizeOneInchSizeButton_clicked(self):
        self.set_photo_width_height("295", "413")

    @pyqtSlot()
    def on_idPhotoGenParamsOptionalSizeTwoInchSizeButton_clicked(self):
        self.set_photo_width_height("413", "579")

    @pyqtSlot()
    def on_idPhotoGenParamsColorWhiteButton_clicked(self):
        self._bgcolor = BgColor.white

    @pyqtSlot()
    def on_idPhotoGenParamsColorBlueButton_clicked(self):
        self._bgcolor = BgColor.blue

    @pyqtSlot()
    def on_idPhotoGenParamsColorRedButton_clicked(self):
        self._bgcolor = BgColor.red

    @pyqtSlot()
    def on_idPhotoGenPushButton_clicked(self):
        # 检查输入图片
        if check_img_empty(self, self._input_img):
            return

        # 检查参数
        if not self.check_params():
            return

        # 生成证件照
        idphoto = self.gen_idphoto()

        # 显示结果
        self.show_idphoto(idphoto)

        show_tips(self, "生成证件照成功！")

    def gen_idphoto(self):
        # 调整尺寸
        src = cv2.resize(self._input_img, (self._width, self._height))

        # 转为灰度图像
        dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

        # 使用OTSU自动计算阈值将灰度图像二值化
        _, dst = cv2.threshold(dst, 0, 255,
                               cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # 使用形态学开运算消除噪点
        kernel = np.ones((3, 3), np.uint8)
        dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel)

        # 获取图像轮廓
        contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

        # 为分水岭算法创建marker
        markers = np.zeros(dst.shape, dtype=np.int32)

        # 绘制前景
        cv2.drawContours(markers, contours, -1, 255, -1)

        # 绘制背景
        cv2.circle(markers, (5, 5), 3, 100, -1)

        # 执行分水岭算法，获得图像的前景和背景
        markers = cv2.watershed(src, markers)
        markers = np.uint8(markers)

        # 填充背景
        dst = np.zeros(src.shape, np.uint8)
        dst[markers == 255] = src[markers == 255]
        dst[markers != 255] = self._bgcolor.value

        # 保存一下输出图像
        self._output_img = dst

        return dst

    def show_idphoto(self, idphoto=None):
        if idphoto is None:
            idphoto = self._output_img

        idphoto = mat2qimage(idphoto)
        show_img_on_label(self._ui.idPhotoGenShowOutputImgLabel, idphoto)
        self._ui.idPhotoGenShowOutputImgScrollAreaWidgetContents.adjustSize()

    def check_params(self):
        width = self._ui.idPhotoGenParamsCustomSizeWidthLineEdit.text()
        height = self._ui.idPhotoGenParamsCustomSizeHeightLineEdit.text()
        if len(width) <= 0 or len(height) <= 0:
            show_tips(self, "请指定证件照的宽和高！")
            return False

        if int(width) <= 0 or int(height) <= 0:
            show_tips(self, "证件照的宽和高必须为正数！")
            return False

        self._width = int(width)
        self._height = int(height)

        return True

    def set_photo_width_height(self, width: str, height: str):
        self._ui.idPhotoGenParamsCustomSizeWidthLineEdit.setText(width)
        self._ui.idPhotoGenParamsCustomSizeHeightLineEdit.setText(height)
