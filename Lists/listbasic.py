nums = []

##### Adding Elements to an Array / List
# 1st Method - Direct Defintion
nums = [1,2,4,3,8,5,6]
# print(nums)

# 2nd Method - Using Inbuilt Method Append()
nums.append(9)
# print(nums)

nums.append(10) # Methods......
# print(nums)

# Mixed Data Types in a SIngle List
mixed = [1, 'apple', 3.5]
print(mixed)


# List Methods 
print(nums) # Before Sorting
nums.sort()
print(nums) # After Sorting

# Min and Max
print(min(nums)) # This function returns the Minimum element in a Array
print(max(nums)) # This function returns the MAximum element in a Array

print(nums[-1])
print(nums[::-1]) # This line prints the List/Array in reverse


ages = [21, 23, 14, 16, 19, 17] # Integer data - Ages
names = ["siri", "nitin", "vaishnavi", "virat", "madan", "vamsi"] # String data - Names
ages[3] = 46 # Updating an element in Array
names[3] = "uttam" #Updating an Element in an Array.
for i in range(6):
    print(f"{names[i].upper()} age is {ages[i]}")
    if ages[i] >= 18:
        print(f"{names[i].upper()} is eligible to Vote")
    else:
        print(f"{names[i].upper()} is not eligible to Vote")