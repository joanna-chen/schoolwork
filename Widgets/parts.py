'''
Name: Shi Lin (Joanna) Chen    
This program computes the
'''

class Parts():
	def __init__(self, name, price, quantity):
		self.partName = name
		self.partPrice = price
		self.partQuantity = quantity
	
	# getter methods
	def getName(self):
		return self.partName
		
	def getPrice(self):
		return self.partPrice
		
	def getQuantity(self):
		return self.partQuantity
		
	# setter methods	
	def setName(self, name):
		self.partName = name
	
	def setPrice(self, price): 
		self.partPrice = price
		
	def setQuantity(self, quantity):
		self.partQuantity = quantity
	
	def equals(self, other):
		if self.partName == other.partName:
			return True
		else:
			return False
	
class PartInventory():
	def __init__(self):
		self.partsInventory = []
		
	def addParts(self, fileName):
		file = open(fileName, "r")
		partName = []
		for line in file: 
			l = line.split()
			partName = Parts(l[0], l[1], l[2])
			self.partInventory.append(partName)
			
	def getParts(self):
		return self.partsInventory
	
	def removePart(self, part):
		self.partsInventory.remove(part)
		
def widgetCost(widget):
	partsThere = True
	while partsThere:
		for part in widget:
			if not part in inventory:
				partsThere = False
			# count how many parts
				
		
def widgetInfo(widgetFile):
	wFile = open(widgetFile, "r")
	widget = []
	for line in wFile: 
		if line == '\n':
			continue
			widgetCost(widget) 
			widget = {}
		else:
			widget.append(line)
			
	
def main():
	inventory = PartInventory()
	inventory.addParts(parts.txt)