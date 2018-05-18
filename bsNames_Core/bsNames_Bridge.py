from Modules.Qt import QtCore, QtGui, QtWidgets
import os
from functools import partial

import Modeling.Maya_Modeling_bsCreator.bsNames_Core.bsNames_Core
reload(Modeling.Maya_Modeling_bsCreator.bsNames_Core.bsNames_Core)
from Modeling.Maya_Modeling_bsCreator.bsNames_Core.bsNames_Core import bsNamer

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

		self.curr = 0


	def duplicate(self):
		'''
		'''
		self.xAxis.setEnabled(True)
		self.yAxis.setEnabled(True)
		self.dupMeshes = self.core.main(self.bsList)

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

		#sliders separation
		self.lbl_xAxis = QtWidgets.QLabel()
		self.lbl_xAxis.setText('Distance on X')
		self.lbl_xAxis.setAlignment(QtCore.Qt.AlignCenter)
		self.lbl_yAxis = QtWidgets.QLabel()
		self.lbl_yAxis.setText('Distance on Y')
		self.lbl_yAxis.setAlignment(QtCore.Qt.AlignCenter)
		self.xAxis = QtWidgets.QSlider()
		self.yAxis = QtWidgets.QSlider()
		self.xAxis.setEnabled(False)
		self.yAxis.setEnabled(False)
		self.xAxis.setOrientation(QtCore.Qt.Horizontal)
		self.yAxis.setOrientation(QtCore.Qt.Horizontal)
		self.window.lyt_vertical_basic.addWidget(self.lbl_xAxis)
		self.window.lyt_vertical_basic.addWidget(self.xAxis)
		self.window.lyt_vertical_basic.addWidget(self.lbl_yAxis)
		self.window.lyt_vertical_basic.addWidget(self.yAxis)

		self.xAxis.valueChanged[int].connect(partial(self.sliderSeparate, '.translateX'))
		self.yAxis.valueChanged[int].connect(partial(self.sliderSeparate, '.translateY'))

		self.sliderAttrs(self.xAxis)
		self.sliderAttrs(self.yAxis)
		
	def sliderSeparate(self, attr, value):
		
			if self.curr < value:
				self.core.separateBS(self.bsList, attr, value, 1)
				self.curr = value
			else:
				self.core.separateBS(self.bsList, attr, value, -1)
				self.curr = value

	def sliderAttrs(self, slider):
			slider.setMinimum(1)
			slider.setMaximum(5)
			slider.setSingleStep(1)
			slider.setValue(1)

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