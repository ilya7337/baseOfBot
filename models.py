import json
import os

class Library:
    def __init__(self):
        """Инициализирует библиотеку и создает базу данных книг"""

        self.books_id = 0
        self.initialize_db()

    def initialize_db(self) -> None:
        """Создает базу данных книг"""

        data = []
        if os.path.exists('books.json'):
            all_books = self.get_books()
            if len(all_books) > 0:
                self.books_id = all_books[-1]['id'] + 1
            return
        with open('books.json', 'w') as f:
            json.dump(data, f, indent=4)

    def get_books(self) -> list:
        """Возвращает список всех книг"""

        with open('books.json', 'r', encoding='utf-8') as f:
            books = json.load(f)
        return books
    
    def set_books(self, books: dict) -> None:
        """Перезаписывает список книг"""

        with open('books.json', 'w', encoding='utf-8') as f:
            json.dump(books, f, indent=4, ensure_ascii=False)

    def add_new_book(self, title: str, author: str, year: str) -> str:
        """Добавляет новую книгу"""

        all_books = self.get_books()
        all_books.append({'id': self.books_id, 'title': title, 'author': author, 'year': year, 'status': "в наличии"})
        self.books_id += 1
        self.set_books(all_books)
        return f'Книга {title} успешно добавлена'
    
    def delete_book_by_id(self, book_id: int) -> str:
        """Удаляет книгу по id"""

        all_books = self.get_books()
        update_books = [book for book in all_books if book['id'] != book_id]
        if len(update_books) == len(all_books):
            return f'Книги с id {book_id} нет'
        else:
            self.set_books(update_books)
            return f'Книга с id {book_id} удалена'
        
    def search_books(self, parametr: str) -> list:
        """Ищет книги по заданным параметрам"""

        parametr = parametr.split(' ')
        all_books = self.get_books()
        if len(parametr) == 1:
            parametr = parametr[0].lower()
            return [book for book in all_books if parametr in book['author'].lower() or 
                    parametr in book['title'].lower() or
                    parametr in book['year']]
        elif len(parametr) == 2:
            return [book for book in all_books if parametr[1].lower() in book[parametr[0]].lower()]
        else:
            return all_books

    def change_status(self, book_id: int, new_status: str) -> str:
        """Изменяет статус книги по id"""

        all_books = self.get_books()
        for i in range(len(all_books)):
            if all_books[i]['id'] == book_id and all_books[i]['status'].lower() != new_status.lower():
                all_books[i]['status'] = new_status
                self.set_books(all_books)
                return "Статус успешно изменён"
            elif all_books[i]['id'] == book_id:
                return "У книги уже такой статус"
        else:
            return f'Книги с id {book_id} нет'
    



    
