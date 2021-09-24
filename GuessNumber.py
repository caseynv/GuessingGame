import random

print("Please select your level of difficulty."  "1 - Easy, 2 - Medium, 3 - Hard")
x = int(input("Enter your level of difficulty: "))
if (x == 1):
    n = int(input("You have 6 guesses. Enter a number between 1 - 10: "))
    
    count = 1
    
    guess = random.randint(1, 11)
 
    if n != guess:
        print("You have", (6 - count), "guesses left")

        while (n != guess) and (count < 6):
            n = int(input("Enter another number between 1 - 10: "))
            count += 1
            if count < 6:
                print("You have", 6 - count, "guesses")
            else:
                t = int(input("The end! You can select 1 to Start again or 0 to End: "))
                if (t == 1):
                    print("Please select your level of difficulty."  "1 - Easy, 2 - Medium, 3 - Hard")
                    x = int(input("Enter your level of difficulty: "))
                elif(t == 0):
                    print("Thank You!")
                else:
                    print("Invalid")
                    
    if n == guess:
        print("Your guess", n, "was correct")

elif (x == 2):
    n = int(input("You have 6 guesses. Enter a number between 1 - 20: "))
    
    count = 1
    
    guess = random.randint(1, 21)
 
    if n != guess:
        print("You have", (4 - count), "guesses left")

        while (n != guess) and (count < 4):
            n = int(input("Enter another number between 1 - 20: "))
            count += 1
            if count < 4:
                print("You have", 4 - count, "guesses")
            else:
                t = int(input("The end! You can select 1 to Start again or 0 to End: "))
                if (t == 1):
                    print("Please select your level of difficulty."  "1 - Easy, 2 - Medium, 3 - Hard")
                    x = int(input("Enter your level of difficulty: "))
                elif(t == 0):
                    print("Thank You!")
                else:
                    print("Invalid")
                    
    if n == guess:
        print("Your guess", n, "was correct")


elif (x == 3):
    n = int(input("You have 6 guesses. Enter a number between 1 - 50: "))
    
    count = 1
    
    guess = random.randint(1, 51)
 
    if n != guess:
        print("You have", (6 - count), "guesses left")

        while (n != guess) and (count < 6):
            n = int(input("Enter another number between 1 - 50: "))
            count += 1
            if count < 3:
                print("You have", 3 - count, "guesses")
            else:
                t = int(input("The end! You can select 1 to Start again or 0 to End: "))
                if (t == 1):
                    print("Please select your level of difficulty."  "1 - Easy, 2 - Medium, 3 - Hard")
                    x = int(input("Enter your level of difficulty: "))
                elif(t == 0):
                    print("Thank You!")
                else:
                    print("Invalid")
                    
    if n == guess:
        print("Your guess", n, "was correct")
            
else:
    print("You entered a wrong choice!")




        




           
    
