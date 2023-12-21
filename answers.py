#           DAY002

# 1 Fibonacci Sequence upto Nth term

num = int(input("Enter the number (>0) :"))
n1 , n2 , sum = 0 ,1 ,0
for i in range(num):
    print(sum,end=" ")
    n1 = n2 
    n2 = sum
    sum = n1 + n2 


# 2 To check the palindrome 

num = int(input("Enter the number :"))
actual = num 
reverse = 0 
while(num != 0 ):
    swap = num % 10
    reverse = reverse * 10 + swap
    num = num // 10

if reverse == actual :
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")


# 3 count vowels and consonants
word = input("Enter your word :")
word = word.lower()
count = 0
for w in word :
     
    if w == "a" or  w == "e" or w == "i" or w == "o" or w == "u" :
        count = count +1 
print("There are ",count , " vowels and ", len(word)-count , "consonants in th word")

# 4 reverse the string

str = input("Enter your string :")

reverse =""

for i in range(len(str)-1,-1,-1):
    reverse = reverse + str[i]

print(reverse)

# 5 Character Frequency
Str = input('Enter your string :')
l = list(Str)
f = [l.count(i) for i in l]
d = dict(zip(l,f))

print(d)

# 6 Title Case Conversion

Sent = input(" Enter your sentence :")

title_case = Sent.title()
print(title_case)


print("The reversed string is :",reverse)








             
            
    