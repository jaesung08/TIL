import json


def best_new_books(books):
    # 여기에 코드를 작성합니다.  
    pass



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_new_books(books_list))
