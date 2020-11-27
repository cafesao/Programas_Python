## Apenas para testes de comandos ##


with open('arquivos/arquivo.txt', 'r+') as text_file:
    print ('The file content BEFORE writing content:')
    print (text_file.read())
    text_file.write(' and I\'m looking for more')
    print ('The file content AFTER writing content:')
    text_file.seek(0)
    print (text_file.read())