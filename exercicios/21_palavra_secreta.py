'''Jogo da palavra secreta --> Propor a palavra secreta --> Usuario so podera digitar uma letra --> Se a letra estiver na palavra --> Exibir a letra --> Se a letra nao estiver na palavra --> Exibir * --> Fazer a contagem de tentativas do usuario'''

palavra_secreta = 'Anagrama'
palavra_secreta_formatada = palavra_secreta.lower()
lista_secreta_asterisco = list('*' * len(palavra_secreta_formatada))
ultima_letra = ''
contador = 0

while True:

    palavra_secreta_asterisco = ''

    letra_usuario = input('Digite apenas uma letra: ')
    letra_usuario_formatada = letra_usuario.lower().strip()
    
    while (letra_usuario_formatada.isnumeric() is True) or (letra_usuario_formatada.isalnum() is False) or (letra_usuario_formatada.isalpha() is False) or (len(letra_usuario_formatada) > 1):
        print('Valor inválido!')
        letra_usuario = input('Por favor, digite apenas uma letra: ').lower()
        letra_usuario_formatada = letra_usuario.lower().strip()
        contador += 1
    
    for indice_letra_secreta in range(0, len(palavra_secreta_formatada)):
        if palavra_secreta_formatada[indice_letra_secreta] == letra_usuario_formatada:
                lista_secreta_asterisco[indice_letra_secreta] = letra_usuario_formatada

    
    for letra in lista_secreta_asterisco:
        palavra_secreta_asterisco += letra
    
    print(palavra_secreta_asterisco.capitalize())

    contador += 1

    if lista_secreta_asterisco == list(palavra_secreta_formatada):
        break

print(f'Parabéns! Você acertou a palavra em {contador} tentativas.')