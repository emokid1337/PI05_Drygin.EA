def test_all_algorithms():
    """Функция для тестирования всех алгоритмов"""
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ ВСЕХ АЛГОРИТМОВ")
    print("=" * 50)
    
    # Тестовые данные
    test_sort_arr = [64, 34, 25, 12, 22, 11, 90]
    test_search_arr = [2, 3, 4, 10, 40, 45, 50, 60, 70]
    target = 45
    
    print("\n1. Блочная сортировка:")
    float_arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print(f"   До: {float_arr}")
    print(f"   После: {bucket_sort(float_arr)}")
    
    print("\n2. Блинная сортировка:")
    print(f"   До: {test_sort_arr}")
    print(f"   После: {pancake_sort(test_sort_arr.copy())}")
    
    print("\n3. Сортировка бусинами:")
    bead_arr = [3, 1, 4, 1, 5]
    print(f"   До: {bead_arr}")
    print(f"   После: {bead_sort(bead_arr.copy())}")
    
    print(f"\n4. Поиск скачками (элемент {target}):")
    print(f"   Индекс: {jump_search(test_search_arr, target)}")
    
    print(f"\n5. Экспоненциальный поиск (элемент {target}):")
    print(f"   Индекс: {exponential_search(test_search_arr, target)}")
    
    print(f"\n6. Тернарный поиск (элемент {target}):")
    print(f"   Индекс: {ternary_search(test_search_arr, target)}")

# Запуск тестирования
test_all_algorithms()