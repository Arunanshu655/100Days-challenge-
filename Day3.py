
#        DAY003

# 1 Reverse a number 
num = int(input("Enter number:"))
reverse = 0 
while(num != 0):
    lastDig = num % 10 
    reverse = reverse*10 + lastDig
    num = num // 10
print("So the reversed number is :",reverse)

# 2 Reverse an array

def rev_arr(arr):
    for i in range(len(arr)//2):
        arr[i] , arr[len(arr)-1-i] = arr[len(arr)-1-i] , arr[i]
    return arr

#exp 
a = rev_arr([1,2,3,4,5,6,7])
print(a)

# 3 concatenate 2 arrays

def concat_arrays(arr1, arr2):
    l_arr1 = len(arr1)
    l_arr2 = len(arr2)

    concat_array = [0] * (l_arr1 + l_arr2)

    for i in range(l_arr1):
        concat_array[i] = arr1[i]

    for i in range(l_arr2):
        concat_array[l_arr1 + i] = arr2[i]

    print(concat_array)

concat_arrays([1,2,3,4],["a","b","c"])

# 4 Determine Leap year
year = int(input("Enter the year(in numbers):"))

if year % 4 == 0 and year % 100 != 0:
    print("This is a Leap Year")
elif year % 100 == 0 and year % 400 == 0:
    print("This is  a Leap Year")
else :
    print("This not a Leap Year")

# 5 Finds common elements

def com_ele(arr1,arr2):
    for a in arr1 :
        for b in arr2:
            if a == b :
                print(a,end=" ")
com_ele([1,2,3,4,5],[2,4,6,8])

# 6 Array Deduplication

def arr_dedup(arr):
    new_arr = []
    for a in arr:
        if a not in new_arr:
            new_arr.append(a)
    print(new_arr)

arr_dedup([1,2,1,3,3,4,5,6,2])

