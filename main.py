import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console

account_sid = "ACc4679be812014d772b472f5e4e55b7a2"
# Your Auth Token from twilio.com/console
auth_token  = "c900df94f5408f61ad093ee5f8dd2b4e"
client = Client(account_sid, auth_token)

# abrir os 6 arquivos em excel

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

message = client.messages.create(
    to="+5553984859488", 
    from_="+15017250604",
    body="f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'")

print(message.sid)

#para cada arquivo: 
# verificar se há algum valor na coluna vendas que seja maior que 55.000
#se for maior -> enviar um sms com o nome, o mes e as vendas do vendedor
#caso não seja maior, não vai fazer nada
