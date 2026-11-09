import pandas as pd
import time
import random
import pyautogui as py
import pywhatkit as kit

planilha = pd.read_csv("contatos.csv", sep=",")
planilha.columns = planilha.columns.str.strip()

# Trata o telefone e agrupa os contatos repetidos
planilha['Telefone_Limpo'] = "+" + planilha['Telefone'].astype(str).str.strip()
grupo_contatos = planilha.groupby('Telefone_Limpo')

for numero, grupo in grupo_contatos:
     nomes = grupo['Nome'].tolist()          

# Monta o texto dos nomes (Ex: "João", "João e Maria" ou "João, Maria e Ana")
     if len(nomes) == 1:
         texto_nomes = nomes[0]
     elif len(nomes) == 2:
        texto_nomes = f"{nomes[0]} e {nomes[1]}"
     else:
        texto_nomes = ", ".join(nomes[:-1]) + f" e {nomes[-1]}"

     saudacoes = ["Olá", "Oi", "Tudo bem"]
     saudacao = random.choice(saudacoes)      
    
     mensagem = f"{saudacao}, {texto_nomes}! Passando para lembrar sobre nossa ação odontológica no *sábado*, das *8h às 12h*. 👍 "      

     try:
         print(f"Enviando para {texto_nomes}...")         
         kit.sendwhatmsg_instantly(numero, message=mensagem, wait_time=20, tab_close=True, close_time=5)         
         print("Enviada!")         

         time.sleep(5)         
         tempo_espera = random.randint(45, 90)         
         print(f"Aguardando {tempo_espera} segundos antes do próximo envio...")
         time.sleep(tempo_espera)      

     except Exception as e:
         print(f"Erro no envio para {texto_nomes}: {e}")  

print("Processo concluído!")
