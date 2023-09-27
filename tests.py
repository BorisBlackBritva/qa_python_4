from main import BooksCollector
import pytest


class TestBooksCollector:
# -------------------------------------------         add_new_book()         -------------------------------------------
    def test_add_new_book_add_two_books_success_and_have_not_genre(self):
        collector = BooksCollector()

        book1 = 'Гордость и предубеждение и зомби'
        book2 = 'Что делать, если ваш кот хочет вас убить'

        collector.add_new_book(book1)
        collector.add_new_book(book2)

        assert len(collector.books_genre) == 2 \
               and collector.books_genre[book1] == '' \
               and collector.books_genre[book2] == ''

    @pytest.mark.parametrize('book', ['b', 'bookbookbookbookbookbookbookbookbookbook'])
    def test_add_new_book_book_length_success_and_dont_have_genre(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)

        assert book in collector.books_genre

    @pytest.mark.parametrize('book', ['', 'bookbookbookbookbookbookbookbookbookbookb'])
    def test_add_new_book_book_length_didnt_add(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)

        assert not (book in collector.books_genre)

    def test_add_new_book_book_already_exist_didnt_add(self):
        collector = BooksCollector()

        book = 'book_dont_exist'

        collector.add_new_book(book)
        collector.add_new_book(book)

        assert len(collector.books_genre) == 1

# -------------------------------------------        set_book_genre()        -------------------------------------------
    @pytest.mark.parametrize('book, genre', [['book', 'Ужасы'], ['book', 'Детективы']])
    def test_set_book_genre_set_and_change_genre_success(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.books_genre[book] == genre

    def test_set_book_genre_book_not_exist_didnt_set(self):
        collector = BooksCollector()

        book = 'book_dont_exist'
        genre = 'Фантастика'

        collector.set_book_genre(book, genre)

        assert genre not in collector.books_genre.values()

    def test_set_book_genre_genre_not_exist_didnt_set(self):
        collector = BooksCollector()

        book = 'book_dont_exist'
        genre = 'genre_dont_exist'

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert genre not in collector.books_genre.values()

# -------------------------------------------        get_book_genre()        -------------------------------------------
    def test_get_book_genre_genre_exist_success(self):
        collector = BooksCollector()

        book = 'book'
        genre = 'Фантастика'

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    def test_get_book_genre_genre_dont_exist_success(self):
        collector = BooksCollector()

        book = 'book'
        collector.add_new_book(book)

        assert collector.get_book_genre(book) == ''

    def test_get_book_genre_book_dont_exist_none(self):
        collector = BooksCollector()

        book = 'book_dont_exist'

        assert collector.get_book_genre(book) == None

# ------------------------------------        get_books_with_specific_genre()        -----------------------------------
    def test_get_books_with_specific_genre_books_exist_success(self):
        collector = BooksCollector()

        book1 = 'Гордость и предубеждение и зомби'
        book2 = 'Что делать, если ваш кот хочет вас убить'
        book3 = 'Марта, Френки два крота'
        genre1 = 'Фантастика'
        genre2 = 'Мультфильмы'

        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.add_new_book(book3)
        collector.set_book_genre(book1, genre1)
        collector.set_book_genre(book2, genre1)
        collector.set_book_genre(book3, genre2)

        assert collector.get_books_with_specific_genre(genre1) == [book1, book2]

    def test_get_books_with_specific_genre_books_dont_exist_success(self):
        collector = BooksCollector()

        genre = 'Фантастика'

        assert collector.get_books_with_specific_genre(genre) == []

    def test_get_books_with_specific_genre_genre_dont_exist_success(self):
        collector = BooksCollector()

        genre = 'genry_dont_exist'

        assert collector.get_books_with_specific_genre(genre) == []

# -------------------------------------------        get_books_genre()       -------------------------------------------
    def test_get_books_genre_success(self):
        collector = BooksCollector()

        books = ['Гордость и предубеждение и зомби',
                 'Что делать, если ваш кот хочет вас убить',
                 'Марта, Френки два крота',
                 'Как клонировать анус',
                 'Мохнатка Бетти'
                 ]
        genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        books_genres_obj = {}

        for i in range(len(books)):
            collector.add_new_book(books[i])
            collector.set_book_genre(books[i], genres[i])
            books_genres_obj[books[i]] = genres[i]

        assert collector.get_books_genre() == books_genres_obj

# ---------------------------------------        get_books_for_children()        ---------------------------------------
    def test_get_books_for_children_success(self):
        collector = BooksCollector()

        books = ['Гордость и предубеждение и зомби',
                 'Что делать, если ваш кот хочет вас убить',
                 'Марта, Френки два крота',
                 'Как клонировать анус',
                 'Мохнатка Бетти'
                 ]
        genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        books_for_children = ['Гордость и предубеждение и зомби',
                              'Как клонировать анус',
                              'Мохнатка Бетти'
                              ]

        for i in range(len(books)):
            collector.add_new_book(books[i])
            collector.set_book_genre(books[i], genres[i])

        assert collector.get_books_for_children() == books_for_children

# ---------------------------------------        add_book_in_favorites()        ---------------------------------------
    def test_add_book_in_favorites_all_conditions_success(self):
        collector = BooksCollector()


        book1 = 'Гордость и предубеждение и зомби'
        book2 = 'Что делать, если ваш кот хочет вас убить'

        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.add_book_in_favorites(book1)
        collector.add_book_in_favorites(book2)

        assert collector.favorites == [book1, book2]

    def test_add_book_in_favorites_book_already_exists_didnt_add(self):
        collector = BooksCollector()

        book = 'Гордость и предубеждение и зомби'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)

        assert collector.favorites == [book]

    def test_add_book_in_favorites_book_doesnt_exist_in_books_genre_didnt_add(self):
        collector = BooksCollector()

        book = 'Гордость и предубеждение и зомби'

        collector.add_book_in_favorites(book)

        assert collector.favorites == []

# -------------------------------------        delete_book_from_favorites()        -------------------------------------
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()

        book1 = 'Гордость и предубеждение и зомби'
        book2 = 'Что делать, если ваш кот хочет вас убить'

        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.add_book_in_favorites(book1)
        collector.add_book_in_favorites(book2)
        collector.delete_book_from_favorites(book1)

        assert collector.favorites == [book2]

    def test_delete_book_from_favorites_book_doesnt_exist_didnt_delete(self):
        collector = BooksCollector()

        book1 = 'Гордость и предубеждение и зомби'
        book2 = 'Что делать, если ваш кот хочет вас убить'

        collector.add_new_book(book1)
        collector.add_book_in_favorites(book1)
        collector.delete_book_from_favorites(book2)

        assert collector.favorites == [book1]

# -------------------------------------        get_list_of_favorites_books()       -------------------------------------
    def test_get_list_of_favorites_books_books_exist_in_favorites_success(self):
        collector = BooksCollector()

        book1 = 'Гордость и предубеждение и зомби'
        book2 = 'Что делать, если ваш кот хочет вас убить'

        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.add_book_in_favorites(book1)
        collector.add_book_in_favorites(book2)

        assert collector.get_list_of_favorites_books() == [book1, book2]

    def test_get_list_of_favorites_books_books_doest_exist_in_favorites_success(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []
