def add_contact(file):
    last_name = input('Last name: ')
    first_name = input('First name: ')
    patronymic = input('Third name: ')
    phone_number = input('Phone number: ')
    with open(file, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name},{first_name},{patronymic},{phone_number}')
    

def show_all(file):
    with open(file, 'r', encoding='utf-8') as fd:
        contacts = fd.readlines()
    for contact in contacts:
        print(' | '.join(contact.rstrip().split(',')))


def main():
    file_name = 'contacts.txt'
    flag = True
    while flag:
        user_answer = input('')
        if user_answer == '1':
            add_contact(file_name)
        elif user_answer == '2':
            print(show_all(file_name))
        elif user_answer == '0':
            print('Thanks :)')
            flag = False

if __name__ == '__main__':
    main()




##############    ##############    ##############    ##############

def add_contact(file):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name},{first_name},{patronymic},{phone_number}\n')

def get_contacts_from_file(file):
    with open(file, 'r', encoding='utf-8') as fd:
        contacts = fd.readlines()
    result = []
    for i, c in enumerate(contacts):
        # print(f'{i} = {c}')
        # print('[***]', c.rstrip().split(','))
        lst = [str(i)]
        lst.extend(c.rstrip().split(','))
        # print(lst)
        result.append(lst)
    return result
    # return [[idx].extend(contact.rstrip().split(',')) for idx, contact in enumerate(contacts)]


def print_contacts(contacts_list):
    for contact in contacts_list:
        print(' | '.join(contact))

def show_all(file):
    contacts = get_contacts_from_file(file)
    # print(contacts)
    print_contacts(contacts)

def search_contacts(file):
    search_str = input('Введите фамилию для поиска: ').lower()
    contacts = get_contacts_from_file(file)
    search_result = []
    for contact in contacts:
        if search_str in contact[1].lower():
            search_result.append(contact)
    return search_result


def edit_contact(f):
    res = search_contacts(f)
    print_contacts(res)
    select_contact = int(input('выберите индекс контакта: '))
    all_contacts = get_contacts_from_file(f)
    print(all_contacts)
    last_name = input('Введите фамилию для изменения или Enter если оставить прежнюю: ')
    first_name = input('Введите имя для изменения или Enter если оставить прежнее: ')
    patronymic = input('Введите отчество для изменения или Enter если оставить прежнее: ')
    phone_number = input('Введите номер телефона для изменения или Enter если оставить прежний: ')
    if len(last_name) > 0:
        all_contacts[select_contact][1] = last_name
    if len(first_name) > 0:
        all_contacts[select_contact][2] = first_name
    if len(patronymic) > 0:
        all_contacts[select_contact][3] = patronymic
    if len(phone_number) > 0:
        all_contacts[select_contact][4] = phone_number
    print(all_contacts)
    res = []
    for i in all_contacts:
        res.append(f"{','.join(i[1:])}\n")
    print(res)
    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(res)


def main():
    file_name = 'contacts.txt'
    flag = True
    while flag:
        user_answer = input('Выберите для записи - 1, для чтения - 2, для поиска - 3, редактировать контак - 4, для выхода - 0: ')
        if user_answer == '1':
            add_contact(file_name)
        elif user_answer == '2':
            show_all(file_name)
        elif user_answer == '3':
            print_contacts(search_contacts(file_name))
        elif user_answer == '4':
            edit_contact(file_name)
        elif user_answer == '0':
            print('Спасибо за использование нашей программы')
            flag = False


if __name__ == '__main__':
    main()