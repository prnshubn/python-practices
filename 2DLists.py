fruits=["apples","oranges","bananas","grapes"]
vegetables=["carrots","potatoes","cabbage","spinach"]
foods1=[fruits,vegetables]
print(fruits)
print(foods1)
print(foods1[0])
print(foods1[0][0])

print("---------------")

foods2=[["apples","oranges","bananas","grapes"],
       ["carrots","potatoes","cabbage","spinach"]]
print(foods2)
print(foods2[0])
print(foods2[0][0])

print("---------------")

for food in foods1:
    for f in food:
        print(f, end=" ")
    print()
