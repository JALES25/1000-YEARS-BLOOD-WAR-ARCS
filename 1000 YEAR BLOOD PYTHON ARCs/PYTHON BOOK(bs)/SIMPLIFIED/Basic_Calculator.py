# Define the functions {add}, {sub}, {mul}  and {div}
# print options to user
# ask for values
# call the functions
# Add the while loop to the continue program until user exits


def add(a,b):
    return a + b

def subs(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b): 
    return a / b




"""ex = input("Calculate? ")

print("What operand would you like to use")
op = input("> ")

print("Enter first number(s)")
nums1 = input("> ")

print("Enter second number(s)")
nums2 = input("> ")"""


"""while True:
        print("Would you like to enter another number")
        res = input("> ")

        if res[1].upper() == "N":
            break"""

print("What operand would you like to use")
op = input("> ")

# dictionary func to mimic a switch statement
def get_ans(op):
    print("Enter first number(s)")
    nums1 = int(input("> "))

    print("Enter second number(s)")
    nums2 = int(input("> "))
    return {
        add: add(nums1,nums2),
        subs: subs(nums1,nums2),
        mult: mult(nums1,nums2),
        div: div(nums1,nums2)

    }.get(op,"inavalid Operand")

# elif func to mimic a switch statement
def get_ans0(op):
    if op[0].upper() == "A":
        print("Enter first number(s)")
        nums1 = int(input("> "))

        print("Enter second number(s)")
        nums2 = int(input("> "))

        print( add(nums1,nums2))
    elif op[0].upper() == "S":
        print("Enter first number(s)")
        nums1 = int(input("> "))

        print("Enter second number(s)")
        nums2 = int(input("> "))

        print( subs(nums1,nums2))
    elif op[0].upper() == "M":
        print("Enter first number(s)")
        nums1 = int(input("> "))

        print("Enter second number(s)")
        nums2 = int(input("> "))

        print( mult(nums1,nums2))
    elif op[0].upper() == "D":
        print("Enter first number(s)")
        nums1 = int(input("> "))

        print("Enter second number(s)")
        nums2 = int(input("> "))
        print( div(nums1,nums2))
    
    else:
        return "INVALID OPERAND"


# operates on more than two numbers (SAME OPERATOR)
# Numbers are added to list then a for loop iterates through the list with operation

def op_more():
    arr_list = []
    comb = 0

    print("Enter operand to use on the given numbers: (ADD), (SUBSTRACT), (DIVIDE) OR (MULTIPLY)")
    op = input("> ")

    while True:

        print("Enter numbers to be operated on:")
        res = input("> ")
        if not res.isdecimal(): 
            print("Enter valid number")
        else:
            arr_list.append(int(res))

        res1 = input("Would you like to add another number to list of numbers to operate on: ")

        

        if res1[0].upper() == "N":
            break

    if op[0].upper() == "A":
        for i in arr_list:
            comb += i
    elif op[0].upper() == "S":
        for i in arr_list:
            comb -= i
    elif op[0].upper() == "M":
        for i in arr_list:
            comb *= i
    elif op[0].upper() == "D":
        for i in arr_list:
            comb /= i

    return comb
        

# takes input stores it in a list and then (trying to support multiple operators)
# 

def do_calc():
    ar_list = []
    comb = 0
    
    def for_num():

        while True:
            print("Enter number")
            res = input("> ")
            if not res.isdecimal():
                print("Enter a valid number")
            else:
                break
            
        
        
        return int(res)

    def for_op():

        while True:
            print("Enter Operand")
            op = input("> ")

            if op[0].upper() == "A":
                op = "ADD"
                #ar_list.append(op)
                break
            elif op[0].upper() == "S":
                op = "SUB"
                #ar_list.append(op)
                break
            elif op[0].upper() == "D":
                op = "DIV"
                #ar_list.append(op)
                break
            elif op[0].upper() == "M":
                op = "MUL"
                #ar_list.append(op)
                break
            else:
                print("Enter a valid Operand")
        
        return op
    
    for_num()
    ar_list.append(for_num())

    for_op()
    ar_list.append(for_op)

    for_num()
    ar_list.append(for_num())

    while True:

        print("Would you like to add another operand and number to equation")
        resp = input("> ")

        if resp.upper() == "Y":
            for_op()
            ar_list.append(for_op)

            for_num()
            ar_list.append(for_num())
        else:
            break


    # The actual hell iterator that takes first/current index and does an operation based on the next index 
    # Changed it so it takes the numbers and operation and stores them in a new list then does calculation
    nums = []
    operations = []

    for i in range(len(ar_list)):
        if i % 2 == 0:
            nums.append(ar_list[i])
        else:
            operations.append(ar_list[i])

    



    

    






#get_ans0(op)  
#print(op_more())


def calc(a , b):
    print("hi")