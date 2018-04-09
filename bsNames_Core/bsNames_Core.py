import maya.cmds as cmds

class bsNamer(object):
	def __init__(self):
		pass
		
	def main(self, dictBS):
		bsList = self.dupBS(dictBS)
		#self.checkHierarchy()

	def getMainMesh(self):
		'''
		'''
		for mesh in cmds.ls(et='mesh'):
			if mesh.find('CABEZA') != -1 and mesh.find('MD') != -1:
				meshParent = cmds.listRelatives(mesh, p=True)

		return meshParent

	def dupBS(self, dictBS):
		'''
		'''
		bsList = []

		mainMesh = self.getMainMesh()
		for mesh, coords in dictBS.iteritems():
			newBS = cmds.duplicate(mainMesh, n=mesh)[0]
			bsList.append(newBS)

			cmds.setAttr(newBS + '.translateX', int(coords[0]))
			cmds.setAttr(newBS + '.translateY', int(coords[1]))

		cmds.group(bsList, n='GRP_BLENDSHAPES')
		return bsList


	def checkHierarchy(self):
		'''
		pending approval
		'''
		isGRP_GEO = False
		grpGeo = ''

		for grp in cmds.ls(et='transform'):
			if grp.endswith("GRP_GEO"):
				grpGeo = grp
				isGRP_GEO = True
				break
			else:
				continue

		
		if isGRP_GEO == False:
			cmds.select(cl=True)
			grpGeo = cmds.group(em=True, n='GRP_GEO')[0]


		for mesh in cmds.ls(et='mesh'):
			meshParent = cmds.listRelatives(mesh, p=True)[0]
			if meshParent.endswith('BS') == True and cmds.listRelatives(meshParent, p=True)[0] != isGRP_GEO:
				
				cmds.select(cl=True)
				cmds.parent(meshParent, grpGeo)
		