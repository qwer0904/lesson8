def copy_line(source_file_path, destination_file_path):
    try:
        
        with open(source_file_path, 'r', encoding='utf-8') as source_file:
            
            lines = source_file.readlines()

            
            line_number = int(input("Введите номер строки для копирования: ")) - 1

            
            if 0 <= line_number < len(lines):
                
                with open(destination_file_path, 'a', encoding='utf-8') as destination_file:
                    
                    destination_file.write(lines[line_number])
                    print("Строка успешно скопирована.")
            else:
                print("Ошибка: Некорректный номер строки.")
    except FileNotFoundError:
        print("Ошибка: Один из файлов не найден.")


source_file_path = 'phonebook.csv'
destination_file_path = 'phon.txt'

copy_line(source_file_path, destination_file_path)

