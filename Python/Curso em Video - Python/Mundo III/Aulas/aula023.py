'''ERROS E EXCEÇÕES'''

#print('oi') #execução ok
#print(x) #erro  -- variavél não declarada

#erro Sintatico - Sintaxe correta

#erro Semântico - erro de escrita

#Exceções:    - List Exceptions PY
#NameError
#ValueError
#ZeroDivisionError
#TypeError
#IndexError
#KeyError
#EOFError
#KeyboardInterrupt
#OSError
#MemoryError
#ConnectionError
#RuntimeError
#ModuleNotFoundError

#Comando para resolver problemas:

#try:
    #Operação
#except:
    #Falhou

'''PARTE PRATICA'''
#Exemplo 1
try: #tente
    a= int(input('Numerador: '))
    b= int(input('Denominador: '))
    r = a/b
except Exception as erro: #exceto com as classes
    print(f'Problema encontrado foi {erro.__class__}')
except: #exceto
    print('Infelizmente tivemos um problema :(')
else: #senão
    print(f'O resultado é {r:.1f}')
finally: #finalmente
    print('Volte sempre! Muito Obrigado!')

#Exemplo 2
try: #tente
    a= int(input('Numerador: '))
    b= int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: #senão
    print(f'O resultado é {r:.1f}')
finally: #finalmente
    print('Volte sempre! Muito Obrigado!')
