"""In Implicit type conversion,
 Python automatically converts one data type to another data type"""
""" Python always converts smaller data types to larger data types to
    avoid the loss of data."""
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo
print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

[print()]
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

#print(num_int+num_str)  -> error
print()
#    num=int("a")  ->we cannot typecast string to integer
#    print(num)
print("explicit conversion")
#explicit conversion
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))
