inventory_items = {}


def add_product():
    p_name = input("enter the product name: ").lower().strip()
    if p_name in inventory_items:
        print("product already exist ")
    else:
        p_quantity = int(input("enter the product quantity : "))
        p_price = int(input("enter the product price : "))
        inventory_items[p_name]={"p_quantity" : p_quantity , "p_price" : p_price }
        return

def show_items():
    if inventory_items is None:
        print("no item exist")
    else:
        print(inventory_items,"\n") 
    
def update_proudct():
    p_name = input("enter the product name that u want to change : ").lower().strip()
    if p_name in inventory_items:
        p_quantity = int(input("enter the product new quantity : "))
        p_price = int(input("enter the product price : "))
        inventory_items[p_name]={"p_quantity" : p_quantity , "p_price" : p_price }
    return

def delete_product():
    d_name = input("enter the product name that u want to delete").lower().strip()
    if d_name in inventory_items:
        del d_name
    else:
        print("item not found in inventory")
    return


while True:
    user_input = str(input("selcect operations :- \n  1: add to product,\n  2: show Product,\n  3: Update Product,\n  4: Remove items,\n  5: exit,\n ")
) 
    if user_input == "1":
        add_product()
    elif user_input == "2":
        show_items()
    elif user_input == "3":
        update_proudct()
    elif user_input == "4":
        delete_product()
    elif user_input == "5":
        break

    
             
             


    


           



