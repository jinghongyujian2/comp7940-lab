#Exercise 1: Factors
x = 52633
for i in range(1, x + 1):  
    if x % i == 0:          
        print(i)


#Exercise 2: Function
def print_factor(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


#Exercise 3:List Iteration
l = [52633, 8137, 1024, 999]

for num in l:
    print(f"Factors of {num}:")
    print_factor(num)
    print("-" * 30)  # divider line
