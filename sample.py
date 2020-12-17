# write a python function to print every alternate number in the user provided list 
def print_alternate_numbers(list1):
	print(list1[::2])


	
# write a python function  to convert a list of string list to a string list
def convert_to_string_list(list_of_string_list):
	res = [''.join(str(b) for b in eval(a)) for a in list_of_string_list] 
	return res


	
# write a python program to clear a list
given_list - = [6, 0, 4, 1] 
given_list.clear()



# write a python program to sort and print a list
given_list - = [6, 0, 4, 1] 
sorted_list = sorted(given_list)
print(f'sorted list is {sorted_list}')



# write a python program to add every alternate elements in a list of even elements and print the final list 
 given_list = [8, 6, 0, 4, 1, 6, 7, 8, 9, 10, 4, 5] 
if len(given_list) % 2 == 0:
	res_list = []
	for i in range(len(given_list)-2):
		res_list.append(given_list[i] + given_list[i + 2])
	print(f'Resultant list is {res_list}')
	

	
# write a Python program to print all the prime numbers within an interval
lower = 900
upper = 1000
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
		   

		   
# Write a Python Program to print the Factorial of a Number
num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   

   

# Write a Python Program to Check and print if a given year is a Leap Year
year = 2000
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(f"{year} is a leap year")
       else:
           print(f"{year} is not a leap year")
   else:
       print(f"{year} is a leap year")
else:
   print(f"{year} is not a leap year")
   

   

# Write Python Program to print if a Number is Odd or Even
num = 102
if (num % 2) == 0:
   print(f"{num} is Even")
else:
   print(f"{num} is Odd")

   


# Write a python function to Compute LCM of two input number
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

   
   

# write a python Program to print the ASCII value of the given character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))



# write Python Program to print the Sum of 10 Natural Numbers
num = 10
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
   

   
   
# write  a Python Program to Swap Two Variables and print them
x = 5
y = 10
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))



# Write a Python Program to Convert Kilometers to Miles
kilometers = 10000
conv_fac = 0.621371
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))



# Write Python Program to Convert Celsius To Fahrenheit
celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))



# Write Python Program to print the Square Root of a number
num = 8 
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))



# Write python function to count number of 1s in binary representation of an integer.
def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 

	
	
# Write Python function to check if a string is palindrome or not
def isPalindrome(s):
    return s == s[::-1]

	
	
# Write a python program to reverse a string
s = "i like this program very much"
words = s.split(' ')
string =[]
for word in words:
    string.insert(0, word)
 
print("Reversed String:")
print(" ".join(string))



# Write a python function to merge two Dictionaries
def Merge(dict1, dict2):
    return(dict2.update(dict1))
	
	
	
# Write a python program to print sum of number digits in List
test_list = [12, 67, 98, 34] 
res = [] 
for ele in test_list: 
    sum = 0
    for digit in str(ele): 
        sum += int(digit) 
    res.append(sum) 
print ("List Integer Summation : " + str(res)) 



# Write a Python function to count number of lists in a list of lists 
def countList(lst): 
    count = 0
    for el in lst: 
        if type(el)== type([]): 
            count+= 1          
    return count 
	
	
# Write a Python program to print largest element in an array
arr = [10, 324, 45, 90, 9808] 
print(f'the largest element in the array is {max(arr)}')




# Write a Python function to interchange first and last elements in a list
def swapList(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp 
    return newList
	

	

# Write a Python function to multiply all values in the list
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x 
    return result 

	
	
# Write a Python program to Multiply two list and print the resultant list
test_list1 = [1, 3, 4, 6, 8] 
test_list2 = [4, 5, 6, 2, 10] 
res_list = [] 
for i in range(0, len(test_list1)): 
    res_list.append(test_list1[i] * test_list2[i])	
print ("Resultant list is : " + str(res_list)) 	




#write a Python program to print positive numbers in a list
list1 = [11, -21, 0, 45, 66, -93] 
for num in list1: 
    if num >= 0: 
       print(num, end = " ") 
	   
	   
	   
# Write a Python program to print negative numbers in a list
list1 = [11, -21, 0, 45, 66, -93] 
for num in list1: 
    if num < 0: 
       print(num, end = " ") 	



# Write a python program to Count occurrences of given element in a list	
def countX(lst, x): 
    return lst.count(x)
	
	
	
# Write a python function to remove numeric digits from given string	
def removedigits(ini_string):
	res = ''.join([i for i in ini_string if not i.isdigit()]) 
    return res
	
	
	
# Write a Python program to print the number words in a sentence
test_string = "India is my country"
res = len(test_string.split()) 
print (f"The number of words in string are : {res}") 



# Write Python function to check if a string has at least one letter and one number
def checkString(str): 
    flag_l = False
    flag_n = False
    for i in str: 
        if i.isalpha(): 
            flag_l = True
        if i.isdigit(): 
            flag_n = True
    return flag_l and flag_n 
	
	
# Write a python function to Check whether triangle is valid or not if three points are given 	
def checkTriangle(x1, y1, x2, y2, x3, y3): 
    a = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) 
    if a == 0: 
        return False 
    else: 
        return True

		
		
# Write a python function to Check whether triangle is valid or not if sides are given		
def checkValidity(a, b, c):  
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True 
		
		

# Write a Python Program to print words starting with Vowel From A list		
test_list = ["all", "love", "and", "get", "educated", "by", "gfg"] 
print("The original list is : " + str(test_list)) 
res = [] 
vow = "aeiou"
for sub in test_list: 
    flag = False
    for ele in vow: 
        if sub.startswith(ele): 
            flag = True 
            break
    if flag: 
        res.append(sub)  
print("The extracted words : " + str(res)) 



# Write a python function to extract odd length words in String
def findoddlenthwords(test_str):
	res = [] 
	for ele in test_str.split(): 
		if len(ele) % 2 : 
			res.append(ele) 
	return res
	

	
# Write a python function to extract even length words in String
def findevenlenthwords(test_str):
	res = [] 
	for ele in test_str.split(): 
		if len(ele) % 2 == 0: 
			res.append(ele)  
	return res
	
	
	
# Write a python program to print Words lengths in String	
test_string = "India is my country"
res = list(map(len, test_string.split())) 
print ("The list of words lengths is : " + str(res)) 



# Write a python program to check if a number is positive or negative
num = 15
if num > 0:
   print(f"Positive number")
elif num == 0:
   print(f"Zero")
else:
   print(f"Negative number")
   
   
   
# write a Python Program to Display the multiplication Table of given number
num = 12
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)   
   
   
   
# write a Python function to Convert Decimal to Binary 
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')
   
   
   
# write a Python Program to Count and print the Number of Each Vowel in the input string
vowels = 'aeiou'
ip_str = 'India is my country'
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
   if char in count:
       count[char] += 1
print(count)



# write a Python Program to Check Whether a String is Palindrome or Not
my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
   
   
   
   
# Write Python Program to Remove Punctuations From a String and print the cleaned string.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)   
   
	



# Write a Python program to print unique triplets whose three elements gives the sum of zero from an array of n integers.
num = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
len_list = len(num)
trips = []
for i in range(len_list):
    if i+3 > len_list:
        break
    triplets = num[i:i+3]
    if len(set(triplets))==3:
        if sum(triplets) == 0:
            trips.append(triplets)
print(trips)



# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
num = [10,20,30,40,50,60,70,80,90]
len_list = len(num)
position = 3 - 1
idx = 0
while len_list > 0:
    idx = (idx+position) % len_list
    print(num.pop(idx))
    len_list-=1 
	
	
	
# Write a Python function to compute simple interest
def simple_interest(p,t,r): 
    si = (p * t * r)/100
    return si 
	
	
	
# Write a Python function to compute compound interest	
def compound_interest(principle, rate, time):  
    Amount = principle * (pow((1 + rate / 100), time)) 
    CI = Amount - principle 
    return CI
	

	
# Write a Python function for Program to find area of a circle
def findArea(r): 
    PI = 3.142
    return PI * (r*r)



# Write a python function to find Area Of Rectangle
def areaRectangle(a, b): 
    return (a * b) 




# Write a python function to find perimeter Of Rectangle 	
def perimeterRectangle(a, b): 
    return (2 * (a + b))
      



# write a python function to convert string in to binary
def convertstringtobinary(text):
	for chr in text:
		bin = ''
		asciiVal = int(ord(chr))
		while asciiVal > 0:
			if asciiVal % 2 == 0:
				bin = bin + '0'
			else:
				bin = bin + '1'
			asciiVal = int(asciiVal/2)
		return(bin + " : " + bin[::-1])
		
		
		
# Write a python program to print the Sum of digits of a number
n = 12345
q = 0
while(n>0):
 r=n%10
 q=q+r
 n=n//10
print("Sum of digits is: "+str(q))	



# Write a python program to sort alphabetically the words form a string provided by the user 	
def sortwords(my_str):
	words = my_str.split()
	words.sort()
	return ' '.join(words)




# Write a python function to replace all the spaces in an entered string with a hyphen "-"
def replacetext(string):
    string = string.replace(" ", "-")
    return string
	
	
	
# write a python program to rotate a list 10 times and print it
list = [11,22,33,44,55,66,77,88,99]
n = 10
finalList = []
for i in range(0, N):
    finalList.append(list[(i+d)%N])
print(finalList)



# write a Python Program to Add two binary numbers and print the sum
num1 = '00001'
num2 = '10001'
sum = bin(int(num1,2) + int(num2,2))
print(sum)




# write a Python Program to Calculate and print the Average of Numbers in a Given List 
a= [11,22,33,44,55,66,77,88,99]
avg=sum(a)/len(a)
print("Average of elements in the list",round(avg,2))



# write a Python Program to check if a number is a Perfect number and print the result
n = 7
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")




# write a Python function to convert binary to Gray codeword
def binary_to_gray(n):
    n = int(n, 2)
    n ^= (n >> 1)
    return bin(n)[2:]
 
 
 
# write a Python function to convert Gray code to binary 
def gray_to_binary(n):
    n = int(n, 2) # convert to int
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
    return bin(n)[2:]
	
	
	
# write a Python Program to Replace all Occurrences of ‘a’ with $ in a String
def replacestring(txt):
	return txt.replace('A','$')
	

	
# write a python program to Print Quotient and Remainder of two numbers 
a = 15
b = 4
quotient=a//b
remainder=a%b
print("Quotient is:",quotient)
print("Remainder is:",remainder)



# write a python program to print the Area of a Triangle Given All Three Sides
a = 15
b = 9
c = 7
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of the triangle is: ",round(area,2))



# write a Python function to Determine all Pythagorean Triplets in the Range
def findpythagoreantriplets(limit):
	c=0
	m=2
	while(c<limit):
		for n in range(1,m+1):
			a=m*m-n*n
			b=2*m*n
			c=m*m+n*n
			if(c>limit):
				break
			if(a==0 or b==0 or c==0):
				break
			print(a,b,c)
		m=m+1
		
		
		
# write a Python Program to print all the Divisors of an Integer
n = 20
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)		
		
		
		
		
# Write a python program to print dimension in centimeter to inches
cm = 50
inches=0.394*cm
print("The dimension in inches ",round(inches,2))


		
# Write a python program to print dimension in centimeter to feet
cm = 50
feet=0.0328*cm
print("The dimension in feet ",round(feet,2))




# write Python Program to print the Union of two Lists
l1 = [11,22,33,44]
l2 = [55,66,77,88]
union = list(set().union(l1,l2)) 
print('The Union of two lists is:',union)




# write a python function to Check if a Substring is Present in a Given String
def checksubstring(string,sub_string):
	if(string.find(sub_str)==-1):
      return False
	else:
		return True
		
		
		
# Write a Python Program to Multiply All the Items in a Dictionary and print the result
d={'A':10,'B':10,'C':239}
tot=1
for i in d:    
    tot=tot*d[i]
print(tot)




# Write Python Program to print Common Letters in Two Input Strings		
s1="Trump was the American President"
s2="Who is the American President now?"
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)
	
	
	
	
# Write a Python function to Find Whether a Number is a Power of Two
def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0
		
		
		
# Write a Python Program to Search the Number of Times a Particular Number Occurs in a List		
a = [2,3,2,3,4,4,5,5,6,6,6]
k=0
num=6
for j in a:
    if(j==num):
        k=k+1
print("Number of times",num,"appears is",k)



# write Python function to Clear the Rightmost Set Bit of a Number
def clear_rightmost_set_bit(n):
    return n & (n - 1)
	
	
	
# write a Python function to Find HCF of two numbers
def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf  
   
   
   
# Write a Python Program to Add Two Matrices and print result.
X = [[1,2,3],  
    [4,5,6],  
    [7,8,9]]  

Y = [[10,11,12],  
    [13,14,15],  
    [16,17,18]]  
	
	
result = [[0,0,0],  
               [0,0,0],  
              [0,0,0]] 

for i in range(len(X)):  
   for j in range(len(X[0])):  
       result[i][j] = X[i][j] + Y[i][j]  
for r in result:  
   print(r)  	
   
   
   
# write Python Program to Multiply Two Matrices and print result.
X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  
  
Y = [[10,11,12],  
      [13,14,15],  
      [16,17,18]]  
	  
result = [[0,0,0],  
               [0,0,0],  
              [0,0,0]]   
for i in range(len(X)):  
   for j in range(len(Y[0])):  
       for k in range(len(Y)):  
           result[i][j] += X[i][k] * Y[k][j]  
for r in result:  
   print(r)  
   
   
   
# Write a Python Program to Transpose a Matrix  and print result. 
X = [[1,2],  
      [4,5],  
     [7,8]]  
  
Result = [[0,0,0],  
             [0,0,0]]  
   
for i in range(len(X)):  
   for j in range(len(X[0])):  
       result[j][i] = X[i][j]  
  
for r in result:  
   print(r)
   
   
   
   
# Write a Python function to Find the Intersection of Two Lists   
def intersection(a, b):
    return list(set(a) & set(b))
	
	
	

# write a Python function to Sort a List According to the Length of the Elements.
def sortlistwithlen(list):
	list.sort(key=len)
	return list
	
	
# Write a Python Program to Print an Identity Matrix
n = 3
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ") 	
			
			
	
			
# Write a Python Program to print Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers		
lower = 1
upper = 100
for i in range (lower,upper+1):
    if(i%7==0 and i%5==0):
        print(i)
		
		
		
# write Python function to find the Length of the Longest One element in the list
def findlongest(list):
	max1=len(list[0])
	temp=list[0]
	for i in list:
		if(len(i)>max1):
		   max1=len(i)
		   temp=i
	return temp
	
	
	
# write a Python function to Detect if Two Strings are Anagrams	
def check_if_anagram(s1,s2):
	if(sorted(s1)==sorted(s2)):
		  return True
	else:
		  return False
		  
		  
		  
# Write Python Program to print the Length of a String Without Using a Library Function		  
string= "United States of America"
count=0
for i in string:
      count=count+1
print("Length of the string is:")
print(count)




# Write Python Program to Find the Area of a Rectangle Using Classes
class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=15
b=10
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())



# Write a Python Program to Find the Second Largest Number in a List
a= [11,22,33,44,55,66,77,88,99]
a.sort()
print("Second largest element is:",a[n-2])





# Write a Python Program to Count Number of Lowercase Characters in a String and print the result
string="SriNAtH"
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)




# write a Python Program to Sum All the Items in a Dictionary and print the result
d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))



# write Python function to Count the Frequency of Words Appearing in a String Using a Dictionary
def countword(test_string):
	l=[]
	l=test_string.split()
	wordfreq=[l.count(p) for p in l]
	return(dict(zip(l,wordfreq)))
	
	
	
# write Python Program to Read the Contents of a File
a=str(input("Enter the name of the file with .txt extension:"))
file2=open(a,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()	



# write Python Program to Count the Number of Lines in a Text File
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)



# write Python Program to Count the Number of Words in a Text File
fname = input("Enter file name: ")
num_words = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)



# write a Python Program to Read a File and Capitalize the First Letter of Every Word in the File
fname = input("Enter file name: ")
with open(fname, 'r') as f:
    for line in f:
        l=line.title()
        print(l)
		
		
		
# write Python Program to Read the Contents of a File in Reverse Order
filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())



# write a Python function to Remove the Given Key from a Dictionary
def deletekey(dict,key)
	if key in dict: 
		del dict[key]
	return dict
	
	
	
# Write a python function to remove an item from list
def deleteelement(list, item):
	list.remove(item)
	return list



# write a python function to Check if a given string is binary string or not
def check(string) :  
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        return True 
    else : 
        return False
		
		
		
# write a python function to compute minimum number of rotations required to get the same string		
def findRotations(str): 
    tmp = str + str
    n = len(str)   
    for i in range(1, n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
	
	
	
# write a Python function to check if count of divisors is even or odd
def NumOfDivisor(n): 
    if n < 1: 
        return
    root_n = n**0.5
    if root_n**2 == n: 
        print("Odd") 
    else: 
        print("Even") 
