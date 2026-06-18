# Exercise 1 - Dog Class
class Dog:
    def __init__(self, name, breed, age):
        # Initialising the variables
        self.name = name
        self.breed = breed
        self.age = age
    # Function to bark
    def bark(self):
        return f"{self.name} says woof!"
    # Function to find breed
    def describe(self):
        return f"{self.name} is a {self.breed}."
    
# Exercise 2 - Bank Account Class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} has been deposited into Bank Account."
    def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient funds in the Bank Account."
        self.balance -= amount
        return f"{amount} has been withdrawn from the Bank Account"
    def check_balance(self):
        return f"{self.owner}, the balance in your account is {self.balance}."
    
# Exercise 3 - Student Class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = []
        self.grade = None
    def add_score(self, score):
        self.scores.append(score)
        self.update_grade()
    def minus_score(self, score):
        if score in self.scores:
            self.scores.remove(score)
            self.update_grade()
        else:
            return f"There is no score to minus."
    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
    def update_grade(self):
        avg = self.average()
        if avg <= 50:
            self.grade = "F"
        elif avg <= 60:
            self.grade = "D"
        elif avg <= 70:
            self.grade = "C"
        elif avg <= 80:
            self.grade = "B"
        else:
            self.grade = "A"

# Exercise 4 - Library
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return f"The {self.title} is already borrowed."
        self.is_borrowed = True
        return f"You borrowed '{self.title}'."
        
    def return_book(self):
        if not self.is_borrowed:
            return f"The {self.title} is not borrowed."
        self.is_borrowed = False
        return f"You returned '{self.title}'"
        
    def describe(self):
        if self.is_borrowed:
            return f"'{self.title}' by {self.author} (borrowed)."
        else:
            return f"'{self.title}' by {self.author} (Available)."
        
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for b in self.books:
            if title == b.title:
                return b
        return None
    
    def list_available(self):
        titles = []
        for b in self.books:
            if not b.is_borrowed:
                titles.append(b.title)
        return titles

    def list_borrowed(self):
        titles = []
        for b in self.books:
            if b.is_borrowed == True:
                titles.append(b.title)
        return titles

# ========================== Test ===============================

# Test Exercise 1 - Dog
# my_dog = Dog("Buddy", "Golden Retriever", 3)
# print(my_dog.bark())
# print(my_dog.describe())
        
# # Test Exercise 2 - Bank Account
# my_acc = BankAccount("Simon", 10000)
# print(my_acc.deposit(10000))
# print(my_acc.withdraw(50000))
# print(my_acc.check_balance())

# # Test Exercise 3 - Student Class
# students = [
#     Student("Alice", 16),
#     Student("Bob", 17),
#     Student("Carol", 16),
# ]

# students[0].add_score(85)
# students[1].add_score(60)
# students[1].add_score(65)
# students[2].add_score(45)

# for s in students:
#     print(s.name, s.average(), s.grade)

# Test Exercise 4 - Book + Library

lib = Library("City Library")
lib.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
lib.add_book(Book("1984", "George Orwell"))
lib.add_book(Book("Dune", "Frank Herbert"))
lib.list_available()

# Borrow one book
hobbit = lib.find_book("The Hobbit")
print(hobbit.borrow())

# Check the lists
print(f"List of available books: {lib.list_available()}")     # ['1984', 'Dune']
print(f"List of borrowed books: {lib.list_borrowed()}")      # ['The Hobbit']

# Return it
print(hobbit.return_book())     # You returned 'The Hobbit'.
print(lib.list_available())     # ['The Hobbit', '1984', 'Dune']

# Look up something that doesn't exist
print(lib.find_book("Nonexistent"))   # None
