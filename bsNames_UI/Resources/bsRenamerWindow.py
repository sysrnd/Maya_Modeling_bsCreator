# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\RnD\Pipeline\Maya\Scripts\Modeling\Maya_modeling_bsCreator\bsNames_UI\Resources\bsRenamerWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_window_bsNamer(object):
    def setupUi(self, window_bsNamer):
        window_bsNamer.setObjectName(_fromUtf8("window_bsNamer"))
        window_bsNamer.resize(290, 239)
        self.lyt_main = QtGui.QWidget(window_bsNamer)
        self.lyt_main.setObjectName(_fromUtf8("lyt_main"))
        self.verticalLayout = QtGui.QVBoxLayout(self.lyt_main)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lyt_middle = QtGui.QGridLayout()
        self.lyt_middle.setObjectName(_fromUtf8("lyt_middle"))
        self.wdgt_tabs = QtGui.QTabWidget(self.lyt_main)
        self.wdgt_tabs.setObjectName(_fromUtf8("wdgt_tabs"))
        self.tab_basic = QtGui.QWidget()
        self.tab_basic.setObjectName(_fromUtf8("tab_basic"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_basic)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lyt_vertical_basic = QtGui.QVBoxLayout()
        self.lyt_vertical_basic.setObjectName(_fromUtf8("lyt_vertical_basic"))
        self.txt_charName = QtGui.QLineEdit(self.tab_basic)
        self.txt_charName.setObjectName(_fromUtf8("txt_charName"))
        self.lyt_vertical_basic.addWidget(self.txt_charName)
        self.verticalLayout_3.addLayout(self.lyt_vertical_basic)
        self.wdgt_tabs.addTab(self.tab_basic, _fromUtf8(""))
        self.tab_advanced = QtGui.QWidget()
        self.tab_advanced.setObjectName(_fromUtf8("tab_advanced"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_advanced)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lyt_vertical_advanced = QtGui.QVBoxLayout()
        self.lyt_vertical_advanced.setObjectName(_fromUtf8("lyt_vertical_advanced"))
        self.list_bs = QtGui.QListView(self.tab_advanced)
        self.list_bs.setObjectName(_fromUtf8("list_bs"))
        self.lyt_vertical_advanced.addWidget(self.list_bs)
        self.verticalLayout_5.addLayout(self.lyt_vertical_advanced)
        self.wdgt_tabs.addTab(self.tab_advanced, _fromUtf8(""))
        self.lyt_middle.addWidget(self.wdgt_tabs, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.lyt_middle)
        self.lyt_vertical_bottom = QtGui.QVBoxLayout()
        self.lyt_vertical_bottom.setContentsMargins(10, -1, 10, -1)
        self.lyt_vertical_bottom.setObjectName(_fromUtf8("lyt_vertical_bottom"))
        self.btn_duplicate = QtGui.QPushButton(self.lyt_main)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_duplicate.setFont(font)
        self.btn_duplicate.setObjectName(_fromUtf8("btn_duplicate"))
        self.lyt_vertical_bottom.addWidget(self.btn_duplicate)
        self.lbl_status = QtGui.QLabel(self.lyt_main)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_status.setFont(font)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.lyt_vertical_bottom.addWidget(self.lbl_status)
        self.verticalLayout.addLayout(self.lyt_vertical_bottom)
        window_bsNamer.setCentralWidget(self.lyt_main)
        self.menubar = QtGui.QMenuBar(window_bsNamer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 290, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        window_bsNamer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(window_bsNamer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
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

