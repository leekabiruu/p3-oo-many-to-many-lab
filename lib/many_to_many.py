class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def __repr__(self):
        return f"Author({self.name})"
    
    def contracts(self):
        return self._contracts
    
    def books(self):
        return [contract.book for contract in self._contracts]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def __repr__(self):
        return f"Book({self.title})"

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise TypeError("royalties must be a number")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        author._contracts.append(self)
        book._contracts.append(self)
        Contract.all.append(self)
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]