rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇



print("Hey There! Let's play Rock, Paper, Scissors!")

user_choice= int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors."))

if user_choice == 0:
  print (rock)
elif user_choice == 1:
  print (paper)
else:
  print (scissors)

print("The computer chooses:")
import random

random_number = random.randint(0,2)

if random_number == 0:
  print(rock)
elif random_number == 1:
  print(paper)
elif random_number ==2:
  print(scissors)
else:
  print("zero")

if user_choice == random_number:
  print("It's a Draw!")
elif((user_choice == 0 and random_number == 2) or (user_choice == 1 and random_number == 0) or (user_choice == 2 and random_number == 1) ):
  print("Yaay!! You Win!!")
elif((user_choice == 0 and random_number == 1) or (user_choice == 1 and random_number == 2) or (user_choice == 2 and random_number == 0) ):
  print("Oops!! Tou Lose:(")
