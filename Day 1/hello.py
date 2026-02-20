# Variables - Variables are a way to store the data, so that comouter can easiky understand what it is, and do operations on the data.

a = 1 # Integer
b = "string" # String
c = 9.67 # Float
d = True # Bool
e = [1,2,3,4,6] # List
f = (1,2,9, "ant", "ball") # Tuple
g = {
    'key1' : 12, # Dictionary
    'key2' : 14
}
h = {1,1,2, 2,2, 2,2,2,2,3,3,4} # Set

dtypes = [] # List
dtypes.append(a) # Add a to list
dtypes.append(b) # Add b to list
dtypes.append(c)
dtypes.append(d)
dtypes.append(e)
dtypes.append(f)
dtypes.append(g)
dtypes.append(h)
print(dtypes)

for i in dtypes:
    print(f"{i} is {type(i)}")