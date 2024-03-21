import os
sistema = os.environ
# print(sistema)
print(sistema["USERNAME"])

print(os.getcwd())

novo_caminho = r"C:\Users\ueris\OneDrive\Área de Trabalho"

os.chdir(novo_caminho)
print(os.getcwd())

os.mkdir("TESTE")
print(os.listdir())

os.startfile(r"C:\Users\ueris\OneDrive\Área de Trabalho\Projetos-Python\automação\output\bot\automacao.exe")

os.getcwd()
os.remove("TESTE")