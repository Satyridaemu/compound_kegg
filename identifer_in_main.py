import json
import re



def find_and_store_values(dictionary):
    pattern = r'(?<!\w)C(\d{5})(.*)(?=(?:|$))'
    updated_dict = {}
    for key, value_list in dictionary.items():
        if isinstance(value_list, list):
            sub_dict = {}
            for value in value_list:
                if isinstance(value, str):
                    matches = re.findall(pattern, value)
                    for match in matches:
                        num_key = 'C'+match[0]
                        rest_value = match[1].strip()
                        sub_dict[num_key] = rest_value
            if sub_dict:
                updated_dict[key] = sub_dict
    return updated_dict

# 调用函数并输出结果
