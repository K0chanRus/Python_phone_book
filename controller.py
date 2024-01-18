import text
import view
import model

def find_contact():
    word = view.input_data(text.input_search_word)
    result = model.find_contact(word)
    view.show_contacts(result, text.contact_not_faund(word))

def start_app():
    pb = model.PhoneBook()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                pb.open_file()
                view.print_massage(text.load_successful)
            case 2:
                pb.save_file()
                view.print_massage(text.save_successful)
            case 3:
                view.show_contacts(pb, text.empty_phone_book)
            case 4:
                contact = view.add_contact(text.new_contact)
                pb.new_contact(contact)
                view.print_massage(text.new_contact_added_successful(contact[0]))
            case 5:
                find_contact()
            case 6:
                find_contact()
                c_id = int(view.input_data(text.input_id_change_contact))
                c_contact = view.add_contact(text.change_contact, pb.phonebook[c_id ])
                pb.change_contact(c_id, c_contact)
                view.print_massage(text.contact_change_successful(c_contact[0]))
            case 7:
                find_contact()
                c_id = int(view.input_data(text.input_id_delite_contact))
                name = pb.delite_contact(c_id)[0]
                view.print_massage(text.contact_delite_successful(name))
            case 8:
                break
            