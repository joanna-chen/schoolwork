# import modules 
from plotpoints import createGrid
from plotpoints import drawDots
from graphics import GraphicsWindow

# get user input
pollMax = int(input('What is the maximum amount of pollutant? '))
pollRate = float(input('What is the rate at which the pollutant is leaking? '))
minutes = int(input('How many minutes to run the simulation? '))

# initialize pollution level variables
poll1 = 0
poll2 = 0
poll3 = 0
pollLeak = 0
poll = {0: [0, 0, 0, 0]}

# constant values 
RATE_BETWEEN_POND = 0.005

# create the graphics window and get the canvas
win = GraphicsWindow(500, 500)
canvas = win.canvas()

def main():
    createGrid(canvas, minutes, int(pollMax))
    
    # calculate pollution levels of every minute
    for i in range(1, minutes):
        poll[i] = [pond1(i), pond2(i), pond3(i), pollutantLeak(i)]
        
    # print pollution levels for each hour
    for i in range(60, minutes, 60):
        if i < minutes:
            print('Minutes: ', i)
        else:
            print('Minutes [FINAL]: ', i)
        print('Pond 1: ', poll[i][0], ' Pond 2: ', poll[i][1], ' Pond 3: ', poll[i][2])
     
    # print pollution level for after 1440 minutes    
    if minutes <= 1440:
        print('Minutes: 1440')
        print('Pond 1: ', pond1(1440), ' Pond 2: ', pond2(1440), ' Pond 3: ', pond3(1440))
        
# calculate the amount of pollutant flowing into the ponds        
def pollutantLeak(t):
    pollLeak = t * pollRate
    if pollLeak <= pollMax:
    	return pollLeak - (t-1)*pollRate
    else:
    	return 0

# calculate pollutant level of Pond 1 and plot pollutant amount on graph
def pond1(t):
    inflow3 = RATE_BETWEEN_POND*poll[t-1][2] 
    outflow2 = RATE_BETWEEN_POND*poll[t-1][0]
    poll1 = poll[t-1][0] + inflow3 - outflow2 + pollutantLeak(t) 
    drawDots(canvas, t, minutes, poll1, pollMax, "red")
    return round(poll1, 5)

# calculate pollutant level of Pond 2 and plot pollutant amount on graph
def pond2(t):
    inflow1 = RATE_BETWEEN_POND*poll[t-1][0]
    outflow3 = RATE_BETWEEN_POND*poll[t-1][1]
    poll2 = poll[t-1][1] + inflow1 - outflow3
    drawDots(canvas, t, minutes, poll2, pollMax, "green")
    return round(poll2, 5)

# calculate pollutant level of Pond 3 and plot pollutant amount on graph
def pond3(t):
    inflow2 = RATE_BETWEEN_POND*poll[t-1][1]
    outflow1 = RATE_BETWEEN_POND*poll[t-1][2]
    poll3 = poll[t-1][2] + inflow2 - outflow1
    drawDots(canvas, t, minutes, poll3, pollMax, "blue")
    return round(poll3, 5)

if __name__ == "__main__":
    main()




