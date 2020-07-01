import random

def hangman(word):
	wrong = 0 #number of wrong guesses

	stages = ["",
		  "___________ 		",
		  "|			",
		  "|	      |		",
		  "|	      o		",
		  "|	     /|\	",
		  "|	     / \	",
		  "|			"
		  ]

	letters_in_a_list = list(word) #stores each letter in a list
	your_guess = ["_"] * len(word) #initially prints "_" instead of letters
	win = False
	print("Win or Die")

	while wrong < len(stages) - 1:		
		print("\n")
		letter = "Enter the letter: "
		char = input(letter)
		if char in letters_in_a_list:
			for i in range(len(letters_in_a_list)): #loop for multiple identical letters
				if char not in letters_in_a_list: #continues if the letter's unique
					continue
				else:
					n = letters_in_a_list.index(char) #finds an index of the correct letter
					your_guess[n] = char #replaces "_" with the letter in your_guess
					letters_in_a_list[n] = '0' #changes correct letter to '0', so other identical letters can be found
		else:
			wrong += 1 #increments if guess is wrong
		print((" ".join(your_guess)))
		e = wrong + 1 #to cut the stages list
		print("\n".join(stages[0: e]))
		if "_" not in your_guess: #if a player guesses each letter, s/he wins
			print("YOU WIN! The word is ")
			print(" ".join(your_guess))
			win = True
			break
	if not win: #id win is still False
		print("\n".join(stages[0: wrong + 1]))
		print("YOU LOSE! The word is {}.".format(word))

q_a = [ "coronavirus", 
	"fuji", 
	"fizzbuzz", 
	"telangana", 
	"constant", 
	"collaboration",
	"heterogeneous",
	"obscura",
	"eureka",
	"assembler",
	"ubuntu",
	"cacoethes",
	"boffola",
	"breatharian"]

hangman(q_a[random.randint(0, len(q_a))])
