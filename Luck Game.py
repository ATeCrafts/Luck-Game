import random

def roll():
    number = random.randint(1, 6)
    return number

def inputPlayers():
    while True:
        try:
            players = int(input("Enter the number of players (1-4): "))
            break
        except:
            print("Invalid input!")
    return players

players = inputPlayers()
while players < 1 or players > 4:
    print("Invalid input!")
    players = inputPlayers()

maxScore = 100
playerScores = [0 for i in range(players)]

while max(playerScores) < maxScore:
    for i in range(players):
        print("\nPlayer", i+1, "turn has started!")
        print("Your total score is:", playerScores[i], "\n")
        currentScore = 0

        while True:
            rollQ = input("Would you like to roll (y/n)?: ")
            while rollQ != "y" and rollQ != "n":
                print("Invalid input!")
                rollQ = input("Would you like to roll (y/n)?: ")
            
            if rollQ == "n":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                currentScore = 0
                playerScores[i] -= 10
                break
            else:
                currentScore += value
                playerScores[i] += value
                print("You rolled a:", value)
            
            print("Your score is:", currentScore)

            if playerScores[i] >= maxScore:
                break
        
        print("Your total score is:", playerScores[i])

print("Player", playerScores.index(max(playerScores)) + 1, "won with a score of:", max(playerScores))