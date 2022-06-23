import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
print(random.choice(names),"is going to buy the meal today!")

#########################  OR #####################


import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
rn=len(names)
rc=random.randint(0,rn-1)
print(names[rc],"is going to buy the meal today!")