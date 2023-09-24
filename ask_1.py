phone_book = {}
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
    for i, contact in enumerate(contacts, 1):
        phone_book[i] = contact.strip().split(';')
    #print(phone_book)

def save_file():
    data = []
    for contact in phone_book.values():
        contact = ';'.join(contact)
        data.append(contact)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def show_all_cont(pb:dict):
    print()
    for i, contact in pb.items():
        print(f'{i:>3}.{contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
    print()

def new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий: ')    
    u_id = max(phone_book.keys())+1
    phone_book[u_id] = [name,phone,comment]
    return name

def find_contact():
    result = {}
    word = input('Введите ключевое слово для поиска: ').lower()
    for i, contact in phone_book.items():
        if word in ''.join(contact).lower():
            result[i]=contact
    return result

def edit_contact():
    result = find_contact()
    show_all_cont(result)
    u_id = int(input('Введите ID контакта,который хотите изменить: '))
    c_name, c_phone, c_comment = phone_book[u_id]
    name = input('Введите новое имя контакта: ')
    phone = input('Введите новый телефон контакта: ')
    comment = input('Введите новый комментарий: ')  
    phone_book[u_id] = [name if name else c_name, phone if phone else c_phone,comment if comment else c_comment]
    return name if name else c_name

def del_contact():
    result = find_contact()
    show_all_cont(result)
    u_id = int(input('Введите ID контакта,который хотите удалить: '))
    name = phone_book.pop(u_id)
    return name[0]


menu = '''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''

while True:
    print(menu)
    choice = input('Выберите пункт меню: ')
    print()
    match choice:
        case '1':
            open_file()
            print('\nТелефонная книга загружена!\n')          
        case '2':
            save_file()
            print('\nТелефонная книга сохранена!\n')
            print()
        case '3':
            show_all_cont(phone_book)
            print()
        case '4':
            name = new_contact()
            print(f'\n Контакт {name} удачно создан!\n')
        case '5':
            result = find_contact()
            show_all_cont(result)
        case '6':
            name = edit_contact()
            print(f'Контакт {name} успешно изменен.')
        case '7':
            name = del_contact()
            print(f'Контакт {name} успешно удален.')
        case '8':
            print('До свидания, всего хорошего!')
            print()
            break
        case _:
            print('Ошибка ввода! Выберите пункт меню от 1 до 8')
            print()