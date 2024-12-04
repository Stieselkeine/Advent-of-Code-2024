li1 = []
li2 = []

#parse the input file
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        numbers = line.split()
        li1.append(int(numbers[0]))
        li2.append(int(numbers[1]))

#Sort the lists
li1.sort()
li2.sort()

#Find the difference between the lists
li3 = [abs(li1[i]-li2[i]) for i in range(len(li1))]

#Sum the differences
result = sum(li3)
print("Result: "+str(result))
