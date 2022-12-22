import datetime
import json


class Post:
    def __init__(self, author, content, date):
        if not date:
            date = str(datetime.datetime.now()).split(" ")[0]
        self.author = author
        self.content = content
        self.date = date

    def __repr__(self):
        return f"{self.author}\t\t{self.date}\n" \
               f"{self.content}"

    def search_by_author(self, author):
        return author.lower() in self.author.lower()

    def search_by_date(self, date):
        return date.lower() in self.date.lower()

    def search_by_content(self, content):
        return content.lower() in self.content.lower()


class Posts:
    def __init__(self, path):
        self.path = path
        self.posts = []
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        for post in data:
            self.posts.append(Post(post["author"],
                                   post["content"],
                                   post["date"]))

    def append(self, post):
        self.posts.append(post)
        s = []
        with open(self.path, "w", encoding="utf-8") as file:
            for post in self.posts:
                s.append({
                    "author": post.author,
                    "content": post.content,
                    "date": post.date
                })
            json.dump(s, file, ensure_ascii=False)

    def delete(self, post):
        self.posts.remove(post)
        s = []
        with open(self.path, "w", encoding="utf-8") as file:
            for post in self.posts:
                s.append({
                    "author": post.author,
                    "content": post.content,
                    "date": post.date
                })
            json.dump(s, file, ensure_ascii=False)

    def search_by_author(self, author_name):
        posts = []
        for post in self.posts:
            if post.search_by_author(author_name):
                posts.append(post)
        return posts

    def search_by_content(self, content):
        posts = []
        for post in self.posts:
            if post.search_by_content(content):
                posts.append(post)
        return posts

    def search_by_date(self, date):
        posts = []
        for post in self.posts:
            if post.search_by_date(date):
                posts.append(post)
        return posts


def main():
    posts = Posts("posts.json")
    user_answer = int(input("0. Выход\n"
                            "1. Добавить пост\n"
                            "2. Показать посты\n"
                            "3. Поиск по автору\n"
                            "4. Поиск по контенту\n"
                            "5. Поиск по дате\n"
                            "6. Удалить пост по номеру\n"))
    if user_answer == 0:
        exit()
    elif user_answer == 1:
        posts.append(Post(
            input("Ваше имя: "),
            input("Текст публикации:\n"),
            input("Дата DD.MM.YYYY(пропустите, чтобы установить текущую): ")
        ))
        exit()
    elif user_answer == 2:
        posts2 = posts.posts
        for post in posts.posts:
            i = posts2.index(post)
            print(f"{i + 1}.")
            print(post)
    elif user_answer == 3:
        user_input = input("Введите имя автора\n")
        posts2 = posts.search_by_author(user_input)
        for post in posts2:
            i = posts2.index(post)
            print(f"{i + 1}.")
            print(post)
    elif user_answer == 4:
        user_input = input("Введите ключевое слов\n")
        posts2 = posts.search_by_content(user_input)
        for post in posts2:
            i = posts2.index(post)
            print(f"{i + 1}.")
            print(post)
    elif user_answer == 5:
        user_input = input("Введите дату в формате: DD.MM.YYYY\n")
        posts2 = posts.search_by_date(user_input)
        for post in posts2:
            i = posts2.index(post)
            print(f"{i + 1}.")
            print(post)
    user_input = int(input("Введите индекс для удаления\n"
                           "0. Выход"))
    if user_input == 0:
        exit()
    posts.delete(posts2[user_input - 1])


if __name__ == "__main__":
    main()
