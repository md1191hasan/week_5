# Week 5 - Tutorial 5 Documentation

## 1. Problem Statement

A small cafe needs a simple Python program to calculate customer bills. The cashier will enter the customer's name and the quantity of each item bought. The program will calculate the total bill and print a simple receipt.

The cafe sells three items:

- Coffee = RM 8.50
- Tea = RM 6.00
- Sandwich = RM 12.00

## 2. Inputs

The program needs these inputs:

1. Customer name
2. Coffee quantity
3. Tea quantity
4. Sandwich quantity

## 3. Outputs

The program will print a receipt that shows:

1. Customer name
2. Coffee quantity
3. Tea quantity
4. Sandwich quantity
5. Total bill amount in RM

## 4. Process Flow

1. Start the program.
2. Ask the user to enter the customer name.
3. Ask the user to enter coffee quantity.
4. Ask the user to enter tea quantity.
5. Ask the user to enter sandwich quantity.
6. Calculate the total bill using the fixed prices.
7. Print the receipt.
8. End the program.

## 5. Constraints

1. The quantity should be a whole number.
2. The quantity should not be negative.
3. The item prices are fixed.
4. The program only calculates Coffee, Tea, and Sandwich.
5. The total amount should be shown in Malaysian Ringgit.

## 6. Problem Decomposition

I divided the program into smaller parts:

1. Store the item prices.
2. Create one function to calculate the total bill.
3. Create one function to print the receipt.
4. Use main.py to get user input and run the program.

This makes the program easier to understand because the calculation and receipt printing are separated from the main program.

## 7. Pseudocode

START

SET coffee price = 8.50  
SET tea price = 6.00  
SET sandwich price = 12.00  

ASK user to enter customer name  
ASK user to enter coffee quantity  
ASK user to enter tea quantity  
ASK user to enter sandwich quantity  

CALCULATE total bill:

total = coffee quantity * coffee price + tea quantity * tea price + sandwich quantity * sandwich price

PRINT receipt with customer name, item quantities, and total bill

END

## 8. Sample Output

Customer name: Bobby  
Coffee quantity: 3  
Tea quantity: 3  
Sandwich quantity: 2  

===== RECEIPT =====  
Customer : Bobby  
Coffee   : 3  
Tea      : 3  
Sandwich : 2  
------------------  
Total = RM 67.50
