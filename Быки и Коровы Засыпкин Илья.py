import random
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
​
comp = " "
for i in range(5,8):
    comp += str(numbers[i])
​
p=5
while p >0:
    me = input("\nGuess the number:\n")
    
    keywords = []
    
    if comp == me:
        print("You won!")
        break
    else:
        for i in range(3):
            if comp[i] == me[i]:
                keywords.append("Byk")
            elif me[i] in comp:
                keywords.append("Korova")
    keywords.sort()
    if len(keywords) == 0:
        print("No matches!")
    else:
        for key in keywords:
            print(key, end = ", ") 
    p-=1
    print("\n", p, "tries left")
if p == 0:
    print("You lose! My number was ",comp)
