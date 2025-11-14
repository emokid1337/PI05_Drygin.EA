def bucket_sort(arr):
    """
    Блочная сортировка - распределяет элементы по "корзинам",
    затем сортирует каждую корзину отдельно.
    """
    if len(arr) == 0:
        return arr
    
    # Определяем количество корзин (обычно равно количеству элементов)
    num_buckets = len(arr)
    
    # Создаем корзины
    buckets = [[] for _ in range(num_buckets)]
    
    # Распределяем элементы по корзинам
    max_val = max(arr)
    for num in arr:
        # Вычисляем индекс корзины
        index = min(int(num * num_buckets / (max_val + 1)), num_buckets - 1)
        buckets[index].append(num)
    
    # Сортируем каждую корзину и объединяем результат
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Пример использования
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print("Исходный массив:", arr)
print("Отсортированный массив:", bucket_sort(arr))
