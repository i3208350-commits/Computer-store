def manu_reports(previous_transactions,products):
    while True:
        print("============= REPORTS =============")

        print("1. Total Sales")
        print("2. Total Revenue")
        print("3. Best Selling Products")
        print("4. Average Sale")
        print("5. Sales History")
        print("6. Category Statistics")
        print("7. Back")
        choose =input("Enter your choice:")
        if choose=="1":
            total_Sales(previous_transactions)
        if choose=="2":
            best_Selling_Products(previous_transactions)
        if choose=="3":
            best_Selling_Products(previous_transactions)
        if choose=="4":
            average_Sale(previous_transactions)
        if choose=="5":
            sales_History(previous_transactions)
        if choose=="6":
            category_Statistics(previous_transactions)
        if choose=="7":
            return


def total_Sales(previous_transactions):
    return len(previous_transactions)

def best_Selling_Products(previous_transactions):
    total=0.0
    for i in previous_transactions:
        total+=i["total"]
        return total


def sales_History(previous_transactions):
    x=total_Sales(previous_transactions)
    o=best_Selling_Products(previous_transactions)
    return o/x

def average_Sale(previous_transactions):
    return sales_History


def best_Selling_Products(previous_transactions):
    best={}
    for i in previous_transactions:
        if i["name"] in best:
            best[i["name"]]+=i["quantity"]
        else:
            best[i["name"]]=i["quantity"]
    x=sorted(best.items(),key=lambda p:p[1], reverse=True)
    return x[0:5]



def category_Statistics(previous_transactions,products):
    best={}
    for i in products:
            for t in previous_transactions:
                 
                if i["id"]==t["id"]:
                    if i["category"] in best: 
                       best[i["category"]]+=t["quantity"]
                    else:
                       best[i["category"]]=t["quantity"]
    x=sorted(best.items(),key=lambda p:p[1], reverse=True)
    return x