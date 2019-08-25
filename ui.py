# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Interferometry(object):
    def setupUi(self, Interferometry):
        Interferometry.setObjectName("Interferometry")
        Interferometry.resize(1800, 921)
        self.centralwidget = QtWidgets.QWidget(Interferometry)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem)
        self.logOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.logOutput.setBaseSize(QtCore.QSize(369, 214))
        self.logOutput.setReadOnly(True)
        self.logOutput.setObjectName("logOutput")
        self.verticalLayout_8.addWidget(self.logOutput)
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setObjectName("calculate")
        self.verticalLayout_8.addWidget(self.calculate)
        self.gridLayout_7.addLayout(self.verticalLayout_8, 2, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setMinimumSize(QtCore.QSize(100, 28))
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout.addWidget(self.btn_load)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.swapButton = QtWidgets.QPushButton(self.centralwidget)
        self.swapButton.setMinimumSize(QtCore.QSize(100, 28))
        self.swapButton.setObjectName("swapButton")
        self.horizontalLayout.addWidget(self.swapButton)
        self.gridLayout_7.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.editTab = QtWidgets.QTabWidget(self.centralwidget)
        self.editTab.setBaseSize(QtCore.QSize(369, 465))
        self.editTab.setObjectName("editTab")
        self.savgolTab = QtWidgets.QWidget()
        self.savgolTab.setObjectName("savgolTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.savgolTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.savgolWindow = QtWidgets.QLineEdit(self.savgolTab)
        self.savgolWindow.setMinimumSize(QtCore.QSize(0, 40))
        self.savgolWindow.setObjectName("savgolWindow")
        self.verticalLayout_12.addWidget(self.savgolWindow)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem3)
        self.savgolOrder = QtWidgets.QLineEdit(self.savgolTab)
        self.savgolOrder.setMinimumSize(QtCore.QSize(0, 40))
        self.savgolOrder.setObjectName("savgolOrder")
        self.verticalLayout_12.addWidget(self.savgolOrder)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem4)
        self.horizontalLayout_23.addLayout(self.verticalLayout_12)
        self.gridLayout_4.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)
        self.editTab.addTab(self.savgolTab, "")
        self.peakTab = QtWidgets.QWidget()
        self.peakTab.setObjectName("peakTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.peakTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem5)
        self.peaksMin = QtWidgets.QLineEdit(self.peakTab)
        self.peaksMin.setMinimumSize(QtCore.QSize(0, 40))
        self.peaksMin.setObjectName("peaksMin")
        self.verticalLayout_15.addWidget(self.peaksMin)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem6)
        self.peaksMax = QtWidgets.QLineEdit(self.peakTab)
        self.peaksMax.setMinimumSize(QtCore.QSize(0, 40))
        self.peaksMax.setObjectName("peaksMax")
        self.verticalLayout_15.addWidget(self.peaksMax)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem7)
        self.peaksThreshold = QtWidgets.QLineEdit(self.peakTab)
        self.peaksThreshold.setMinimumSize(QtCore.QSize(0, 40))
        self.peaksThreshold.setObjectName("peaksThreshold")
        self.verticalLayout_15.addWidget(self.peaksThreshold)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem8)
        self.horizontalLayout_25.addLayout(self.verticalLayout_15)
        self.gridLayout_3.addLayout(self.horizontalLayout_25, 0, 0, 1, 1)
        self.editTab.addTab(self.peakTab, "")
        self.convolTab = QtWidgets.QWidget()
        self.convolTab.setObjectName("convolTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.convolTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.convolutionStd = QtWidgets.QLineEdit(self.convolTab)
        self.convolutionStd.setMinimumSize(QtCore.QSize(0, 40))
        self.convolutionStd.setObjectName("convolutionStd")
        self.verticalLayout_14.addWidget(self.convolutionStd)
        self.gridLayout_2.addLayout(self.verticalLayout_14, 0, 0, 1, 1)
        self.editTab.addTab(self.convolTab, "")
        self.cutTab = QtWidgets.QWidget()
        self.cutTab.setObjectName("cutTab")
        self.gridLayout = QtWidgets.QGridLayout(self.cutTab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem9)
        self.sliceStart = QtWidgets.QLineEdit(self.cutTab)
        self.sliceStart.setMinimumSize(QtCore.QSize(0, 40))
        self.sliceStart.setObjectName("sliceStart")
        self.verticalLayout_13.addWidget(self.sliceStart)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem10)
        self.sliceStop = QtWidgets.QLineEdit(self.cutTab)
        self.sliceStop.setMinimumSize(QtCore.QSize(0, 40))
        self.sliceStop.setObjectName("sliceStop")
        self.verticalLayout_13.addWidget(self.sliceStop)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem11)
        self.horizontalLayout_24.addLayout(self.verticalLayout_13)
        self.gridLayout.addLayout(self.horizontalLayout_24, 0, 0, 1, 1)
        self.editTab.addTab(self.cutTab, "")
        self.verticalLayout_5.addWidget(self.editTab)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.temporalApplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.temporalApplyButton.setMinimumSize(QtCore.QSize(150, 40))
        self.temporalApplyButton.setObjectName("temporalApplyButton")
        self.verticalLayout_7.addWidget(self.temporalApplyButton)
        spacerItem13 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem13)
        self.commitChanges = QtWidgets.QPushButton(self.centralwidget)
        self.commitChanges.setMinimumSize(QtCore.QSize(150, 40))
        self.commitChanges.setObjectName("commitChanges")
        self.verticalLayout_7.addWidget(self.commitChanges)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.gridLayout_7.addLayout(self.verticalLayout_5, 0, 2, 2, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setMinimumSize(QtCore.QSize(100, 28))
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_4.addWidget(self.resetButton)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.refreshGraph = QtWidgets.QPushButton(self.centralwidget)
        self.refreshGraph.setMinimumSize(QtCore.QSize(100, 28))
        self.refreshGraph.setObjectName("refreshGraph")
        self.horizontalLayout_4.addWidget(self.refreshGraph)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 735))
        self.tableWidget.setBaseSize(QtCore.QSize(379, 738))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        spacerItem17 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem17)
        self.gridLayout_7.addLayout(self.verticalLayout, 1, 0, 2, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setMinimumSize(QtCore.QSize(900, 500))
        self.MplWidget.setObjectName("MplWidget")
        self.verticalLayout_2.addWidget(self.MplWidget)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.methodWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.methodWidget.setMinimumSize(QtCore.QSize(0, 290))
        self.methodWidget.setBaseSize(QtCore.QSize(869, 249))
        self.methodWidget.setAutoFillBackground(False)
        self.methodWidget.setTabsClosable(False)
        self.methodWidget.setMovable(False)
        self.methodWidget.setTabBarAutoHide(False)
        self.methodWidget.setObjectName("methodWidget")
        self.sppTab = QtWidgets.QWidget()
        self.sppTab.setObjectName("sppTab")
        self.label = QtWidgets.QLabel(self.sppTab)
        self.label.setGeometry(QtCore.QRect(370, 100, 97, 16))
        self.label.setObjectName("label")
        self.methodWidget.addTab(self.sppTab, "")
        self.cffTab = QtWidgets.QWidget()
        self.cffTab.setObjectName("cffTab")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.cffTab)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem18)
        self.iReferenceArm = QtWidgets.QPushButton(self.cffTab)
        self.iReferenceArm.setMinimumSize(QtCore.QSize(150, 40))
        self.iReferenceArm.setObjectName("iReferenceArm")
        self.horizontalLayout_13.addWidget(self.iReferenceArm)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem19)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem20)
        self.iSampleArm = QtWidgets.QPushButton(self.cffTab)
        self.iSampleArm.setMinimumSize(QtCore.QSize(150, 40))
        self.iSampleArm.setObjectName("iSampleArm")
        self.horizontalLayout_14.addWidget(self.iSampleArm)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem21)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem22)
        self.initGD = QtWidgets.QLineEdit(self.cffTab)
        self.initGD.setMinimumSize(QtCore.QSize(70, 30))
        self.initGD.setObjectName("initGD")
        self.horizontalLayout_9.addWidget(self.initGD)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem23)
        self.initGDD = QtWidgets.QLineEdit(self.cffTab)
        self.initGDD.setMinimumSize(QtCore.QSize(70, 30))
        self.initGDD.setObjectName("initGDD")
        self.horizontalLayout_9.addWidget(self.initGDD)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem24)
        self.initTOD = QtWidgets.QLineEdit(self.cffTab)
        self.initTOD.setMinimumSize(QtCore.QSize(70, 30))
        self.initTOD.setObjectName("initTOD")
        self.horizontalLayout_9.addWidget(self.initTOD)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem25)
        self.initFOD = QtWidgets.QLineEdit(self.cffTab)
        self.initFOD.setMinimumSize(QtCore.QSize(70, 30))
        self.initFOD.setObjectName("initFOD")
        self.horizontalLayout_9.addWidget(self.initFOD)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem26)
        self.initQOD = QtWidgets.QLineEdit(self.cffTab)
        self.initQOD.setMinimumSize(QtCore.QSize(70, 30))
        self.initQOD.setObjectName("initQOD")
        self.horizontalLayout_9.addWidget(self.initQOD)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem27)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_15.addLayout(self.verticalLayout_9)
        self.methodWidget.addTab(self.cffTab, "")
        self.mmTab = QtWidgets.QWidget()
        self.mmTab.setObjectName("mmTab")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.mmTab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 10, 872, 249))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem28)
        self.iReferenceArm_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.iReferenceArm_2.setMinimumSize(QtCore.QSize(150, 40))
        self.iReferenceArm_2.setObjectName("iReferenceArm_2")
        self.horizontalLayout_16.addWidget(self.iReferenceArm_2)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem29)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem30)
        self.iSampleArm_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.iSampleArm_2.setMinimumSize(QtCore.QSize(150, 40))
        self.iSampleArm_2.setObjectName("iSampleArm_2")
        self.horizontalLayout_17.addWidget(self.iSampleArm_2)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem31)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem32)
        self.getSPP = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.getSPP.setMinimumSize(QtCore.QSize(70, 30))
        self.getSPP.setObjectName("getSPP")
        self.horizontalLayout_18.addWidget(self.getSPP)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem33)
        self.printCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget_8)
        self.printCheck.setObjectName("printCheck")
        self.horizontalLayout_18.addWidget(self.printCheck)
        self.verticalLayout_10.addLayout(self.horizontalLayout_18)
        self.methodWidget.addTab(self.mmTab, "")
        self.fftTab = QtWidgets.QWidget()
        self.fftTab.setObjectName("fftTab")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.fftTab)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 10, 872, 249))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem34)
        self.doFFT = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.doFFT.setMinimumSize(QtCore.QSize(150, 40))
        self.doFFT.setObjectName("doFFT")
        self.horizontalLayout_19.addWidget(self.doFFT)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem35)
        self.verticalLayout_11.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem36)
        self.doCut = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.doCut.setMinimumSize(QtCore.QSize(150, 40))
        self.doCut.setObjectName("doCut")
        self.horizontalLayout_20.addWidget(self.doCut)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem37)
        self.gaussianCut = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.gaussianCut.setMinimumSize(QtCore.QSize(0, 30))
        self.gaussianCut.setText("")
        self.gaussianCut.setObjectName("gaussianCut")
        self.horizontalLayout_20.addWidget(self.gaussianCut)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem38)
        self.gaussianCut2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.gaussianCut2.setMinimumSize(QtCore.QSize(0, 30))
        self.gaussianCut2.setObjectName("gaussianCut2")
        self.horizontalLayout_20.addWidget(self.gaussianCut2)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem39)
        self.verticalLayout_11.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem40)
        self.doIFFT = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.doIFFT.setMinimumSize(QtCore.QSize(150, 40))
        self.doIFFT.setObjectName("doIFFT")
        self.horizontalLayout_21.addWidget(self.doIFFT)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem41)
        self.verticalLayout_11.addLayout(self.horizontalLayout_21)
        self.methodWidget.addTab(self.fftTab, "")
        self.verticalLayout_3.addWidget(self.methodWidget)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 2, 1, 1, 1)
        Interferometry.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Interferometry)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        Interferometry.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Interferometry)
        self.statusbar.setObjectName("statusbar")
        Interferometry.setStatusBar(self.statusbar)
        self.actionSave_log_file = QtWidgets.QAction(Interferometry)
        self.actionSave_log_file.setObjectName("actionSave_log_file")
        self.actionSave_current_data = QtWidgets.QAction(Interferometry)
        self.actionSave_current_data.setObjectName("actionSave_current_data")
        self.actionLoad_data_manually = QtWidgets.QAction(Interferometry)
        self.actionLoad_data_manually.setObjectName("actionLoad_data_manually")
        self.actionExit = QtWidgets.QAction(Interferometry)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(Interferometry)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUndo = QtWidgets.QAction(Interferometry)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(Interferometry)
        self.actionRedo.setObjectName("actionRedo")
        self.actionGenerator = QtWidgets.QAction(Interferometry)
        self.actionGenerator.setObjectName("actionGenerator")
        self.actionUnit_converter = QtWidgets.QAction(Interferometry)
        self.actionUnit_converter.setObjectName("actionUnit_converter")
        self.actionOpen_documentation = QtWidgets.QAction(Interferometry)
        self.actionOpen_documentation.setObjectName("actionOpen_documentation")
        self.menuFile.addAction(self.actionSave_log_file)
        self.menuFile.addAction(self.actionSave_current_data)
        self.menuFile.addAction(self.actionLoad_data_manually)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionOpen_documentation)
        self.menuPreferences.addAction(self.actionGenerator)
        self.menuPreferences.addAction(self.actionUnit_converter)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Angular frequency", "Intensity"])
        self.tableWidget.setSizeAdjustPolicy(
        QtWidgets.QAbstractScrollArea.AdjustToContents)

        self.savgolTab.setStyleSheet(" background-color: rgb(240,240,240);")
        self.peakTab.setStyleSheet(" background-color: rgb(240,240,240);")
        self.convolTab.setStyleSheet(" background-color: rgb(240,240,240);")
        self.cutTab.setStyleSheet(" background-color: rgb(240,240,240);")
        self.sppTab.setStyleSheet(" background-color: rgb(240,240,240);")
        self.cffTab.setStyleSheet(" background-color: rgb(240,240,240);")
        self.mmTab.setStyleSheet(" background-color: rgb(240,240,240);")
        self.fftTab.setStyleSheet(" background-color: rgb(240,240,240);")

        self.retranslateUi(Interferometry)
        self.editTab.setCurrentIndex(3)
        self.methodWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Interferometry)

    def retranslateUi(self, Interferometry):
        _translate = QtCore.QCoreApplication.translate
        Interferometry.setWindowTitle(_translate("Interferometry", "Interferometry"))
        self.calculate.setText(_translate("Interferometry", "Calculate"))
        self.btn_load.setText(_translate("Interferometry", "Load data"))
        self.swapButton.setText(_translate("Interferometry", "Swap axes"))
        self.savgolWindow.setPlaceholderText(_translate("Interferometry", "Window size"))
        self.savgolOrder.setPlaceholderText(_translate("Interferometry", "Order"))
        self.editTab.setTabText(self.editTab.indexOf(self.savgolTab), _translate("Interferometry", "Savitzky-Golay filter"))
        self.peaksMin.setPlaceholderText(_translate("Interferometry", "Min. prominence"))
        self.peaksMax.setPlaceholderText(_translate("Interferometry", "Max. prominence"))
        self.peaksThreshold.setPlaceholderText(_translate("Interferometry", "Threshold"))
        self.editTab.setTabText(self.editTab.indexOf(self.peakTab), _translate("Interferometry", "Peaks"))
        self.convolutionStd.setPlaceholderText(_translate("Interferometry", "Standard deviation"))
        self.editTab.setTabText(self.editTab.indexOf(self.convolTab), _translate("Interferometry", "Convolution"))
        self.sliceStart.setPlaceholderText(_translate("Interferometry", "Start value"))
        self.sliceStop.setPlaceholderText(_translate("Interferometry", "End value"))
        self.editTab.setTabText(self.editTab.indexOf(self.cutTab), _translate("Interferometry", "Cut"))
        self.temporalApplyButton.setText(_translate("Interferometry", "Preview"))
        self.commitChanges.setText(_translate("Interferometry", "Commit"))
        self.resetButton.setText(_translate("Interferometry", "Clear data"))
        self.refreshGraph.setText(_translate("Interferometry", "Refresh graph"))
        self.comboBox.setItemText(0, _translate("Interferometry", "PHz"))
        self.comboBox.setItemText(1, _translate("Interferometry", "nm"))
        self.comboBox.setItemText(2, _translate("Interferometry", "Ångström"))
        self.label.setText(_translate("Interferometry", "Not implemented"))
        self.methodWidget.setTabText(self.methodWidget.indexOf(self.sppTab), _translate("Interferometry", "SPP"))
        self.iReferenceArm.setText(_translate("Interferometry", "Reference Arm"))
        self.iSampleArm.setText(_translate("Interferometry", "Sample Arm"))
        self.initGD.setPlaceholderText(_translate("Interferometry", "GD"))
        self.initGDD.setPlaceholderText(_translate("Interferometry", "GDD"))
        self.initTOD.setPlaceholderText(_translate("Interferometry", "TOD"))
        self.initFOD.setPlaceholderText(_translate("Interferometry", "FOD"))
        self.initQOD.setPlaceholderText(_translate("Interferometry", "QOD"))
        self.methodWidget.setTabText(self.methodWidget.indexOf(self.cffTab), _translate("Interferometry", "CFF"))
        self.iReferenceArm_2.setText(_translate("Interferometry", "Reference Arm"))
        self.iSampleArm_2.setText(_translate("Interferometry", "Sample Arm"))
        self.getSPP.setPlaceholderText(_translate("Interferometry", "Type reference point position there"))
        self.printCheck.setText(_translate("Interferometry", "Print fit report"))
        self.methodWidget.setTabText(self.methodWidget.indexOf(self.mmTab), _translate("Interferometry", "MM"))
        self.doFFT.setText(_translate("Interferometry", "1.  FFT"))
        self.doCut.setText(_translate("Interferometry", "2.  Window"))
        self.gaussianCut.setPlaceholderText(_translate("Interferometry", "Spike"))
        self.gaussianCut2.setPlaceholderText(_translate("Interferometry", "Full Width at Half Maximum"))
        self.doIFFT.setText(_translate("Interferometry", "3.  IFFT"))
        self.methodWidget.setTabText(self.methodWidget.indexOf(self.fftTab), _translate("Interferometry", "FFT"))
        self.menuFile.setTitle(_translate("Interferometry", "File"))
        self.menuEdit.setTitle(_translate("Interferometry", "Edit"))
        self.menuHelp.setTitle(_translate("Interferometry", "Help"))
        self.menuPreferences.setTitle(_translate("Interferometry", "Tools"))
        self.actionSave_log_file.setText(_translate("Interferometry", "Save log file"))
        self.actionSave_current_data.setText(_translate("Interferometry", "Save current data"))
        self.actionLoad_data_manually.setText(_translate("Interferometry", "Load data manually"))
        self.actionExit.setText(_translate("Interferometry", "Exit"))
        self.actionAbout.setText(_translate("Interferometry", "About"))
        self.actionUndo.setText(_translate("Interferometry", "Undo"))
        self.actionRedo.setText(_translate("Interferometry", "Redo"))
        self.actionGenerator.setText(_translate("Interferometry", "Generator"))
        self.actionUnit_converter.setText(_translate("Interferometry", "Unit converter"))
        self.actionOpen_documentation.setText(_translate("Interferometry", "Open documentation"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Interferometry = QtWidgets.QMainWindow()
    ui = Ui_Interferometry()
    ui.setupUi(Interferometry)
    Interferometry.show()
    sys.exit(app.exec_())

