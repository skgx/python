

#Function using 'end' and 'sep' parameters to print desired output
# string1 = "Geeks"
# string2 = "For"
def print_func(string1, string2):
    print (  string1,string2  ,string1  , sep = '$', end = '$')
# Use string1 & string2 with sep and end parameter to print desired output
#sep is separator for the given strings and end is the ending you want
def print_fun1(string, x):
    # Your code here
    print(string*x) #prints the string desired number of times

def main():
    string1 = "Geeks"
    string2 = "For"
    print_func(string1, string2)
    print()
    print_fun1(string1,5)



if __name__ == "__main__":
    main()