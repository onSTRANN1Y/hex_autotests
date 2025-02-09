from code.capitalize import capitalize

print('hi')

if capitalize('hello!') != 'Hello!':
    raise Exception(f'Ошибка:Ожидается вывод "Hello!", вывелось {capitalize("hello!")}')
if capitalize('') != '':
    raise Exception('Ошибка')
print('Все тесты выполнены. Ошибок нет!')

