"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries
from random import choice
from customers import get_customers_from_file, Customer

file_name = "customers.txt"

rand_cust = choice(get_customers_from_file(file_name))

print(f'{rand_cust.name} you are the lucky winner! We will email you at {rand_cust.email} information on how to collect your prize!')

