
inp = "Hello!"
legen = ""
spc = "nothing"

while len(legen) <= 68:
    legen += inp

leg = ""
lis = []
""" 
while len(leg) <= 18:
    for index1, elemA in enumerate(inp):
        leg += inp[index1]
        lis.append(elemA)
        print(inp[index1])
        for index2, elemB in enumerate(inp[index1 + 1 :]):
            print(" ")
 
    """  

while len(leg) <= 21:    
    for item in inp: 
        for index88, it in enumerate(item):
            #print(spc[index88 % len(spc)], end="")
            leg += item[index88]

print(leg)
print(len(leg))
print(lis)