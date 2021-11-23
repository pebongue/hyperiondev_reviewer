#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */HYPERIONDE_REVIEWER.GIT/secton_c/string_calculator.py
#                                                                             
# PROGRAMMER: Placide E.
# DATE CREATED: 9 November 2021                                
# REVISED DATE: 17 November 2021
# PURPOSE: Create a function to evaluate string expression with and operand 
#           at the beginning of the string and output the result as a string.
#
## 
import re

def display_help_menu():
    valid_expression_list = ['This is the list of valid operators:',
                              'factorial [Factorial of the given value]\t-   e.g: factorial 5',
                              'prime [Highest prime under given value]\t-    e.g: prime 10',
                              'fibonacci [Highest Fibonacci under given value]\t-   e.g: fobonacci 12',
                              '+ [Addition of n-values]\t-   e.g: + 2 34.5',
                              '- [Subtraction of n-values]\t-   e.g: - 7 4.5',
                              '* [Multiplication of n-values]\t-   e.g: * 2 -34.5',
                              '/ [Division of n-values]\t-   e.g: / 10 34.5',
                              '+ [Long artihmetic of n-values]\t-   e.g: + 2 34 7 90',
                              'with () [Nested expressions with parentheses]\t-   e.g: / (factorial (* 2 2 5)) 600',
                              '\\t [Expression with contiguous whitespace]\t-   e.g: \\t 3.14',
                              '[A given value]\t-   e.g: 3.14']
    
    print('\n'.join(valid_expression_list))

def get_user_expression():
    user_exp = input("Give your expression or type 'help' [quit - to exit]: ").strip().lower()

    while not is_valid_expression(user_exp):
        user_exp = input("Give a valid expression or use the help: ").strip().lower()
    
    return user_exp


def is_valid_operator(operator):
    return operator in ('factorial', 'prime', 'fibonacci', '+', '-', '*', '/')


def get_expr_value(term):
    pass

def is_valid_expression(expression):
    if len(expression) == 0:
        return False, 'empty'
    
    if expression.replace('.', '', 1).lstrip('-').isdigit():
        return True, 'value'
    
    operator, *block_expr = expression.split()

    if not is_valid_operator(operator):
        return False, 'invalid'

    process_exp = re.sub("\s|factorial|fibonacci|prime|+|-|*|/|.", "", expression)
    if expression.find('(') != -1 and expression.count('(') == expression.count(')'):
        if process_exp.replace("(", "").replace(")", "").isdigit():
            return True, 'bracket'
        else:
            return False, 'invalid'
    
    is_term = False
    for term in block_expr:
        is_term = term.replace('.', '', 1).lstrip('-').isdigit()
        if is_term == False:
            break
    
    return is_term, 'valid'


def process_expression(expression):
    pass

def is_numeric(expression):
    pass


def factorial(n):
    return n if n == 1 else n*factorial(n)


def find_highest_prime(n):
    pass


def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def highest_fib(n):
    for num in range(n+1):
        if fibonacci(num) >= n:
            break
    return fibonacci(num-1)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a*b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero not allowed.")
    
    return a/b


def long_arithmetic(*arg):
    return sum(arg)


def expression_with_space(expression):
    return expression.strip()


def calc_nested_expression(**kwarg):
    pass


def do_calculation():

    input_exp = ""
    while input_exp != 'quit':
        input_exp = get_user_expression()

        if input_exp == 'help':
            display_help_menu()
        
        is_valid, exp_type = is_valid_expression(input_exp)

        if not is_valid:
            print("Give a valid expression. Use 'help' for example.")
            continue

        if exp_type == 'value':
            print(f"{input_exp} -> {input_exp}")
        elif exp_type == 'bracket':
            pass
        elif input_exp.startswith('factorial'):
            pass
        elif input_exp.startswith('fibonacci'):
            pass
        elif input_exp.startswith('prime'):
            pass
        elif input_exp.startswith('+'):
            pass
        elif input_exp.startswith('-'):
            pass
        elif input_exp.startswith('*'):
            pass
        elif input_exp.startswith('/'):
            pass


if __name__ == '__main__':
    do_calculation()
    print(fibonacci(5))