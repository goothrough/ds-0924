user_input_num = input("Enter a number: ")
user_input_n = input("Enter n: ")

# User input should always be integer value.
# If the user inputs 0 into n, 
# this program outputs the whole num because the nth digit does not exist.
num = int(user_input_num)
n = int(user_input_n)

divided_num = num
mod_num = num

for i in range(n):
    mod_num = divided_num % 10
    divided_num //= 10

print(mod_num)
