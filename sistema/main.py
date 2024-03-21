from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog, QTreeWidgetItem, QCheckBox)
from PySide6 import QtCore
from tl_login import Ui_login
import sys
from Tela_principal import Ui_MainWindow
from bc_dados import Banco_Dados
import sqlite3
from PySide6.QtSql import QSqlDatabase, QSqlTableModel 
import pandas as pd
from orc import Ui_orc
from datetime import datetime
from nota import Pdf
from time import sleep


class login(QWidget, Ui_login):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do Sisitema")
        self.btn_entrar.clicked.connect(self.checar_log)
        self.tentativas = 0

    def checar_log(self):
        self.user = Banco_Dados()
        autenticado = self.user.checar_usu(self.txt_usuario_log.text().upper(), self.txt_senha_log.text()) 
        if  autenticado.lower() == "admin" or autenticado.lower() == "user":
            self.w = Tela_principal(self.txt_usuario_log.text(), autenticado.lower())
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f"Login ou senha incorreto \n \n Tentativa: {self.tentativas + 1} de 3")
                msg.exec()
                self.tentativas += 1
            if self.tentativas >= 3:
                self.user.desconecta_db()
                sys.exit(0)

class Tela_principal(QMainWindow,Ui_MainWindow ):
    def __init__(self, user, perfil):
        self.perfil = perfil
        self.name_user = user
        super(Tela_principal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sisteam-EF")
        self.botoes()
        self.reseta_table()

        select_del = self.tw_pedido.selectionModel().selectionChanged.connect(self.selected_del)

        self.txt_filtro.textChanged.connect(self.update_filter_orc)

        self.txt_nome_prod.textChanged.connect(self.update_filter)

    def botoes(self):
        # paginas_sistema
        self.btn_pg_home.clicked.connect(lambda:self.Pages.setCurrentWidget(self.home))
        self.btn_pg_estoque.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_estoque))
        self.btn_pg_cad_produto.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_cad_prod))
        self.btn_pg_cd_usu.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_cad_usu))
        if self.perfil == "user":
            self.btn_pg_cd_usu.setVisible(False)
            self.pg_cad_usu.setVisible(False)
        self.btn_pg_orc.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_orc))
        self.btn_pg_sobre.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_sobre))

        self.btn_cad_usu.clicked.connect(self.cadastrar_usuario)

        self.btn_cad_produto.clicked.connect(self.cadastrar_produto)

        self.btn_altera_estoque.clicked.connect(self.alterar_lista)

        self.btn_adiciona.clicked.connect(self.adcionar_pedido)

        self.btn_retirar.clicked.connect(self.deleta_pedido)

        self.btn_fecha_orc.clicked.connect(self.fecha_orc)
                                            
    def cadastrar_usuario(self):
        usuario = self.txt_nome_usu.text()
        email = self.txt_email.text()
        senha = self.txt_senha.text()
        comfirma_senha = self.txt_comfirma_senha.text()
        perfil = self.cb_perfil.currentText()

        if senha != comfirma_senha:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas divergentes")
            msg.setText("A senha não e igual")
            msg.exec()
            return None
        elif email.endswith("@gmail.com") or  email.endswith("@hotmail.com"):
            db = Banco_Dados()
            db.conecta_db()
            db.insert_user(usuario, email, senha, perfil)
            db.desconecta_db()
            msg = QMessageBox()
            msg.setWindowTitle("Cadastro realizado")
            msg.setText("Novo Usuario cadastro no banco de dados")
            msg.exec()
            self.txt_nome_usu.setText("")
            self.txt_email.setText("")
            self.txt_senha.setText("")
            self.txt_comfirma_senha.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Email Invalido")
            msg.setText("O email vc digitou esta incorreto")
            msg.exec()
            return None

    def cadastrar_produto(self):
        tipo = self.txt_novo_tipo.text()
        nome = self.txt_novo_produto.text()
        preco = self.txt_novo_quant.value()
        quantidade = self.txt_quantidade_cad_produto.value()
        db = Banco_Dados()
        db.insert_prod(tipo, nome, preco,quantidade)
        msg = QMessageBox()
        msg.setWindowTitle("Cadastro realizado")
        msg.setText("Novo Produto cadastro no banco de dados")
        msg.exec()    
        self.txt_novo_tipo.setText("")
        self.txt_novo_produto.setText("")
        self.txt_novo_quant.setValue(0)
        self.txt_quantidade_cad_produto.setValue(0)
        self.reseta_table()

    def table_estoque(self):
        
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("sistema.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_estoque.setModel(self.model)
        self.model.setTable("produtos")
        self.model.select()
        self.tb_estoque.selectionModel().selectionChanged.connect(self.selecionado)

    def selecionado(self,selected):
        lista = list()
        for ix in selected.indexes():
            lista.append(ix.data())
        self.txt_cod.setText(str(lista[0]))
        self.txt_tipo.setText(lista[1])
        self.txt_nome_prod.setText(lista[2])
        self.txt_quant.setValue(lista[4])
        self.txt_preco.setValue(lista[3])

    def limpa_campo(self):
        self.txt_tipo.setText("")
        self.txt_nome_prod.setText("")
        self.txt_preco.setValue(0)
        self.txt_quant.setValue(0)
        self.txt_cod.setText("")

    def alterar_lista(self):
        tipo = self.txt_tipo.text()
        nome = self.txt_nome_prod.text()
        preco = self.txt_preco.value()
        quantidade = self.txt_quant.value()
        cod = self.txt_cod.text()
        db = Banco_Dados()
        db.update_prod(cod, tipo, nome, preco,quantidade)
        self.reseta_table()
        self.limpa_campo()

    def update_filter(self, s):
        # s = re.sub("[\W_]+", "", s)
        filter_str = 'nome LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    def table_estoque_orc(self):
        cn = sqlite3.connect("sistema.db")
        result = pd.read_sql_query("SELECT * FROM produtos", cn)
        result = result.values.tolist()
        newlista = []
        def strin(word):
            return str(word)
        for c in result:
            lista = list(map(strin, c))
            newlista.append(lista)

 
        for i in newlista:
            if int(i[4]) > 0:
                self.campo = QTreeWidgetItem(self.tw_estoque, i)

        self.tw_estoque.setSortingEnabled(True)
        select = self.tw_estoque.selectionModel().selectionChanged.connect(self.selected)
        

        

        # for i in range(1, 15):
        #     self.tw_estoque.resizeColumnToContents(i)

    def adcionar_pedido(self):
        
        self.lista_pedido = []
        db = Banco_Dados()
        retirada = self.txt_quantidade_orc.value()
        lista = db.pega_item(int(self.lista_select[0]), int(self.txt_quantidade_orc.value()), add=True)
        if lista == "Invalido":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Fora do estoque")
            msg.setText("O Quantidade desejada e maior do que a do estoque, escolha um valor menor")
            msg.exec()
        else:
            self.lista_pedido.append(lista)
            self.lança_pedido()
            self.reseta_table()

    def deleta_pedido(self):    
        cn = Banco_Dados()
        cn.pega_item(int(self.lista_select_del), int(self.quant), add= False )
        
        parent = self.tw_pedido.invisibleRootItem()
        parent.removeChild(parent.child(self.linha))
        self.reseta_table()
        
    def selected_del(self, sele):
        self.lista_select_del = ""
        self.linha = 0
        self.quant = ""

        cont = 0
        for ix in sele.indexes():
            if cont <= 0:
                self.lista_select_del = ix.data()
                self.linha = ix.row()
               

            if cont == 4:
                self.quant = ix.data()

            else:
                cont += 1
       
    def selected(self, sl):
        self.lista_select = list()
        for ix in sl.indexes():
            self.lista_select.append(ix.data())        

    def lança_pedido(self):
        newlista = []
        def strin(word):
            return str(word)
        for c in self.lista_pedido:
            lista = list(map(strin, c))
            lista.append(str(self.txt_quantidade_orc.value()))
            newlista.append(lista)
      

        for i in newlista:
            self.campo = QTreeWidgetItem(self.tw_pedido, i)

        self.tw_pedido.setSortingEnabled(True)
        self.txt_quantidade_orc.setValue(1)

    def reseta_table(self):
        self.tw_estoque.clear()

        self.table_estoque_orc()
        self.table_estoque()

    def fecha_orc(self):
        
        lista = list()
        linha = list()
        parent = self.tw_pedido.invisibleRootItem()
        for row in range(parent.childCount()):
            child = parent.child(row)
            linha.clear()
            for c in range(5):  
                linha.append(child.text(c))
            lista.append(linha.copy())

        self.tw_pedido.clear()
        self.tl_orc = Tela_orc(lista, self.name_user)
        self.tl_orc.show()

    def update_filter_orc(self, s):
        # s = re.sub("[\W_]+", "", s)
        filter_str =  '{}%'.format(s)
        print (filter_str)
        self.tw_estoque.clear()
        db = Banco_Dados()
        db.conecta_db()
        db.cursor.execute(""" SELECT * FROM produtos WHERE nome LIKE '%s'""" % filter_str)
        result = db.cursor.fetchall()
        newlista = []
        def strin(word):
            return str(word)
        for c in result:
            lista = list(map(strin, c))
            newlista.append(lista)

        for i in newlista:
            self.campo = QTreeWidgetItem(self.tw_estoque, i)

        self.tw_estoque.setSortingEnabled(True)

class Tela_orc(QWidget, Ui_orc, Ui_MainWindow):
    def __init__(self, lista, user):
        super(Tela_orc, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Fechar Orçamento")

        self.lista = lista
        self.nome_usu = user

        hj = datetime.now()
        print(hj.hour, hj.minute)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(hj.year, hj.month, hj.day), QtCore.QTime(0, 0)))

        self.tb_orc()
        self.valor_tot()
        self.botoes_orc()

    def tb_orc(self):
        for i in self.lista:
            self.campo = QTreeWidgetItem(self.tb_orc_pedido, i)
            self.tb_orc_pedido.setSortingEnabled(True)
        
        data = self.dateTimeEdit.date()
        self.date = f"{data.getDate()[2]}/{data.getDate()[1]}/{data.getDate()[0]}"
        self.progressBar.setVisible(False)
     
    def valor_tot(self):
        petisquiras = []
        outros = []
        quantidade_pet = []
        quantidade_other = []
        for lis in self.lista:
            if lis[1] == "Petisqueira":
                quantidade_pet.append(int(lis[4]))
                petisquiras.append(float(lis[3]))
            else:
                quantidade_other.append(int(lis[4]))
                outros.append(float(lis[3]))

        sun = soma = 0             
        self.desconto = False
        for n in quantidade_pet:
            sun += n
        if sun >= 10:
            self.desconto = True
            for e in range(0, len(petisquiras)):
                petisquiras[e] = float(25)       
        
        tudo = petisquiras + outros
        quanttot = quantidade_pet + quantidade_other

        self.quant = 0
        for v in quanttot:
            self.quant += v 

        for c in range(0, len(tudo)):
            num = tudo[c]
            q = quanttot[c]
            num *= q
            soma += num
        print(soma)
        self.total = soma
    def botoes_orc(self):
        self.btn_pdf.clicked.connect(self.gera_Nota)

    def gera_Nota(self):
        self.progressBar.setVisible(True)
        valor = 0
        for c in range(101):
            self.progressBar.setValue(valor)
            valor += 1
            sleep(0.1)
        self.progressBar.setVisible(False)
        nt = Pdf()
        nt.geraNota(self.date, self.total, self.quant, self.lista, self.txt_cliente.text(), self.txt_cnpj.text(), self.nome_usu, self.comboBox.currentText())
        print("Gerando PDF")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = login()
    window.show()
    app.exec()