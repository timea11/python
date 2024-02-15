import random
import time

ls = ['rock', 'paper', 'sizers']

random.seed(time.time())
random_num = random.randint(0,2)

# time.sleep(2)
# print(time.time())
# time.sleep(1)
# print(time.time())

print("Chose your power young padovan: ")
print(" rock \n paper \n sizars \n")

count_win = 0
count_lose = 0
computer_power = ls[random_num]


while ((count_win <3) and (count_lose <3)):

    
    power  = input("I want to chose: ")
    print("You chose :" , power, "against: ", computer_power)

    if(power == computer_power):
        print("\nthere are equal, try again")
    else:
        
        if((power == 'rock' and computer_power == 'sizers') or 
        (power == 'sizers' and computer_power == 'paper') or (power == 'paper' and computer_power == 'rock')):
            print("\nWOHO! YOU WON!")
            count_win = count_win + 1
        else:
            print("\nyou lose, idiot!")
            count_lose = count_lose + 1

    
    #count_win =+ 1
    print("Count win is: ", count_win)
    print("count lose", count_lose)

print("\n END OF THE GAME!!!")





