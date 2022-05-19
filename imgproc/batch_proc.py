from enum import Enum
from math import floor
import os
from PyQt5.QtWidgets import QWidget, QFileDialog, QListWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt, QUrl
from PyQt5.QtGui import QDesktopServices
import cv2
from ui.Ui_batchproc import Ui_BatchProc

from utils import mat2qimage, show_tips, check_img_empty, generate_imagename


class ResizeType(Enum):
    default = 0
    range = 1
    size = 2
    scale = 3


class BatchProcesser(QWidget):

    def __init__(self):
        super().__init__()
        self._ui = Ui_BatchProc()
        self._ui.setupUi(self)

        self._src_path = ""
        self._dst_path = ""
        self._type = ResizeType.default
        self._min_size = 0
        self._max_size = 0
        self._scale = 1.0

    @pyqtSlot()
    def on_batchProcInputPathButton_clicked(self):
        folder = QFileDialog.getExistingDirectory(
            self, "打开文件夹", ".", QFileDialog.Option.ShowDirsOnly
            | QFileDialog.Option.DontResolveSymlinks)
        if len(folder) <= 0:
            show_tips(self, "打开文件夹失败！")
            return

        file_list = [
            filename for filename in os.listdir(folder)
            if filename.endswith((".jpg", ".png", ".jpeg"))
        ]
        self.show_files(file_list)
        self._src_path = folder
        self._ui.batchProcInputPathLineEdit.setText(folder)

    @pyqtSlot()
    def on_batchProcOutputPathButton_clicked(self):
        folder = QFileDialog.getExistingDirectory(
            self, "打开文件夹", ".", QFileDialog.Option.ShowDirsOnly
            | QFileDialog.Option.DontResolveSymlinks)
        if len(folder) <= 0:
            show_tips(self, "打开文件夹失败！")
            return

        self._dst_path = folder
        self._ui.batchProcOutputPathLineEdit.setText(folder)

    @pyqtSlot()
    def on_batchProcInputPathLineEdit_returnPressed(self):
        src_path = self._ui.batchProcInputPathLineEdit.text()
        if os.path.exists(src_path):
            file_list = [
                filename for filename in os.listdir(src_path)
                if filename.endswith((".jpg", ".png", ".jpeg"))
            ]
            self.show_files(file_list)
            self._src_path = src_path
            self._ui.batchProcInputPathLineEdit.setText(src_path)
        else:
            show_tips(self, "文件夹不存在！")

    @pyqtSlot()
    def on_batchProcOutputPathLineEdit_returnPressed(self):
        dst_path = self._ui.batchProcOutputPathLineEdit.text()
        os.makedirs(dst_path, exist_ok=True)
        self._dst_path = dst_path

    @pyqtSlot(QListWidgetItem)
    def on_batchProcShowFileListWidget_itemDoubleClicked(self):
        src = self._ui.batchProcShowFileListWidget
        dst = self._ui.batchProcShowProcessingListWidget
        item = src.currentItem()
        if len(dst.findItems(item.text(), Qt.MatchFlag.MatchFixedString)) <= 0:
            self._ui.batchProcShowProcessingListWidget.addItem(
                QListWidgetItem(item.text()))

    @pyqtSlot(QListWidgetItem)
    def on_batchProcShowProcessingListWidget_itemDoubleClicked(self):
        index = self._ui.batchProcShowProcessingListWidget.currentRow()
        self._ui.batchProcShowProcessingListWidget.takeItem(index)

    @pyqtSlot()
    def on_batchProcShowFileListSelectAllButton_clicked(self):
        src = self._ui.batchProcShowFileListWidget
        dst = self._ui.batchProcShowProcessingListWidget

        dst.clear()
        dst.addItems([src.item(i).text() for i in range(src.count())])

    @pyqtSlot()
    def on_batchProcShowFileListFlushButton_clicked(self):
        self._ui.batchProcShowFileListWidget.clear()
        src_path = self._ui.batchProcInputPathLineEdit.text()
        if os.path.exists(src_path):
            file_list = [
                filename for filename in os.listdir(src_path)
                if filename.endswith((".jpg", ".png", ".jpeg"))
            ]
            self.show_files(file_list)
            self._src_path = src_path
            self._ui.batchProcInputPathLineEdit.setText(src_path)
        else:
            show_tips(self, "文件夹不存在！")

    @pyqtSlot()
    def on_batchProcShowProcessingListCancelAllButton_clicked(self):
        self._ui.batchProcShowProcessingListWidget.clear()

    @pyqtSlot()
    def on_batchProcShowResultListClearButton_clicked(self):
        self._ui.batchProcShowResultListWidget.clear()

    @pyqtSlot()
    def on_batchProcShowResultListExplorerButton_clicked(self):
        path = self._ui.batchProcOutputPathLineEdit.text()
        path.replace("/", "\\")
        QDesktopServices.openUrl(QUrl("file:" + path))

    @pyqtSlot()
    def on_batchProcRangeTypeButton_clicked(self):
        self._type = ResizeType.range

    @pyqtSlot()
    def on_batchProcSizeTypeButton_clicked(self):
        self._type = ResizeType.size

    @pyqtSlot()
    def on_batchProcScaleTypeButton_clicked(self):
        self._type = ResizeType.scale

    @pyqtSlot()
    def on_batchProcDefaultTypeButton_clicked(self):
        self._type = ResizeType.default

    @pyqtSlot()
    def on_batchProcStartButton_clicked(self):
        if not self.check_params():
            return

        processing_list_widget = self._ui.batchProcShowProcessingListWidget
        count = processing_list_widget.count()
        for i in range(count):
            filename = processing_list_widget.item(i).text()
            if len(filename) > 0:
                src = cv2.imread(os.path.join(self._src_path, filename))
                dst = self.process(src)
                save_path = self.save_img(dst)

                item = QListWidgetItem("{}/{}-->{}".format(
                    self._src_path, filename, save_path))
                self._ui.batchProcShowResultListWidget.addItem(item)

        show_tips(self, "批处理完成，一共处理了{}张图片！".format(count))

    def process(self, src: cv2.Mat):
        if src is not None:
            if self._type == ResizeType.default:
                return src.copy()

            if self._type == ResizeType.size:
                return cv2.resize(src, (self._width, self._height))

            if self._type == ResizeType.range:
                max_edge = src.shape[
                    0] if src.shape[0] > src.shape[1] else src.shape[1]
                min_edge = src.shape[
                    1] if src.shape[0] > src.shape[1] else src.shape[0]

                if self._min_size <= 0:
                    self._scale = self._max_size / max_edge
                else:
                    self._scale = self._min_size / min_edge

                self._scale = self._max_size / max_edge if max_edge * self._scale > self._max_size else self._scale

            return cv2.resize(src, (floor(src.shape[1] * self._scale),
                                    floor(src.shape[0] * self._scale)))

    def show_files(self, files):
        self._ui.batchProcShowFileListWidget.clear()
        for file in files:
            item = QListWidgetItem(file)
            self._ui.batchProcShowFileListWidget.addItem(item)

    def check_params(self):
        processing_list_widget = self._ui.batchProcShowProcessingListWidget
        if processing_list_widget.count() <= 0:
            show_tips(self, "没有要处理的图片！")
            return False

        if len(self._src_path) <= 0 or len(self._dst_path) <= 0:
            show_tips(self, "没有指定源文件夹或目标文件夹！")
            return False

        min_size = self._ui.batchProcRangeMinLineEdit.text()
        max_size = self._ui.batchProcRangeMaxLineEdit.text()
        width = self._ui.batchProcSizeWidthLineEdit.text()
        height = self._ui.batchProcSizeHeightLineEdit.text()
        scale = self._ui.batchProcScaleSpinBox.value()
        if self._type == ResizeType.range:
            if len(min_size) <= 0 and len(max_size) <= 0:
                show_tips(self, "最大边和最小边至少要有一个不能为空！")
                return False

            if len(min_size) > 0:
                self._min_size = int(min_size)

            if len(max_size) > 0:
                self._max_size = int(max_size)

            if self._min_size <= 0 and self._max_size <= 0:
                show_tips(self, "最大边和最小边至少要有一个为正数！")
                return False

        if self._type == ResizeType.size:
            if len(width) <= 0 or len(height) <= 0:
                show_tips(self, "宽和高不能为空！")
                return False

            if int(width) <= 0 or int(height) <= 0:
                show_tips(self, "宽和高必须为正数！")
                return False

            self._width = int(width)
            self._height = int(height)

        if self._type == ResizeType.scale:
            self._scale = scale

        return True

    def save_img(self, img: cv2.Mat):
        if check_img_empty(self, img):
            return

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 生成图片名并获取保存图片的路径
        imagepath = os.path.join(os.curdir, generate_imagename())
        abs_img_path = os.path.join(self._dst_path, imagepath)

        # 将mat类型的图片转为Qimage并保存
        img = mat2qimage(img)
        if not img.save(abs_img_path):
            show_tips(self, "图片保存失败：{}".format(abs_img_path))

        return abs_img_path
