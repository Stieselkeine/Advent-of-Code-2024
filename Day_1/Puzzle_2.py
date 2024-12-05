from functools import cache

li1 = []
li2 = []

#parse the input file
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        numbers = line.split()
        li1.append(int(numbers[0]))
        li2.append(int(numbers[1]))

# li1 = [3,4,2,1,3,3]
# li2 = [4,3,5,3,9,3]

#Wrapper of the count function to cache the results
@cache
def occurencesInSecondList(number :int) -> int:
    return li2.count(number)


# Sum similarity score
result = 0
for number in li1:
    result += number * occurencesInSecondList(number)


print("Result: "+str(result))
