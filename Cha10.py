# Cha10 文件和异常
# 10.1 从文件中读取数据
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 10.1.3 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 10.1.4 创建包含文件各行内容的列表
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 10.1.5 使用文件的内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 10.2 写入文件
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I loving programming.\n")
    file_object.write("I love creating new games.\n")

# 10.2.3 附加到文件
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I loving programming.\n")
    file_object.write("I love creating new games.\n")
    file_object.write("I also love finding meaning in large dataset.\n")

# 10.4 存储数据
import json
numbers = [2,3,5,7,9]
filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

import json
filename = 'numbers.json'
with open(filename, 'r') as file_object:
    numbers = json.load(file_object)

print(numbers)