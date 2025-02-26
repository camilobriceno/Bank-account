# Bank-account
This is a simple Python program that simulates the management of a bank account. The program allows the user to create a bank account, make deposits, withdrawals, and check the current balance. Additionally, the program generates a random account number for each customer.


Key Features

Account Creation: The program prompts the user for their first and last name, and automatically generates a unique account number and an initial balance of €0.
Deposit Money: The user can deposit an amount of money into their account, which will be reflected in their current balance.
Withdraw Money: The user can withdraw an amount of money from their account, provided they have sufficient funds.
Interactive Menu: The program presents an interactive menu that allows the user to choose between depositing money, withdrawing money, or exiting the program.
Code Structure

The program is structured around two main classes:

Person: This class represents a person with a first name and a last name.
Client: This class inherits from Person and adds specific attributes for a bank client, such as an account number and balance. It also includes methods to display account information, deposit money, and withdraw money.
Additionally, the program includes functions to create a new client and handle the main menu.

Program Execution

Start: When the program is executed, a welcome message is displayed, and the user is prompted to enter their first and last name to create an account.
Main Menu: After creating the account, the user can choose from the following options:
Deposit money: Enter an amount of money to add to their balance.
Withdraw money: Withdraw an amount of money from their balance, if sufficient funds are available.
Exit menu: Terminate the program.
