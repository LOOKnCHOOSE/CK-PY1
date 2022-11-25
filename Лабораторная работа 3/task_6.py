list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index = 0 # назначаем максимальным первое число в последовательности
max_value = list_numbers[max_index] # присваиваем значение индексу
last_value = list_numbers[-1] # заранее задаем последнюю переменную в списке

for a, current_value in enumerate(list_numbers): # проводим пошаговый перебор кортежей
    if current_value >= max_value: # цикл сравнения изначальной переменной с текущим значением в списке
        max_value = current_value # при выполнении условия присваиваем переменной текущее значение из списка
        max_index = a # при выполнении условия присваиваем переменной текущий индекс из списка

list_numbers[max_index], list_numbers[a] = list_numbers[a], list_numbers[max_index] # меняем местами нужные нам переменные в списке
print(list_numbers) # печатаем результат
