import os


def add_contact(file):
    last_name = input('Last name: ')
    first_name = input('First name: ')
    patronymic = input('Third name: ')
    phone_number = input('Phone number: ')



    contact_id = sum(1 for _ in open(file, 'r', encoding='utf-8'))
    with open(file, 'a', encoding='utf-8') as fd:
        fd.write(
            f'{contact_id},{last_name},{first_name},{patronymic},{phone_number}\n')


def get_contacts_from_file(file):
    if not os.path.isfile(file):
        with open(file, 'w', encoding='utf-8') as fd:
            fd.write('ID,Last Name,First Name,Patronymic,Phone Number\n')  # Header
    with open(file, 'r', encoding='utf-8') as fd:
        contacts = fd.readlines()
    result = []
    for i, c in enumerate(contacts):
        lst = [str(i)]
        lst.extend(c.rstrip().split(','))
        result.append(lst)
    return result


def copy_all_contacts(file, dest_file):
    constacts = get_contacts_from_file(file)
    with open(dest_file, 'w', encoding='utf-8') as dest_fd:
        dest_fd.write(','.join(constacts[0][1:]) + '\n')  # Header
        for contact in constacts[1:]:
            dest_fd.write(','.join(contact[1:]) + '\n')
    print('All contacts copied successfully!')


def print_contacts(contacts_list):
    for contact in contacts_list:
        print(' | '.join(contact))


def show_all(file):
    contacts = get_contacts_from_file(file)
    print_contacts(contacts)


def search_contacts(file):
    search_str = input('Enter the Second name for search: ').lower()
    contacts = get_contacts_from_file(file)
    search_result = []
    for contact in contacts:
        if search_str in contact[1].lower():
            search_result.append(contact)
    return search_result


def edit_contact(f):
    res = search_contacts(f)
    print_contacts(res)
    select_contact = int(input('Choose the index of the contact: '))
    all_contacts = get_contacts_from_file(f)
    print(all_contacts)
    last_name = input(
        'Enter the last name for editing or press Enter to keep the current one: ')
    first_name = input(
        'Enter the first name for editing or press Enter to keep the current one: ')
    patronymic = input(
        'Enter the patronymic for editing or press Enter to keep the current one: ')
    phone_number = input(
        'Enter the phone number for editing or press Enter to keep the current one: ')
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
    file_name = 'contacts.csv'
    flag = True
    while flag:
        user_answer = input(
            '''\nEnter these number for:\n
    1 — Record
    2 — Read
    3 — Search
    4 — Edit contact
    5 — Copy data to another file 
    0 — Quit\n
    =>: '''
        )
        if user_answer == '1':
            add_contact(file_name)
        elif user_answer == '2':
            show_all(file_name)
        elif user_answer == '3':
            print_contacts(search_contacts(file_name))
        elif user_answer == '4':
            edit_contact(file_name)
        elif user_answer == '5':
            new_file_name = input('Enter the new file name: ')
            copy_all_contacts(file_name, new_file_name)
        elif user_answer == '0':
            print('Thanks for using this program :)')
            flag = False


if __name__ == '__main__':
    main()
