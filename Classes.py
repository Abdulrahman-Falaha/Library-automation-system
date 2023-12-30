class customer:

    def __init__(self, customer_name, address):
        self.customer_name = customer_name
        self.address = address


    def adding_customer(storing_dic):
        print("If you wanna exit, please enter 'q'")
        while True:
            customer_name = input("Please enter customer's name: ")
            if customer_name == "q": break
            if customer_name.isdigit():
                print("please enter a valid name.")    
            else:
                dic = {}    
                customer_address = input("please enter customer's address: ")
                if customer_address== "q": break
                obj = customer(customer_name, customer_address)
                dic[obj.customer_name] = obj.address
                storing_dic.update(dic)
        return storing_dic
    
    
    def deleting_customer(storing_dic):
        print("If you wanna exit, please enter 'q'")
        while True:
            if bool(storing_dic) == False:
                print("You dont't have any customer's stored. ")
                break
            deleting_customer = input(f"list of customers that are stored: \n{storing_dic} \nplease write which customer would you like to delete: ")
            if deleting_customer == "q":
                break
            if deleting_customer not in storing_dic:
                print("the name you have entered isn't stored.\n")    
            else:    
                del storing_dic[deleting_customer]
        return storing_dic



class book:
    
    def __init__(self, book_name, rent_fee):
        self.book_name = book_name
        self.rent_fee = rent_fee
    
           
    def adding_book(storing_dic):
        print("If you wanna exit, please enter 'q'")
        while True:
            book_name = input("please enter a book name: ")
            if book_name == "q": break
            if book_name.isdigit():
                print("please enter a valid name.")    
            else:
                try: 
                    dic = {}    
                    rent_fee = float(input("please enter rent cost: $"))
                    if rent_fee == "q": break
                    obj = book(book_name, rent_fee)
                    dic[obj.book_name] = obj.rent_fee
                    storing_dic.update(dic)
                except ValueError as err:
                    print("Please enter a correct number!")
        return storing_dic
    

    def deleting_book(storing_dic):
        print("If you wanna exit, please enter 'q'")
        while True:
            if bool(storing_dic) == False:
                print("You dont't have any books stored. ")
                break
            deleting_book = input(f"list of books that are stored: \n{storing_dic} \nplease enter which book would you like to delete: ")
            if deleting_book == "q":
                break
            if deleting_book not in storing_dic:
                print("the book you have entered isn't stored.\n")    
            else:    
                del storing_dic[deleting_book]
        return storing_dic

