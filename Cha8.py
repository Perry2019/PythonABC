# Cha8 Function
# 8.1 定义函数
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()

# 8.1.1 向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello!, " + username.title() + "!")
greet_user('hank')

# 8.2 传递实参
# 8.2.1 位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster','harry')
describe_pet('Dog', 'pull')

# 8.2.2 关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type = 'hamster', pet_name = 'harry')

# 8.3 返回值
# 8.3.1 返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 8.3.2 让实参可选
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)

# 8.3.3 返回字典
def build_person(first_name, last_name, age=''):
    """返回一个字典"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=31)
print(musician)

# 8.3.3 结合使用函数和while循环
'''
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First_name:")
    if f_name == 'q':
        break
    l_name = input("Lirst_name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello, " + formatted_name + '!')
'''
# 8.4传递列表
def greet_users(names):
    """向列表中的每个人问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hanah', 'ty', 'margot']
greet_users(usernames)

# 8.4.1 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing modeling: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone','robot']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.5 传递任意数量的实参
def make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppongs: ")
    for topping in toppings:
        print("-" + topping)
make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "cheese")

# 8.5.1 结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppongs: ")
    for topping in toppings:
        print("-" + topping)
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "cheese")

# 8.5.2 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einsten',
                             location = 'princeton', field = 'physics')
print(user_profile)
