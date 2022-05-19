from math import floor
import os
import cv2

import numpy as np

from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import pyqtSlot
from ui.Ui_imagebeautify import Ui_ImageBeautify

from utils import mat2qimage, show_img_on_label, show_tips, check_img_empty, generate_imagename


class ImageBeautifier(QWidget):

    def __init__(self):
        super().__init__()
        self._ui = Ui_ImageBeautify()
        self._ui.setupUi(self)

        self._input_img = None
        self._output_img = None

        self._contrast = 1.0
        self._brightness = 0
        self._saturation = 0
        self._gamma = 1.0

    @pyqtSlot()
    def on_beautifyShowInputButton_clicked(self):
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
            max_width = self._ui.beautifyShowInputImgScrollAreaWidgetContents.width(
            )
            max_height = self._ui.beautifyShowInputImgScrollAreaWidgetContents.height(
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
            show_img_on_label(self._ui.beautifyShowInputImgLabel, qimg)
            self._ui.beautifyShowInputImgScrollAreaWidgetContents.adjustSize()

            # 保存一下图片
            self._input_img = img

    @pyqtSlot()
    def on_beautifyShowOutputButton_clicked(self):
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

    @pyqtSlot(int)
    def on_contrastSlider_valueChanged(self):
        val = self._ui.contrastSlider.value() / 100
        self._ui.contrastSpinBox.setValue(val)
        self._contrast = val

        if self._input_img is not None:
            self.contrast_beautify()

    @pyqtSlot(int)
    def on_brightnessSlider_valueChanged(self):
        val = self._ui.brightnessSlider.value()
        self._ui.brightnessSpinBox.setValue(val)
        self._brightness = val

        if self._input_img is not None:
            self.brightness_beautify()

    @pyqtSlot(int)
    def on_saturationSlider_valueChanged(self):
        val = self._ui.saturationSlider.value()
        self._ui.saturationSpinBox.setValue(val)
        self._saturation = val

        if self._input_img is not None:
            self.saturation_beautify()

    @pyqtSlot(int)
    def on_addlightingSlider_valueChanged(self):
        val = self._ui.addlightingSlider.value() / 100
        self._ui.addlightingSpinBox.setValue(val)
        self._gamma = 2 - val

        if self._input_img is not None:
            self.gamma_beautify()

    @pyqtSlot(float)
    def on_contrastSpinBox_valueChanged(self):
        val = self._ui.contrastSpinBox.value()
        self._ui.contrastSlider.setValue(val * 100)
        self._contrast = val

        if self._input_img is not None:
            self.contrast_beautify()

    @pyqtSlot(float)
    def on_brightnessSpinBox_valueChanged(self):
        val = self._ui.brightnessSpinBox.value()
        self._ui.brightnessSlider.setValue(val)
        self._brightness = val

        if self._input_img is not None:
            self.brightness_beautify()

    @pyqtSlot(int)
    def on_saturationSpinBox_valueChanged(self):
        val = self._ui.saturationSpinBox.value()
        self._ui.saturationSlider.setValue(val)
        self._saturation = val

        if self._input_img is not None:
            self.saturation_beautify()

    @pyqtSlot(float)
    def on_addlightingSpinBox_valueChanged(self):
        val = self._ui.addlightingSpinBox.value()
        self._ui.addlightingSlider.setValue(val * 100)
        self._gamma = 2 - val

        if self._input_img is not None:
            self.gamma_beautify()

    @pyqtSlot(str)
    def on_contrastSpinBox_textChanged(self):
        val = self._ui.contrastSpinBox.value()
        self._ui.contrastSlider.setValue(val * 100)
        self._contrast = val

        if self._input_img is not None:
            self.contrast_beautify()

    @pyqtSlot(str)
    def on_brightnessSpinBox_textChanged(self):
        val = self._ui.brightnessSpinBox.value()
        self._ui.brightnessSlider.setValue(val)
        self._brightness = val

        if self._input_img is not None:
            self.brightness_beautify()

    @pyqtSlot(str)
    def on_saturationSpinBox_textChanged(self):
        val = self._ui.saturationSpinBox.value()
        self._ui.saturationSlider.setValue(val)
        self._saturation = val

        if self._input_img is not None:
            self.saturation_beautify()

    @pyqtSlot(str)
    def on_addlightingSpinBox_textChanged(self):
        val = self._ui.addlightingSpinBox.value()
        self._ui.addlightingSlider.setValue(val * 100)
        self._gamma = 2 - val

        if self._input_img is not None:
            self.gamma_beautify()

    @pyqtSlot()
    def on_beautifyCustomSizeButton_clicked(self):
        # 检查输入图片
        if check_img_empty(self, self._input_img):
            return

        # 检查参数
        if not self.check_params():
            return

        self.size_beautify()
        self.show_beautiful_image()

    @pyqtSlot()
    def on_beautifyResetSizeButton_clicked(self):
        # 检查输入图片
        if check_img_empty(self, self._input_img):
            return

        self.size_reset()
        self.show_beautiful_image()

    def contrast_beautify(self):
        self._linear_beautify(self._contrast, 0)
        self.show_beautiful_image()

    def brightness_beautify(self):
        self._linear_beautify(1.0, self._brightness)
        self.show_beautiful_image()

    def saturation_beautify(self):
        self._output_img = cv2.cvtColor(self._input_img, cv2.COLOR_RGB2HSV)
        lookup_table = np.array([
            ImageBeautifier.check_range(i + self._saturation)
            for i in range(0, 256)
        ], np.uint8)
        s_channel = cv2.LUT(self._output_img[:, :, 1], lookup_table)
        self._output_img[:, :, 1] = s_channel
        self._output_img = cv2.cvtColor(self._output_img, cv2.COLOR_HSV2RGB)

        self.show_beautiful_image()

    def gamma_beautify(self):
        lookup_table = np.array([
            ImageBeautifier.check_range(pow(i / 255.0, self._gamma) * 255.0)
            for i in range(0, 256)
        ], np.uint8)
        self._output_img = cv2.LUT(self._input_img, lookup_table)

        self.show_beautiful_image()

    def size_beautify(self):
        self._output_img = cv2.resize(self._input_img,
                                      (self._width, self._height))

    def size_reset(self):
        self._output_img = self._input_img.copy()

    def _linear_beautify(self, alpha: float, beta: int):
        lookup_table = np.array([
            ImageBeautifier.check_range(alpha * i + beta)
            for i in range(0, 256)
        ], np.uint8)
        self._output_img = cv2.LUT(self._input_img, lookup_table)

    def show_beautiful_image(self, beautiful_image=None):
        if beautiful_image is None:
            beautiful_image = self._output_img

        beautiful_image = mat2qimage(beautiful_image)
        show_img_on_label(self._ui.beautifyShowOutputImgLabel, beautiful_image)
        self._ui.beautifyShowOutputImgScrollAreaWidgetContents.adjustSize()

    def check_params(self):
        width = self._ui.beautifyCustomSizeWidthLineEdit.text()
        height = self._ui.beautifyCustomSizeHeightLineEdit.text()
        if len(width) <= 0 or len(height) <= 0:
            show_tips(self, "请指定宽和高！")
            return False

        if int(width) <= 0 or int(height) <= 0:
            show_tips(self, "宽和高必须为正数！")
            return False

        self._width = int(width)
        self._height = int(height)

        return True

    @staticmethod
    def check_range(check_value: int,
                    min_value: int = 0,
                    max_value: int = 255):
        check_value = min_value if check_value < min_value else check_value
        check_value = max_value if check_value > max_value else check_value

        return check_value