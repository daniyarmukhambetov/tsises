from os import replace
import re

# from typing_extensions import final

with open('input.txt', 'r', encoding = 'utf-8') as data:
    text = ''.join(data.readlines())
###### company name ######
comp_name = re.search(r'.+\n(.+)', text)
# print(comp_name.group(1))
###### bin ######
bin = re.search(r'БИН( )(\d+)', text).group(2)
# print(bin)
a = re.findall(r'Стоимость*', text)
item_num = len(a)
item_name = []
item_count = []
item_price = []

items = re.findall(r'\d+\.\n([^\n]+)\n([0-9,]+) x ([0-9, ]+)\n([0-9, ]+)', text)
for i in items:
    print(f'name of item : {i[0]}')
    print(f'count of item : {i[1]}')
    print(f'price per item : {i[2]}')
    print(f'total price : {i[3]}')
date = re.search(r'Время: ([0-9.]+) ([^\n]+)', text).group(0) 
print(date)
adress = re.search(r'г\.[^\n]+', text).group(0)
print(adress)
# item_num = re.findall(r'(\d+,000)   ')
# print(items)

