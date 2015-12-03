'''
Name: Shi Lin (Joanna) Chen    
This program computes whether there are sufficient parts in inventory to build given 
widgets, by taking in information from two text files. If a widget can be built based on 
the inventory, then the cost and the parts used for the widget. Otherwise, the user is 
alerted that the widget cannot be built and told which parts are insufficient.
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
			
def main():
	wFile = open("widgets.txt", "r")

	# add the parts to the inventory 
	inventory = PartInventory()
	inventory.addParts("parts.txt")
	
	# output starting inventory
	print('Starting Inventory: ')
	for part in inventory.getInventory():
		print(part.getName() + ' | Quantity: ' + str(part.getQuantity()))
	print()
	
	# declare and initialize variables 
	buildable = True
	cost = 0
	missingParts = ''
	widget = {}
	
	# output widget building information
	print(wFile.readline())
	for line in wFile:
		# for each widget 
		if line == '\n':
			if buildable == True:
				print('The widget can be built for $%.2f' % (cost))
				print('Parts Used:')
				for part in inventory.getInventory():
					if part.getName() in widget:
						print(part.getName() + ': ' + str(int(part.getQuantity()) - widget[part.getName()]))
						part.setQuantity(widget[part.getName()]) # reduce quantity used
						if part.getQuantity() == 0:
							inventory.removePart(part)
			else: 
				print('It cannot be built')
				print('There is an insufficient supply of the following parts:' + missingParts[1:])
				
			missingParts = ''
			buildable = True
			widget = {}
			cost = 0
			print()
			print(wFile.readline())
			continue
			
			# iterate through all the parts required for a widget
		else: 
			thePart = line.split()
			widget[thePart[0]] = int(thePart[1])
			
			found = False
			
			while found == False:
				# check if the part required is in inventory
				for part in inventory.getInventory():
					if thePart[0] == part.getName() and int(thePart[1]) <= part.getQuantity(): 
						found = True
						# compute cost
						cost = cost + float(part.getPrice()) * int(thePart[1])
						widget[thePart[0]] = part.getQuantity() - int(thePart[1]) 
				if found == False:
					buildable = False
					missingParts = missingParts + ', ' + thePart[0]	
					break
					
	# output ending inventory				
	print('Ending Inventory: ')			
	for part in inventory.getInventory():
		print(part.getName() + ' | Quantity: ' + str(part.getQuantity()))
		
	wFile.close()
				
main()	