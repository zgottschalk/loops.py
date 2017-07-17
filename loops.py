"""input("Choose a Number wisely.")
num = 1
while(num<6):
    y = 1
    while(y<4):
        y=y+9
    num = num+1
    print(".")
"""


horizontal = int(input("Choose a Number wisely."))
x = ""
num = 0
while(num<horizontal):
    num = num+1
    x="."+x
    if(num == horizontal):
        print(x)
