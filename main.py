from models import Library

def main():

    library = Library()
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        try:
            choice = input("Выберите действие (1-6): ")

            if choice == '1':
                #добавляем книгу
                while True:
                    title = input("Введите название книги: ")
                    author = input("Введите автора книги: ")
                    year = input("Введите год релиза книги: ")
                    if title and author and year:
                        break
                    else:
                        print('Название, автор и год не должны быть пустыми.')
                res = library.add_new_book(title, author, year)
                print(res)

            elif choice == '2':
                #удаляем книгу
                try:
                    book_id = int(input("Введите ID книги для удаления: "))
                except ValueError as er:
                    print('ID должен быть числом')
                    continue
                res = library.delete_book_by_id(book_id)
                print(res)

            elif choice == '3':
                #ищем книги
                query = input("Введите параметры для поиска(название параметра (author, title, year) и данные для поиска через\n\
пробел: 'author Пушкин') либо только дынные для поиска по всем параметрам: 'Пушкин': ")
                res = library.search_books(query)
                if len(res) == 0:
                    print('Ничего не найдено')
                else:
                   for book in res:
                        print(book)

            elif choice == '4':
                #отображаем все книги
                res = library.get_books()
                for book in res:
                    print(book)

            elif choice == '5':
                #изменяем статус книги
                try: 
                    book_id = int(input("Введите ID книги для изменения статуса: "))
                    new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                    res = library.change_status(book_id, new_status)
                    print(res)
                except ValueError as er:
                    print('ID должен быть числом')
                    
            elif choice == '6':
                #выход
                print("Выход из программы")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова")
        except EOFError as er:
            print("Выход из программы")
            break


if __name__ == '__main__':
    main()