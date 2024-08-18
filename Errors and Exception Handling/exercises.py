# Exercises

try:
    for i in ['a', 'b', 'c']: 
        print(i**2)
except TypeError:
    print('TypeError') 

# 

try:
    x=5
    y=0

    z=x/y
except:
    print('Error: Division by zero')
finally:
    print("Done!")
# 
def ask():
    while True:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Please try again! \n")
            continue
        else:
            break
    print("Thank you! Your number squared is: ")
    print(n**2)

ask()


def ask():

    waiting =  True
    while waiting:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Please try again! \n")
            continue
        else:
            waiting =False
    print("Thank you! Your number squared is: ")
    print(n**2)

ask()