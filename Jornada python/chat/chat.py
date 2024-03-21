import flet as ft


def main(pagina):
    titulo = ft.Text('Hashzap')

    chat = ft.Column()
    def enviar_msg_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    pagina.pubsub.subscribe(enviar_msg_tunel)


    def enviar_msg(envento):
        text_msg = f'{nome_usuario.value}: {chat_msg.value}'
        pagina.pubsub.send_all(text_msg)
        #colocar o nome do usuario
        #limpar msg
        chat_msg.value = ""
        pagina.update()
    chat_msg = ft.TextField(label='Escreva uma mensgem', on_submit=enviar_msg)
    butao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_msg)


    def entrar_chat(envento):
        #fechar popup
        popup.open =False
        #limpar o tela
        pagina.remove(botao_entrar)
        pagina.add(chat)
        linha_msg = ft.Row(
            [chat_msg, butao_enviar]
        )
        pagina.add(linha_msg)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()
    
    nome_usuario = ft.TextField(label='Escreva seu nome', on_submit=entrar_chat)
    popup = ft.AlertDialog(open=False, modal=True, title=ft.Text('Hastag'), content=nome_usuario, actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)])

    def iniciar_chat(envento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        

    botao_entrar = ft.ElevatedButton ('Entrar', on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_entrar)

#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)