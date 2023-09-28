**Список проверок для каждого метода с указанием номеров тестов**

- `add_new_book` — добавляет новую книгу в словарь без указания жанра. 
Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.
  - Позитивные:
    1. Добавляем 2 книги (1)
    2. 1, 40 символов (2, 5, 6, 7, 8, 10, 12, 13, 14, 16, 17)
  - Негативные
    3. 0, 41 (3)
    4. Уже сущ-щая книга (4)

- `set_book_genre` — устанавливает жанр книги, если книга есть в `books_genre`и её жанр входит в список`genre`.
  - Позитивные:
    1. Добавление\изменение жанра (5, 10, 12)
  - Негативные:
    2. Несуществующая книга (6)
    3. Нет жанра в списке (7)

- `get_book_genre`— выводит жанр книги по её имени.
  - Позитивные:
    1. Получаем жанр сущ. книги (жанр есть) (5)
    2. Получаем жанр сущ. книги (жанра нет) (8)
  - Негативные:
    3. Не существующая книга (9)

- `get_books_with_specific_genre`— выводит список книг с определённым жанром.-
  - Позитивные:
    1. Получаем список книг (10)
  - Негативные:
    2. Книг нет, жанр есть (6)
    3. Несуществующий жанр (11)

- `get_books_genre`— выводит текущий словарь `books_genre`.
  - Позитивные:
    1. Книги есть, книг нет - получаем словарь (1, 2, 3, 4, 7)

- `get_books_for_children` — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
  - Позитивные:
    1. Получаем книги согласно условия (12)

- `add_book_in_favorites` — добавляет книгу в избранное. Книга должна находиться в словаре `books_genre`. 
Повторно добавить книгу в избранное нельзя.
  - Позитивные:
    1. Все условия, добавляем 2 книги (13)
  - Негативные:
    2. Уже добавленная книга (14)
    3. Книги нет в словаре books_genre (15)

- `delete_book_from_favorites` — удаляет книгу из избранного, если она там есть.
  - Позитивные:
    1. Книга есть - удаляем (16)
  - Негативные:
    2. Книги нет (17)

- `get_list_of_favorites_books` — получает список избранных книг.
  - Позитивные:
    1. Книги есть в избр (13, 14)
    2. Книг нет в избр. (15)


**Список созданных тестов с распределением проверок**
1. test_add_new_book_add_two_books_success_and_have_not_genre()
2. test_add_new_book_book_length_success_and_dont_have_genre()
3. test_add_new_book_book_length_didnt_add()
4. test_add_new_book_book_already_exist_didnt_add()
5. test_set_book_genre_set_and_change_genre_success()
6. test_set_book_genre_book_dont_exist_didnt_set()
7. test_set_book_genre_genre_dont_exist_didnt_set()
8. test_get_book_genre_genre_dont_exist_success()
9. test_get_book_genre_book_dont_exist_none()
10. test_get_books_with_specific_genre_books_exist_success()
11. test_get_books_with_specific_genre_genre_dont_exist_success()
12. test_get_books_for_children_success()
13. test_add_book_in_favorites_all_conditions_success()
14. test_add_book_in_favorites_book_already_exists_didnt_add()
15. test_add_book_in_favorites_book_doesnt_exist_in_books_genre_didnt_add()
16. test_delete_book_from_favorites_success()
17. test_delete_book_from_favorites_book_doesnt_exist_didnt_delete()