import pandas as pd

# 1. CRIAR O ARQUIVO INICIAL (Simulando a origem dos dados)
data = {
    'Nome': ['Alice Oliveira', 'Bruno Santos', 'Carla Mendes'],
    'Conta': ['12345-6', '98765-4', '55555-5'],
    'Cartão': ['**** 1234', '**** 5678', '**** 9012']
}

df_inicial = pd.DataFrame(data)
df_inicial.to_csv('clientes.csv', index=False, encoding='utf-8')

# 2. EXTRAÇÃO
df = pd.read_csv('clientes.csv')

# 3. TRANSFORMAÇÃO (Gerar mensagens personalizadas)
def gerar_mensagem(linha):
    return f"Olá {linha['Nome']}, sua conta {linha['Conta']} está ativa. Seu cartão final {linha['Cartão'][-4:]} já pode ser usado!"

df['Mensagem'] = df.apply(gerar_mensagem, axis=1)

# 4. CARREGAMENTO (Salvar em um novo arquivo)
df.to_csv('clientes_com_mensagens.csv', index=False, encoding='utf-8')

print("Pipeline executado com sucesso!")
print("\n--- Conteúdo do arquivo final ---")
print(df[['Nome', 'Mensagem']])