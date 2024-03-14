
def input_name():
     return input("Введите имя: ")

def input_surname():
     return input("Введите фамилию: ")

def input_patronumic():
     return input("Введите отчество: ")

def input_phone():
     return input("Введите номер телефона: ")

def input_address():
     return input("Введите адрес: ")

def create_contact():
     name = input_name()
     surname = input_surname()
     patronumic = input_patronumic()
     phone = input_phone()
     address = input_address()
     return f"{name} {surname} {patronumic} {phone}\n{address}\n\n"

def add_contact():
     contact = create_contact()
     with open(r"C:\Users\user\Desktop\Новая папка\Python_Course\phonebook.txt", "a", encoding='UTF-8') as f_w:
          f_w.write(contact)

def print_phonebook():
     with open(r"C:\Users\user\Desktop\Новая папка\Python_Course\phonebook.txt", "r", encoding='UTF-8') as f_r:
          contacts_str = f_r.read()
     list_contacts = contacts_str.rstrip().split("\n\n")
     for i, contact in enumerate(list_contacts, 1):
          print(i, contact+"\n")


def find_contact():
     search = input("Введите данные для поиска: ")
     print("Возможные варианты поиска:\n"
         "1. По имени\n"
         "2. По фамилии\n"
         "3. По отчеству\n"
         "4. По телефону\n"
         "5. По адресу\n"
          )
     var = input("Выберите вариант поиска: ")
     while var not in ("1", "2", "3", "4", "5"):
          print("Некорректный ввод!")
          var = input("Выберите вариант поиска: ")
     i_var = int(var) - 1
     with open(r"C:\Users\user\Desktop\Новая папка\Python_Course\phonebook.txt", "r", encoding='UTF-8') as f_r:
          contacts_str = f_r.read()
     list_contacts = contacts_str.rstrip().split("\n\n")
     for contact in list_contacts:
          contact_lst = contact.split()
          #print(contact_lst)
          if search in contact_lst(i_var):
               print(contact)

def copy_line(lines):
     line_num = int(input("Введите номер строки копирования: "))
     with open(r"C:\Users\user\Desktop\Новая папка\Python_Course\phonebook.txt", "r", encoding='UTF-8') as file_r:
          lines = file_r.readlines()
          if 0 < line_num <= len(lines):
               with open(r"C:\Users\user\Desktop\Новая папка\Python_Course\copybook.txt", "w", encoding='UTF-8') as file_w:
                    file_w.write(lines[line_num - 1])
                    print("Строка скопирована в файл copybook.txt")
          else:
               print("Некорректный номер строки")
       


def ui():
     with open(r"C:\Users\user\Desktop\Новая папка\Python_Course\phonebook.txt","a", encoding="UTF-8"):
          pass
    
     while True:
          print("\nМеню: ")
          print("1. Добавить контакт")
          print("2. Вывести все контакты")
          print("3. Найти контакт")
          print("4. Скопировать строку из файла")
          print("5. Выход")
          choise = input("Выберите действие: ")

          if choise == "1":
               elif choise == "2":
                    print_phonebook()
               elif choise == "3":
                    find_contact()
               elif choise == "4":
                    with open(r"C:\Users\user\Desktop\Новая папка\Python_Course\phonebook.txt", "r", encoding='UTF-8') as file_r:
                         lines = file_r.readlines()
               copy_line(lines)
               elif choise == "5":
                    break
          else:
                  print("Некорректный выбор, попробуйте еще раз.")
#                 copy_line()
#            else:

ui()