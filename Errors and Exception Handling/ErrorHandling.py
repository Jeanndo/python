
#  To avoid running all at once comment what u are not using, thanks

def add(n1,n2):
    print(n1+n2)


num1 = 10
num2 = input("Enter a number here:")
num2 = 10

add(num1,num2)

# 
try:
    result = num1+num2
except:
    print("Something went wrong")
else:
    print("Addition successful")
    print(add(num1, num2))
# 

try:
    f = open("testfile","r")
    f.write("write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("There was an OS error")

finally:
    print("This will always execute")
    f.close()

# 

def ask_for_int():
    try:
        result = int(input("Please provide a number: "))
    except:
        print("Whoops! this is not a number")
    finally:
        print("End of try/except/finally")

ask_for_int()


# USING LOOP TO CONITNUALLY RUN CODE IF THERE IS ERROR


def ask_for_int():

    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! this is not a number")
            continue
        else:
            print("Yes, thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end")

ask_for_int()



