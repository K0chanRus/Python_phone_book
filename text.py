main_menu = ['Главное меню', 'Открыть файл', 'Сохранить файл', 'Показать контакты', 'Создать контакт', 'Найти контакт', 'Изменить контакт', 'Удалить контакт', 'Выход']

main_menu_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно загружена!'

save_successful = 'Телефонная книга успешно сохранена!'

empty_phone_book = 'Телефонная книга пуста или не открыта!'

new_contact = ['Введите имя: ', 'Введите номер телефона: ', 'Введите коментарий: ']

def new_contact_added_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен!'

input_search_word = 'Введите слово для поиска: '

def contact_not_faund(word: str) -> str:
    return f'Контакты содержащие {word} не найдены!'

input_id_change_contact = 'Введите ID контакта который хотитие изменить: '

change_contact = ['Введите новое имя или ENTER, чтобы оставить без изменений',
                'Введите новый номер телефона или ENTER, чтобы оставить без изменений',
                'Введите новый коментарий или ENTER, чтобы оставить без изменений']

def contact_change_successful(name: str) -> str:
    return  f'Контакт {name} успешно изменен!'

input_id_delite_contact = 'Введите ID контакта который хотитие удалить: '

def contact_delite_successful(name: str) -> str:
    return  f'Контакт {name} успешно удален!'