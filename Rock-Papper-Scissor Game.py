# challange
# rock, paper,scissor
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
import random
first_hand = input('Choose the hand: ')
if first_hand == 'rock':
    print(rock, 'rock')
elif first_hand == 'scissors':
    print(scissors, 'scissors')
elif first_hand == 'paper':
    print(paper, 'paper')
else:
    print('ulang lagi')
game = [rock ,scissors,paper]
print('\n Computer choose:')
second_hand = random.choice(game)
print(second_hand)
if first_hand == 'rock' and second_hand == rock:
    print('tie')
elif first_hand == 'rock' and second_hand == scissors:
    print('you win')
elif first_hand == 'scissors' and second_hand == scissors:
    print('tie')
elif first_hand == 'scissors' and second_hand == paper:
    print('you win')
elif first_hand == 'paper' and second_hand == paper:
    print('you tie')
elif first_hand == 'paper' and second_hand == rock:
    print('you win')
else:
    print('loser')
