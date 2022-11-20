


shopping_list = {
    "Bread" : 1,
    "Milk" : 2,
    "Chocolate" : 1,
    "Butter" : 1,
    "Coffee" : 1,
}

def show_list():
    for item_name, quantity in shopping_list.items():
        print(f"{quantity}x {item_name}")
        
show_list()


#####

print("this is new code")

shopping_list1 = {}

def add_item(item_name, quantity1):
    if item_name in shopping_list1.keys():
        shopping_list1[item_name] += quantity1
    else:
        shopping_list1[item_name] = quantity1
        
add_item("Bread", 1)
add_item("Pies", 4)
print(shopping_list1)