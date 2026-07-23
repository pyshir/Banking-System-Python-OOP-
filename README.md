# 🏦 Banking System (Python OOP)
**Author: Jahid, Whatsapp: 8801309495010**

A simple **Banking System** built with **Python Object-Oriented Programming (OOP)** concepts.

This project was developed as an OOP practice project demonstrating inheritance, abstraction, polymorphism, encapsulation, operator overloading, and menu-driven programming.

---

## 📌 Features

- 💰 Deposit Money
- 💸 Withdraw Money
- 🔄 Transfer Money
- 📈 Calculate Interest
- 📄 Transaction Statement
- 🏦 Bank Summary

---

## 📚 OOP Concepts Used

### ✅ Abstraction
- `Account` (Abstract Base Class)

### ✅ Inheritance
- `SavingsAccount`
- `CurrentAccount`

### ✅ Polymorphism
- `deposit()`
- `withdraw()`
- `interest()`

### ✅ Encapsulation
- Protected Balance Attribute (`_balance`)
- Getter & Setter Methods

### ✅ Operator Overloading

- `__add__()` → Add balances of two accounts
- `__eq__()` → Compare customers by account number
- `__len__()` → Number of accounts in the bank

---

## 📂 Project Structure

```
Banking-System/
│
├── main.py
└── README.md
```

---

## 🏗️ Classes

### Account (Abstract Class)

Base class for all account types.

Methods

- deposit()
- withdraw()
- get_balance()
- set_balance()

---

### SavingsAccount

- Deposit
- Withdraw
- 10% Interest

---

### CurrentAccount

- Deposit
- Withdraw
- 4% Interest

---

### Bank

Responsible for

- Managing Accounts
- Total Bank Balance
- Total Number of Accounts

---

### Customer

Stores

- Account Number

Also implements

- `__eq__()`
- `__hash__()`

---

### Transaction

Maintains transaction history.

Example

```
Deposit : 500
Withdraw : 200
Transferred : 100
Received : 100
```

---

## 🖥️ Menu

```
1. Deposit
2. Withdraw
3. Transfer
4. Interest & Check Balance
5. Statement
6. Bank Statement
```

---

## ▶️ Run

Clone the repository

```bash
git clone https://github.com/your-username/Banking-System.git
```

Go to project directory

```bash
cd Banking-System
```

Run

```bash
python main.py
```

---

## 📷 Example

```
1. Deposit
2. Withdraw
3. Transfer
4. Interest & Check Balance
5. Statement
6. Bank Statement

Choose one: 1

Account Id: 1

Amount: 500

Successful
```

---

## 🔧 Technologies

- Python 3
- Object-Oriented Programming (OOP)
- ABC (Abstract Base Class)

---

## 🚀 Future Improvements

- Database (SQLite/MySQL)
- User Authentication
- Account Creation
- Account Deletion
- File-based Transaction History
- Custom Exceptions
- @property Decorators
- Unit Testing (pytest)
- Logging

---

## 🎯 Learning Objectives

This project demonstrates:

- Abstract Classes
- Inheritance
- Polymorphism
- Encapsulation
- Operator Overloading
- Dictionary with Custom Objects
- Menu Driven Programming
- Transaction Management

---

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/your-username
