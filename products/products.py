import vlidtord.vlidtord as v

def manu_products(products):
    while True:
        print("  --------- PRODUCTS MANAGEMENT - --------")

        print("1._Add_Product")
        print("2.Display_All_Products")
        print("3.Search_Product")
        print("4.Update_Product")
        print("5.Delete_Product")
        print("6.Back_to_Main_Menu")
        choose_products =input("Enter your choice:")
        

        if choose_products =="1":
             add_product(products)
        if choose_products =="2":
             display(products)
        if choose_products=="3":
             Search(products)
        if choose_products=="4":
            product_update(products)
        if choose_products=="5":
            product_deletion(products)
        if choose_products=="6":
            return


def add_product(products):
        
        print("Product_selection (name)")
        the_arc_name=v.input_test("insert name")
        for i in products:
            if the_arc_name==i["name"]:
                 print("There is already such a product")
                 return        
        print("Product does not exist, fill in the product details")
        id=len(products)+1
        name=v.input_test("insert name" )
        category=v.input_test("insert   category")
        price=v.regular_number_check("insert    price")
        stock=v.regular_number_check("insert   stock")

        product_1=v.new_product(id,name,category,price,stock)
        products.append(product_1)
        print(products)
        return products
             
    
        
def display(products):
     for i in products:
          if i["active"]==True:
            print(i)    


def Search(products):
     print("Select an option from the list:")
     print("1.Search  id")
     print("2.Search   name")
     print("3.Search   category")
     choose_Search=v.input_test(" Select")
     if choose_Search=="1":
        x=v.id_check(products)
     if choose_Search=="2":
        x=v.name_check(products)
     if choose_Search=="3":
        x=v.category_check(products)
    
    


    

def product_update(products):
    while True:
        print("Enter search terms")
        print("1.Name.")
        print("2.Category.")
        print("3.Price.")
        choose_Search=v.input_test(c)
        if choose_Search=="1":
            x=v.id_check(products)
        if choose_Search=="2":
            x=v.name_check(products)
        if choose_Search=="3":
            x=v.category_check(products)
        
        o=v.input_test("Which field to change")
        product_change=v.input_test("Why do you want to change?")
        v.change_check(product_change)
        t=v.change_check(product_change)
        if o=="name" and t==True:
            x["name"] == product_change
        if o=="category"   and t==True:
            x["category"]==product_change
        if o=="price"  and t==True:
            x["price"]==product_change
        if o=="active"  and t=="True":
            x["active"]== True 




        
def product_deletion(products):
    print("Enter search terms")
    print("1.id.")
    print("2.Name.")
    print("3.Category.")
    choose_Search=v.input_test("choose")
    if choose_Search=="1":
        x=v.id_check(products)
    if choose_Search=="2":
        x=v.name_check(products)
    if choose_Search=="3":
        x=v.category_check(products)
        products.pop(x)

        
