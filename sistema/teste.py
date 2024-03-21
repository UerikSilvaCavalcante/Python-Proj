# from datetime import datetime

# hj = datetime.now()
# ano = hj.year
# mes = hj.month
# dia = hj.day
# hora = hj.hour
# min = hj.minute

# print(hj)
# print(ano, mes, dia)
# print(hora, min)

# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from reportlab.lib import colors
# from reportlab.pdfgen import canvas

# # Criar o documento PDF
# doc = SimpleDocTemplate("tabela_e_texto.pdf", pagesize=letter)

# # Criar a tabela
# data = [
#     ["Nome", "Idade", "Cidade"],
#     ["João", "25", "São Paulo"],
#     ["Maria", "30", "Rio de Janeiro"],
#     ["Carlos", "28", "Belo Horizonte"]
# ]
# table = Table(data)

# # Aplicar estilos à tabela
# style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                     ('GRID', (0, 0), (-1, -1), 1, colors.black)])
# table.setStyle(style)

# # Criar uma página de canvas
# c = canvas.Canvas("tabela_e_texto.pdf", pagesize=letter)

# # Adicionar a tabela ao PDF
# table.wrapOn(c, 0, 0)
# table.drawOn(c, 50, 600)

# # Adicionar texto à mesma página
# c.drawString(50, 550, "Este é um texto adicionado na mesma página")

# # Finalizar o PDF
# c.save()

# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
# from reportlab.lib import colors

# # Função para criar o documento PDF com a tabela
# def create_pdf_with_table(filename, data):
#     doc = SimpleDocTemplate(filename, pagesize=letter)

#     # Lista para armazenar o conteúdo da tabela
#     table_data = []

#     # Loop sobre os dados da tabela e adicionando-os à lista
#     for row in data:
#         table_data.append(row)

#     # Criando a tabela
#     table = Table(table_data)

#     # Aplicando estilos à tabela
#     style = TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black)
#     ])
#     table.setStyle(style)

#     # Adicionando a tabela ao documento
#     doc.build([table])

# # Dados da tabela (exemplo)
# data = [
#     ["Coluna 1", "Coluna 2", "Coluna 3"],
#     ["Dado 1", "Dado 2", "Dado 3"],
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#     # Adicione mais linhas conforme necessário...
# ]

# # Criando o documento PDF com a tabela
# create_pdf_with_table("tabela.pdf", data)

# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.pdfgen import canvas

# # Função para criar o documento PDF com texto e tabela
# def create_pdf_with_text_and_table(filename):
#     # Criar um objeto Canvas para o PDF
#     c = canvas.Canvas(filename, pagesize=letter)

#     # Adicionar um parágrafo de texto ao PDF
#     text = "Exemplo de Texto"
#     c.drawString(100, 700, text)

#     # Definir dados para a tabela
#     data = [
#         ["Coluna 1", "Coluna 2", "Coluna 3"],
#         ["Dado 1", "Dado 2", "Dado 3"],
#         ["Dado 4", "Dado 5", "Dado 6"]
#     ]

#     # Definir posições iniciais para a tabela
#     x_offset = 100
#     y_offset = 650
#     row_height = 20

#     # Adicionar a tabela ao PDF
#     for row in data:
#         for col_index, cell in enumerate(row):
#             c.drawString(x_offset + col_index * 100, y_offset, cell)
#         y_offset -= row_height

#     # Desenhar linhas da tabela
#     c.grid(range(0, (len(data) + 1) * row_height, row_height), [100, 200, 300, 400, 500])

#     # Salvar o PDF
#     c.save()

# # Criando o documento PDF com texto e tabela
# create_pdf_with_text_and_table("exemplo.pdf")

# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from reportlab.lib import colors
# from reportlab.pdfgen import canvas

# # Criar o documento PDF
# doc = SimpleDocTemplate("tabela_e_texto.pdf", pagesize=letter)

# # Criar a tabela
# data = [
#     ["Nome", "Idade", "Cidade"],
#     ["João", "25", "São Paulo"],
#     ["Maria", "30", "Rio de Janeiro"],
#     ["Carlos", "28", "Belo Horizonte"],
#     ["Dado 1", "Dado 2", "Dado 3"],
#     ["Dado 1", "Dado 2", "Dado 3"],
#     ["Dado 1", "Dado 2", "Dado 3"],
#     ["Dado 1", "Dado 2", "Dado 3"],
#     ["Dado 1", "Dado 2", "Dado 3"],
#     ["Dado 1", "Dado 2", "Dado 3"],
# ]
# table = Table(data)

# # Aplicar estilos à tabela
# style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                     ('GRID', (0, 0), (-1, -1), 1, colors.black)])

# table.setStyle(style)

# # Criar uma página de canvas
# c = canvas.Canvas("tabela_e_texto.pdf", pagesize=letter)

# indice = 400


# # Adicionar a tabela ao PDF
# table.wrapOn(c, 0, 0)
# for row in data:
#     indice -= 10   # Posição da tabela
# table.drawOn(c, 50, indice)
 

# # Adicionar texto à mesma página
# c.drawString(50, 350, "Este é um texto adicionado na mesma página")  # Posição do texto

# # Finalizar o PDF
# c.save()

# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer,HRFlowable
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors

# Função para criar o PDF do orçamento
# def criar_orcamento(nome_arquivo, titulo, info_orcamento, produtos):
#     # Configurar o documento PDF
#     doc = SimpleDocTemplate(nome_arquivo, pagesize=letter)
#     styles = getSampleStyleSheet()
    
#     # Lista de elementos para adicionar ao PDF
#     elementos = []

#     # Adicionar o título
#     elementos.append(Paragraph(titulo, styles['Title']))

#     # Adicionar informações do orçamento
#     for chave, valor in info_orcamento.items():
#         elementos.append(Paragraph(f"<b>{chave}:</b> {valor}", styles['Normal']))

#     elementos.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black))

#     elementos.append(Spacer(1, 30))

#     # Adicionar a tabela de produtos
#     tabela = Table(produtos, colWidths=[100, 200, 100, 100])
#     tabela.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                                 ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                                 ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                                 ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                                 ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                                 ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                                 ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
#     elementos.append(tabela)

#     # Construir o PDF
#     doc.build(elementos)

# # Informações do orçamento
# titulo = "Orçamento de Produtos"
# info_orcamento = {
#     "Nome do Cliente": "Fulano de Tal",
#     "Nome do Vendedor": "Beltrano",
#     "Data": "20/02/2024",
#     "Data de Entrega": "25/02/2024",
#     "Endereço": "Rua das Flores, 123",
#     "Valor Total da Compra": "R$ 500,00",
#     "Quantidade de Produtos": "5",
#     "CNPJ": "123.456.789/0001-00"
# }

# # Lista de produtos
# produtos = [
#     ["ID", "Descrição", "Preço Unitário", "Quantidade"],
#     ["001", "Produto A", "R$ 100,00", "2"],
#     ["002", "Produto B", "R$ 50,00", "3"]
# ]

# # Nome do arquivo PDF
# nome_arquivo = "orcamento.pdf"

# # Criar o PDF do orçamento
# criar_orcamento(nome_arquivo, titulo, info_orcamento, produtos)

# print("PDF do orçamento criado com sucesso!")


from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus.flowables import HRFlowable

# Função para criar o PDF do orçamento
def criar_orcamento(nome_arquivo, titulo, info_orcamento, produtos):
    # Configurar o documento PDF
    doc = SimpleDocTemplate(nome_arquivo, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Define um tamanho de fonte personalizado

    # Lista de elementos para adicionar ao PDF
    elementos = []

    # Adicionar o título com tamanho de fonte personalizado
    elementos.append(Paragraph(titulo, styles['Title']))

    # Adicionar informações do orçamento com tamanho de fonte personalizado
    for chave, valor in info_orcamento.items():
        elementos.append(Paragraph(f"<b>{chave}:</b> {valor}", styles['Custom']))

    # Adicionar uma linha horizontal
    elementos.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black))

    # Adicionar a tabela de produtos com tamanho de fonte personalizado
    tabela = Table(produtos, colWidths=[100, 200, 100, 100])
    tabela.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elementos.append(tabela)

    # Construir o PDF
    doc.build(elementos)

# Informações do orçamento
titulo = "Orçamento de Produtos"
info_orcamento = {
    "Nome do Cliente": "Fulano de Tal",
    "Nome do Vendedor": "Beltrano",
    "Data": "20/02/2024",
    "Data de Entrega": "25/02/2024",
    "Endereço": "Rua das Flores, 123",
    "Valor Total da Compra": "R$ 500,00",
    "Quantidade de Produtos": "5",
    "CNPJ": "123.456.789/0001-00"
}

# Lista de produtos
produtos = [
    ["ID", "Descrição", "Preço Unitário", "Quantidade"],
    ["001", "Produto A", "R$ 100,00", "2"],
    ["002", "Produto B", "R$ 50,00", "3"]
]

# Nome do arquivo PDF
nome_arquivo = "orcamento.pdf"

# Criar o PDF do orçamento
criar_orcamento(nome_arquivo, titulo, info_orcamento, produtos)

print("PDF do orçamento criado com sucesso!")


