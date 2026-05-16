import pandas as pd

class Book:
    def __init__(self, title, author, isbn, is_available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    @property
    def status(self):
        if self.is_available:
            return "Available"
        else:
            return "Checked Out"
        
    @staticmethod
    def validate_isbn(isbn):
        isbn = isbn.replace("-", "")
        if len(isbn) == 13 and isbn.isdigit():
            return "Valid Isbn"
        else:
            return "Invalid Isbn"
        
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"], data["is_available"])


    def __str__(self):
        return f"{self.title} by {self.author} | {self.status}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = 3
        self.membership = "Regular"

    def borrow_book(self, book):
        if book.status == "Available" and len(self.borrowed_books) != self.max_books:
            self.borrowed_books.append(book)
            book.is_available = False
        elif len(self.borrowed_books) == self.max_books:
            print(f"You have already borrowed {len(self.borrowed_books)} / {self.max_books} books")
        else:
            print("Book not available")

    def return_book(self, book):
        if book.status == "Checked Out":
            self.borrowed_books.remove(book)
            book.is_available = True
        else:
            print("Book not checked out")

    def __str__(self):
        return f"{self.name} | ID: {self.member_id} | {self.membership} | Borrowed Books: {len(self.borrowed_books)}"
    
class PremiumMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.max_books = 10
        self.membership = "Premium"
        


book1 = Book("Pinocchio", "Carlo Collodi", "978-0141331645")
book2 = Book("Diplomacy", "Henry Kissinger", "978-0007350834")
book3 = Book("The Adventures of Sherlock Holmes", "Sir Arthur Conan Doyle", "978-0007350834")
book4 = Book("Napoleon: A Life", "Andrew Roberts", "978-0143127857")
book5 = Book("The Alchemist", "Paulo Coelho", "978-0060879075" )
book6 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "978-1408866191", True )
book7 = Book("The Witness", "Nora Roberts", "978-0515152340", True )
book8 = Book("The Throne of Fire", "Rick Riordan", "978-0786838653", True )
book9 = Book("Animal Farm", "George Orwell", "978-0451526342", True )
book10 = Book("The Cottage", "Danielle Steel", "978-0552148539", True )
book11 = Book("A Brief History of Time", "Stephen Hawking", "978-0553380163", True )


book11.__str__()
book1.status


member1 = Member("George Atkins", "72167")
premium_member1 = PremiumMember("Robert Brown", "83722")

member1.borrow_book(book1)
member1.borrow_book(book2)
member1.borrow_book(book3)
member1.borrow_book(book4)

member1.__str__()

premium_member1.borrow_book(book1)

member1.return_book(book1)
member1.return_book(book2)
member1.return_book(book3)

premium_member1.borrow_book(book1)
premium_member1.borrow_book(book2)
premium_member1.borrow_book(book3)
premium_member1.borrow_book(book4)
premium_member1.borrow_book(book5)
premium_member1.borrow_book(book6)
premium_member1.borrow_book(book7)
premium_member1.borrow_book(book8)
premium_member1.borrow_book(book9)
premium_member1.borrow_book(book10)
premium_member1.borrow_book(book11)

premium_member1.__str__()

books = [
    book1,
    book2,
    book3,
    book4,
    book5,
    book6,
    book7,
    book8,
    book9,
    book10,
    book11
]
        
df = pd.DataFrame([vars(b) for b in books])

print(df.loc[df["is_available"]])

print(Book.validate_isbn("978-0141331645"))
print(Book.validate_isbn("123"))
print(Book.validate_isbn("ABCDEFGHIJKLM")) 

data = {
    "title": "Dune",
    "author": "Frank Herbert",
    "isbn": "978-0441013593",
    "is_available": True
}

book12 = Book.from_dict(data)
print(book12.__str__)