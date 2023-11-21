class Author:
    all = []
    
    def __init__(self,name):
        self.name = name
        Author.add_to_all(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    
    def total_royalties(self):
        royalties = [contract.royalties for contract in self.contracts()]
        return sum(royalties)
        
    @classmethod
    def add_to_all(cls,author):
        if(isinstance(author,Author)):
            cls.all.append(author)
        else:
            raise Exception("authors must be objects of the Author class")


class Book:
    all = []
    
    def __init__(self,title):
        self.title = title
        Book.add_to_all(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
        
    @classmethod
    def add_to_all(cls,book):
        if(isinstance(book, Book)):
            cls.all.append(book)
        else:
            raise Exception("books must be objects of the Book class")


class Contract:
    all = []
    
    def __init__(self,author,book,date,royalties):
        if(isinstance(author,Author)):
            self.author = author
        else:
            raise Exception("authors must be objects of the Author class")
        if(isinstance(book, Book)):
            self.book = book
        else:
            raise Exception("books must be objects of the Book class")
        if(isinstance(date,str)):
            self.date = date
        else:
            raise Exception("date must be a valid string")
        if(isinstance(royalties,int)):
            self.royalties = royalties
        else:
            raise Exception("royalties must be entered as an int")
        Contract.add_to_all(self)
    
    @classmethod
    def add_to_all(cls,contract):
        if(isinstance(contract,Contract)):
            cls.all.append(contract)
        else:
            raise Exception("contracts must be objects of the Contract class")
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]