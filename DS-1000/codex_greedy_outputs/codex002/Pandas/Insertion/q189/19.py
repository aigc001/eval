
# Create a function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

# Apply the function to each value in the dataframe
result1 = df.applymap(lambda x: check_even_odd(x) if x % 2 == 0 else x)
result2 = df.applymap(lambda x: check_even_odd(x) if x % 2 != 0 else x)

# Replace 'even' and 'odd' with actual values
result1 = result1.replace({'even': 1, 'odd': 0})
result2 = result2.replace({'even': 0, 'odd': 1})

print("Even values:")
print(result1)
print("\nOdd values:")
print(result2)
