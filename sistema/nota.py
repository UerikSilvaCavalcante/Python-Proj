import webbrowser
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus.flowables import HRFlowable
from orc import Ui_orc
from datetime import datetime

class Pdf(Ui_orc):
    def printCliente(self):
        webbrowser.open(self.nome_arquivo)
    # def geraNota(self, date, total, quant, lista, txt_cliente, txt_cnpj, user,pagamento):
        # data_hj = datetime.now()
        # self.pdf = SimpleDocTemplate("Orçamento.pdf", pagesize=A4 )

        # self.c = canvas.Canvas("Orçamento.pdf", pagesize=A4 )
        # self.c.setFont("Helvetica-Bold", 24)
        # self.c.drawString(250, 800, "Pedido")
        # self.c.rect(0, 740, 600, 10, fill=True, stroke=False)

        # self.c.setFont("Helvetica-Bold", 18)
        

        # self.c.drawString(20, 700, f'Cliente: {txt_cliente}')
        # self.c.drawString(20, 680, f'Data de expidação: {data_hj.day}/{data_hj.month}/{data_hj.year}')
        # self.c.drawString(300, 700, f'Vendedor: {user}')
        # self.c.drawString(300, 680, f'Horario: {data_hj.hour}:{data_hj.minute}')
        # self.c.drawString(20, 660, f'Data de entrega: {date}')
        # self.c.drawString(20, 640, f'Endereço: Exemplo de endereço')
        # self.c.drawString(20, 620, f'Valor total da compra: {total}')
        # self.c.drawString(300, 620, f'Valor total da compra: {pagamento}')
        # self.c.drawString(300, 600, f'Números de produtos : {quant}')
        # self.c.drawString(20, 600, f'CNPJ: {txt_cnpj[:2]}.{txt_cnpj[2:4]}.{txt_cnpj[4:6]}/0001-{txt_cnpj[6:]}')
        # self.c.rect(0, 580, 600, 10, fill=True, stroke=False)

        # # self.c.drawString(230, 560, f'Lista de Produtos' )
        # # self.c.drawString(50, 520, f'codigo: ')
        # # self.c.drawString(150, 520, f'Tipo: ')
        # # self.c.drawString(270, 520, f'Produto: ')
        # # self.c.drawString(400, 520, f'Preço: ')
        # # self.c.drawString(495, 520, 'Quant.')
        # # self.c.rect(20, 540, 550, -25, fill=False, stroke=True)

        # # self.eixo = 470
        # # self.eixo_lin = 450
        # # self.eixo_margin = -130

       

        # tabela = Table(data)
        # style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        #             ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        #             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        #             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        #             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        #             ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        #             ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        # tabela.setStyle(style)

        # tabela.wrapOn(self.c, 0,0)
        # tabela.drawOn(self.c, 150, 50)

        
        
        # # for n in lista:
        # #     self.c.setFont("Helvetica", 18)
        # #     self.c.drawString(50, self.eixo, n[0])
        # #     self.c.drawString(150, self.eixo,  n[1])
        # #     self.c.drawString(270, self.eixo,  n[2])
        # #     self.c.drawString(410, self.eixo,  n[3])
        # #     self.c.drawString(505, self.eixo,  n[4])
        # #     self.c.rect(40, self.eixo_lin, 500, 3, fill=True, stroke=False)
        # #     self.eixo -= 50
        # #     self.eixo_lin -= 48
        # #     self.eixo_margin -= 40

        # # self.c.rect(20, 495, 550, self.eixo_margin, fill=False, stroke=True)

        # self.c.showPage()
        # self.c.save()
        # self.printCliente()

    def criar_orcamento(self,nome_arquivo, titulo, info_orcamento, produtos):
        # Configurar o documento PDF
        doc = SimpleDocTemplate(nome_arquivo, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Lista de elementos para adicionar ao PDF
        elementos = []

        # Adicionar o título
        elementos.append(Paragraph(titulo, styles['Title']))

        elementos.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black))

        elementos.append(Spacer(1, 30)) 


        # Adicionar informações do orçamento
        for chave, valor in info_orcamento.items():
            elementos.append(Paragraph(f"<b>{chave}:</b> {valor}"))

        elementos.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black))

        elementos.append(Spacer(1, 30)) 


        # Adicionar a tabela de produtos
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
    def geraNota(self, date, total, quant, lista, txt_cliente, txt_cnpj, user,pagamento):
        titulo = "Orçamento de Produtos"
        data_hj = datetime.now()
        info_orcamento = {
            "Nome do Cliente": txt_cliente,
            "Nome do Vendedor": user,
            "Data": f"{data_hj.day}/{data_hj.month}/{data_hj.year}",
            "Data de Entrega": date,
            "Endereço": "Rua das Flores, 123",
            "Valor Total da Compra": total,
            "Quantidade de Produtos": quant,
            "CNPJ":f"{txt_cnpj[:2]}.{txt_cnpj[2:4]}.{txt_cnpj[4:6]}/0001-{txt_cnpj[6:]}",
            "Forma de Pagameto": pagamento
        }

        # Lista de produtos
        data = [["Codigo", "Tipo", "Produto", "Preço", "Quantidade"]]

        for n in lista:
            data.append(n)
        # Nome do arquivo PDF
        self.nome_arquivo = f"Orçamento_cliente-{txt_cliente}.pdf"

        # Criar o PDF do orçamento
        self.criar_orcamento(self.nome_arquivo, titulo, info_orcamento, data)

        print("PDF do orçamento criado com sucesso!")