# importar as bibliotecas
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import PySimpleGUI as sg

#PySimpleGUI

class TelaPython:
    def __init__(self):
        sg.theme('Reddit')
        # Layout
        layout = [

            [sg.Text('Contato 1 '), sg.InputText(key='contato1', size=(10,1)), sg.Text('Contato 11 '), sg.InputText(key='contato11', size=(10,1))],
            [sg.Text('Contato 2 '), sg.InputText(key='contato2', size=(10,1)), sg.Text('Contato 12 '), sg.InputText(key='contato12', size=(10,1))],
            [sg.Text('Contato 3 '), sg.InputText(key='contato3', size=(10,1)), sg.Text('Contato 13 '), sg.InputText(key='contato13', size=(10,1))],
            [sg.Text('Contato 4 '), sg.InputText(key='contato4', size=(10,1)), sg.Text('Contato 14 '), sg.InputText(key='contato14', size=(10,1))],
            [sg.Text('Contato 5 '), sg.InputText(key='contato5', size=(10,1)), sg.Text('Contato 15 '), sg.InputText(key='contato15', size=(10,1))],
            [sg.Text('Contato 6 '), sg.InputText(key='contato6', size=(10,1)), sg.Text('Contato 16 '), sg.InputText(key='contato16', size=(10,1))],
            [sg.Text('Contato 7 '), sg.InputText(key='contato7', size=(10,1)), sg.Text('Contato 17 '), sg.InputText(key='contato17', size=(10,1))],
            [sg.Text('Contato 8 '), sg.InputText(key='contato8', size=(10,1)), sg.Text('Contato 18 '), sg.InputText(key='contato18', size=(10,1))],
            [sg.Text('Contato 9 '), sg.InputText(key='contato9', size=(10,1)), sg.Text('Contato 19 '), sg.InputText(key='contato19', size=(10,1))],
            [sg.Text('Contato 10'), sg.InputText(key='contato10', size=(10,1)), sg.Text('Contato 20 '), sg.InputText(key='contato20', size=(10,1))],
            [sg.Text('Mensagem')],
            [sg.Multiline(key='mensagem' ,size=(35, 3)), sg.Button('Enviar')]

        ]
        # Janela
        self.janela = sg.Window('Dados do Usuário', size=(480, 360)).layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            contato1 = self.values['contato1']
            contato2 = self.values['contato2']
            contato3 = self.values['contato3']
            contato4 = self.values['contato4']
            contato5 = self.values['contato5']
            contato6 = self.values['contato6']
            contato7 = self.values['contato7']
            contato8 = self.values['contato8']
            contato9 = self.values['contato9']
            contato10 = self.values['contato10']
            contato11 = self.values['contato11']
            contato12 = self.values['contato12']
            contato13 = self.values['contato13']
            contato14 = self.values['contato14']
            contato15 = self.values['contato15']
            contato16 = self.values['contato16']
            contato17 = self.values['contato17']
            contato18 = self.values['contato18']
            contato19 = self.values['contato19']
            contato20 = self.values['contato20']
            mensagem_gui = self.values['mensagem']

            # importar as bibliotecas
            from selenium import webdriver
            import time
            from selenium.webdriver.common.keys import Keys
            # nav wtz web
            driver = webdriver.Chrome(r'chromedriver.exe')
            driver.get('https://web.whatsapp.com/') #url do wtzp
            time.sleep(30)
            #definir contatos e grupos e mensagens a ser enviadas
            contatos = [
                contato1, contato2, contato3, contato4, contato5, contato6, contato7, contato8, contato9, contato10, contato11, contato12, contato13, contato14, contato15, contato16, contato16, contato17, contato18, contato19, contato20
            ] # o nome tem que estar da mesma forma que ta salvo
            mensagem = mensagem_gui # só a mensagem que voce quer enviar
            #search groups
            def buscar_contato(contato):
                campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
                time.sleep(0.10)
                campo_pesquisa.click()
                campo_pesquisa.send_keys(contato)
                campo_pesquisa.send_keys(Keys.ENTER)
                time.sleep(0.5)

            def enviar_mensagem(mensagem):
                campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]') # inspecionado html no whatsapp
                campo_mensagem[1].click()
                time.sleep(3)
                campo_mensagem[1].send_keys(mensagem)
                campo_mensagem[1].send_keys(Keys.ENTER)




            for contato in contatos:
                buscar_contato(contato)
                enviar_mensagem(mensagem)


tela = TelaPython()
tela.Iniciar()
