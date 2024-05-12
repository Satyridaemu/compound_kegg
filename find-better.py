import pubchempy as pcp
import json
import time
import datetime
f_n=input('输入要执行的文件号：')
time_start = time.time()
with open(f'compound{f_n}.json', 'r') as f:
    data_dict = json.load(f)

for pathway_code in data_dict.keys():  # 代谢路径编码
    compound_dict = data_dict[pathway_code]
    lens = len(data_dict)
    count = 0
    for compound_code in compound_dict.keys():
        compound_name = compound_dict[compound_code]

        # print('done')

        cid_code = pcp.get_cids(compound_name, 'name')  # 查找cid号

        try:
            compound = pcp.Compound.from_cid(cid_code)  # 获取化合物结构
            count = count + 1
            time_end=time.time()
            timer = time_end-time_start
            timer = str(datetime.timedelta(seconds=int(timer)))
            print(f'{pathway_code}共有代谢物{lens}个，已完成{count}个，距离开始用时{timer}')
        except Exception as e:
            continue
        # print(compound)
        properties = compound.to_dict(properties=['isomeric_smiles', 'canonical_smiles'])
        compound_dict[compound_code] = [compound_name, properties]

        # print(compound_code,compound_name,compound_dict[compound_code][1])
        data_dict[pathway_code] = [compound_code, compound_dict]
    with open(f'compound-smiles{f_n}.json', 'w') as f2:
        json.dump(data_dict, f2, separators=(",\n", ": "))
