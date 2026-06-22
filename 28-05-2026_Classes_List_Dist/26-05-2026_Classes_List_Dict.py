# Class Contact with:
# 	•	name (string)
# 	•	phone (string)
# 	•	email (string)
# 	•	A method describe() that returns a formatted string like "Alice — phone: 91234567, email: alice@mail.com"
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def describe(self):
        return f"{self.name} - phone: {self.phone}, email: {self.email}"
# Class ContactBook with:
# 	•	contacts — a dictionary where keys are names (lowercase) and values are Contact objects
# 	•	add(contact) — adds the contact. If name already exists, return "Contact already exists", otherwise add and return "Contact added"
# 	•	remove(name) — removes by name (case-insensitive). Return True if removed, False if not found
# 	•	find(name) — case-insensitive lookup. Returns the Contact object or None
# 	•	search_by_partial_name(query) — returns a list of Contact objects whose name contains the query (case-insensitive). Example: searching “al” returns Alice and Albert.
# 	•	list_all() — returns a list of all contacts sorted alphabetically by name
class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add(self, contact):
        # Check if key matches contact name = True, contact already exists
        if contact.name.lower() in self.contacts.keys():
            return "Contact already exists"
        else: # Key match not found, add in contact to ContactBook
            self.contacts[contact.name.lower()] = contact
            return "Contact has been added"
    def remove(self, name):
        if name.lower() in self.contacts.keys():
            del self.contacts[name.lower()]
            return True
        else:
            return False
    def find(self, name):
        if name.lower() in self.contacts.keys():
            return self.contacts[name.lower()]
        else:
            return None
    def search_by_partial_name(self, query):
        results = []
        for contact in self.contacts.values():
            if query.lower() in contact.name.lower():
                results.append(contact.name)
        return results
    def list_all(self):
        return sorted(self.contacts.values(), key=lambda c: c.name)

# Test code:

book = ContactBook()

# Add
print(book.add(Contact("Alice", "91234567", "alice@mail.com")))   # Contact added
print(book.add(Contact("Bob", "82345678", "bob@mail.com")))       # Contact added
print(book.add(Contact("Albert", "73456789", "albert@mail.com"))) # Contact added
print(book.add(Contact("Alice", "00000000", "fake@mail.com")))    # Contact already exists
# Remove
print(book.remove("bob"))   # True
print(book.remove("xyz"))   # False
# Find
print(book.find("ALICE").describe())   # Alice — phone: 91234567, email: alice@mail.com
print(book.find("Charlie"))            # None
# Partial search
results = book.search_by_partial_name("al")
for c in results:
    print(c.describe())
# Should print Alice and Albert
# List all
for c in book.list_all():
    print(c.name)
# Should print: Albert, Alice  (alphabetical)