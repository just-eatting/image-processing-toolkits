import cv2
import numpy as np

from PyQt5.QtWidgets import QLabel, QMessageBox, QWidget
from PyQt5.QtGui import QImage, QPixmap


def mat2qimage(img: cv2.Mat) -> QImage:
    img = img.astype(np.uint8)
    if len(img.shape) == 2 or img.shape[2] == 1:
        qimg = QImage(img.data, img.shape[1], img.shape[0], img.shape[1],
                      QImage.Format.Format_Grayscale8)
    if len(img.shape) == 3:
        qimg = QImage(img.data, img.shape[1], img.shape[0],
                      img.shape[2] * img.shape[1], QImage.Format.Format_RGB888)

    return qimg


def show_img_on_label(label: QLabel, img: QImage) -> None:
    label.setPixmap(QPixmap.fromImage(img))
    label.adjustSize()


def show_tips(widget: QWidget, text: str, title: str = "操作提示") -> None:
    QMessageBox.information(widget, title, text)


def check_img_empty(widget: QWidget, img: cv2.Mat):
    if img is None:
        show_tips(widget, "读取图片失败！")
        return True

    return False