from Modules.Qt import QtCore, QtGui, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_window_bsNamer(object):
    def setupUi(self, window_bsNamer):
        window_bsNamer.setObjectName("window_bsNamer")
        window_bsNamer.resize(290, 239)
        self.lyt_main = QtWidgets.QWidget(window_bsNamer)
        self.lyt_main.setObjectName("lyt_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.lyt_main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lyt_middle = QtWidgets.QGridLayout()
        self.lyt_middle.setObjectName("lyt_middle")
        self.wdgt_tabs = QtWidgets.QTabWidget(self.lyt_main)
        self.wdgt_tabs.setObjectName("wdgt_tabs")
        self.tab_basic = QtWidgets.QWidget()
        self.tab_basic.setObjectName("tab_basic")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_basic)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lyt_vertical_basic = QtWidgets.QVBoxLayout()
        self.lyt_vertical_basic.setObjectName("lyt_vertical_basic")
        self.txt_charName = QtWidgets.QLineEdit(self.tab_basic)
        self.txt_charName.setObjectName("txt_charName")
        self.lyt_vertical_basic.addWidget(self.txt_charName)
        self.verticalLayout_3.addLayout(self.lyt_vertical_basic)
        self.wdgt_tabs.addTab(self.tab_basic, "")
        self.tab_advanced = QtWidgets.QWidget()
        self.tab_advanced.setObjectName("tab_advanced")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_advanced)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lyt_vertical_advanced = QtWidgets.QVBoxLayout()
        self.lyt_vertical_advanced.setObjectName("lyt_vertical_advanced")
        self.list_bs = QtWidgets.QListWidget(self.tab_advanced)
        self.list_bs.setObjectName("list_bs")
        self.lyt_vertical_advanced.addWidget(self.list_bs)
        self.verticalLayout_5.addLayout(self.lyt_vertical_advanced)
        self.wdgt_tabs.addTab(self.tab_advanced, "")
        self.lyt_middle.addWidget(self.wdgt_tabs, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.lyt_middle)
        self.lyt_vertical_bottom = QtWidgets.QVBoxLayout()
        self.lyt_vertical_bottom.setContentsMargins(10, -1, 10, -1)
        self.lyt_vertical_bottom.setObjectName("lyt_vertical_bottom")
        self.btn_duplicate = QtWidgets.QPushButton(self.lyt_main)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_duplicate.setFont(font)
        self.btn_duplicate.setObjectName("btn_duplicate")
        self.lyt_vertical_bottom.addWidget(self.btn_duplicate)
        self.lbl_status = QtWidgets.QLabel(self.lyt_main)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_status.setFont(font)
        self.lbl_status.setObjectName("lbl_status")
        self.lyt_vertical_bottom.addWidget(self.lbl_status)
        self.verticalLayout.addLayout(self.lyt_vertical_bottom)
        window_bsNamer.setCentralWidget(self.lyt_main)
        self.menubar = QtWidgets.QMenuBar(window_bsNamer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 290, 21))
        self.menubar.setObjectName("menubar")
        window_bsNamer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_bsNamer)
        self.statusbar.setObjectName("statusbar")
        window_bsNamer.setStatusBar(self.statusbar)
        
        self.retranslateUi(window_bsNamer)
        self.wdgt_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window_bsNamer)


    def retranslateUi(self, window_bsNamer):
        window_bsNamer.setWindowTitle(_translate("window_bsNamer", "Blendshape Namer", None))
        self.txt_charName.setPlaceholderText(_translate("window_bsNamer", "Character Name", None))
        self.wdgt_tabs.setTabText(self.wdgt_tabs.indexOf(self.tab_basic), _translate("window_bsNamer", "Basic", None))
        self.wdgt_tabs.setTabText(self.wdgt_tabs.indexOf(self.tab_advanced), _translate("window_bsNamer", "Advanced", None))
        self.btn_duplicate.setText(_translate("window_bsNamer", "Duplicate", None))
        self.lbl_status.setText(_translate("window_bsNamer", "//", None))