import products.products as p
import vlidtord.vlidtord as v



def manu_seles(products,previous_transactions):
    shopping_cart=[]
    while True:
        print("1. Opening a new transaction.")
        print("2. Adding products to a shopping cart.")
        print("3. Updating the quantity of a product in the cart.")
        print("4. Removing a product from the cart.")
        print("5. Allowing a discount.")
        print("6. Executing the transaction.")
        print("7. Updating the inventory according to the products sold.")
        print("8.  exit")
       
        choose =input("Enter your choice:")
        if choose=="1":
            new_transaction(products)
        if choose=="2":
            adding_products(products,shopping_cart)
        if choose=="3":
            quantity(products,shopping_cart)
        if choose=="4":
            removing_product(shopping_cart) 
        if choose=="5":
            subtotal_calculation(shopping_cart)
        if choose=="6":
             possibility_of_discount(shopping_cart)
        if choose=="7":       
             execution(shopping_cart,)
        if choose=="8":
             return
             











def new_transaction(products):
    shopping_cart=[]
    return shopping_cart
    
    

    

def adding_products(products,shopping_cart):
    while True:
        product=v.input_test("Add product name to cart")
        for i in products:
            if i["name"]==product and i["active"]== True:
                print("Item found")
                items={
                    "product_id": i["id"],  
                    "name": i["name"], 
                    "quantity": i["quantity"],          
                    "unit_price": i["price"], 
                    "total": i["total"]        }    
                        
                shopping_cart.append(items)
        print("Item not found, search again.")


def quantity(products,shopping_cart):
       while True:
        x=v.input_test("Enter the product name if you would like to update the quantity.")
        for t in shopping_cart:
            if t["name"]==x:
                  print("Item found")
                  for i in products:
                            if i["name"]==x:
                                print("Item found")
                                quantit=v.regular_number_check("Enter a quantity")
                                if i["stock"]>=quantit:
                                     t["quantity"]+=quantit
                                     t["total"]=t["quantity"]*t["unit_price"]
                                     print("Quantity update done")
                                     return
                                else:
                                     print("Desired quantity not in stock")
        print("Product not found")

                                    


def removing_product(shopping_cart):
     while True:
        product=v.input_test("Enter the name of the product you want to remove.")
        for i in shopping_cart:
                    if i["name"]==product:
                        print("Item found")
                        shopping_cart.remove(i)
                        return
                    print("Product not found")
                
def subtotal_calculation(shopping_cart):
        total = 0.0
        for i in shopping_cart:
               total +=i["total"]
        return total

def possibility_of_discount(shopping_cart):
     discount=v.discount_check("Enter discount amount")
     total=subtotal_calculation(shopping_cart)
     return total*(1-(discount/100))


             
def execution(previous_transactions,shopping_cart):
    if len(shopping_cart)==0:
         return "There are no products in the cart"



    previous_transactions.appens()
     