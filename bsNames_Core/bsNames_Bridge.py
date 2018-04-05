from Modules.Qt import QtCore, QtGui, QtWidgets
import os

import Modeling.Maya_modeling_bsCreator.bsNames_Core.bsNames_Core
reload(Modeling.Maya_modeling_bsCreator.bsNames_Core.bsNames_Core)
from Modeling.Maya_modeling_bsCreator.bsNames_Core.bsNames_Core import bsNamer

class bsNamesBridge(object):
	def __init__(self, window):
		'''
		'''
		self.core = bsNamer()
		self.window = window
		self.window.btn_duplicate.clicked.connect(self.duplicate)

		self.bsList = {}
		BSfile = self.getFile('/bs_list.mkf')
		self.readLocalInfo(BSfile)

		self.populateUI()

		reg_ex = QtCore.QRegExp("[a-zA-Z0-9_]+")
		validator = QtGui.QRegExpValidator(reg_ex, self.window.txt_charName)
		self.window.txt_charName.setValidator(validator)

	def duplicate(self):
		'''
		'''
		contador = self.core.main(self.bsList)
		self.window.lbl_status.setText('Se duplicaron ' + str(contador) + ' blendshapes')
		#self.core.getMainMesh()

	def populateUI(self):
		'''
		'''
		#QlistWidgetBlock
		self.window.list_bs.setSortingEnabled(True)
		self.window.list_bs.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		
		for key, item in self.bsList.iteritems():
			qtItem = QtWidgets.QListWidgetItem()
			qtItem.setText(key)
			self.window.list_bs.addItem(qtItem)

	
	def readLocalInfo(self, BSfile):
		'''
		'''

		with open(str(BSfile), 'r') as f:
			data = f.readlines()
		
		for bs in data:
			self.bsList[bs.split(':')[0]] = bs.split(':')[1], bs.split(':')[2].strip('\r\n')
		
		return data

	def getFile(self, string):
		'''
		'''

		BSfile = os.path.dirname(__file__)
		BSfile = BSfile.replace('\\', '/')
		BSfile = BSfile + string

		return BSfile

	def writeLocalInfo(self, file, txt):
		with open(file + '.txt','w') as f:
			data = f.write(txt)