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
		return int(self.partQuantity)
		
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
		partNum = 0
		file = open(fileName, "r")
		for line in file: 
			l = line.split()
			partNum = Parts(l[0], l[1], l[2])
			self.partsInventory.append(partNum)
			
	def getInventory(self):
		return self.partsInventory
			
	def removePart(self, part):
		self.partsInventory.remove(part)
		
''' old code		
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
'''			
#
'''
wFile = open("widgets.txt", "r")
buildable = True
cost = 0
missingParts = ''
wFile.readline()
for line in wFile: 
	if line == '\n':
		if buildable = True:
			print('The widget can be built for $%f.2' % cost)
		else: 
			print('It cannot be built')
			print('There is an insufficient supply of the following parts:' + missingParts[1:])
		missingParts = ''
		buildable = True
		print()
		wFile.readline()
		continue
		# check if there's enough w
	else: 
		thePart = line.split()
		if thePart[0] in inventory.getInventory: 
			cost = cost + thePart[0].getPrice() * thePart[1]
			thePart[0].setQuantity(thePart[1])
			if thePart[0].getQuantity() == 0:
				inventory.removePart(thePart[0])
		else: # no such part in inventory
			buildable = False
			missingParts = missingParts + ', ' + thePart[0]		
'''
#			
	
def main():
	inventory = PartInventory()
	inventory.addParts("parts.txt")
	print(inventory.getInventory()) ###
	
	wFile = open("widgets.txt", "r")
	buildable = True
	cost = 0
	missingParts = ''
	widget = {}
	print(wFile.readline())
	for line in wFile: 
		if line == '\n':
			if buildable == True:
				print('The widget can be built for $%.2f' % (cost))
				for part in inventory.getInventory():
					if part.getName() in widget:
						part.setQuantity(widget[part.getName()])
						print(part.getQuantity())
						if part.getQuantity() == 0:
							inventory.removePart(part)
			else: 
				print('It cannot be built')
				print('There is an insufficient supply of the following parts:' + missingParts[1:])
			missingParts = ''
			buildable = True
			widget = {}
			print()
			print(wFile.readline())
			continue
			# check if there's enough w
		else: 
			thePart = line.split()
			widget[thePart[0]] = int(thePart[1])
			print(thePart)
			found = False
			while found == False:
				for part in inventory.getInventory():
					print(part.getName(), part.getQuantity()) ### 
					if thePart[0] == part.getName() and int(thePart[1]) <= part.getQuantity(): 
						found = True
						cost = cost + float(part.getPrice()) * float(thePart[1])
						widget[thePart[0]] = part.getQuantity() - int(thePart[1]) 
				if found == False:
					buildable = False
					missingParts = missingParts + ', ' + thePart[0]	
					break
				
		# need to not subtract amount if not buildable
					
				
main()	