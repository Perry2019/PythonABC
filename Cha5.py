# Cha 5 if
# 5.1 sample
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 5.2.3 检查是否不等
requesred_topping = 'mushrooms'
if requesred_topping != 'anchovies':
    print("Hold the anchovies")

# 5.2.4 比较数字
age = 31
answer = 12
if age != answer:
    print("That is not the correct answer. Please try agin!")

# 5.2.5 and 检查多个条件
age = 31
answer = 12
if (age >= 30) and (answer <= 25):
    print("That is the correct answer.")

# 5.2.5 or 检查多个条件
age = 31
answer = 12
if (age >= 50) or (answer <= 25):
    print("\nThat is the correct answer.")

# 5.2.5 检查特定值是否不包含在列表中
banned_users = ['andrew','charlie','Jim']
user = 'bob'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")

# 5.3 if
# 5.3.1 简单的if语句
age = 19
if age >= 18:
    print("You are old enough to vote!")

# 5.3.1 if-else语句
age = 16
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote!")

# 5.3.3 if-elif-else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# 5.3.4 使用多个elif
age = 45
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("\nYour admission cost is $" + str(price) + ".")

# 5.3.6 测试多个条件
requesred_topping = ['mushrooms','cheese']
if 'mushrooms' in requesred_topping:
    print("Adding mushrooms")
if 'pepperoni' in requesred_topping:
    print("Adding pepperoni")
if 'cheese' in requesred_topping:
    print("Adding cheese")
print('\nFinished making your pizza')

# 5.4 使用if语句处理列表
# 5.4.1 检查特殊元素
requested_toppings = ['mushrooms','cheese','peppers']
for requested_topping in requested_toppings:
    if requested_topping == "peppers":
        print("Sorry, we are out of peppers right now")
    else:
        print("Adding " + requested_topping + ".")
print('\nFinished making your pizza')

# 5.4.2 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_topping:
        print("Adding " + requested_topping + ".")
    print('\nFinished making your pizza')
else:
    print("Are you sure you want a plain pizza?")

# 5.4.3 使用多个列表
available_toppings = ['mushrooms','olives','peppers','pepperoni','pineapple','cheese']
requested_toppings = ['mushrooms','french fries','cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print('\nFinished making your pizza')