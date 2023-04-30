class Machine():
    def __init__(self):
        self.drink={"Cola":30,"GTea":25,"LTea":29,"Water":20}
        self.orders={}
    def display_menu(self):
        print("(1)choose drinks (2)list (3)pay (4)exit")    
    def display_drink(self):
        print("choose drinks (drinks / amount)\n(1)Cola (2)GTea (3)LTea (4)Water")
    def choose_drink(self,name,quantity):
        if name in self.orders:
            self.orders[name]+=quantity
        else:
            self.orders[name]=quantity
    def list(self):
        total=0
        drink=self.orders.keys()
        for item in drink:
            print(item," x",self.orders[item],"--",self.orders[item]*self.drink[item])
            total+=self.orders[item]*self.drink[item]
        print("total: ",total)
        return total
    def pay(self,paid,total):
        if paid>=total:
            print("thank you")
            print("找零: ",paid-total)
        else:
            print("money not enough")
M=Machine()
while True:
    M.display_menu()
    case=input("Please select a option.")
    if case=="1":
        M.display_drink()
        order=input().split()
        if len(order)!=2 or not order[1].isdigit() or order[0] not in M.drink.keys():
            print("invalid input")
            continue
        else:
            order[1]=int(order[1])
            M.choose_drink(order[0],order[1])
    elif case=="2":
        M.list()
    elif case=="3":
        total=M.list()
        paid=int(input("Enter your paid:$"))
        M.pay(paid,total)
        break
    elif case=="4":
        print("exit")
        break
    else:
        print("invalid input")