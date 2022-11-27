class Stats:
    """Отслеживание статистики"""
    def __init__(self):
        """Инициализирует статистику"""
        self.reset_stats()
        self.run_game = True
        with open('./high_score.txt', 'r') as file:
            self.high_score = int(file.readline())


    def reset_stats(self):
        """Статистика изменений"""
        self.guns_left = 3
        self.score = 0

