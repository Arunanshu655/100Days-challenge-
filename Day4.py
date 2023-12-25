# 1 Removal of alphanumeric characters:

def remove_alphanumeric(input_string):
    result = ""
    for char in input_string:
        if not (ord('0') <= ord(char) <= ord('9') or
                ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z')):
            result += char
    return result

# Exp:
input_str = "Hello123World!"
output_str = remove_alphanumeric(input_str)
print("Input String:", input_str)
print("Output String:", output_str)


# 2 roots of Quadratic Equation
import cmath as cm
print("General Quadratic Equation : ax**2 + bx + c = 0 \n according to this :-")
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))
d = (b**2) - (4*a*c)
r1 = (-b-cm.sqrt(d))/(2*a)
r2 = (-b+cm.sqrt(d))/(2*a)
if r1 == r2 :
    count = 0 
else :
    count = 1
match count :
     case 0:
        print(f'The unique root of this Quadratic Equaton is {r1}')
     case 1:
        print(f'The roots of this Quadratic Equaton are {r1} and {r2}')


# 3 Return indicies of two elements 
def give_indices(arr,tar):
    if tar not in arr : 
        print("The target value is not in the  array")
    else:
        for i in range(len(arr)):
            new_arr= arr.copy()
            new_arr = [item for item in new_arr if item != arr[i]]
            for j in range(len(new_arr)):
                if arr[i] + new_arr[j] == tar:
                    print(arr.index(arr[i]),arr.index(new_arr[j]))

#Exp:
arr = [1,2,3,4,5]
give_indices(arr,5)


# 4 number to word 
import inflect

def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)

# Exp:
number = 123
words = number_to_words(number)

print(f"{number} in words: {words}")



