
import random

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



chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if chose == 0:
  print(rock)
elif chose == 1:
  print(paper)
elif chose == 2:
  print(scissors)
  
print("computer chose:")

computer = random.randint(0,2)
print(computer)
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)

rock = ['you won','you lose', 'you won']
paper = ['you lose', 'you lose', 'you won']
scissors = ['you won', 'you lose', 'you lose']

score = [rock, paper, scissors]
print(score[chose][computer])