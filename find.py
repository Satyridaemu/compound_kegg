import pubchempy as pcp
import json
with open('compound1.json', 'r') as f:
    data_dict = json.load(f)

for pathway_code in data_dict.keys():#代谢路径编码
    compound_dict=data_dict[pathway_code]
    for compound_code in compound_dict.keys():
        compound_name=compound_dict[compound_code]

        #print('done')

        cid_code=pcp.get_cids(compound_name,'name')#查找cid号
        
        try:
            compound=pcp.Compound.from_cid(cid_code) #获取化合物结构
            print('done')
        except Exception as e:
            continue
        #print(compound)
        properties=compound.to_dict(properties=['isomeric_smiles','canonical_smiles'])
        compound_dict[compound_code]=[compound_name,properties]

        #print(compound_code,compound_name,compound_dict[compound_code][1])
    data_dict[pathway_code]=[compound_code,compound_dict]
    with open('compound-smiles.json', 'w') as f2:
        json.dump(data_dict, f2,separators=(",\n", ": "))
