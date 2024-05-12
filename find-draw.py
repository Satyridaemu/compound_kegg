import pubchempy as pcp
import json
from ChemStructDrawer import chemstrdrawer
with open('compound1.json', 'r') as f:
    data_dict = json.load(f)
count=0
for pathway_code in data_dict.keys():#代谢路径编码
    compound_dict=data_dict[pathway_code]
    for compound_code in compound_dict.keys():
        compound_name=compound_dict[compound_code]

        #print('done')

        cid_code=pcp.get_cids(compound_name,'name')#查找cid号
        
        try:
            compound=pcp.Compound.from_cid(cid_code) #获取化合物结构
            count=count+1
            print(count,'done')
            if (count==50):
                exit()
        except Exception as e:
            continue
        #print(compound)
        properties=compound.to_dict(properties=['isomeric_smiles','canonical_smiles'])
        print(properties['canonical_smiles'])
        chemstrdrawer(pathway_code,compound_code,compound_name,properties['canonical_smiles'],'c')
        chemstrdrawer(pathway_code,compound_code,compound_name,properties['isomeric_smiles'],'i')
        compound_dict[compound_code]=[compound_name,properties]

        #print(compound_code,compound_name,compound_dict[compound_code][1])
    data_dict[pathway_code]=[compound_code,compound_dict]
    with open('compound-smiles.json', 'w') as f2:
        json.dump(data_dict, f2,separators=(",\n", ": "))
