import numpy as np
import os

def print_colored(text, color):
    """Цветной вывод в терминал"""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'end': '\033[0m'
    }
    print(f"{colors[color]}{text}{colors['end']}")

def read_matrix(filename):
    """Чтение матрицы из файла"""
    try:
        with open(filename, 'r') as f:
            matrix = []
            for line in f:
                if line.strip():
                    row = [float(x) for x in line.strip().split()]
                    if row:
                        matrix.append(row)
            return np.array(matrix)
    except FileNotFoundError:
        return None

def main():
    print("=" * 60)
    print("ВЕРИФИКАЦИЯ РЕЗУЛЬТАТОВ С ПОМОЩЬЮ NUMPY")
    print("=" * 60)
    
    # Пути к файлам
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    matrixA_path = os.path.join(base_dir, 'data', 'matrixA.txt')
    matrixB_path = os.path.join(base_dir, 'data', 'matrixB.txt')
    result_path = os.path.join(base_dir, 'data', 'result.txt')
    
    # Чтение матриц
    A = read_matrix(matrixA_path)
    B = read_matrix(matrixB_path)
    C_cpp = read_matrix(result_path)
    
    if A is None:
        print_colored("✗ Ошибка: файл matrixA.txt не найден", 'red')
        return
    if B is None:
        print_colored("✗ Ошибка: файл matrixB.txt не найден", 'red')
        return
    if C_cpp is None:
        print_colored("✗ Ошибка: файл result.txt не найден", 'red')
        print("Сначала запустите C++ программу!")
        return
    
    print(f"\n📊 Размер матрицы A: {A.shape}")
    print(f"📊 Размер матрицы B: {B.shape}")
    print(f"📊 Размер результата: {C_cpp.shape}")
    
    # Вычисление с помощью NumPy
    print("\n🔄 Вычисление с помощью NumPy...")
    C_numpy = np.dot(A, B)
    
    print("=" * 60)
    print("РЕЗУЛЬТАТЫ ВЕРИФИКАЦИИ")
    print("=" * 60)
    
    # Сравнение результатов
    if np.allclose(C_cpp, C_numpy, rtol=1e-10, atol=1e-10):
        print_colored("✓ ВЕРИФИКАЦИЯ ПРОЙДЕНА: Результаты совпадают!", 'green')
    else:
        print_colored("✗ ВЕРИФИКАЦИЯ НЕ ПРОЙДЕНА: Результаты различаются!", 'red')
        
        diff = np.abs(C_cpp - C_numpy)
        print(f"Максимальная разница: {np.max(diff):.2e}")
        print(f"Средняя разница: {np.mean(diff):.2e}")
        
        # Показываем сравнение
        print("\nСравнение первых 3x3 элементов:")
        print("C++ результат:")
        print(C_cpp[:3, :3])
        print("\nNumPy результат:")
        print(C_numpy[:3, :3])
    
    # Вычисление объема задачи
    n = A.shape[0]
    operations = 2 * n**3
    print(f"\n📊 Объем задачи: {operations} операций")
    
    if np.allclose(C_cpp, C_numpy, rtol=1e-10, atol=1e-10):
        print_colored("\n✓ Все проверки успешно пройдены!", 'green')

if __name__ == "__main__":
    main()
