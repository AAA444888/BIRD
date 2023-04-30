list=[]
class Furniture():
    
   def __init__(self,name,area):
        self.name=name
        self.area=area
        
   def __str__(self):
        return f"{self.name} 佔地: {self.area}"

class House():

   def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        self.left_area=area
        
   def __str__(self):
        return f"戶型: {self.house_type}\n總面積: {self.area}[剩餘面積: {self.left_area}]\n家具: {[str(item.name) for item in list]}"

   def add_item(self,item):
        if item.area > self.left_area:
            print(item.name+"太大")
        else:
            list.append(item)
            self.left_area=self.left_area-item.area
        

   #2.添加傢俱 TODO

   #3.計算剩餘面積 TODO
choice=int(input())
if choice:
    bed = Furniture('bed',4)
    print(bed)
    yigui = Furniture('yigui',200)
    print(yigui)
    table = Furniture('table',1.5)
    print(table)

    my_house = House('獨門獨棟',400)

    my_house.add_item(bed)
    my_house.add_item(yigui)
    my_house.add_item(table)
    print(my_house)
else:
    bed = Furniture('bed',4)
    print(bed)
    yigui = Furniture('yigui',400)
    print(yigui)
    table = Furniture('table',1.5)
    print(table)

    my_house = House('獨門獨棟',400)

    my_house.add_item(bed)
    my_house.add_item(yigui)
    my_house.add_item(table)
    print(my_house)