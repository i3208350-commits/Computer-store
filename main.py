import inventory.inventory as i
import products.products as p
import seles.seles as s
import reports.reports as r
def main():
    inventory=[]
    previous_transactions=[]
    products = [{"id": 1, "name": "Gaming Mouse", "category": "Gaming", "price": 150.0, "stock": 20, "active": True},
                {"id": 2, "name": "Mechanical Keyboard", "category": "Accessories", "price": 350.0, "stock": 10,
                 "active": True}]
    while True:
        print("COMPUTER STORE SYSTEM")
        print("== == == == == == == == == == == == == == == == =")

        print("1.Products Management")
        print("2.Inventory Management")
        print("3.Sales Management")
        print("4.Reports")
        print("5.Exit")

        choose=input("Choose an option:")
        if choose=="1":
            p.manu_products(products)
        if choose=="2":
            i.manu_inventory(products)
        if choose=="3":
            s.manu_seles(products,previous_transactions)
        if choose=="4":
            r.manu_reports()
        if choose=="5":
            print("Thank you for shopping with us")
            break
        else:
            print("Error entering the number")
            continue
        



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
