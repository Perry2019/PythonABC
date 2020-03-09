# Cha7 用户输入和while循环
# 7.1 input function
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 7.1.2 使用int()来获取数值输入
height = input("How tall are you? ")
height = int(height)
if height >= 16:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
'''
# 7.2 while循环
# 7.2.1 while loop
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
'''
# 7.2.2 让用户选择何时退出
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
'''

# 7.2.3 使用标志
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
'''
# 7.2.4 使用break退出循环
'''
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd like to go to " + city.title() + "!")
'''
# 7.2.5 continue in loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 7.3 使用while loop 处理列表和字典
# 7.3.1 在列表之间移动元素
unconfirmed_users = ['alice','bob','hank']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 7.3.2 删除包含特定值的所有列表元素
pets = ['cat','dog','cat','goldfish','rabbit']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 7.3.3 使用用户输入填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is yur name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n--Poll Results---")
for name, response in responses.items():
    print(name + " wold like to climb " + response + ".")