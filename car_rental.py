##################################
# Name: Shi Lin (Joanna) Chen    
# This program computes the rental cost of a car based on the classification code.
# The program asks for user input for the user's name, classification code, the number of days the car is rented for,
# the starting odometer reading and the ending odometer reading. The program then computes the total rental cost.
##################################

# receiving user input for name, classification code, and details about the car rental
name = input('What is your name? ')
classCode = input('What is your classification code? ')
daysRented = int(input('How many days did you rent the car for? '))
startOdometer = int(input('When was the odometer reading at the start of the rental period? '))
endOdometer = int(input('When was the odometer reading at the end of the rental period? '))

# initializations for variables
base = 0
bill = 0.0
error = False
kilometersDriven = endOdometer - startOdometer
kilometersDrivenAverage = kilometersDriven / daysRented
weeksRented = 0

# initializations for constants
CHARGE_RATE = 0.25

# shows all the car rental information
def showSummary():
	print()
	print('Name: ' + name)
	print('Classification code: %s' % classCode)
	print('Number of days rented: %d' % daysRented)
	print('Starting odometer reading: %d' % startOdometer)
	print('Ending odometer reading: %d' % endOdometer)
	print('Number of kilometers driven during rental period: %d' % kilometersDriven)
	print('Rental Cost: $%.2f' % bill)

# calculation for budget classification code
if classCode == 'B' or classCode == 'b':
	base = 40 
	bill = base * daysRented + kilometersDriven * CHARGE_RATE

# calculation for daily classification code
elif classCode == 'D' or classCode == 'd':
	base = 60
	if kilometersDrivenAverage <= 100:
		bill = base * daysRented
	else:
		print(kilometersDrivenAverage)
		bill = base * daysRented + CHARGE_RATE * (kilometersDrivenAverage - 100) * daysRented

# calculation for weekly classification code
elif classCode == 'W' or classCode == 'w':
    # checking whether or not there is a fraction of week
	if daysRented % 7 == 0:
		weeksRented = daysRented / 7
	else:
        # count the fraction of a week as a full week
		weeksRented = daysRented // 7 + 1

	base = 190
	kilometersDrivenWeekly = kilometersDriven / weeksRented

	if kilometersDrivenWeekly <= 900:
		bill = base * weeksRented
	elif kilometersDrivenWeekly <= 1500:
		base += 50
		bill = base * weeksRented
	else:
		base += 100
		bill = base * weeksRented + CHARGE_RATE * (kilometersDrivenWeekly - 1500) * weeksRented
	
else:
    # error message in the case that the user enters an invalid classification code
	print('Error: Invalid classification code.')
	error = True

if error == False:
    # show the car rental information (including the bill amount)
	showSummary()


