# love calculator based on word TRUE LOVE
print('Welcome to the love calculator')
name = input('What is your name : \n')
name2 = input('What your crush : \n')
total_name = name + name2
lower = total_name.lower()
count1 = lower.count('t') + lower.count('r') + lower.count('u') + lower.count('e') 
count2 = lower.count('l') + lower.count('o') + lower.count('v') + lower.count('e') 
final_score = int(str(count1)+str(count2))
# print(final_score, type(final_score))
if final_score <= 10 or final_score >= 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f'your score is {final_score}, sorry you don\'t match each other')
