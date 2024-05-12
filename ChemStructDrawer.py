from rdkit import Chem
from rdkit.Chem import Draw


def chemstrdrawer(pathway,code, name, smiles,cata):
    # 从SMILES字符串创建分子对象
    mol = Chem.MolFromSmiles(smiles)
    if (cata=='c'):
        filename=f"{pathway}-{code}-{name}-canonical.png"
    else: 
        if(cata=='i'):
            filename=f"{pathway}-{code}-{name}-isomeric.png"
    # 绘制分子结构
    img = Draw.MolToFile(mol,f'/usr/work/igem-tjusx/picture/{filename}',size=(1000,1000))
 
