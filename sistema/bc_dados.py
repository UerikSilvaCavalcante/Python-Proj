import sqlite3
import pandas as pd


class Banco_Dados():
    def __init__(self, name="sistema.db") -> None:
        self.name = name
        pass

    def conecta_db(self):
        self.conn = sqlite3.connect("sistema.db");print("Conectando ao banco de dados")
        self.cursor = self.conn.cursor()

    def desconecta_db(self):
        self.conn.close();print("Fechando banco de dados")

    def monta_tb_users(self):
        try: 
            self.conecta_db()
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                user TEXT UNIQUE NOT NULL,
                                email TEXT NOT NULL,
                                senha TEXT NOT NULL,
                                perfil TEXT NOT NULL
            ) """)
            self.conn.commit()
            self.desconecta_db()
        except AttributeError:
            print("Faça conexão")

    def insert_user(self, nome, mail, password, acess):
        # try:
        self.conecta_db()
        self.cursor.execute(""" INSERT INTO usuarios(user, email, senha , perfil) VALUES(?,?,?,?)""", (nome, mail, password, acess))
        self.conn.commit()
        self.desconecta_db()
        # except AttributeError:
        #     print("Erro ao cadastrar usuario")

    def checar_usu(self, user, password):
        self.conecta_db()
        self.cursor.execute("SELECT * FROM usuarios")
        pessoa = self.cursor.fetchall()
        self.desconecta_db()
        for i in pessoa:
            if i[1].upper() == user.upper() and i[3] == password and i[4] == "Adiministrador":
                return "admin"
            elif i[1].upper() == user.upper() and i[3] == password and i[4] == "Usuario":
                return "user"
            else:
                continue
        return "Sem acesso"
    
    def monta_tabela_prod(self):
        self.conecta_db()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS produtos(
                            cod INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            tipo TEXT NOT NULL,
                            nome TEXT NOT NULL,
                            preco FLOAT NOT NULL,
                            quantidade INT NOT NULL
        )""")
        self.desconecta_db()
    
    def insert_prod(self,tipo, nome, preco,quantidade):
        self.conecta_db()
        self.cursor.execute("INSERT INTO produtos(tipo, nome, preco, quantidade) VALUES(?,?,?,?)",(tipo, nome, preco, quantidade))
        self.conn.commit()
        self.desconecta_db()

    def update_prod(self, cod,tipo, nome, preco,quantidade):
        self.conecta_db()
        self.cursor.execute("UPDATE produtos SET tipo = ?, nome = ?, preco = ?, quantidade = ? WHERE cod = ?", (tipo, nome,preco, quantidade, cod,))
        self.conn.commit()
        self.desconecta_db()

    def pega_item(self, cod = 1, retirada = 1, add = False):
        self.conecta_db()

        cn = sqlite3.connect("sistema.db")
        quantidade_atual = pd.read_sql_query(f"SELECT quantidade FROM produtos WHERE cod = {cod}", cn)
        quantidade_atual = quantidade_atual.values.tolist()
        if add:
            if quantidade_atual[0][0] < retirada:
                return "Invalido"

            indexes = self.cursor.execute("SELECT cod, tipo, nome, preco FROM produtos WHERE cod = ?", (cod,))
            for i in indexes:
                # print(i[4])
                retirada = quantidade_atual[0][0] - retirada
            self.cursor.execute("UPDATE produtos SET quantidade = ? WHERE cod = ?", (retirada, cod))
            self.conn.commit()
            self.desconecta_db()
            return i
        else:
            quantidade_atual[0][0] = quantidade_atual[0][0] + retirada
            self.cursor.execute("UPDATE produtos SET quantidade = ? WHERE cod = ?", (quantidade_atual[0][0], cod))
            self.conn.commit()


        
        

        



if __name__ == "__main__":
    db = Banco_Dados()
    db.conecta_db()
    db.monta_tb_users()
    db.monta_tabela_prod()
    db.pega_item()
    db.desconecta_db()
