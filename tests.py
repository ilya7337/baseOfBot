import unittest
import os
from models import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Создает экземпляр библиотеки и очищает файл books.json перед каждым тестом"""

        self.library = Library()
        self.library.set_books([])

    def tearDown(self):
        """Удаляет файл books.json после каждого теста"""

        if os.path.exists('books.json'):
            os.remove('books.json')

    def test_add_new_book(self):
        """Тестирует добавление новой книги"""

        response = self.library.add_new_book("1984", "Джордж Оруэлл", "1949")
        self.assertEqual(response, "Книга 1984 успешно добавлена")
        books = self.library.get_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "1984")
        self.assertEqual(books[0]['author'], "Джордж Оруэлл")
        self.assertEqual(books[0]['year'], "1949")

    def test_delete_book_by_id(self):
        """Тестирует удаление книги по ID"""

        self.library.add_new_book("1984", "Джордж Оруэлл", "1949")
        response = self.library.delete_book_by_id(0)
        self.assertEqual(response, "Книга с id 0 удалена")
        books = self.library.get_books()
        self.assertEqual(len(books), 0)

    def test_search_books(self):
        """Тестирует поиск книг"""

        self.library.add_new_book("1984", "Джордж Оруэлл", "1949")
        self.library.add_new_book("Мастер и Маргарита", "Булгаков", "1967")
        
        # Поиск по автору
        results = self.library.search_books("author Булгаков")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Мастер и Маргарита")

        # Поиск по названию
        results = self.library.search_books("1984")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['author'], "Джордж Оруэлл")

    def test_change_status(self):
        """Тестирует изменение статуса книги"""

        self.library.add_new_book("1984", "Джордж Оруэлл", "1949")
        response = self.library.change_status(0, "выдана")
        self.assertEqual(response, "Статус успешно изменён")
        books = self.library.get_books()
        self.assertEqual(books[0]['status'], "выдана")

        # Проверка на попытку изменить статус на тот же
        response = self.library.change_status(0, "выдана")
        self.assertEqual(response, "У книги уже такой статус")

    def test_delete_nonexistent_book(self):
        """Тестирует удаление несуществующей книги"""

        response = self.library.delete_book_by_id(999)
        self.assertEqual(response, 'Книги с id 999 нет')
