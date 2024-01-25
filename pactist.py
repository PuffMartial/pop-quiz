def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in questions[question_num-1]:
            print(i)
            guess = input("enter A,B,C or D")
            guess = guess.upper()
            guesses.append(guess)
            
            correct_guesses += check_answer(quations.get(key),guess)
            question_num += 1

display_score(correct_guesses, guesses)

# --------------------------------------------------------------------------

def check_answer(answer, guess):
    if answer == guess:
        print("correct!")
        return 1
    else:
        print("incorrect!")
        return 0

# -------------------------------------------------------------------------

def display_score(correct_guesses, guesses):
    print("------------------------------------")
    print("RESULTS")
    print("------------------------------------")
    print("Answer", end="")
    for i in quations:
        print(questions.get(i), end=" ")
        print()
    
    print("Guesses", end="")
    for i in guesses:
        print(i, end=" ")
        print()
    
    score = int((correct_guesses/len(quations))*100)
    print("Your score is:  " + str(score)+"%")
 
# -------------------------------------------------------------------------

def play_again():
    responce = input("wanna play again (Y or N):  ")
    responce = responce.upper()
    
    if responce == "Y":
        return True
    else:
        return False


# -------------------------------------------------------------------------

questions = {
    "Who created python?:  ":"A",
    "What year was python creatad?:  ":"B",
    "Python is tributed to wich comedy group?:  ":"C",
    "Is the earth flat?:  ":"D"
}

options = [["A.Guido van rossum","B.alian with a mask","C.lord wojak","D.Mark Zakazaka"],
          ["A.1989","B.1991","C.2002","D.2020"],
          ["A.SNL","B.smosh","C.monty python","D.ntosh"],
          ["A.True", "B.False", "C.I DONT KNOW","D.What is this quation?" ]]

new_game()
while play_again():
    new_game
print("see yaaaaa")