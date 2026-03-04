import numpy as np
import time
import os
import glob

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

def verify_size(size):
    print(f"\n{'='*50}")
    print(f"VERIFYING SIZE: {size}x{size}")
    print('='*50)
    
    A = read_matrix(f"matrices/matrixA_{size}.txt")
    B = read_matrix(f"matrices/matrixB_{size}.txt")
    C = read_matrix(f"results/result_{size}.txt")
    
    if A is None or B is None or C is None:
        print(f"❌ Cannot read files for size {size}")
        return False
    
    print(f"Matrix A shape: {A.shape}")
    print(f"Matrix B shape: {B.shape}")
    print(f"Matrix C shape: {C.shape}")
    
    # NumPy вычисление
    print("\n🔄 Computing with NumPy...")
    start = time.time()
    C_numpy = np.dot(A, B)
    end = time.time()
    numpy_time = end - start
    
    print(f"NumPy time: {numpy_time:.6f} seconds")
    
    # Сравнение
    if np.allclose(C, C_numpy, rtol=1e-5, atol=1e-5):
        print("\n✅ VERIFICATION PASSED!")
        return True
    else:
        print("\n❌ VERIFICATION FAILED!")
        diff = np.abs(C - C_numpy)
        print(f"Max difference: {np.max(diff):.2e}")
        return False

def main():
    sizes = [100, 500, 800, 1000, 2000]
    
    print("="*60)
    print("VERIFICATION FOR ALL MATRIX SIZES")
    print("="*60)
    
    results = []
    for size in sizes:
        if verify_size(size):
            results.append(f"{size}x{size}: ✅ PASSED")
        else:
            results.append(f"{size}x{size}: ❌ FAILED")
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    for r in results:
        print(r)

if __name__ == "__main__":
    main()