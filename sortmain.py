import math

# 1. Блочная сортировка
def bucket_sort(arr):
    """
    Блочная сортировка - работает лучше всего с числами от 0 до 1
    """
    if len(arr) == 0:
        return arr
    
    # Нормализуем числа если нужно
    min_val = min(arr)
    max_val = max(arr)
    
    if min_val < 0 or max_val > 1:
        # Нормализуем в диапазон [0, 1]
        normalized_arr = [(x - min_val) / (max_val - min_val + 1e-9) for x in arr]
    else:
        normalized_arr = arr.copy()
    
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    
    for num in normalized_arr:
        index = min(int(num * num_buckets), num_buckets - 1)
        buckets[index].append(num)
    
    sorted_normalized = []
    for bucket in buckets:
        sorted_normalized.extend(sorted(bucket))
    
    # Денормализуем обратно если нужно
    if min_val < 0 or max_val > 1:
        sorted_arr = [x * (max_val - min_val) + min_val for x in sorted_normalized]
    else:
        sorted_arr = sorted_normalized
    
    return sorted_arr

# 2. Блинная сортировка
def flip(arr, i):
    """Переворачивает массив от 0 до i-го элемента"""
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max_index(arr, n):
    """Находит индекс максимального элемента в массиве до n-го элемента"""
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    """Блинная сортировка"""
    if len(arr) == 0:
        return arr
        
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for curr_size in range(n, 1, -1):
        max_index = find_max_index(arr_copy, curr_size)
        
        if max_index != curr_size - 1:
            if max_index != 0:
                flip(arr_copy, max_index)
            flip(arr_copy, curr_size - 1)
    
    return arr_copy

# 3. Сортировка бусинами
def bead_sort(arr):
    """
    Сортировка бусинами работает только с неотрицательными целыми числами
    """
    if len(arr) == 0:
        return arr
        
    if any(x < 0 or not isinstance(x, int) for x in arr):
        raise ValueError("Сортировка бусинами работает только с неотрицательными целыми числами")
    
    max_val = max(arr)
    if max_val == 0:
        return arr
    
    # Создаем матрицу бусин
    beads = [[0] * max_val for _ in range(len(arr))]
    
    # Размещаем бусины
    for i in range(len(arr)):
        for j in range(arr[i]):
            beads[i][j] = 1
    
    # Гравитация - бусины падают вниз
    for j in range(max_val):
        bead_count = 0
        for i in range(len(arr)):
            bead_count += beads[i][j]
            beads[i][j] = 0
        
        # Размещаем бусины внизу
        for i in range(len(arr) - bead_count, len(arr)):
            beads[i][j] = 1
    
    # Преобразуем обратно в числа
    result = [sum(row) for row in beads]
    return result

# 4. Поиск скачками
def jump_search(arr, target):
    """
    Поиск скачками требует отсортированного массива
    """
    if not arr:
        return -1
    
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Прыгаем вперед пока не найдем блок с целевым элементом
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Линейный поиск в найденном блоке
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
        if arr[i] > target:
            break
    
    return -1

# 5. Экспоненциальный поиск
def binary_search(arr, left, right, target):
    """Вспомогательная функция бинарного поиска"""
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    """
    Экспоненциальный поиск требует отсортированного массива
    """
    if not arr:
        return -1
    
    n = len(arr)
    
    if arr[0] == target:
        return 0
    
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    
    return binary_search(arr, i // 2, min(i, n - 1), target)

# 6. Тернарный поиск
def ternary_search(arr, target):
    """
    Тернарный поиск требует отсортированного массива
    """
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
            
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

def ternary_search_recursive(arr, left, right, target):
    """Рекурсивная версия тернарного поиска"""
    if left > right:
        return -1
    
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    if target < arr[mid1]:
        return ternary_search_recursive(arr, left, mid1 - 1, target)
    elif target > arr[mid2]:
        return ternary_search_recursive(arr, mid2 + 1, right, target)
    else:
        return ternary_search_recursive(arr, mid1 + 1, mid2 - 1, target)

# ФУНКЦИИ ТЕСТИРОВАНИЯ
def test_all_algorithms():
    """Исправленная функция тестирования"""
    print("=" * 60)
    print("ПРАВИЛЬНОЕ ТЕСТИРОВАНИЕ ВСЕХ АЛГОРИТМОВ")
    print("=" * 60)
    
    # Тестирование алгоритмов сортировки
    print("\n1. БЛОЧНАЯ СОРТИРОВКА (лучше с числами 0-1):")
    float_arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print(f"   До: {float_arr}")
    result = bucket_sort(float_arr)
    print(f"   После: {[round(x, 2) for x in result]}")
    print(f"   Проверка: {'✓ Отсортирован' if result == sorted(float_arr) else '✗ Ошибка'}")
    
    print("\n2. БЛИННАЯ СОРТИРОВКА:")
    pancake_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"   До: {pancake_arr}")
    result = pancake_sort(pancake_arr)
    print(f"   После: {result}")
    print(f"   Проверка: {'✓ Отсортирован' if result == sorted(pancake_arr) else '✗ Ошибка'}")
    
    print("\n3. СОРТИРОВКА БУСИНАМИ (только неотрицательные целые):")
    bead_arr = [3, 1, 4, 1, 5, 2]
    print(f"   До: {bead_arr}")
    try:
        result = bead_sort(bead_arr)
        print(f"   После: {result}")
        print(f"   Проверка: {'✓ Отсортирован' if result == sorted(bead_arr) else '✗ Ошибка'}")
    except ValueError as e:
        print(f"   Ошибка: {e}")
    
    # Тестирование алгоритмов поиска
    print("\n" + "=" * 50)
    print("АЛГОРИТМЫ ПОИСКА (требуют отсортированный массив)")
    print("=" * 50)
    
    search_arr = [2, 3, 4, 10, 40, 45, 50, 60, 70, 80, 90, 100]
    targets = [45, 10, 100, 1]  # Существующие и несуществующие цели
    
    for target in targets:
        print(f"\nПоиск элемента {target} в массиве: {search_arr}")
        
        jump_result = jump_search(search_arr, target)
        exp_result = exponential_search(search_arr, target)
        tern_result = ternary_search(search_arr, target)
        tern_rec_result = ternary_search_recursive(search_arr, 0, len(search_arr)-1, target)
        
        # Ожидаемый результат
        expected = search_arr.index(target) if target in search_arr else -1
        
        print(f"   Ожидаемый результат: {expected}")
        print(f"   Поиск скачками: {jump_result} {'✓' if jump_result == expected else '✗'}")
        print(f"   Экспоненциальный: {exp_result} {'✓' if exp_result == expected else '✗'}")
        print(f"   Тернарный: {tern_result} {'✓' if tern_result == expected else '✗'}")
        print(f"   Тернарный рекурсивный: {tern_rec_result} {'✓' if tern_rec_result == expected else '✗'}")

def additional_tests():
    """Дополнительные тесты для граничных случаев"""
    print("\n" + "=" * 50)
    print("ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ (граничные случаи)")
    print("=" * 50)
    
    # Пустой массив
    print("\n1. Пустой массив:")
    empty_arr = []
    print(f"   Блочная сортировка: {bucket_sort(empty_arr)}")
    print(f"   Блинная сортировка: {pancake_sort(empty_arr)}")
    print(f"   Поиск в пустом массиве: {jump_search(empty_arr, 5)}")
    
    # Массив из одного элемента
    print("\n2. Массив из одного элемента:")
    single_arr = [5]
    print(f"   Блочная сортировка: {bucket_sort(single_arr)}")
    print(f"   Блинная сортировка: {pancake_sort(single_arr)}")
    print(f"   Поиск существующего: {jump_search(single_arr, 5)}")
    print(f"   Поиск несуществующего: {jump_search(single_arr, 10)}")
    
    # Уже отсортированный массив
    print("\n3. Уже отсортированный массив:")
    sorted_arr = [1, 2, 3, 4, 5]
    print(f"   Исходный: {sorted_arr}")
    print(f"   После блинной сортировки: {pancake_sort(sorted_arr)}")
    
    # Тест сортировки бусинами с нулями
    print("\n4. Сортировка бусинами с нулями:")
    zeros_arr = [3, 0, 2, 1, 0]
    print(f"   До: {zeros_arr}")
    try:
        result = bead_sort(zeros_arr)
        print(f"   После: {result}")
    except ValueError as e:
        print(f"   Ошибка: {e}")

# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    test_all_algorithms()
    additional_tests()
    
    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ!")
    print("=" * 60)
