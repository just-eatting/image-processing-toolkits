from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BatchProc(object):

    def setupUi(self, tabBatchProc: QtWidgets.QWidget):
        tabBatchProc.setObjectName("tabBatchProc")
        self.tabBatchProcLayout = QtWidgets.QVBoxLayout(tabBatchProc)
        self.tabBatchProcLayout.setObjectName("tabBatchProcLayout")
        spacerItem45 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBatchProcLayout.addItem(spacerItem45)
        self.batchProcInputPathLayout = QtWidgets.QHBoxLayout()
        self.batchProcInputPathLayout.setObjectName("batchProcInputPathLayout")
        self.batchProcInputPathLabel = QtWidgets.QLabel(tabBatchProc)
        self.batchProcInputPathLabel.setObjectName("batchProcInputPathLabel")
        self.batchProcInputPathLayout.addWidget(self.batchProcInputPathLabel)
        self.batchProcInputPathLineEdit = QtWidgets.QLineEdit(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.batchProcInputPathLineEdit.setFont(font)
        self.batchProcInputPathLineEdit.setObjectName(
            "batchProcInputPathLineEdit")
        self.batchProcInputPathLayout.addWidget(
            self.batchProcInputPathLineEdit)
        self.batchProcInputPathButton = QtWidgets.QPushButton(tabBatchProc)
        self.batchProcInputPathButton.setObjectName("batchProcInputPathButton")
        self.batchProcInputPathLayout.addWidget(self.batchProcInputPathButton)
        self.tabBatchProcLayout.addLayout(self.batchProcInputPathLayout)
        self.batchProcOutputPathLayout = QtWidgets.QHBoxLayout()
        self.batchProcOutputPathLayout.setObjectName(
            "batchProcOutputPathLayout")
        self.batchProcOutputPathLabel = QtWidgets.QLabel(tabBatchProc)
        self.batchProcOutputPathLabel.setObjectName("batchProcOutputPathLabel")
        self.batchProcOutputPathLayout.addWidget(self.batchProcOutputPathLabel)
        self.batchProcOutputPathLineEdit = QtWidgets.QLineEdit(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.batchProcOutputPathLineEdit.setFont(font)
        self.batchProcOutputPathLineEdit.setObjectName(
            "batchProcOutputPathLineEdit")
        self.batchProcOutputPathLayout.addWidget(
            self.batchProcOutputPathLineEdit)
        self.batchProcOutputPathButton = QtWidgets.QPushButton(tabBatchProc)
        self.batchProcOutputPathButton.setObjectName(
            "batchProcOutputPathButton")
        self.batchProcOutputPathLayout.addWidget(
            self.batchProcOutputPathButton)
        self.tabBatchProcLayout.addLayout(self.batchProcOutputPathLayout)
        spacerItem46 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBatchProcLayout.addItem(spacerItem46)
        self.batchProcShowLayout = QtWidgets.QHBoxLayout()
        self.batchProcShowLayout.setObjectName("batchProcShowLayout")
        spacerItem47 = QtWidgets.QSpacerItem(20, 40,
                                             QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.Expanding)
        self.batchProcShowLayout.addItem(spacerItem47)
        self.batchProcShowFileListLayout = QtWidgets.QVBoxLayout()
        self.batchProcShowFileListLayout.setObjectName(
            "batchProcShowFileListLayout")
        self.batchProcShowFileListLabel = QtWidgets.QLabel(tabBatchProc)
        self.batchProcShowFileListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.batchProcShowFileListLabel.setObjectName(
            "batchProcShowFileListLabel")
        self.batchProcShowFileListLayout.addWidget(
            self.batchProcShowFileListLabel)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowFileListLayout.addItem(spacerItem48)
        self.batchProcShowFileListWidget = QtWidgets.QListWidget(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.batchProcShowFileListWidget.setFont(font)
        self.batchProcShowFileListWidget.setObjectName(
            "batchProcShowFileListWidget")
        self.batchProcShowFileListLayout.addWidget(
            self.batchProcShowFileListWidget)
        spacerItem49 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowFileListLayout.addItem(spacerItem49)
        self.batchProcShowFileListButtonLayout = QtWidgets.QHBoxLayout()
        self.batchProcShowFileListButtonLayout.setObjectName(
            "batchProcShowFileListButtonLayout")
        spacerItem50 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowFileListButtonLayout.addItem(spacerItem50)
        self.batchProcShowFileListSelectAllButton = QtWidgets.QPushButton(
            tabBatchProc)
        self.batchProcShowFileListSelectAllButton.setObjectName(
            "batchProcShowFileListSelectAllButton")
        self.batchProcShowFileListButtonLayout.addWidget(
            self.batchProcShowFileListSelectAllButton)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowFileListButtonLayout.addItem(spacerItem51)
        self.batchProcShowFileListFlushButton = QtWidgets.QPushButton(
            tabBatchProc)
        self.batchProcShowFileListFlushButton.setObjectName(
            "batchProcShowFileListFlushButton")
        self.batchProcShowFileListButtonLayout.addWidget(
            self.batchProcShowFileListFlushButton)
        spacerItem52 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowFileListButtonLayout.addItem(spacerItem52)
        self.batchProcShowFileListLayout.addLayout(
            self.batchProcShowFileListButtonLayout)
        self.batchProcShowLayout.addLayout(self.batchProcShowFileListLayout)
        spacerItem53 = QtWidgets.QSpacerItem(20, 40,
                                             QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.Expanding)
        self.batchProcShowLayout.addItem(spacerItem53)
        self.batchProcShowProcessingListLayout = QtWidgets.QVBoxLayout()
        self.batchProcShowProcessingListLayout.setObjectName(
            "batchProcShowProcessingListLayout")
        self.batchProcShowProcessingListLabel = QtWidgets.QLabel(tabBatchProc)
        self.batchProcShowProcessingListLabel.setAlignment(
            QtCore.Qt.AlignCenter)
        self.batchProcShowProcessingListLabel.setObjectName(
            "batchProcShowProcessingListLabel")
        self.batchProcShowProcessingListLayout.addWidget(
            self.batchProcShowProcessingListLabel)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowProcessingListLayout.addItem(spacerItem54)
        self.batchProcShowProcessingListWidget = QtWidgets.QListWidget(
            tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.batchProcShowProcessingListWidget.setFont(font)
        self.batchProcShowProcessingListWidget.setObjectName(
            "batchProcShowProcessingListWidget")
        self.batchProcShowProcessingListLayout.addWidget(
            self.batchProcShowProcessingListWidget)
        spacerItem55 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowProcessingListLayout.addItem(spacerItem55)
        self.batchProcShowProcessingListButtonLayout = QtWidgets.QHBoxLayout()
        self.batchProcShowProcessingListButtonLayout.setObjectName(
            "batchProcShowProcessingListButtonLayout")
        spacerItem56 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowProcessingListButtonLayout.addItem(spacerItem56)
        self.batchProcShowProcessingListCancelAllButton = QtWidgets.QPushButton(
            tabBatchProc)
        self.batchProcShowProcessingListCancelAllButton.setObjectName(
            "batchProcShowProcessingListCancelAllButton")
        self.batchProcShowProcessingListButtonLayout.addWidget(
            self.batchProcShowProcessingListCancelAllButton)
        spacerItem57 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowProcessingListButtonLayout.addItem(spacerItem57)
        self.batchProcShowProcessingListLayout.addLayout(
            self.batchProcShowProcessingListButtonLayout)
        self.batchProcShowLayout.addLayout(
            self.batchProcShowProcessingListLayout)
        spacerItem58 = QtWidgets.QSpacerItem(20, 40,
                                             QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.Expanding)
        self.batchProcShowLayout.addItem(spacerItem58)
        self.batchProcShowResultListLayout = QtWidgets.QVBoxLayout()
        self.batchProcShowResultListLayout.setObjectName(
            "batchProcShowResultListLayout")
        self.batchProcShowResultListLabel = QtWidgets.QLabel(tabBatchProc)
        self.batchProcShowResultListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.batchProcShowResultListLabel.setObjectName(
            "batchProcShowResultListLabel")
        self.batchProcShowResultListLayout.addWidget(
            self.batchProcShowResultListLabel)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowResultListLayout.addItem(spacerItem59)
        self.batchProcShowResultListWidget = QtWidgets.QListWidget(
            tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.batchProcShowResultListWidget.setFont(font)
        self.batchProcShowResultListWidget.setObjectName(
            "batchProcShowResultListWidget")
        self.batchProcShowResultListLayout.addWidget(
            self.batchProcShowResultListWidget)
        spacerItem60 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowResultListLayout.addItem(spacerItem60)
        self.batchProcShowResultListClearLayout = QtWidgets.QHBoxLayout()
        self.batchProcShowResultListClearLayout.setObjectName(
            "batchProcShowResultListClearLayout")
        self.batchProcShowResultListExplorerButton = QtWidgets.QPushButton(
            tabBatchProc)
        self.batchProcShowResultListExplorerButton.setObjectName(
            "batchProcShowResultListExplorerButton")
        self.batchProcShowResultListClearLayout.addWidget(
            self.batchProcShowResultListExplorerButton)
        spacerItem61 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcShowResultListClearLayout.addItem(spacerItem61)
        self.batchProcShowResultListClearButton = QtWidgets.QPushButton(
            tabBatchProc)
        self.batchProcShowResultListClearButton.setObjectName(
            "batchProcShowResultListClearButton")
        self.batchProcShowResultListClearLayout.addWidget(
            self.batchProcShowResultListClearButton)
        self.batchProcShowResultListLayout.addLayout(
            self.batchProcShowResultListClearLayout)
        self.batchProcShowLayout.addLayout(self.batchProcShowResultListLayout)
        spacerItem62 = QtWidgets.QSpacerItem(20, 40,
                                             QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.Expanding)
        self.batchProcShowLayout.addItem(spacerItem62)
        self.batchProcShowLayout.setStretch(0, 1)
        self.batchProcShowLayout.setStretch(1, 4)
        self.batchProcShowLayout.setStretch(3, 4)
        self.batchProcShowLayout.setStretch(5, 4)
        self.batchProcShowLayout.setStretch(6, 1)
        self.tabBatchProcLayout.addLayout(self.batchProcShowLayout)
        spacerItem63 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBatchProcLayout.addItem(spacerItem63)
        self.batchProcLine_1 = QtWidgets.QFrame(tabBatchProc)
        self.batchProcLine_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.batchProcLine_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.batchProcLine_1.setObjectName("batchProcLine_1")
        self.tabBatchProcLayout.addWidget(self.batchProcLine_1)
        self.batchProcTypeLayout = QtWidgets.QHBoxLayout()
        self.batchProcTypeLayout.setObjectName("batchProcTypeLayout")
        self.batchProcTypeLabel = QtWidgets.QLabel(tabBatchProc)
        self.batchProcTypeLabel.setObjectName("batchProcTypeLabel")
        self.batchProcTypeLayout.addWidget(self.batchProcTypeLabel)
        self.batchProcRangeTypeButton = QtWidgets.QRadioButton(tabBatchProc)
        self.batchProcRangeTypeButton.setObjectName("batchProcRangeTypeButton")
        self.batchProcTypeLayout.addWidget(self.batchProcRangeTypeButton)
        self.batchProcSizeTypeButton = QtWidgets.QRadioButton(tabBatchProc)
        self.batchProcSizeTypeButton.setObjectName("batchProcSizeTypeButton")
        self.batchProcTypeLayout.addWidget(self.batchProcSizeTypeButton)
        self.batchProcScaleTypeButton = QtWidgets.QRadioButton(tabBatchProc)
        self.batchProcScaleTypeButton.setObjectName("batchProcScaleTypeButton")
        self.batchProcTypeLayout.addWidget(self.batchProcScaleTypeButton)
        self.batchProcDefaultTypeButton = QtWidgets.QRadioButton(tabBatchProc)
        self.batchProcDefaultTypeButton.setChecked(True)
        self.batchProcDefaultTypeButton.setObjectName(
            "batchProcDefaultTypeButton")
        self.batchProcTypeLayout.addWidget(self.batchProcDefaultTypeButton)
        spacerItem64 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcTypeLayout.addItem(spacerItem64)
        self.tabBatchProcLayout.addLayout(self.batchProcTypeLayout)
        self.batchProcLine_2 = QtWidgets.QFrame(tabBatchProc)
        self.batchProcLine_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.batchProcLine_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.batchProcLine_2.setObjectName("batchProcLine_2")
        self.tabBatchProcLayout.addWidget(self.batchProcLine_2)
        self.batchProcRangeLayout = QtWidgets.QHBoxLayout()
        self.batchProcRangeLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.batchProcRangeLayout.setSpacing(0)
        self.batchProcRangeLayout.setObjectName("batchProcRangeLayout")
        self.batchProcRangeLabel = QtWidgets.QLabel(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.batchProcRangeLabel.setFont(font)
        self.batchProcRangeLabel.setStyleSheet("")
        self.batchProcRangeLabel.setObjectName("batchProcRangeLabel")
        self.batchProcRangeLayout.addWidget(self.batchProcRangeLabel)
        self.batchProcRangeMinLayout = QtWidgets.QHBoxLayout()
        self.batchProcRangeMinLayout.setObjectName("batchProcRangeMinLayout")
        self.batchProcRangeMinLabel = QtWidgets.QLabel(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.batchProcRangeMinLabel.setFont(font)
        self.batchProcRangeMinLabel.setAlignment(QtCore.Qt.AlignLeading
                                                 | QtCore.Qt.AlignLeft
                                                 | QtCore.Qt.AlignVCenter)
        self.batchProcRangeMinLabel.setObjectName("batchProcRangeMinLabel")
        self.batchProcRangeMinLayout.addWidget(self.batchProcRangeMinLabel)
        self.batchProcRangeMinLineEdit = QtWidgets.QLineEdit(tabBatchProc)
        self.batchProcRangeMinLineEdit.setObjectName(
            "batchProcRangeMinLineEdit")
        self.batchProcRangeMinLayout.addWidget(self.batchProcRangeMinLineEdit)
        self.batchProcRangeLayout.addLayout(self.batchProcRangeMinLayout)
        self.batchProcRangeMaxLayout = QtWidgets.QHBoxLayout()
        self.batchProcRangeMaxLayout.setObjectName("batchProcRangeMaxLayout")
        self.batchProcRangeMaxLabel = QtWidgets.QLabel(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.batchProcRangeMaxLabel.setFont(font)
        self.batchProcRangeMaxLabel.setAlignment(QtCore.Qt.AlignLeading
                                                 | QtCore.Qt.AlignLeft
                                                 | QtCore.Qt.AlignVCenter)
        self.batchProcRangeMaxLabel.setObjectName("batchProcRangeMaxLabel")
        self.batchProcRangeMaxLayout.addWidget(self.batchProcRangeMaxLabel)
        self.batchProcRangeMaxLineEdit = QtWidgets.QLineEdit(tabBatchProc)
        self.batchProcRangeMaxLineEdit.setObjectName(
            "batchProcRangeMaxLineEdit")
        self.batchProcRangeMaxLayout.addWidget(self.batchProcRangeMaxLineEdit)
        self.batchProcRangeLayout.addLayout(self.batchProcRangeMaxLayout)
        spacerItem65 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcRangeLayout.addItem(spacerItem65)
        self.batchProcRangeLayout.setStretch(0, 1)
        self.batchProcRangeLayout.setStretch(1, 1)
        self.batchProcRangeLayout.setStretch(2, 1)
        self.batchProcRangeLayout.setStretch(3, 9)
        self.tabBatchProcLayout.addLayout(self.batchProcRangeLayout)
        self.batchProcLine_3 = QtWidgets.QFrame(tabBatchProc)
        self.batchProcLine_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.batchProcLine_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.batchProcLine_3.setObjectName("batchProcLine_3")
        self.tabBatchProcLayout.addWidget(self.batchProcLine_3)
        self.batchProcSizeLayout = QtWidgets.QHBoxLayout()
        self.batchProcSizeLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.batchProcSizeLayout.setSpacing(0)
        self.batchProcSizeLayout.setObjectName("batchProcSizeLayout")
        self.batchProcSizeLabel = QtWidgets.QLabel(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.batchProcSizeLabel.setFont(font)
        self.batchProcSizeLabel.setStyleSheet("")
        self.batchProcSizeLabel.setObjectName("batchProcSizeLabel")
        self.batchProcSizeLayout.addWidget(self.batchProcSizeLabel)
        self.batchProcSizeWidthLayout = QtWidgets.QHBoxLayout()
        self.batchProcSizeWidthLayout.setObjectName("batchProcSizeWidthLayout")
        self.batchProcSizeWidthLabel = QtWidgets.QLabel(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.batchProcSizeWidthLabel.setFont(font)
        self.batchProcSizeWidthLabel.setAlignment(QtCore.Qt.AlignLeading
                                                  | QtCore.Qt.AlignLeft
                                                  | QtCore.Qt.AlignVCenter)
        self.batchProcSizeWidthLabel.setObjectName("batchProcSizeWidthLabel")
        self.batchProcSizeWidthLayout.addWidget(self.batchProcSizeWidthLabel)
        self.batchProcSizeWidthLineEdit = QtWidgets.QLineEdit(tabBatchProc)
        self.batchProcSizeWidthLineEdit.setObjectName(
            "batchProcSizeWidthLineEdit")
        self.batchProcSizeWidthLayout.addWidget(
            self.batchProcSizeWidthLineEdit)
        self.batchProcSizeLayout.addLayout(self.batchProcSizeWidthLayout)
        self.batchProcSizeHeightLayout = QtWidgets.QHBoxLayout()
        self.batchProcSizeHeightLayout.setObjectName(
            "batchProcSizeHeightLayout")
        self.batchProcSizeHeightLabel = QtWidgets.QLabel(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.batchProcSizeHeightLabel.setFont(font)
        self.batchProcSizeHeightLabel.setAlignment(QtCore.Qt.AlignLeading
                                                   | QtCore.Qt.AlignLeft
                                                   | QtCore.Qt.AlignVCenter)
        self.batchProcSizeHeightLabel.setObjectName("batchProcSizeHeightLabel")
        self.batchProcSizeHeightLayout.addWidget(self.batchProcSizeHeightLabel)
        self.batchProcSizeHeightLineEdit = QtWidgets.QLineEdit(tabBatchProc)
        self.batchProcSizeHeightLineEdit.setObjectName(
            "batchProcSizeHeightLineEdit")
        self.batchProcSizeHeightLayout.addWidget(
            self.batchProcSizeHeightLineEdit)
        self.batchProcSizeLayout.addLayout(self.batchProcSizeHeightLayout)
        spacerItem66 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcSizeLayout.addItem(spacerItem66)
        self.batchProcSizeLayout.setStretch(0, 1)
        self.batchProcSizeLayout.setStretch(1, 1)
        self.batchProcSizeLayout.setStretch(2, 1)
        self.batchProcSizeLayout.setStretch(3, 10)
        self.tabBatchProcLayout.addLayout(self.batchProcSizeLayout)
        self.batchProcLine_4 = QtWidgets.QFrame(tabBatchProc)
        self.batchProcLine_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.batchProcLine_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.batchProcLine_4.setObjectName("batchProcLine_4")
        self.tabBatchProcLayout.addWidget(self.batchProcLine_4)
        self.batchProcScaleLayout = QtWidgets.QHBoxLayout()
        self.batchProcScaleLayout.setObjectName("batchProcScaleLayout")
        self.batchProcScaleLabel = QtWidgets.QLabel(tabBatchProc)
        self.batchProcScaleLabel.setObjectName("batchProcScaleLabel")
        self.batchProcScaleLayout.addWidget(self.batchProcScaleLabel)
        self.batchProcScaleSpinBox = QtWidgets.QDoubleSpinBox(tabBatchProc)
        self.batchProcScaleSpinBox.setDecimals(2)
        self.batchProcScaleSpinBox.setMinimum(0.1)
        self.batchProcScaleSpinBox.setSingleStep(0.1)
        self.batchProcScaleSpinBox.setProperty("value", 1.0)
        self.batchProcScaleSpinBox.setObjectName("batchProcScaleSpinBox")
        self.batchProcScaleLayout.addWidget(self.batchProcScaleSpinBox)
        spacerItem67 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcScaleLayout.addItem(spacerItem67)
        self.tabBatchProcLayout.addLayout(self.batchProcScaleLayout)
        self.batchProcLine_5 = QtWidgets.QFrame(tabBatchProc)
        self.batchProcLine_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.batchProcLine_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.batchProcLine_5.setObjectName("batchProcLine_5")
        self.tabBatchProcLayout.addWidget(self.batchProcLine_5)
        self.batchProcStartLayout = QtWidgets.QHBoxLayout()
        self.batchProcStartLayout.setObjectName("batchProcStartLayout")
        spacerItem68 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcStartLayout.addItem(spacerItem68)
        self.batchProcStartButton = QtWidgets.QPushButton(tabBatchProc)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.batchProcStartButton.setFont(font)
        self.batchProcStartButton.setObjectName("batchProcStartButton")
        self.batchProcStartLayout.addWidget(self.batchProcStartButton)
        spacerItem69 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.batchProcStartLayout.addItem(spacerItem69)
        self.tabBatchProcLayout.addLayout(self.batchProcStartLayout)
        spacerItem70 = QtWidgets.QSpacerItem(40, 20,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.tabBatchProcLayout.addItem(spacerItem70)

        QtCore.QMetaObject.connectSlotsByName(tabBatchProc)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.batchProcInputPathLabel.setText(_translate("MainWindow", "图片目录："))
        self.batchProcInputPathButton.setText(_translate(
            "MainWindow", "打开文件夹"))
        self.batchProcOutputPathLabel.setText(_translate("MainWindow", "保存至："))
        self.batchProcOutputPathButton.setText(
            _translate("MainWindow", "选择文件夹"))
        self.batchProcShowFileListLabel.setText(
            _translate("MainWindow", "文件列表（双击加入处理列表）"))
        self.batchProcShowFileListSelectAllButton.setText(
            _translate("MainWindow", "全选"))
        self.batchProcShowFileListFlushButton.setText(
            _translate("MainWindow", "刷新"))
        self.batchProcShowProcessingListLabel.setText(
            _translate("MainWindow", "要处理的文件（双击取消）"))
        self.batchProcShowProcessingListCancelAllButton.setText(
            _translate("MainWindow", "全部取消"))
        self.batchProcShowResultListLabel.setText(
            _translate("MainWindow", "处理结果"))
        self.batchProcShowResultListExplorerButton.setText(
            _translate("MainWindow", "打开文件管理器查看"))
        self.batchProcShowResultListClearButton.setText(
            _translate("MainWindow", "清空"))
        self.batchProcTypeLabel.setText(_translate("MainWindow", "调整类型："))
        self.batchProcRangeTypeButton.setText(_translate("MainWindow", "按范围"))
        self.batchProcSizeTypeButton.setText(_translate("MainWindow", "按尺寸"))
        self.batchProcScaleTypeButton.setText(_translate("MainWindow", "按比例"))
        self.batchProcDefaultTypeButton.setText(
            _translate("MainWindow", "只修改文件名"))
        self.batchProcRangeLabel.setText(_translate("MainWindow", "按范围："))
        self.batchProcRangeMinLabel.setText(
            _translate("MainWindow", "最小边(px)："))
        self.batchProcRangeMaxLabel.setText(
            _translate("MainWindow", "最大边(px)："))
        self.batchProcSizeLabel.setText(_translate("MainWindow", "按尺寸："))
        self.batchProcSizeWidthLabel.setText(_translate(
            "MainWindow", "宽(px)："))
        self.batchProcSizeHeightLabel.setText(
            _translate("MainWindow", "高(px)："))
        self.batchProcScaleLabel.setText(_translate("MainWindow", "按比例："))
        self.batchProcStartButton.setText(_translate("MainWindow", "开始批处理"))