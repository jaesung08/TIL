# book.py
number_of_book = 100

def decrease_book(books):
    global number_of_book
    number_of_book -= books
    print(f"남은 책의 수 : {number_of_book}")
