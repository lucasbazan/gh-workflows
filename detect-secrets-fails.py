# Este é um exemplo de arquivo Python com segredos embutidos

# Chave de API do serviço fictício
api_key = "12345-abcde-67890-fghij"

# Senha do banco de dados
db_password = "supersecretpassword"

# Token de acesso
access_token = "abcdef1234567890"

# Função que usa os segredos
def connect_to_service(api_key, db_password, access_token):
    print("Conectando ao serviço com a chave de API:", api_key)
    print("Usando a senha do banco de dados:", db_password)
    print("Token de acesso:", access_token)

# Chamada da função
connect_to_service(api_key, db_password, access_token)
