books = { # Создание словаря
    1 :{"Title" : "Гарри Поттер", "author" : "Джоан Роулинг", "year" : "1997"}, # Прописываем информацию о книге
    2 :{"Title" : "Сумерки", "author" : "Стефани Майер", "year" : "2005"}, # Прописываем информацию о книге
    3 :{"Title" : "Портрет Дориана Грея", "author" : "Оскар Уайльд", "year" : "1890"}, # Прописываем информацию о книге
    4 :{"Title" : "Необыкновенные приключения Арбузика и Бебешки", "author" : "Эдуард Скобелев", "year" : "1985"}, # Прописываем информацию о книге
    5 :{"Title" : "В поисках утраченного времен", "author" : "Марсель Пруст", "year" : "1913"}, # Прописываем информацию о книге
} # Закончили заполнение словаря

for i,inf in books.items(): #
    print(f"-----------------------------Книга {i}-----------------------------") # Вывод на экран
    print(f"Название: {inf['Title']}, Автор :{inf['author']}") # Вывод на экрон
    print(f"-----------------------------{inf['year']}-----------------------------\n") # Вывод на экран
