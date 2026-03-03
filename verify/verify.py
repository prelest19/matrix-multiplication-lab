import numpy as np
import os

def read_matrix(filename):
    try:
        with open(filename, 'r') as f:
            matrix = []
            for line in f:
                if line.strip():
                    row = [float(x) for x in line.strip().split()]
                    if row:
                        matrix.append(row)
            return np.array(matrix)
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

def main():
    print("=" * 50)
    print("VERIFICATION WITH NUMPY")
    print("=" * 50)
    
    # Чтение файлов
    A = read_matrix("data/matrixA.txt")
    B = read_matrix("data/matrixB.txt")
    C = read_matrix("data/result.txt")
    
    if A is None or B is None or C is None:
        print("❌ Error: Cannot read files")
        return
    
    print(f"Matrix A: {A.shape}")
    print(f"Matrix B: {B.shape}")
    print(f"Matrix C: {C.shape}")
    
    # Вычисление с numpy
    C_numpy = np.dot(A, B)
    
    # Сравнение
    if np.allclose(C, C_numpy, rtol=1e-10, atol=1e-10):
        print("\n✅ VERIFICATION PASSED! Results match!")
    else:
        print("\n❌ VERIFICATION FAILED! Results differ!")
        diff = np.abs(C - C_numpy)
        print(f"Max difference: {np.max(diff):.2e}")
    
    # Объем задачи
    n = A.shape[0]
    operations = 2 * n**3
    print(f"\nTask volume: {operations} operations")

if __name__ == "__main__":
    main()