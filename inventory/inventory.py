import products.products as p
import vlidtord.vlidtord as v



def manu_inventory(products):
    while True:
        print("1. Full inventory display.")
        print("2. Search for a product in stock.")
        print("3. Adding units to inventory")
        print("4. Reducing units from inventory")
        print("5. Displaying out-of-stock products")
        print("6. Displaying products with low inventory.")
        print("7.Back_to_Main_Menu")

        choose_inventory =input("Enter your choice:")
        if choose_inventory=="1":
            show_full_inventory(products)
        if choose_inventory=="2":
             p.Search(products)
        if choose_inventory=="3":
             Change_units_in_inventory(products)
        if choose_inventory=="4":
                     Units(products)
        if choose_inventory=="5": 
             out_of_Stock_Products(products)
        if choose_inventory=="6":
             low_Stock_Products(products)
        if choose_inventory=="7":
             return





def show_full_inventory(products):
    for i in products:
              if i["active"]==True:
                print(i["name"],i["stock"]) 

def Change_units_in_inventory(products):
    while True:
        id=v.regular_number_check("Enter id")
        for i in products:
                 if i["id"]==id:
                    stock=v.regular_number_check("Enter Updated quantity")
                    i["stock"]+=stock
                    return i 
                 else:
                      print("Error, try again.")
                 

def Units(products):
    while True:
        id=v.regular_number_check("Enter id")
        for i in products:
                if i["id"]==id:
                    stock=v.regular_number_check("Enter Updated quantity")
                    if i["stock"]-stock>0:
                        i["stock"]-=stock
                        return i 
                    else:
                            print("Error, try again.")

def out_of_Stock_Products(products):
     for i in products:
          if i["stock"]==0:
            print(i)


def low_Stock_Products(products):
     low_Stock=v.regular_number_check("Enter the total units that products below this amount will be displayed.")
     for i in products:
               if i["stock"]<low_Stock:
                 print(i)