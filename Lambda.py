# lambda arguments: expession

add10 = lambda x: x + 10
print(add10(5)) # 15

mul = lambda x,y: x*y
print(mul(2,4)) # 8

# sorted

points2D = [(1,2), (15,1), (5,-1), (10,4)]

# sorted by x
points2Dsorted = sorted(points2D)
print(points2Dsorted)

# sorted by y using lambda
points2Dsorted = sorted(points2D, key=lambda x: x[1])
print(points2Dsorted)

# sorted by x+y using lambda
points2Dsorted = sorted(points2D, key=lambda x: x[0]+x[1])
print(points2Dsorted)

# map(func, seq)

numlist = [1,2,3,4]
numsquarelist = map(lambda x: x**2, numlist)
print(numlist, list(numsquarelist), sep="\n")
# also
numsquarelist2 = [num**2 for num in numlist]
print(numsquarelist2)

# filter(func, seq) return boolen
oddsnum = filter(lambda x: x%2 == 1, numlist)
print(numlist, list(oddsnum), sep="\n")
# also
oddsnum2 = [num for num in numlist if num%2 == 1]
print(numlist, oddsnum2, sep="\n")

# reduce(func, seq)
# have no idea 
