from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):


    def __init__(self):
        self.saveMode = 0   # 0 => saving inside points, 1 => saving outside points, 2 => saving both inside and outside
        self.sourceFile = ""
        self.targetFile = ""

    def iniWindow(self, MainWindow):
        self.setupUi(MainWindow)
        self.loadSourcePushButton.click.connect(self.onSetSourcePathButtonClick)
        self.loadTargetPushButton.click.connect(self.onSetTargetCategoryButtonClick)
        self.startPushButton.click.connect(self.onStartButtonClick)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 550)
        MainWindow.setMinimumSize(QtCore.QSize(1032, 550))
        MainWindow.setMaximumSize(QtCore.QSize(1032, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sourceGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sourceGroupBox.setGeometry(QtCore.QRect(10, 10, 491, 91))
        self.sourceGroupBox.setStyleSheet("font: 75 10pt \"楷体\";")
        self.sourceGroupBox.setObjectName("sourceGroupBox")
        self.sourceLineEdit = QtWidgets.QLineEdit(self.sourceGroupBox)
        self.sourceLineEdit.setGeometry(QtCore.QRect(20, 30, 401, 41))
        self.sourceLineEdit.setObjectName("sourceLineEdit")
        self.loadSourcePushButton = QtWidgets.QPushButton(self.sourceGroupBox)
        self.loadSourcePushButton.setGeometry(QtCore.QRect(430, 30, 41, 41))
        self.loadSourcePushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loadSourcePushButton.setObjectName("loadSourcePushButton")
        self.targetGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.targetGroupBox.setGeometry(QtCore.QRect(10, 129, 491, 91))
        self.targetGroupBox.setStyleSheet("font: 75 10pt \"楷体\";")
        self.targetGroupBox.setObjectName("targetGroupBox")
        self.targetLineEdit = QtWidgets.QLineEdit(self.targetGroupBox)
        self.targetLineEdit.setGeometry(QtCore.QRect(20, 30, 401, 41))
        self.targetLineEdit.setObjectName("targetLineEdit")
        self.loadTargetPushButton = QtWidgets.QPushButton(self.targetGroupBox)
        self.loadTargetPushButton.setGeometry(QtCore.QRect(430, 30, 41, 41))
        self.loadTargetPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loadTargetPushButton.setObjectName("loadTargetPushButton")
        self.logGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.logGroupBox.setGeometry(QtCore.QRect(520, 10, 491, 471))
        self.logGroupBox.setStyleSheet("font: 75 10pt \"楷体\";")
        self.logGroupBox.setObjectName("logGroupBox")
        self.logTextEdit = QtWidgets.QTextEdit(self.logGroupBox)
        self.logTextEdit.setGeometry(QtCore.QRect(20, 30, 451, 421))
        self.logTextEdit.setObjectName("logTextEdit")
        self.saveProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.saveProgressBar.setGeometry(QtCore.QRect(10, 280, 491, 41))
        self.saveProgressBar.setStyleSheet("font: 75 10pt \"楷体\";")
        self.saveProgressBar.setProperty("value", 24)
        self.saveProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.saveProgressBar.setObjectName("saveProgressBar")
        self.startPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startPushButton.setGeometry(QtCore.QRect(200, 350, 93, 41))
        self.startPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startPushButton.setStyleSheet("font: 75 12pt \"楷体\";")
        self.startPushButton.setObjectName("startPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 26))
        self.menubar.setObjectName("menubar")
        self.programMenu = QtWidgets.QMenu(self.menubar)
        self.programMenu.setObjectName("programMenu")
        self.optionMenu = QtWidgets.QMenu(self.menubar)
        self.optionMenu.setObjectName("optionMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.exitAction.triggered.connect(QtWidgets.QApplication.quit)
        self.insideAreaAction = QtWidgets.QAction(MainWindow)
        self.insideAreaAction.setObjectName("insideAreaAction")
        self.insideAreaAction.setCheckable(True)
        self.insideAreaAction.setChecked(True)
        self.insideAreaAction.triggered.connect(self.setModeInside)
        self.outsideAreaAction = QtWidgets.QAction(MainWindow)
        self.outsideAreaAction.setObjectName("outsideAreaAction")
        self.outsideAreaAction.setCheckable(True)
        self.outsideAreaAction.triggered.connect(self.setModeOutside)
        self.inoutAction = QtWidgets.QAction(MainWindow)
        self.inoutAction.setObjectName("inoutAction")
        self.inoutAction.triggered.connect(self.setModeInOut)
        self.inoutAction.setCheckable(True)
        self.programMenu.addAction(self.exitAction)
        self.optionMenu.addAction(self.insideAreaAction)
        self.optionMenu.addAction(self.outsideAreaAction)
        self.optionMenu.addAction(self.inoutAction)
        self.menubar.addAction(self.programMenu.menuAction())
        self.menubar.addAction(self.optionMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sourceGroupBox.setTitle(_translate("MainWindow", "源文件路径"))
        self.loadSourcePushButton.setText(_translate("MainWindow", "..."))
        self.targetGroupBox.setTitle(_translate("MainWindow", "输出目录"))
        self.loadTargetPushButton.setText(_translate("MainWindow", "..."))
        self.logGroupBox.setTitle(_translate("MainWindow", "日志"))
        self.startPushButton.setText(_translate("MainWindow", "开始"))
        self.programMenu.setTitle(_translate("MainWindow", "程序"))
        self.optionMenu.setTitle(_translate("MainWindow", "选项"))
        self.exitAction.setText(_translate("MainWindow", "退出"))
        self.insideAreaAction.setText(_translate("MainWindow", "区域内"))
        self.outsideAreaAction.setText(_translate("MainWindow", "区域外"))
        self.inoutAction.setText(_translate("MainWindow", "区域内 + 区域外"))

    def setModeInside(self):
        self.saveMode = 0
        self.addLog("保存给定区域内部的点。", color="blue")
        self.insideAreaAction.setChecked(True)
        self.outsideAreaAction.setChecked(False)
        self.inoutAction.setChecked(False)

    def setModeOutside(self):
        self.saveMode = 0
        self.addLog("保存给定区域外部的点。", color="blue")
        self.insideAreaAction.setChecked(False)
        self.outsideAreaAction.setChecked(True)
        self.inoutAction.setChecked(False)

    def setModeInOut(self):
        self.saveMode = 0
        self.addLog("保存所有点。", color="blue")
        self.insideAreaAction.setChecked(False)
        self.outsideAreaAction.setChecked(False)
        self.inoutAction.setChecked(True)

    def onSetSourcePathButtonClick(self):
        fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                    "选取源数据文件路径",
                                                                    "./",
                                                                    "Csv Files (*.csv)")
        self.sourceLineEdit.setText(fileName)
        sourceFile = fileName
        # pass

    def onSetTargetCategoryButtonClick(self):
        directory1 = QtWidgets.QFileDialog.getExistingDirectory
        pass

    def onStartButtonClick(self):
        pass

    def addLog(self, text, color="black", size="3"):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        content = self._formatString("%s: %s\n" % (now, text), color, size)
        self.logTextEdit.append(content)

    def _formatString(self, text, color="black", size="3"):
        return "<font size=\"" + size + "\" " \
                    "color=\"" + color + "\">" + text + "</font>"


