import os


class MorningBot:

    def __init__(self, filename="words.txt"):
        self.filename = filename

    def get_and_delete_word(self):
        # 1. Проверяем, существует ли файл
        if not os.path.exists(self.filename):
            print(f"Ошибка: Файл {self.filename} не найден!")
            return

        # 2. Читаем все слова
        with open(self.filename, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]

        # 3. Проверяем, есть ли слова в списке
        if not words:
            print(
                "✨ Все слова закончились! Скрипт завершил работу. База пуста."
            )
            return

        # 4. Забираем самое первое слово
        current_word = words[0]

        # 5. Перезаписываем файл, но уже БЕЗ первого слова
        with open(self.filename, "w", encoding="utf-8") as file:
            for word in words[1:]:
                file.write(f"{word}\n")

        # 6. Формируем финальное сообщение
        message = f"{current_word.capitalize()}, доброе утречко ☀️😘❤️‍🔥"
        print(message)


if __name__ == "__main__":
    bot = MorningBot()
    bot.get_and_delete_word()