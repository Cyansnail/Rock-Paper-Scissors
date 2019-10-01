import random
# Isaac Lynn
# Period 4
#Variables:
pScore = 0 
cScore = 0
ties = 0
computerChoices = ["s","p","r"]
# Three main pieces: 
# Welcome message
print("Welcome to Rock Paper Scissors!") 
print( )
print("The official rules of Rock, Paper, Scissors:")
print(" 1.Rock beats Scissors")
print(" 2.Scissors beats Paper")
print(" 3.Paper beats Rock")
print( )
pName = input("What is your name? ")
# Game loop

# Final score 
def pintscore():
# Write message 
	print("The score is: ")
# Write player score
	print(pName + ":" + str(pScore))
# Write computer score
	print("Computer: " + str(cScore))
# Write how many ties
	print("Ties: " + str(ties))

# Game loop
# Make forever loop
while True:
	print("\n")
	# Print current score 
	pintscore()
	# Prompt for a choice (r for rock, p for paper, s for scissors, q for quit)
	pChoice = input("Enter r (rock), p (paper), s (scissors), or q (quit): ") 
	if pChoice == "q":
		break
	# Deals with q 
	# Get computer's choice
	cChoice = random.choice(computerChoices)
	# compare for player entering r 
	if pChoice == "r":
		print(pName + " picked Rock")
		# If computer is r 
		if cChoice == "r":
			print("Computer picked Rock")
			print("It's a tie")
			ties = ties + 1
		# If computer is p
		elif cChoice == "p":
			print("Computer picked Paper")
			print("The computer wins")
			cScore = cScore + 1
		# If computer is s
		else:
			print("Computer picked Scissors")
			print("You win!")
			pScore = pScore + 1
	# compare for player entering p
	elif pChoice == "p":
		print(pName + " picked Paper")
		# If computer is r 
		if cChoice == "r":
			print("Computer picked Rock")
			print("You win!")
			pScore = pScore + 1
		# If computer is p
		elif cChoice == "p":
			print("Computer picked Paper")
			print("It's a tie")
			ties = ties + 1
		# If computer is s
		else:
			print("Computer picked Scissors")
			print("The computer wins")
			cScore = cScore + 1
		
	# compare for player entering s 
	elif pChoice == "s":
		print(pName + " picked Scissors")
		# If computer is r 
		if cChoice == "r":
			print("Computer picked Rock")
			print("The computer wins")
			cScore = cScore + 1
		# If computer is p
		elif cChoice == "p":
			print("Computer picked Paper")
			print("You win!")
			pScore = pScore + 1
		# If computer is s
		else:
			print("Computer picked Scissors")
			print("It's a tie")
			ties = ties + 1
	# deal with player entering anything else
	else:
		print("You do know this is rock, paper, scissors, don't you?")

