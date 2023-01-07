from translate import Translator

# Configure a tradução

s = Translator(from_lang='english', to_lang='pt-br')

# Traduz o desejado

desejado = s.translate(input('Digite o desejado: '))
traducao = s.translate(desejado)
# res = s.translate('Hello World')

# Mostra a Tradução

# print(res)
print("A tradução é: {}" .format(traducao))