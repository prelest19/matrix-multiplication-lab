#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <chrono>
#include <iomanip>

using namespace std;
using namespace chrono;

typedef vector<vector<double>> Matrix;

// Функция для проверки существования файла
bool fileExists(const string& filename) {
    ifstream f(filename);
    return f.good();
}

// Чтение квадратной матрицы
bool readMatrix(const string& filename, Matrix& mat) {
    ifstream fin(filename);
    if (!fin) {
        cerr << "❌ Ошибка: не могу открыть файл " << filename << endl;
        return false;
    }

    string line;
    size_t expectedSize = 0;

    while (getline(fin, line)) {
        istringstream iss(line);
        vector<double> row;
        double value;

        while (iss >> value)
            row.push_back(value);

        if (!row.empty()) {
            if (expectedSize == 0)
                expectedSize = row.size();
            else if (row.size() != expectedSize) {
                cerr << "❌ Ошибка: матрица не прямоугольная." << endl;
                return false;
            }
            mat.push_back(row);
        }
    }
    fin.close();

    if (mat.empty()) {
        cerr << "❌ Ошибка: матрица пустая." << endl;
        return false;
    }
    
    if (mat.size() != mat[0].size()) {
        cerr << "❌ Ошибка: матрица должна быть квадратной. Получено " 
             << mat.size() << "x" << mat[0].size() << endl;
        return false;
    }

    cout << "✅ Файл " << filename << " успешно прочитан. Размер: " 
         << mat.size() << "x" << mat.size() << endl;
    return true;
}

// Запись матрицы
void writeMatrix(const string& filename, const Matrix& mat) {
    ofstream fout(filename);
    for (const auto& row : mat) {
        for (size_t j = 0; j < row.size(); ++j) {
            fout << fixed << setprecision(6) << row[j];
            if (j < row.size() - 1) fout << " ";
        }
        fout << "\n";
    }
    fout.close();
    cout << "✅ Результат записан в " << filename << endl;
}

// Умножение матриц
Matrix multiplyMatrices(const Matrix& A, const Matrix& B) {
    size_t n = A.size();
    Matrix C(n, vector<double>(n, 0.0));

    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < n; ++j)
            for (size_t k = 0; k < n; ++k)
                C[i][j] += A[i][k] * B[k][j];

    return C;
}

int main() {
    cout << "=====================================" << endl;
    cout << "   УМНОЖЕНИЕ КВАДРАТНЫХ МАТРИЦ      " << endl;
    cout << "=====================================" << endl;
    
    Matrix A, B, C;

    // Пути к файлам
    const string fileA = "../data/matrixA.txt";
    const string fileB = "../data/matrixB.txt";
    const string fileResult = "../data/result.txt";

    // Проверка существования файлов
    if (!fileExists(fileA)) {
        cerr << "❌ Файл " << fileA << " не найден!" << endl;
        cerr << "Создайте файл с матрицей в папке data" << endl;
        return 1;
    }
    if (!fileExists(fileB)) {
        cerr << "❌ Файл " << fileB << " не найден!" << endl;
        return 1;
    }

    // Чтение матриц
    if (!readMatrix(fileA, A)) return 1;
    if (!readMatrix(fileB, B)) return 1;

    // Проверка размеров
    if (A.size() != B.size()) {
        cerr << "❌ Ошибка: матрицы должны быть одинакового размера." << endl;
        cerr << "Размер A: " << A.size() << "x" << A.size() << endl;
        cerr << "Размер B: " << B.size() << "x" << B.size() << endl;
        return 1;
    }

    size_t n = A.size();
    
    cout << "\n📊 Размер матриц: " << n << "x" << n << endl;
    cout << "🔄 Выполняется умножение..." << endl;

    // Замер времени
    auto start = high_resolution_clock::now();
    C = multiplyMatrices(A, B);
    auto end = high_resolution_clock::now();

    duration<double> elapsed = end - start;

    // Запись результата
    writeMatrix(fileResult, C);

    // Вычисление объема задачи
    unsigned long long operations = 2ULL * n * n * n;

    // Вывод результатов
    cout << "\n========== РЕЗУЛЬТАТЫ ==========" << endl;
    cout << "⏱️  Время выполнения: " << fixed << setprecision(6) 
         << elapsed.count() << " секунд" << endl;
    cout << "📈 Объем задачи (операций): " << operations << endl;
    cout << "⚡ Производительность: " << fixed << setprecision(2) 
         << (operations / elapsed.count() / 1e6) << " MFLOPS" << endl;
    cout << "================================" << endl;

    cout << "\n💾 Результат сохранен в data/result.txt" << endl;
    
    return 0;
}
