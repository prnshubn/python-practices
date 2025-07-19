foods=[]
prices=[]
total=0

while True:
    food=input("Enter food item (q to quit): ")
    if food.lower()=="q":
        break
    price=float(input(f"Enter price of {food} $: "))
    foods.append(food)
    prices.append(price)
print("-----Your Cart-----")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")
total+=prices[i]
print(f"Total: ${total:.2f}")