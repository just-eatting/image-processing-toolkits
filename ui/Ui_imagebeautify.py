from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageBeautify(object):

    def setupUi(self, tabBeautify: QtWidgets.QWidget):
        tabBeautify.setObjectName("tabBeautify")
        self.tabBeautifyLayout = QtWidgets.QVBoxLayout(tabBeautify)
        self.tabBeautifyLayout.setObjectName("tabBeautifyLayout")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBeautifyLayout.addItem(spacerItem23)
        self.beautifyShowLayout = QtWidgets.QHBoxLayout()
        self.beautifyShowLayout.setObjectName("beautifyShowLayout")
        self.beautifyShowInputLayout = QtWidgets.QVBoxLayout()
        self.beautifyShowInputLayout.setObjectName("beautifyShowInputLayout")
        self.beautifyShowInputLabel = QtWidgets.QLabel(tabBeautify)
        self.beautifyShowInputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.beautifyShowInputLabel.setObjectName("beautifyShowInputLabel")
        self.beautifyShowInputLayout.addWidget(self.beautifyShowInputLabel)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowInputLayout.addItem(spacerItem24)
        self.beautifyShowInputImgLayout = QtWidgets.QHBoxLayout()
        self.beautifyShowInputImgLayout.setObjectName(
            "beautifyShowInputImgLayout")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowInputImgLayout.addItem(spacerItem25)
        self.beautifyShowInputImgScrollArea = QtWidgets.QScrollArea(
            tabBeautify)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beautifyShowInputImgScrollArea.
                                     sizePolicy().hasHeightForWidth())
        self.beautifyShowInputImgScrollArea.setSizePolicy(sizePolicy)
        self.beautifyShowInputImgScrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.beautifyShowInputImgScrollArea.setWidgetResizable(False)
        self.beautifyShowInputImgScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.beautifyShowInputImgScrollArea.setObjectName(
            "beautifyShowInputImgScrollArea")
        self.beautifyShowInputImgScrollAreaWidgetContents = QtWidgets.QWidget()
        self.beautifyShowInputImgScrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 321, 352))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.beautifyShowInputImgScrollAreaWidgetContents.sizePolicy(
            ).hasHeightForWidth())
        self.beautifyShowInputImgScrollAreaWidgetContents.setSizePolicy(
            sizePolicy)
        self.beautifyShowInputImgScrollAreaWidgetContents.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.beautifyShowInputImgScrollAreaWidgetContents.setObjectName(
            "beautifyShowInputImgScrollAreaWidgetContents")
        self.beautifyShowInputImgLabel = QtWidgets.QLabel(
            self.beautifyShowInputImgScrollAreaWidgetContents)
        self.beautifyShowInputImgLabel.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.beautifyShowInputImgLabel.setFont(font)
        self.beautifyShowInputImgLabel.setAutoFillBackground(False)
        self.beautifyShowInputImgLabel.setStyleSheet("")
        self.beautifyShowInputImgLabel.setLineWidth(1)
        self.beautifyShowInputImgLabel.setText("")
        self.beautifyShowInputImgLabel.setScaledContents(False)
        self.beautifyShowInputImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.beautifyShowInputImgLabel.setWordWrap(True)
        self.beautifyShowInputImgLabel.setObjectName(
            "beautifyShowInputImgLabel")
        self.beautifyShowInputImgScrollArea.setWidget(
            self.beautifyShowInputImgScrollAreaWidgetContents)
        self.beautifyShowInputImgLayout.addWidget(
            self.beautifyShowInputImgScrollArea)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowInputImgLayout.addItem(spacerItem26)
        self.beautifyShowInputImgLayout.setStretch(0, 1)
        self.beautifyShowInputImgLayout.setStretch(1, 3)
        self.beautifyShowInputImgLayout.setStretch(2, 1)
        self.beautifyShowInputLayout.addLayout(self.beautifyShowInputImgLayout)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowInputLayout.addItem(spacerItem27)
        self.beautifyShowInputButtonLayout = QtWidgets.QHBoxLayout()
        self.beautifyShowInputButtonLayout.setObjectName(
            "beautifyShowInputButtonLayout")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowInputButtonLayout.addItem(spacerItem28)
        self.beautifyShowInputButton = QtWidgets.QPushButton(tabBeautify)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.beautifyShowInputButton.setFont(font)
        self.beautifyShowInputButton.setObjectName("beautifyShowInputButton")
        self.beautifyShowInputButtonLayout.addWidget(
            self.beautifyShowInputButton)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowInputButtonLayout.addItem(spacerItem29)
        self.beautifyShowInputLayout.addLayout(
            self.beautifyShowInputButtonLayout)
        self.beautifyShowInputLayout.setStretch(2, 9)
        self.beautifyShowInputLayout.setStretch(4, 1)
        self.beautifyShowLayout.addLayout(self.beautifyShowInputLayout)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40,
                                             QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.Expanding)
        self.beautifyShowLayout.addItem(spacerItem30)
        self.beautifyShowOutputLayout = QtWidgets.QVBoxLayout()
        self.beautifyShowOutputLayout.setObjectName("beautifyShowOutputLayout")
        self.beautifyShowOutputLabel = QtWidgets.QLabel(tabBeautify)
        self.beautifyShowOutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.beautifyShowOutputLabel.setObjectName("beautifyShowOutputLabel")
        self.beautifyShowOutputLayout.addWidget(self.beautifyShowOutputLabel)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowOutputLayout.addItem(spacerItem31)
        self.beautifyShowOutputImgLayout = QtWidgets.QHBoxLayout()
        self.beautifyShowOutputImgLayout.setObjectName(
            "beautifyShowOutputImgLayout")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowOutputImgLayout.addItem(spacerItem32)
        self.beautifyShowOutputImgScrollArea = QtWidgets.QScrollArea(
            tabBeautify)
        self.beautifyShowOutputImgScrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.beautifyShowOutputImgScrollArea.setWidgetResizable(False)
        self.beautifyShowOutputImgScrollArea.setAlignment(
            QtCore.Qt.AlignCenter)
        self.beautifyShowOutputImgScrollArea.setObjectName(
            "beautifyShowOutputImgScrollArea")
        self.beautifyShowOutputImgScrollAreaWidgetContents = QtWidgets.QWidget(
        )
        self.beautifyShowOutputImgScrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 321, 352))
        self.beautifyShowOutputImgScrollAreaWidgetContents.setObjectName(
            "beautifyShowOutputImgScrollAreaWidgetContents")
        self.beautifyShowOutputImgLabel = QtWidgets.QLabel(
            self.beautifyShowOutputImgScrollAreaWidgetContents)
        self.beautifyShowOutputImgLabel.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.beautifyShowOutputImgLabel.setFont(font)
        self.beautifyShowOutputImgLabel.setStyleSheet("")
        self.beautifyShowOutputImgLabel.setLineWidth(1)
        self.beautifyShowOutputImgLabel.setText("")
        self.beautifyShowOutputImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.beautifyShowOutputImgLabel.setWordWrap(True)
        self.beautifyShowOutputImgLabel.setObjectName(
            "beautifyShowOutputImgLabel")
        self.beautifyShowOutputImgScrollArea.setWidget(
            self.beautifyShowOutputImgScrollAreaWidgetContents)
        self.beautifyShowOutputImgLayout.addWidget(
            self.beautifyShowOutputImgScrollArea)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowOutputImgLayout.addItem(spacerItem33)
        self.beautifyShowOutputImgLayout.setStretch(0, 1)
        self.beautifyShowOutputImgLayout.setStretch(1, 3)
        self.beautifyShowOutputImgLayout.setStretch(2, 1)
        self.beautifyShowOutputLayout.addLayout(
            self.beautifyShowOutputImgLayout)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowOutputLayout.addItem(spacerItem34)
        self.beautifyShowOutputButtonLayout = QtWidgets.QHBoxLayout()
        self.beautifyShowOutputButtonLayout.setObjectName(
            "beautifyShowOutputButtonLayout")
        spacerItem35 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowOutputButtonLayout.addItem(spacerItem35)
        self.beautifyShowOutputButton = QtWidgets.QPushButton(tabBeautify)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.beautifyShowOutputButton.setFont(font)
        self.beautifyShowOutputButton.setObjectName("beautifyShowOutputButton")
        self.beautifyShowOutputButtonLayout.addWidget(
            self.beautifyShowOutputButton)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyShowOutputButtonLayout.addItem(spacerItem36)
        self.beautifyShowOutputLayout.addLayout(
            self.beautifyShowOutputButtonLayout)
        self.beautifyShowOutputLayout.setStretch(2, 9)
        self.beautifyShowOutputLayout.setStretch(4, 1)
        self.beautifyShowLayout.addLayout(self.beautifyShowOutputLayout)
        self.tabBeautifyLayout.addLayout(self.beautifyShowLayout)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBeautifyLayout.addItem(spacerItem37)
        self.beautifyLine_1 = QtWidgets.QFrame(tabBeautify)
        self.beautifyLine_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.beautifyLine_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.beautifyLine_1.setObjectName("beautifyLine_1")
        self.tabBeautifyLayout.addWidget(self.beautifyLine_1)
        self.contrastLayout = QtWidgets.QHBoxLayout()
        self.contrastLayout.setObjectName("contrastLayout")
        self.contrastLabel = QtWidgets.QLabel(tabBeautify)
        self.contrastLabel.setObjectName("contrastLabel")
        self.contrastLayout.addWidget(self.contrastLabel)
        self.contrastSpinBox = QtWidgets.QDoubleSpinBox(tabBeautify)
        self.contrastSpinBox.setDecimals(2)
        self.contrastSpinBox.setMinimum(0.0)
        self.contrastSpinBox.setMaximum(2.0)
        self.contrastSpinBox.setSingleStep(0.1)
        self.contrastSpinBox.setProperty("value", 1.0)
        self.contrastSpinBox.setObjectName("contrastSpinBox")
        self.contrastLayout.addWidget(self.contrastSpinBox)
        self.contrastSlider = QtWidgets.QSlider(tabBeautify)
        self.contrastSlider.setMinimum(0)
        self.contrastSlider.setMaximum(200)
        self.contrastSlider.setSingleStep(10)
        self.contrastSlider.setPageStep(10)
        self.contrastSlider.setProperty("value", 100)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.contrastSlider.setTickInterval(0)
        self.contrastSlider.setObjectName("contrastSlider")
        self.contrastLayout.addWidget(self.contrastSlider)
        self.tabBeautifyLayout.addLayout(self.contrastLayout)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBeautifyLayout.addItem(spacerItem38)
        self.brightnessLayout = QtWidgets.QHBoxLayout()
        self.brightnessLayout.setObjectName("brightnessLayout")
        self.brightnessLabel = QtWidgets.QLabel(tabBeautify)
        self.brightnessLabel.setObjectName("brightnessLabel")
        self.brightnessLayout.addWidget(self.brightnessLabel)
        self.brightnessSpinBox = QtWidgets.QSpinBox(tabBeautify)
        self.brightnessSpinBox.setMinimum(-100)
        self.brightnessSpinBox.setMaximum(100)
        self.brightnessSpinBox.setSingleStep(1)
        self.brightnessSpinBox.setObjectName("brightnessSpinBox")
        self.brightnessLayout.addWidget(self.brightnessSpinBox)
        self.brightnessSlider = QtWidgets.QSlider(tabBeautify)
        self.brightnessSlider.setMinimum(-100)
        self.brightnessSlider.setMaximum(100)
        self.brightnessSlider.setSingleStep(10)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.brightnessSlider.setTickInterval(0)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.brightnessLayout.addWidget(self.brightnessSlider)
        self.tabBeautifyLayout.addLayout(self.brightnessLayout)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBeautifyLayout.addItem(spacerItem39)
        self.saturationLayout = QtWidgets.QHBoxLayout()
        self.saturationLayout.setObjectName("saturationLayout")
        self.saturationLabel = QtWidgets.QLabel(tabBeautify)
        self.saturationLabel.setObjectName("saturationLabel")
        self.saturationLayout.addWidget(self.saturationLabel)
        self.saturationSpinBox = QtWidgets.QSpinBox(tabBeautify)
        self.saturationSpinBox.setMinimum(-100)
        self.saturationSpinBox.setMaximum(100)
        self.saturationSpinBox.setSingleStep(1)
        self.saturationSpinBox.setProperty("value", 0)
        self.saturationSpinBox.setObjectName("saturationSpinBox")
        self.saturationLayout.addWidget(self.saturationSpinBox)
        self.saturationSlider = QtWidgets.QSlider(tabBeautify)
        self.saturationSlider.setMinimum(-100)
        self.saturationSlider.setMaximum(100)
        self.saturationSlider.setSingleStep(10)
        self.saturationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.saturationSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.saturationSlider.setTickInterval(0)
        self.saturationSlider.setObjectName("saturationSlider")
        self.saturationLayout.addWidget(self.saturationSlider)
        self.tabBeautifyLayout.addLayout(self.saturationLayout)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBeautifyLayout.addItem(spacerItem40)
        self.addlightingLayout = QtWidgets.QHBoxLayout()
        self.addlightingLayout.setObjectName("addlightingLayout")
        self.addlightingLabel = QtWidgets.QLabel(tabBeautify)
        self.addlightingLabel.setObjectName("addlightingLabel")
        self.addlightingLayout.addWidget(self.addlightingLabel)
        self.addlightingSpinBox = QtWidgets.QDoubleSpinBox(tabBeautify)
        self.addlightingSpinBox.setDecimals(2)
        self.addlightingSpinBox.setMinimum(0.0)
        self.addlightingSpinBox.setMaximum(2.0)
        self.addlightingSpinBox.setSingleStep(0.01)
        self.addlightingSpinBox.setProperty("value", 1.0)
        self.addlightingSpinBox.setObjectName("addlightingSpinBox")
        self.addlightingLayout.addWidget(self.addlightingSpinBox)
        self.addlightingSlider = QtWidgets.QSlider(tabBeautify)
        self.addlightingSlider.setMinimum(0)
        self.addlightingSlider.setMaximum(200)
        self.addlightingSlider.setSingleStep(10)
        self.addlightingSlider.setPageStep(10)
        self.addlightingSlider.setProperty("value", 100)
        self.addlightingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.addlightingSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.addlightingSlider.setTickInterval(0)
        self.addlightingSlider.setObjectName("addlightingSlider")
        self.addlightingLayout.addWidget(self.addlightingSlider)
        self.tabBeautifyLayout.addLayout(self.addlightingLayout)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBeautifyLayout.addItem(spacerItem41)
        self.beautifyCustomSizeLayout = QtWidgets.QHBoxLayout()
        self.beautifyCustomSizeLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.beautifyCustomSizeLayout.setSpacing(0)
        self.beautifyCustomSizeLayout.setObjectName("beautifyCustomSizeLayout")
        self.beautifyCustomSizeLabel = QtWidgets.QLabel(tabBeautify)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.beautifyCustomSizeLabel.setFont(font)
        self.beautifyCustomSizeLabel.setStyleSheet("")
        self.beautifyCustomSizeLabel.setObjectName("beautifyCustomSizeLabel")
        self.beautifyCustomSizeLayout.addWidget(self.beautifyCustomSizeLabel)
        self.beautifyCustomSizeWidthLayout = QtWidgets.QHBoxLayout()
        self.beautifyCustomSizeWidthLayout.setObjectName(
            "beautifyCustomSizeWidthLayout")
        self.beautifyCustomSizeWidthLabel = QtWidgets.QLabel(tabBeautify)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.beautifyCustomSizeWidthLabel.setFont(font)
        self.beautifyCustomSizeWidthLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
            | QtCore.Qt.AlignVCenter)
        self.beautifyCustomSizeWidthLabel.setObjectName(
            "beautifyCustomSizeWidthLabel")
        self.beautifyCustomSizeWidthLayout.addWidget(
            self.beautifyCustomSizeWidthLabel)
        self.beautifyCustomSizeWidthLineEdit = QtWidgets.QLineEdit(tabBeautify)
        self.beautifyCustomSizeWidthLineEdit.setObjectName(
            "beautifyCustomSizeWidthLineEdit")
        self.beautifyCustomSizeWidthLayout.addWidget(
            self.beautifyCustomSizeWidthLineEdit)
        self.beautifyCustomSizeLayout.addLayout(
            self.beautifyCustomSizeWidthLayout)
        self.beautifyCustomSizeHeightLayout = QtWidgets.QHBoxLayout()
        self.beautifyCustomSizeHeightLayout.setObjectName(
            "beautifyCustomSizeHeightLayout")
        self.beautifyCustomSizeHeightLabel = QtWidgets.QLabel(tabBeautify)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.beautifyCustomSizeHeightLabel.setFont(font)
        self.beautifyCustomSizeHeightLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
            | QtCore.Qt.AlignVCenter)
        self.beautifyCustomSizeHeightLabel.setObjectName(
            "beautifyCustomSizeHeightLabel")
        self.beautifyCustomSizeHeightLayout.addWidget(
            self.beautifyCustomSizeHeightLabel)
        self.beautifyCustomSizeHeightLineEdit = QtWidgets.QLineEdit(
            tabBeautify)
        self.beautifyCustomSizeHeightLineEdit.setObjectName(
            "beautifyCustomSizeHeightLineEdit")
        self.beautifyCustomSizeHeightLayout.addWidget(
            self.beautifyCustomSizeHeightLineEdit)
        self.beautifyCustomSizeLayout.addLayout(
            self.beautifyCustomSizeHeightLayout)
        spacerItem42 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyCustomSizeLayout.addItem(spacerItem42)
        self.beautifyCustomSizeButton = QtWidgets.QPushButton(tabBeautify)
        self.beautifyCustomSizeButton.setObjectName("beautifyCustomSizeButton")
        self.beautifyCustomSizeLayout.addWidget(self.beautifyCustomSizeButton)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyCustomSizeLayout.addItem(spacerItem43)
        self.beautifyResetSizeButton = QtWidgets.QPushButton(tabBeautify)
        self.beautifyResetSizeButton.setObjectName("beautifyResetSizeButton")
        self.beautifyCustomSizeLayout.addWidget(self.beautifyResetSizeButton)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.beautifyCustomSizeLayout.addItem(spacerItem44)
        self.beautifyCustomSizeLayout.setStretch(0, 2)
        self.beautifyCustomSizeLayout.setStretch(1, 1)
        self.beautifyCustomSizeLayout.setStretch(2, 1)
        self.beautifyCustomSizeLayout.setStretch(3, 1)
        self.beautifyCustomSizeLayout.setStretch(4, 3)
        self.beautifyCustomSizeLayout.setStretch(7, 16)
        self.tabBeautifyLayout.addLayout(self.beautifyCustomSizeLayout)
        self.beautifyLine_2 = QtWidgets.QFrame(tabBeautify)
        self.beautifyLine_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.beautifyLine_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.beautifyLine_2.setObjectName("beautifyLine_2")
        self.tabBeautifyLayout.addWidget(self.beautifyLine_2)

        QtCore.QMetaObject.connectSlotsByName(tabBeautify)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.beautifyShowInputLabel.setText(_translate("MainWindow", "原图"))
        self.beautifyShowInputButton.setText(_translate("MainWindow", "选择照片"))
        self.beautifyShowOutputLabel.setText(_translate("MainWindow", "结果图"))
        self.beautifyShowOutputButton.setText(_translate("MainWindow", "保存照片"))
        self.contrastLabel.setText(_translate("MainWindow", "对比度："))
        self.brightnessLabel.setText(_translate("MainWindow", "亮度："))
        self.saturationLabel.setText(_translate("MainWindow", "饱和度："))
        self.addlightingLabel.setText(_translate("MainWindow", "智能补光："))
        self.beautifyCustomSizeLabel.setText(_translate(
            "MainWindow", "自定义尺寸："))
        self.beautifyCustomSizeWidthLabel.setText(
            _translate("MainWindow", "宽(px)："))
        self.beautifyCustomSizeHeightLabel.setText(
            _translate("MainWindow", "高(px)："))
        self.beautifyCustomSizeButton.setText(_translate("MainWindow", "调整尺寸"))
        self.beautifyResetSizeButton.setText(_translate("MainWindow", "恢复原图"))
