def bead_sort(arr):
    """
    Сортировка бусинами - представляет числа как столбцы бусин,
    затем "роняет" их под действием гравитации.
    """
    if len(arr) == 0:
        return arr
    
    # Находим максимальное значение
    max_val = max(arr)
    
    # Создаем "рейки" с бусинами
    beads = [[0] * max_val for _ in range(len(arr))]
    
    # Размещаем бусины согласно значениям массива
    for i in range(len(arr)):
        for j in range(arr[i]):
            beads[i][j] = 1
    
    # "Роняем" бусины под действием гравитации
    for j in range(max_val):
        # Считаем количество бусин в каждом столбце
        sum_beads = 0
        for i in range(len(arr)):
            sum_beads += beads[i][j]
            beads[i][j] = 0
        
        # Размещаем бусины внизу
        for i in range(len(arr) - 1, len(arr) - sum_beads - 1, -1):
            beads[i][j] = 1
    
    # Преобразуем обратно в числа
    result = []
    for i in range(len(arr)):
        result.append(sum(beads[i]))
    
    return result

# Пример использования
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print("Исходный массив:", arr)
print("Отсортированный массив:", bead_sort(arr.copy()))