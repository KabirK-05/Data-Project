# build pascals triangle and use it to create graph
# use random variable to traverse down with random left or right direction
import random 
import math

#main tree
result = [[1]]
graphPosition = [0,0]

def generateTriangle(numRows: int):
	# list of lists containing rows
	global result
	global resultCopy

	for i in range(numRows-1):
		#to make next row, make temp list with 0's on ends and tails to add
		tmp = [0] + result[-1] + [0]

		#not mutating main list, create empty row first then when complete append
		emptyRow = []

		#nested loop to make each succesive row
		for j in range(len(result[-1])+1):
			#using 2 pointers add to emptyRow
			emptyRow.append(tmp[j] + tmp[j+1])

		#zeroes in graph:
		if i+1 == 4:
			emptyRow = [1,0,6,0,1]
		if i+1 == 6:
			emptyRow = [1,2,7,0,7,2,1]
		if i+1 == 8:
			emptyRow = [1,4,12,16,0,16,12,4,1]
		if i+1 == 9:
			emptyRow = [1,5,16,0,16,16,0,16,5,1]

		result.append(emptyRow)



#traverse given result and start guessing 
def traverse():
	nodePosition = 0
	global graphPosition
	
	x,y = graphPosition[0], graphPosition[1]
	#mine points
	points = {4:-20,6:-15,8:-10,9:-5}
	#points for making it to the end
	finalPoints = {1:30,6:20,21:5,16:15,32:1}

	for i in range(1,len(result)):
		coinFlip = random.randint(0,1)
		#let 0 = heads (move left)
		#let 1 = tails (move right)
		
		if coinFlip == 0:
			#move down left
			nodePosition = nodePosition
			graphPosition = [i,nodePosition]
			x,y = graphPosition[0], graphPosition[1]

		else:
			#move down right
			nodePosition += 1
			graphPosition = [i,nodePosition]
			x,y = graphPosition[0], graphPosition[1]

		#print(x,y)

		if result[x][y] == 0:
			lossPoints = points[x]
			return lossPoints 

	#store vector coordinates in terms of main result
	# if they made it to the end, return the last value
	finalResult = result[x][y]
	return finalPoints[finalResult]


wins = 0
lose = 0
totalPoints = 0

#generate pascals triangle with 11 rows
#run simulation "iteration" number of times
generateTriangle(11)
iterations = 10000

#simulating if player made it to the end:
for i in range(iterations):
	traverseResult = traverse()
	traverseResult += 10
	totalPoints += traverseResult
	x,y = graphPosition

	if x == 10:
		wins += 1
	else:
		lose += 1

p1 = 0
p2 = 0

#simulating player 1 against player 2
for i in range(iterations):
	p1Points = traverse()
	p2Points = traverse()

	if p1Points>p2Points:
		p1+=1
	elif p2Points>p1Points:
		p2+=1

	while p1Points == p2Points:
		p1Points = traverse()
		p2Points = traverse()
		if p1Points>p2Points:
			p1+=1
		elif p2Points>p1Points:
			p2+=1

print("Number of trials: ", iterations)

print("Number of wins: ",wins, "Number of losses: ",lose)
print("expected value: ", totalPoints/iterations)

print("Player 1 Wins: ", p1, "Player 2 Wins: ", p2)
