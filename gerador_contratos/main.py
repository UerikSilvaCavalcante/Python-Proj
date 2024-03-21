from docx import Document
import pandas as pd
import os

documento = Document('./Contrato.docx')

tabela = pd.read_excel('./Informações.xlsx')

for linha in tabela.index:    
    for paragrafo in documento.paragraphs:
        paragrafo.text = paragrafo.text.replace('XXXX', tabela.loc[linha, 'Nome'])
        paragrafo.text = paragrafo.text.replace('YYYY', tabela.loc[linha, 'Item1'])
        paragrafo.text = paragrafo.text.replace('ZZZZ', tabela.loc[linha, 'Item2'])
        paragrafo.text = paragrafo.text.replace('WWWW', tabela.loc[linha, 'Item3'])
    documento.save(f'Nome/contrato-{tabela.loc[linha, 'Nome']}.docx')

# pasta = r'C:\Users\ueris\OneDrive\Área de Trabalho\Projetos-Python\gerador_contratos\Nome'

# arquivos = os.listdir(pasta)

# for arquivo in arquivos:
#     if os.path.isfile(os.path.join(pasta, arquivo)):
#         # Se sim, exclui o arquivo
#         os.remove(os.path.join(pasta, arquivo))
