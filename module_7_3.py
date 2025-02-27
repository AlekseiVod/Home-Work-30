# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Определяем результат соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# Форматирование с использованием %
result1 = "В команде Мастера кода участников: %d !" % team1_num
result2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Форматирование с использованием format()
result3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
result4 = "Волшебники данных решили задачи за {:.2f} с !".format(team2_time)

# Форматирование с использованием f-строк
result5 = f"Команды решили {score_1} и {score_2} задач."
result6 = f"Результат битвы: {challenge_result}"
result7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."

# Результат
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
