menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80
}
print("Welcome to PYTHON restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")
order_total=0
item1=input("Enter the name of item you want to order=")
if item1 in menu:
    order_total+=menu[item1]
    print(f"Your item {item1} has been added to your order")
else:
    print(f"Ordered item {item1} is not available yet!")
another_order=input("Do you want to add another item?(Yes/No)")
if another_order=="Yes":
    item2=input("Enter the name of second item=")
    if item2 in menu:
        order_total+=menu[item2]
        print(f"Item {item2} has been added to order")
    else:
        print(f"Ordered item {item2} is not available!")
print(f"The total amount of items to pay is {order_total}")