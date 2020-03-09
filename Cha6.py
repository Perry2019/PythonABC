# Cha6 字典
# 6.2 使用字典
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(alien_0['color'])
print(alien_0['points'])
print("You have earned " + str(new_points) + " points!")

# 6.2.2 添加键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 6.2.3 定义空字典
alien_0 = {}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 6.2.4 修改字典中的值
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 6.2.5 删除键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# 6.2.6 类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'Bob': 'C',
    'Hank': 'ruby',
    'phil': 'python',
}
print("Bob's favorite language is " +
      favorite_languages['Bob'].title() +
      '.')

# 6.3 遍历字典
# 6.3.1 遍历所有的键值对
favorite_languages = {
    'jen': 'python',
    'Bob': 'C',
    'Hank': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + '.')

# 6.3.2 遍历字典中的所有的键
favorite_languages = {
    'jen': 'python',
    'Bob': 'C',
    'Hank': 'ruby',
    'phil': 'python',
}
friends = ['Bob','Hank']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() +
              ", I see you favorite language is " +
              favorite_languages[name].title() + '!')

# 6.3.3 按顺序遍历字典中的所有的键
favorite_languages = {
    'jen': 'python',
    'Bob': 'C',
    'Hank': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the pool!")

# 6.3.4 无重复的遍历字典中的所有的值
favorite_languages = {
    'jen': 'python',
    'Bob': 'C',
    'Hank': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 6.4 嵌套
# 6.4.1 字典列表
aliens = []
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)
print("...")

# 6.4.2 在字典中存储列表
favorite_languages = {
    'jen': ['python', 'C'],
    'Bob': ['C'],
    'Hank': ['ruby', 'go'],
    'phil': ['python'],
}
for name, languages in favorite_languages.items():
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())

# 6.4.3 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())