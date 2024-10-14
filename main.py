# -*- coding: UTF-8 -*-

import json

# 读取 old.txt 文件内容，指定编码为 utf-8
with open('old.txt', 'r', encoding='utf-8') as old_file:
    old_content = old_file.read()

# 读取 dict.txt 文件内容并解析为 JSON，指定编码为 utf-8
with open('dict.txt', 'r', encoding='utf-8') as dict_file:
    dict_content = json.load(dict_file)

# 创建一个字典来存储 itemId 和替换格式
replacement_dict = {item['itemId']: '{{item_id{}}}'.format(i) for i, item in enumerate(dict_content)}

# 替换 old_content 中的 itemId
for item_id, replacement in replacement_dict.items():
    old_content = old_content.replace(item_id, replacement)

# 将替换后的内容写入 new.txt，指定编码为 utf-8
with open('new.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(old_content)

print("替换完成，结果已写入 new.txt！")