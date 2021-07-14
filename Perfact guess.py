import random
number = random.randint(1, 100)
i = 1
print("""Welcome To This Small Game 
Created By Randeep Singh.
I Hope You Like this.""")

try:
    while True:
        guess = input(f"Guess {i}: ")
        try:
            if int(guess) == number:
                print(f"Congratulation! You Guessed Correct Number\nNumber of Guesses {i}")

                with open("HighScore.txt", "r") as f:
                    content = f.read()

                if content == "":
                    with open("HighScore.txt", "w") as f:
                        f.write(str(i)) 

                elif i < int(content):
                    print("Congratulation! You Have Just Broke High Score.")
                    with open("HighScore.txt", "w") as f:
                        f.write(str(i))

        
                if int(content) > i:
                    print(f"You Win! High Score is {content} and You Scored {str(i)} ")
                elif int(content) < i:
                    print(f"You Lose! High Score is {content} and You Scored {str(i)} ")
                break

            elif int(guess) > number:
                print("You Guessed Wrong. Too high! Please Enter Smaller Number.")
            elif int(guess) < number:
                print("You Guessed Wrong. Too Small! Please Enter Greater Number.")
            i += 1
        except ValueError:
            print("Please! Number Only")
except TypeError:
    print("Please! Enter Number")
except ValueError:
    print("Please! Enter Number Only.")
except FileNotFoundError:
    print("File not Found.")