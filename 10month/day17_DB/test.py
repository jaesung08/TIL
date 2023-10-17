# 장고 ==> 지연로딩(lazy loading) 이라는 기술을 사용함
# 데이터를 실제로 사용할 때 DB로 쿼리를 전송한다.

articles = Article.objects.all()

# 쿼리문을 2번 호출한다.
print(articles[0].title)
print(articles[1].title)

# 실제로 사용할 때 쿼리문이 DB로 전송된다.
# articles : 전체 데이터 가져올 때 1번호출
for article in articles:
    # article은 이미 가져왔기 때문에 -> 호출 하지않음
    print(article.title)
    # 정참조 -> 호출 -> N번
    print(article.author.username)
    # 역참조 -> 호출 -> N번
    print(article.comment_set.all())