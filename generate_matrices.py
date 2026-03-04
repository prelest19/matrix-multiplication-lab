import numpy as np
import os

# Создаем папку для матриц, если её нет
os.makedirs("matrices", exist_ok=True)

# Размеры матриц
sizes = [100, 500, 800, 1000, 2000]

for n in sizes:
    print(f"Генерация матриц размера {n}x{n}...")
    
    # Генерируем случайные матрицы
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    
    # Сохраняем в файлы
    np.savetxt(f"matrices/matrixA_{n}.txt", A, fmt='%.6f', delimiter=' ')
    np.savetxt(f"matrices/matrixB_{n}.txt", B, fmt='%.6f', delimiter=' ')
    
    print(f"✓ Матрицы {n}x{n} сохранены")

print("\n✅ Все матрицы сгенерированы!")
print(f"Файлы сохранены в папке: {os.path.abspath('matrices')}")