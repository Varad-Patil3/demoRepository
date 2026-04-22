# write a python function which will take user input and will printthe table of the that number

def print_table():
    num = int(input("Enter a number: "))
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Call the function
print_table()