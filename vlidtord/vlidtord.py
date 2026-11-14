def input_test(c):
    while True:
        x=input(c)
        if bool(str(x).strip()):
            return x 
        print("Input error test")
        continue



def discount_check(c):
    while True:
        x=input(c)
        if x>0 or x<100:
            return x
        print("Input error")
        continue

def regular_number_check(c):
    while True:
        
            x=int(input(c))
            if isinstance (x,int) and x>0:
                return x
        
            print("Input error")
            continue
            


    
def regular_float_check(c):
    while True:
        try:
            x=input(float(c))
            if x %1==0:
               if  x>0:
                 return x
        except Exception:
            print("Input error float ")
            continue



def new_product(id,name,category,price,stock):
    print("66666")
    new_product={"id":id,
                 "name":name,
                 "category":category,
                 "price":price,
                 "stock":stock,
                 "active": True}
    return new_product

    
    
    
def id_check(products):
    x=int(input("Enter id"))
    for i in products:
        if i["id"]==x:
          return(i)
    print("No product found")
    

def name_check(products):
    x=input("Enter name")
    for i in products:
            if i["name"]==x:
              return(i)
    print("No product found")



def category_check(products):
    x=input("Enter category")
    for i in products:
        if i["category"]==x:
                return(i)
    print("No product found")


def change_check(product_change):
    if product_change=="name":
       return bool(str(product_change).strip())
    
    if product_change=="category":
        return bool(str(product_change).strip())
    if product_change=="price":
        return isinstance (product_change,int) and product_change>0
    if product_change=="active":
        if product_change==True:
            return True
        return False