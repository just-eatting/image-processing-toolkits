from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IdPhotoGen(object):

    def setupUi(self, tabIdPhotoGen: QtWidgets.QWidget):
        tabIdPhotoGen.setObjectName("tabIdPhotoGen")
        self.tabIdPhotoGenLayout = QtWidgets.QVBoxLayout(tabIdPhotoGen)
        self.tabIdPhotoGenLayout.setObjectName("tabIdPhotoGenLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.tabIdPhotoGenLayout.addItem(spacerItem)
        self.idPhotoGenShowLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenShowLayout.setObjectName("idPhotoGenShowLayout")
        self.idPhotoGenShowInputLayout = QtWidgets.QVBoxLayout()
        self.idPhotoGenShowInputLayout.setObjectName(
            "idPhotoGenShowInputLayout")
        self.idPhotoGenShowInputLabel = QtWidgets.QLabel(tabIdPhotoGen)
        self.idPhotoGenShowInputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.idPhotoGenShowInputLabel.setObjectName("idPhotoGenShowInputLabel")
        self.idPhotoGenShowInputLayout.addWidget(self.idPhotoGenShowInputLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowInputLayout.addItem(spacerItem1)
        self.idPhotoGenShowInputImgLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenShowInputImgLayout.setObjectName(
            "idPhotoGenShowInputImgLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowInputImgLayout.addItem(spacerItem2)
        self.idPhotoGenShowInputImgScrollArea = QtWidgets.QScrollArea(
            tabIdPhotoGen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idPhotoGenShowInputImgScrollArea.
                                     sizePolicy().hasHeightForWidth())
        self.idPhotoGenShowInputImgScrollArea.setSizePolicy(sizePolicy)
        self.idPhotoGenShowInputImgScrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.idPhotoGenShowInputImgScrollArea.setWidgetResizable(False)
        self.idPhotoGenShowInputImgScrollArea.setAlignment(
            QtCore.Qt.AlignCenter)
        self.idPhotoGenShowInputImgScrollArea.setObjectName(
            "idPhotoGenShowInputImgScrollArea")
        self.idPhotoGenShowInputImgScrollAreaWidgetContents = QtWidgets.QWidget(
        )
        self.idPhotoGenShowInputImgScrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 321, 352))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.idPhotoGenShowInputImgScrollAreaWidgetContents.sizePolicy(
            ).hasHeightForWidth())
        self.idPhotoGenShowInputImgScrollAreaWidgetContents.setSizePolicy(
            sizePolicy)
        self.idPhotoGenShowInputImgScrollAreaWidgetContents.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.idPhotoGenShowInputImgScrollAreaWidgetContents.setObjectName(
            "idPhotoGenShowInputImgScrollAreaWidgetContents")
        self.idPhotoGenShowInputImgLabel = QtWidgets.QLabel(
            self.idPhotoGenShowInputImgScrollAreaWidgetContents)
        self.idPhotoGenShowInputImgLabel.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.idPhotoGenShowInputImgLabel.setFont(font)
        self.idPhotoGenShowInputImgLabel.setAutoFillBackground(False)
        self.idPhotoGenShowInputImgLabel.setStyleSheet("")
        self.idPhotoGenShowInputImgLabel.setLineWidth(1)
        self.idPhotoGenShowInputImgLabel.setText("")
        self.idPhotoGenShowInputImgLabel.setScaledContents(False)
        self.idPhotoGenShowInputImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.idPhotoGenShowInputImgLabel.setWordWrap(True)
        self.idPhotoGenShowInputImgLabel.setObjectName(
            "idPhotoGenShowInputImgLabel")
        self.idPhotoGenShowInputImgScrollArea.setWidget(
            self.idPhotoGenShowInputImgScrollAreaWidgetContents)
        self.idPhotoGenShowInputImgLayout.addWidget(
            self.idPhotoGenShowInputImgScrollArea)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowInputImgLayout.addItem(spacerItem3)
        self.idPhotoGenShowInputImgLayout.setStretch(0, 1)
        self.idPhotoGenShowInputImgLayout.setStretch(1, 3)
        self.idPhotoGenShowInputImgLayout.setStretch(2, 1)
        self.idPhotoGenShowInputLayout.addLayout(
            self.idPhotoGenShowInputImgLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowInputLayout.addItem(spacerItem4)
        self.idPhotoGenShowInputButtonLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenShowInputButtonLayout.setObjectName(
            "idPhotoGenShowInputButtonLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowInputButtonLayout.addItem(spacerItem5)
        self.idPhotoGenShowInputButton = QtWidgets.QPushButton(tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.idPhotoGenShowInputButton.setFont(font)
        self.idPhotoGenShowInputButton.setObjectName(
            "idPhotoGenShowInputButton")
        self.idPhotoGenShowInputButtonLayout.addWidget(
            self.idPhotoGenShowInputButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowInputButtonLayout.addItem(spacerItem6)
        self.idPhotoGenShowInputLayout.addLayout(
            self.idPhotoGenShowInputButtonLayout)
        self.idPhotoGenShowInputLayout.setStretch(2, 9)
        self.idPhotoGenShowInputLayout.setStretch(4, 1)
        self.idPhotoGenShowLayout.addLayout(self.idPhotoGenShowInputLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.idPhotoGenShowLayout.addItem(spacerItem7)
        self.idPhotoGenShowOutputLayout = QtWidgets.QVBoxLayout()
        self.idPhotoGenShowOutputLayout.setObjectName(
            "idPhotoGenShowOutputLayout")
        self.idPhotoGenShowOutputLabel = QtWidgets.QLabel(tabIdPhotoGen)
        self.idPhotoGenShowOutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.idPhotoGenShowOutputLabel.setObjectName(
            "idPhotoGenShowOutputLabel")
        self.idPhotoGenShowOutputLayout.addWidget(
            self.idPhotoGenShowOutputLabel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowOutputLayout.addItem(spacerItem8)
        self.idPhotoGenShowOutputImgLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenShowOutputImgLayout.setObjectName(
            "idPhotoGenShowOutputImgLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowOutputImgLayout.addItem(spacerItem9)
        self.idPhotoGenShowOutputImgScrollArea = QtWidgets.QScrollArea(
            tabIdPhotoGen)
        self.idPhotoGenShowOutputImgScrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.idPhotoGenShowOutputImgScrollArea.setWidgetResizable(False)
        self.idPhotoGenShowOutputImgScrollArea.setAlignment(
            QtCore.Qt.AlignCenter)
        self.idPhotoGenShowOutputImgScrollArea.setObjectName(
            "idPhotoGenShowOutputImgScrollArea")
        self.idPhotoGenShowOutputImgScrollAreaWidgetContents = QtWidgets.QWidget(
        )
        self.idPhotoGenShowOutputImgScrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 321, 352))
        self.idPhotoGenShowOutputImgScrollAreaWidgetContents.setObjectName(
            "idPhotoGenShowOutputImgScrollAreaWidgetContents")
        self.idPhotoGenShowOutputImgLabel = QtWidgets.QLabel(
            self.idPhotoGenShowOutputImgScrollAreaWidgetContents)
        self.idPhotoGenShowOutputImgLabel.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.idPhotoGenShowOutputImgLabel.setFont(font)
        self.idPhotoGenShowOutputImgLabel.setStyleSheet("")
        self.idPhotoGenShowOutputImgLabel.setLineWidth(1)
        self.idPhotoGenShowOutputImgLabel.setText("")
        self.idPhotoGenShowOutputImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.idPhotoGenShowOutputImgLabel.setWordWrap(True)
        self.idPhotoGenShowOutputImgLabel.setObjectName(
            "idPhotoGenShowOutputImgLabel")
        self.idPhotoGenShowOutputImgScrollArea.setWidget(
            self.idPhotoGenShowOutputImgScrollAreaWidgetContents)
        self.idPhotoGenShowOutputImgLayout.addWidget(
            self.idPhotoGenShowOutputImgScrollArea)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowOutputImgLayout.addItem(spacerItem10)
        self.idPhotoGenShowOutputImgLayout.setStretch(0, 1)
        self.idPhotoGenShowOutputImgLayout.setStretch(1, 3)
        self.idPhotoGenShowOutputImgLayout.setStretch(2, 1)
        self.idPhotoGenShowOutputLayout.addLayout(
            self.idPhotoGenShowOutputImgLayout)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowOutputLayout.addItem(spacerItem11)
        self.idPhotoGenShowOutputButtonLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenShowOutputButtonLayout.setObjectName(
            "idPhotoGenShowOutputButtonLayout")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowOutputButtonLayout.addItem(spacerItem12)
        self.idPhotoGenShowOutputButton = QtWidgets.QPushButton(tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.idPhotoGenShowOutputButton.setFont(font)
        self.idPhotoGenShowOutputButton.setObjectName(
            "idPhotoGenShowOutputButton")
        self.idPhotoGenShowOutputButtonLayout.addWidget(
            self.idPhotoGenShowOutputButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenShowOutputButtonLayout.addItem(spacerItem13)
        self.idPhotoGenShowOutputLayout.addLayout(
            self.idPhotoGenShowOutputButtonLayout)
        self.idPhotoGenShowOutputLayout.setStretch(2, 9)
        self.idPhotoGenShowOutputLayout.setStretch(4, 1)
        self.idPhotoGenShowLayout.addLayout(self.idPhotoGenShowOutputLayout)
        self.tabIdPhotoGenLayout.addLayout(self.idPhotoGenShowLayout)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabIdPhotoGenLayout.addItem(spacerItem14)
        self.idPhotoGenLine_1 = QtWidgets.QFrame(tabIdPhotoGen)
        self.idPhotoGenLine_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.idPhotoGenLine_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.idPhotoGenLine_1.setObjectName("idPhotoGenLine_1")
        self.tabIdPhotoGenLayout.addWidget(self.idPhotoGenLine_1)
        self.idPhotoGenParamsLayout = QtWidgets.QVBoxLayout()
        self.idPhotoGenParamsLayout.setObjectName("idPhotoGenParamsLayout")
        self.idPhotoGenParamsSizeLayout = QtWidgets.QVBoxLayout()
        self.idPhotoGenParamsSizeLayout.setObjectName(
            "idPhotoGenParamsSizeLayout")
        self.idPhotoGenParamsOptionalSizeLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenParamsOptionalSizeLayout.setObjectName(
            "idPhotoGenParamsOptionalSizeLayout")
        self.idPhotoGenParamsOptionalSizeLabel = QtWidgets.QLabel(
            tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.idPhotoGenParamsOptionalSizeLabel.setFont(font)
        self.idPhotoGenParamsOptionalSizeLabel.setAlignment(
            QtCore.Qt.AlignCenter)
        self.idPhotoGenParamsOptionalSizeLabel.setObjectName(
            "idPhotoGenParamsOptionalSizeLabel")
        self.idPhotoGenParamsOptionalSizeLayout.addWidget(
            self.idPhotoGenParamsOptionalSizeLabel)
        self.idPhotoGenParamsOptionalSizeOneInchSizeButton = QtWidgets.QPushButton(
            tabIdPhotoGen)
        self.idPhotoGenParamsOptionalSizeOneInchSizeButton.setObjectName(
            "idPhotoGenParamsOptionalSizeOneInchSizeButton")
        self.idPhotoGenParamsOptionalSizeLayout.addWidget(
            self.idPhotoGenParamsOptionalSizeOneInchSizeButton)
        self.idPhotoGenParamsOptionalSizeTwoInchSizeButton = QtWidgets.QPushButton(
            tabIdPhotoGen)
        self.idPhotoGenParamsOptionalSizeTwoInchSizeButton.setObjectName(
            "idPhotoGenParamsOptionalSizeTwoInchSizeButton")
        self.idPhotoGenParamsOptionalSizeLayout.addWidget(
            self.idPhotoGenParamsOptionalSizeTwoInchSizeButton)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenParamsOptionalSizeLayout.addItem(spacerItem15)
        self.idPhotoGenParamsSizeLayout.addLayout(
            self.idPhotoGenParamsOptionalSizeLayout)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenParamsSizeLayout.addItem(spacerItem16)
        self.idPhotoGenParamsCustomSizeLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenParamsCustomSizeLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.idPhotoGenParamsCustomSizeLayout.setSpacing(0)
        self.idPhotoGenParamsCustomSizeLayout.setObjectName(
            "idPhotoGenParamsCustomSizeLayout")
        self.idPhotoGenParamsCustomSizeLabel = QtWidgets.QLabel(tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.idPhotoGenParamsCustomSizeLabel.setFont(font)
        self.idPhotoGenParamsCustomSizeLabel.setStyleSheet("")
        self.idPhotoGenParamsCustomSizeLabel.setObjectName(
            "idPhotoGenParamsCustomSizeLabel")
        self.idPhotoGenParamsCustomSizeLayout.addWidget(
            self.idPhotoGenParamsCustomSizeLabel)
        self.idPhotoGenParamsCustomSizeWidthLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenParamsCustomSizeWidthLayout.setObjectName(
            "idPhotoGenParamsCustomSizeWidthLayout")
        self.idPhotoGenParamsCustomSizeWidthLabel = QtWidgets.QLabel(
            tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.idPhotoGenParamsCustomSizeWidthLabel.setFont(font)
        self.idPhotoGenParamsCustomSizeWidthLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
            | QtCore.Qt.AlignVCenter)
        self.idPhotoGenParamsCustomSizeWidthLabel.setObjectName(
            "idPhotoGenParamsCustomSizeWidthLabel")
        self.idPhotoGenParamsCustomSizeWidthLayout.addWidget(
            self.idPhotoGenParamsCustomSizeWidthLabel)
        self.idPhotoGenParamsCustomSizeWidthLineEdit = QtWidgets.QLineEdit(
            tabIdPhotoGen)
        self.idPhotoGenParamsCustomSizeWidthLineEdit.setObjectName(
            "idPhotoGenParamsCustomSizeWidthLineEdit")
        self.idPhotoGenParamsCustomSizeWidthLayout.addWidget(
            self.idPhotoGenParamsCustomSizeWidthLineEdit)
        self.idPhotoGenParamsCustomSizeLayout.addLayout(
            self.idPhotoGenParamsCustomSizeWidthLayout)
        self.idPhotoGenParamsCustomSizeHeightLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenParamsCustomSizeHeightLayout.setObjectName(
            "idPhotoGenParamsCustomSizeHeightLayout")
        self.idPhotoGenParamsCustomSizeHeightLabel = QtWidgets.QLabel(
            tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.idPhotoGenParamsCustomSizeHeightLabel.setFont(font)
        self.idPhotoGenParamsCustomSizeHeightLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
            | QtCore.Qt.AlignVCenter)
        self.idPhotoGenParamsCustomSizeHeightLabel.setObjectName(
            "idPhotoGenParamsCustomSizeHeightLabel")
        self.idPhotoGenParamsCustomSizeHeightLayout.addWidget(
            self.idPhotoGenParamsCustomSizeHeightLabel)
        self.idPhotoGenParamsCustomSizeHeightLineEdit = QtWidgets.QLineEdit(
            tabIdPhotoGen)
        self.idPhotoGenParamsCustomSizeHeightLineEdit.setObjectName(
            "idPhotoGenParamsCustomSizeHeightLineEdit")
        self.idPhotoGenParamsCustomSizeHeightLayout.addWidget(
            self.idPhotoGenParamsCustomSizeHeightLineEdit)
        self.idPhotoGenParamsCustomSizeLayout.addLayout(
            self.idPhotoGenParamsCustomSizeHeightLayout)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenParamsCustomSizeLayout.addItem(spacerItem17)
        self.idPhotoGenParamsCustomSizeLayout.setStretch(0, 2)
        self.idPhotoGenParamsCustomSizeLayout.setStretch(1, 1)
        self.idPhotoGenParamsCustomSizeLayout.setStretch(2, 1)
        self.idPhotoGenParamsCustomSizeLayout.setStretch(3, 16)
        self.idPhotoGenParamsSizeLayout.addLayout(
            self.idPhotoGenParamsCustomSizeLayout)
        self.idPhotoGenParamsSizeLayout.setStretch(0, 9)
        self.idPhotoGenParamsSizeLayout.setStretch(2, 1)
        self.idPhotoGenParamsLayout.addLayout(self.idPhotoGenParamsSizeLayout)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenParamsLayout.addItem(spacerItem18)
        self.idPhotoGenParamsColorLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenParamsColorLayout.setObjectName(
            "idPhotoGenParamsColorLayout")
        self.idPhotoGenParamsColorLabel = QtWidgets.QLabel(tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.idPhotoGenParamsColorLabel.setFont(font)
        self.idPhotoGenParamsColorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.idPhotoGenParamsColorLabel.setObjectName(
            "idPhotoGenParamsColorLabel")
        self.idPhotoGenParamsColorLayout.addWidget(
            self.idPhotoGenParamsColorLabel)
        self.idPhotoGenParamsColorWhiteButton = QtWidgets.QRadioButton(
            tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.idPhotoGenParamsColorWhiteButton.setFont(font)
        self.idPhotoGenParamsColorWhiteButton.setChecked(True)
        self.idPhotoGenParamsColorWhiteButton.setObjectName(
            "idPhotoGenParamsColorWhiteButton")
        self.idPhotoGenParamsColorLayout.addWidget(
            self.idPhotoGenParamsColorWhiteButton)
        self.idPhotoGenParamsColorBlueButton = QtWidgets.QRadioButton(
            tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.idPhotoGenParamsColorBlueButton.setFont(font)
        self.idPhotoGenParamsColorBlueButton.setObjectName(
            "idPhotoGenParamsColorBlueButton")
        self.idPhotoGenParamsColorLayout.addWidget(
            self.idPhotoGenParamsColorBlueButton)
        self.idPhotoGenParamsColorRedButton = QtWidgets.QRadioButton(
            tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.idPhotoGenParamsColorRedButton.setFont(font)
        self.idPhotoGenParamsColorRedButton.setObjectName(
            "idPhotoGenParamsColorRedButton")
        self.idPhotoGenParamsColorLayout.addWidget(
            self.idPhotoGenParamsColorRedButton)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenParamsColorLayout.addItem(spacerItem19)
        self.idPhotoGenParamsLayout.addLayout(self.idPhotoGenParamsColorLayout)
        self.idPhotoGenParamsLayout.setStretch(0, 1)
        self.tabIdPhotoGenLayout.addLayout(self.idPhotoGenParamsLayout)
        self.idPhotoGenLine_2 = QtWidgets.QFrame(tabIdPhotoGen)
        self.idPhotoGenLine_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.idPhotoGenLine_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.idPhotoGenLine_2.setObjectName("idPhotoGenLine_2")
        self.tabIdPhotoGenLayout.addWidget(self.idPhotoGenLine_2)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabIdPhotoGenLayout.addItem(spacerItem20)
        self.idPhotoGenPushLayout = QtWidgets.QHBoxLayout()
        self.idPhotoGenPushLayout.setSpacing(36)
        self.idPhotoGenPushLayout.setObjectName("idPhotoGenPushLayout")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenPushLayout.addItem(spacerItem21)
        self.idPhotoGenPushButton = QtWidgets.QPushButton(tabIdPhotoGen)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.idPhotoGenPushButton.setFont(font)
        self.idPhotoGenPushButton.setObjectName("idPhotoGenPushButton")
        self.idPhotoGenPushLayout.addWidget(self.idPhotoGenPushButton)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.idPhotoGenPushLayout.addItem(spacerItem22)
        self.tabIdPhotoGenLayout.addLayout(self.idPhotoGenPushLayout)
        self.tabIdPhotoGenLayout.setStretch(1, 1)

        QtCore.QMetaObject.connectSlotsByName(tabIdPhotoGen)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.idPhotoGenShowInputLabel.setText(
            _translate("MainWindow", "半身照（纯色背景，不与人像同色）"))
        self.idPhotoGenShowInputButton.setText(_translate(
            "MainWindow", "选择照片"))
        self.idPhotoGenShowOutputLabel.setText(_translate("MainWindow", "证件照"))
        self.idPhotoGenShowOutputButton.setText(
            _translate("MainWindow", "保存照片"))
        self.idPhotoGenParamsOptionalSizeLabel.setText(
            _translate("MainWindow", "尺寸设置："))
        self.idPhotoGenParamsOptionalSizeOneInchSizeButton.setText(
            _translate("MainWindow", "一寸照(25x35 mm, 295x413 px)"))
        self.idPhotoGenParamsOptionalSizeTwoInchSizeButton.setText(
            _translate("MainWindow", "二寸照(35x49 mm, 413x579 px)"))
        self.idPhotoGenParamsCustomSizeLabel.setText(
            _translate("MainWindow", "自定义尺寸："))
        self.idPhotoGenParamsCustomSizeWidthLabel.setText(
            _translate("MainWindow", "宽(px)："))
        self.idPhotoGenParamsCustomSizeHeightLabel.setText(
            _translate("MainWindow", "高(px)："))
        self.idPhotoGenParamsColorLabel.setText(
            _translate("MainWindow", "背景设置："))
        self.idPhotoGenParamsColorWhiteButton.setText(
            _translate("MainWindow", "白底"))
        self.idPhotoGenParamsColorBlueButton.setText(
            _translate("MainWindow", "蓝底"))
        self.idPhotoGenParamsColorRedButton.setText(
            _translate("MainWindow", "红底"))
        self.idPhotoGenPushButton.setText(_translate("MainWindow", "生成证件照"))
