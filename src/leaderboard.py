"""

=== Таблица лидеров ===

    new_score(score) - необходимо вызвать для добавления нового результата
    get_leaders() - возвращает лист лидеров (от 0 до 3 элементов)

    Подгрузка сохранения из файла происходит при создании класса
    Сохранение в файл - при добавлении нового результата

=======================

"""


from src.aes import CryptoAES
import os.path


class Leaderboard:

    leaderboard = []
    key = '$XRVG@9(bND+TVrz8Zs`5.uFZWf'

    def __init__(self):
        self.aes = CryptoAES(self.key)
        self.load()
        self.leaderboard.sort(reverse=True)

    def new_score(self, score):
        self.leaderboard.append(score)
        self.leaderboard.sort(reverse=True)
        self.save()

    def get_leaders(self):
        ans = []
        i = 0
        for score in self.leaderboard:
            ans.append(score)
            i += 1
            if i >= 3:
                break
        return ans

    def load(self):
        if not os.path.isfile('../saves/leaderboard.save'):
            self.leaderboard = []
            return

        file = open('../saves/leaderboard.save', 'rb')
        data = self.aes.decrypt(file.read())
        file.close()

        self.leaderboard = []
        for score in data.split('_'):
            if score.isdigit():
                self.leaderboard.append(int(score))
        self.leaderboard.sort(reverse=True)

    def save(self):
        self.leaderboard.sort(reverse=True)

        data = ''
        for score in self.leaderboard:
            data += str(score) + '_'

        file = open('../saves/leaderboard.save', 'wb')
        file.write(self.aes.encrypt(data))
        file.close()
