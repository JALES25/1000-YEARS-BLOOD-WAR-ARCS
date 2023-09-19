ar = [1,"ADD",3,"SUB",5,"DIV",7,"MUL",9]

nums = []
op = []

com = 0
temp = 0

"""for i in range(0, len(ar),1):
    print(ar[i], "All")

for i in range(0, len(ar),2):
    print(ar[i], "Odds")"""

for i in range(len(ar)):
    if i % 2 == 0:
        nums.append(ar[i])
    else:
        op.append(ar[i])


"""print(nums)

print(op)"""

for i in range(len(nums)):
        print( nums[i] , op[i])
