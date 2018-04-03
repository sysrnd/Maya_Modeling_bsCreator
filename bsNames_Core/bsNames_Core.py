import maya.cmds as cmds

class bsNamer(object):
	def __init__(self):
		pass
	def main(self, dictBS):
		mainMesh = self.getMainMesh()
		total = 0
		for mesh, coords in dictBS.iteritems():
			total += 1
			newBS = cmds.duplicate(mainMesh, n=mesh)[0]
			cmds.setAttr(newBS + '.translateX', int(coords[0]))
			cmds.setAttr(newBS + '.translateY', int(coords[1]))

		return total

	def getMainMesh(self):
		for mesh in cmds.ls(et='mesh'):
			if mesh.find('CABEZA') != -1 and mesh.find('MD') != -1:
				meshParent = cmds.listRelatives(mesh, p=True)

		return meshParent