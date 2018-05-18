import sys
import platform
from Modules.Qt import QtCore, QtGui, QtWidgets
import Modeling.Maya_Modeling_bsCreator.bsNames_UI.bsRenamerWindow_Qt5
reload(Modeling.Maya_Modeling_bsCreator.bsNames_UI.bsRenamerWindow_Qt5)
from Modeling.Maya_Modeling_bsCreator.bsNames_UI.bsRenamerWindow_Qt5 import Ui_window_bsNamer

import Modeling.Maya_Modeling_bsCreator.bsNames_Core.bsNames_Bridge
reload(Modeling.Maya_Modeling_bsCreator.bsNames_Core.bsNames_Bridge)
from Modeling.Maya_Modeling_bsCreator.bsNames_Core.bsNames_Bridge import bsNamesBridge#import alembicExportBridge

class MyApplication(QtWidgets.QMainWindow, Ui_window_bsNamer):

	def __init__(self, parent=None):
		super(MyApplication, self).__init__(parent)
		self.setupUi(self)

if __name__ != "__main__":
	try:
		app = QtWidgets.QApplication(sys.argv)
	except:
		app = QtCore.QCoreApplication.instance()
	window = MyApplication()
	window.setWindowFlags(
		window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
	interfaceMacho = bsNamesBridge(window=window)
	window.show()

	try:
		sys.exit(app.exec_())
	except:
		"error al intentar salir"


