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
        print(' | '.join(contact.rstrip().split(','))) # rstrip() mad zapisivat' o nem


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