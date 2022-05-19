from PyQt5.QtWidgets import QMainWindow
from ui.Ui_mainwindow import Ui_MainWindow

from .batch_proc import BatchProcesser
from .idphoto_gen import IdPhotoGenerator
from .image_beautify import ImageBeautifier


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.id_photo_generator = IdPhotoGenerator()
        self.image_beautifier = ImageBeautifier()
        self.batch_processer = BatchProcesser()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
