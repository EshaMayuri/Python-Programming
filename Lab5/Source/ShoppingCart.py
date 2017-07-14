import numpy as np

# person class that displays person details
class Person(object):
    # constructor
    def __init__(self):
        self._FirstName =''
        self._LastName = ''
    def _welcomeMessage(self):
        if(self._FirstName!='' and self._LastName!=''):
            print("\nHello",self._FirstName,"Welcome to our application!\n")
            print("User details:")
            print("Name:", self._FirstName,self._LastName)
        else:
            print("\nNo data to display\n")

# Address class to display address details
class Address():
    # constructor
    def __init__(self):
        self._addr = ''
    def displayAddress(self):
        if(self._addr!=''):
            print("Address details:",self._addr,"\n")
        else:
            print("\nNo data to display\n")

# user class inheriting Person and address class and displaying details
class User(Person, Address):
    # constructor
    def __init__(self, user_fname, user_lname, address):
        self.type = "user"
        Person._FirstName = user_fname
        Person._LastName = user_lname
        Person._welcomeMessage(self)
        Address._addr = address
        Address.displayAddress(self)
        # super(User, self).__init__()
        # Person._welcomeMessage(self)

# admin class inheriting Person and address class and displaying details
class Admin(Person):
    # constructor
    def __init__(self, user_fname, user_lname):
        self.type = "Admin"
        Person._FirstName = user_fname
        Person._LastName = user_lname
        Person._welcomeMessage(self)
    def _welcomeMessage(self):
        super(Admin, self)._welcomeMessage()
        print("\nAdmin Login\n")

# product class displays list of products and if admin gives privileges to edit the items
class Products(object):
    # constructor
    def __init__(self):
        print("List of Items that you can select from:")
        product_list = ["Product Id", "Product Name", "Price($)"]
        row_count = [1, 2, 3]
        self.data = np.array([[1, 'Python Book1', 10],
                         [2, 'Python Book2', 20],
                         [3, 'Python Book3', 30]])

        row_format = "{:>15}" * (len(product_list) + 1)
        print(row_format.format("", *product_list))
        for team, row in zip(row_count, self.data):
            print(row_format.format(team, *row))

    # editing items of list
    def changeList(self, type):
        if(type == "Admin"):
            print("\nYou have privilages to edit the Items\n")
            decision = input("Do you want to Add an item:")
            product_list = ["Product Id", "Product Name", "Price($)"]
            row_count = [1, 2, 3]
            if(decision.upper() == "YES"):
                list = input("Enter the Data(id,name, price):").split(",")
                np.append(self.data, list)
                print(np.append(self.data, list))
        else:
            print("You have no privilages to edit the products details!")

# Item details that a user is going to add to cart
class Item(object):
    # constructor
    def __init__(self, unq_id, name, price, qty):
        self.id = unq_id
        self.name = name
        self.price = price
        self.qty = qty

# Cart class that adds the items to user list and calculates the total amount
class Cart(object):
    # constructor
    def __init__(self, user_fn, data):
        self.details = dict()
        self.qty = 0
        self.total = 0
        self.__data = data
        print("Hello", user_fn)
        self.itemNum = input("Please pick an item from the list(Item Id):")

    def pickItem(self, itemnum):
        self.itemNum = itemnum
        for i in range(0, len(self.__data)):
            if (str(self.__data[i][0]) == str(self.itemNum)):
                print("You have picked-", self.__data[i][1])
                __c = input("Please input the quantity:")
                _item = Item(self.__data[i][0], self.__data[i][1], self.__data[i][2], __c)
                self.add(_item)
                print("You have %i items in your cart for a total of $%.02f" % (int(self.qty), int(self.total)))

    def add(self,_item1):
        self.qty = _item1.qty
        self.total = int(_item1.price) * int(_item1.qty)


print("----Users------")
print("please enter your credentials.")
user_fn = input("please enter your first name")
user_ln = input("please enter your last name")
address = input("please enter your address")

# Creating instance of user class and accessing various features
user = User(user_fn, user_ln, address)
# creating instance of product to get list of items available
prod = Products()
# creating instance of cart to add items to cart
cart = Cart(user_fn, prod.data)
cart.pickItem(cart.itemNum)
# accessing change list method to show just admin has access to edit items
prod.changeList(user.type)



print("----Admin------")
print("please enter your credentials(Admin).")
admin_fn = input("please enter your first name")
admin_ln = input("please enter your last name")
# Creating instance of user class and accessing various features
admin = Admin(admin_fn, admin_ln)
admin._welcomeMessage()
# creating instance of product to get list of items available
prod = Products()
# accessing change list method to show admin has access to edit items
prod.changeList(admin.type)
