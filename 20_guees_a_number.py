##Final Answer
corret_answer=18
print("Welcome to a number game\n","You have 9 lives to guess a number")
num=int(input("Guess a number:"))
i = 10
while True:
   if i == 0:
        print("Game over")
        break
   elif num == 18:
        print("You Won")
        print("8 lives left")
        break
   elif num<18:
       print("Enter a Greater number",i-1,"lives left")
       i =  i- 1
       num = int(input("Try again:"))
   elif num > 18:
       print("Enter a lesser number",i-1,"lives left")
       i = i - 1
       num = int(input("Try again:"))
