from Classes import customer
from Classes import book
import json

cust_list = {}
book_list = {}
rented_list = {}
rented_prices_list = {}


def combine_dictionaries(customers_dic, books_dic, rented_dic, prices_dic):
    list_of_dic = {"customer_name":customers_dic, "book_name":books_dic, "customers book rent": rented_dic, "customers rent fees": prices_dic}
    with open('Storing_data.json', 'w') as file:
        json.dump(list_of_dic, file, indent = 1)
    return list_of_dic


def reading_from_json():
    with open('Storing_data.json', 'r') as file:
        data = json.load(file)
        return data


def first_operation(cust, book, rented, prices):
    while True:
        try:
            first_operation_check = input("Is this your first time running this operation? y/n\n")
            if first_operation_check == "y":
                double_check = input("Please note all lists in Json will be reset! Do you want to proceed? y/n \n")
                if double_check == "y":
                    combine_dictionaries(cust, book, rented, prices)
                    all_dic = reading_from_json()
                    customerlist = all_dic["customer_name"]
                    booklist = all_dic["book_name"]
                    rentlist = all_dic["customers book rent"]
                    rent_pricelist = all_dic["customers rent fees"]
                    break
            if first_operation_check == "n":
                all_dic = reading_from_json()
                customerlist = all_dic["customer_name"]
                booklist = all_dic["book_name"]
                rentlist = all_dic["customers book rent"]
                rent_pricelist = all_dic["customers rent fees"]
                break
        except ValueError:
            print("Please note you haven't registered a Json list before, please enter 'y'.")
    return all_dic, customerlist, booklist, rentlist, rent_pricelist


def adding_sales(stored_customers_dic, stored_books_dic, rented_list, rented_prices_list):
    print("If you wanna exist, please enter 'q'")
    customers = [key for key in stored_customers_dic]
    books = [key for key in stored_books_dic]

    print(f"Stored customers: {customers}\nStored books: {books}")
    while True:
        renter = input("name of customer who has rented the book? ")
        if renter == "q": break
        if renter not in customers:
            print(f"the customer you have entered isn't stored, here is the list of stored customers: \n{customers}\n")       
        else:
            book_rented = input("name of the book that has been rented? ")
            fee = stored_books_dic[book_rented]
            if book_rented == "q": break
            if book_rented not in books:
                print(f"the book you have entered isn't stored, here is the list of stored books: \n{books}\n")   
            else: 
                rented_list, rented_prices_list = add_sales_dic_two(renter, book_rented, rented_list, fee, rented_prices_list)
    return rented_list, rented_prices_list               


def add_sales_dic_two(renter, book_rented, book_renting_dic, fee, rented_prices_list):
    dic_book = {}
    dic_fee = {}
    inner_book_dic = {}
    inner_fee_dic = {}
    if renter in book_renting_dic:
        inner_book_dic = book_renting_dic[renter]
        inner_book_dic[len(inner_book_dic)] = book_rented
        inner_fee_dic = rented_prices_list[renter]
        inner_fee_dic[len(inner_fee_dic)] = fee

    else:
        inner_book_dic[len(inner_book_dic)] = book_rented
        inner_fee_dic[len(inner_fee_dic)] = fee

    dic_book[renter] = inner_book_dic
    book_renting_dic.update(dic_book)

    dic_fee[renter] = inner_fee_dic
    rented_prices_list.update(dic_fee)

    return book_renting_dic, rented_prices_list


def number_books_rented(rented_list):
    if bool(rented_list) == False:
        print("You dont't have any rent activities stored. ")
    else:
        maximum = 0
        highest_rent = []
        for key in rented_list:
            maximum = max(len(rented_list[key]), maximum)
        for key in rented_list:
            if len(rented_list[key]) == maximum:
                highest_rent.append(key)
        print(f"Here is the names of customers with the highest number of books {maximum} total rented.\n{highest_rent}")
       

def rent_fee_total(price_list):
    if bool(price_list) == False:
        print("You dont't have any rent activities stored. ")
    else:
        maximum = 0
        highest_fee = []
        for key in price_list:
            x = 0
            print(key)
            for key2 in price_list[key]:
                x += float(price_list[key][key2])
                maximum = max(maximum, x)
        for key in price_list:
            x = 0
            for key2 in price_list[key]:
                x += float(price_list[key][key2])
                if maximum == x:
                    highest_fee.append(key)
        print(f"Here is the names of customers with the highest rent fee {maximum} total paid.\n{highest_fee}")


def main():
    all_dic, customerlist, booklist, rentlist, rent_pricelist = first_operation(cust_list, book_list, rented_list, rented_prices_list)

    while True:
        options = input("\nto Show list of operation enter 'p', To quit enter 'q'\n")
        if options == "q":
            break
        if options == "p":
            print("\nPlease choose one of the below operation you would like to implement. \nFor inserting customers and addresses, enter '1'. \nFor deleting customers and addresses, enter '2'. \nFor inserting books and rent fees, enter '3'.\nFor deleting books and rent fees, enter '4'. \nTo add rent activities, enter '5'. \nTo return a list of customers with the highest number of books rented, enter '6'. \nTo return a list of customers with the highest rent fee total, enter '7'. \nTo return all your current lists, enter '0'\nTo quit enter 'q'")
            operation_choice = input("\nWhat is your choice?\n")
            if operation_choice == "1":
                customerlist = customer.adding_customer(customerlist)
            if operation_choice == "2":
                customerlist = customer.deleting_customer(customerlist)
            if operation_choice == "3":
                booklist = book.adding_book(booklist)
            if operation_choice == "4":
                booklist = book.deleting_book(booklist)
            if operation_choice == "5":
                rentlist, rent_pricelist = adding_sales(customerlist, booklist, rentlist, rent_pricelist)
            if operation_choice == "6":
                number_books_rented(rentlist)
            if operation_choice == "7":
                rent_fee_total(rent_pricelist)
            if operation_choice == "0":
                print(all_dic)
            if operation_choice == "q":
                break

        all_dic = combine_dictionaries(customerlist, booklist, rentlist, rent_pricelist)

main()


