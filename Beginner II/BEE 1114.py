password = 2002
while True:
    attempt = int(input())
    if attempt == password:
        print('Acesso Permitido')
        break
    print('Senha Invalida')
