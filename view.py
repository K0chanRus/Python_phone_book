import text
from model import Contact, PhoneBook

def main_menu() -> int:
    for n, item in enumerate(text.main_menu):
        if n == 0:
            print(item)
        else:
            print(f'\t{n}. {item}')
    while True:
        choice = input(text.main_menu_choice)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(f'Введите пункт меню от 1 до {len(text.main_menu) - 1}')

def show_contacts(p_book: dict[int, Contact], error_messege: str):
    max_size = p_book.max_len()
    if p_book:
        print('\n' + '=' * (sum(max_size) + 9))
        for n, contact in p_book.phonebook.items():
            print(f'{n:>3}. {contact.name:<{max_size[0] + 1}} {contact.phone:<{max_size[1] + 1}} {contact.comment:<{max_size[2] + 1}}')
        print('=' * (sum(max_size) + 9) + '\n')
    else:
        print(error_messege)

def print_massage(massage: str):
    print('\n' + '=' * len(massage))
    print(massage)
    print('=' * len(massage) + '\n')

def add_contact(massage: list[str], contact: list[str] = None):
    contact = contact if contact else ['', '', '']
    for n, mes in enumerate(massage):
        field = input(mes)
        contact[n] = field if field else contact[n]
    return contact

def input_data(massage: str) -> str:
    return input(massage)

