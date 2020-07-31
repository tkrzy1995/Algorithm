#	TAOCP
#
#    random_k
#
#
#    author : tkrzy1995
#

def getPos(x, p):
    nums = []
    while x:
        nums.append(x % 10)
        x //= 10
	
    if len(nums) <= 1:
        return 0 
    return nums[-p]

def randomK(x):
    y = getPos(x//(1000000000), 1)#step 1
    step = 1
    z = getPos(((x // 100000000) % 10), 2) # step 2
    step = 2
    while y > 0:
	if z + 3 == 3 or step == 2: #step 3
	    if x < 5000000000:
		x += 5000000000
	    step = 3
	if z + 3 == 4 or step == 3:
	    x = (((x ** 2) // 100000) % 10000000000)
	    step = 4
	if z + 3 == 5 or step == 4:
	    x = ((1001001001 * x) % 10000000000)
	    step = 5
	if z + 3 == 6 or step == 5:
	    if x < 100000000:
	        x = x + 9814055677
	    else:
		x = 10000000000 - x
	    step = 6
	if z + 3 == 7 or step == 6:
	    x = 100000 * ( x % 100000) + ( x // 100000)
	    step = 7
	if z + 3 == 8 or step == 7:
	    x = (((x ** 2) // 100000) % 10000000000)
	    step = 8
	if z + 3 == 9 or step == 8:
	    num = 0
	    while x:
		num += (x % 10 - 1)
		x //= 10
	    x = num
	    step = 9
	if z + 3 == 10 or step == 9:
	    if x < 100000:
		x = x**2 + 99999
	    else:
		x = x - 99999
	    step = 10
	if z + 3 == 11 or step == 10:
	    while x < 1000000000:
		x = 10 * x
            step = 11
	if z + 3 == 12 or step == 11:
	    x = ((x * ( x - 1)) // 100000) % 10000000000
  	    step = 12
	if z + 3 == 13 or step == 12:
	    if y > 0:
		y -= 1	
		step = 1
	    elif y == 0:
		return x
		
print("input a num: ")
num = int(input())

randnum = randomK(num)
print(randnum)

