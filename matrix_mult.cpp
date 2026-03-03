#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <chrono>
#include <iomanip>

using namespace std;
using namespace chrono;

typedef vector<vector<double>> Matrix;

bool readMatrix(const string& filename, Matrix& mat) {
    ifstream fin(filename.c_str());
    if (!fin) {
        cerr << "Error: cannot open file " << filename << endl;
        return false;
    }

    string line;
    while (getline(fin, line)) {
        istringstream iss(line);
        vector<double> row;
        double value;
        while (iss >> value)
            row.push_back(value);
        if (!row.empty())
            mat.push_back(row);
    }
    fin.close();
    return (!mat.empty() && mat.size() == mat[0].size());
}

void writeMatrix(const string& filename, const Matrix& mat) {
    ofstream fout(filename.c_str());
    for (size_t i = 0; i < mat.size(); i++) {
        for (size_t j = 0; j < mat[i].size(); j++) {
            fout << fixed << setprecision(6) << mat[i][j];
            if (j < mat[i].size() - 1) fout << " ";
        }
        fout << "\n";
    }
    fout.close();
}

Matrix multiplyMatrices(const Matrix& A, const Matrix& B) {
    size_t n = A.size();
    Matrix C(n, vector<double>(n, 0.0));
    for (size_t i = 0; i < n; ++i)
        for (size_t k = 0; k < n; ++k) {
            double aik = A[i][k];
            for (size_t j = 0; j < n; ++j)
                C[i][j] += aik * B[k][j];
        }
    return C;
}

int main() {
    Matrix A, B, C;
    
    string fileA = "data/matrixA.txt";
    string fileB = "data/matrixB.txt";
    string fileResult = "data/result.txt";

    cout << "Reading matrix A..." << endl;
    if (!readMatrix(fileA, A)) return 1;
    
    cout << "Reading matrix B..." << endl;
    if (!readMatrix(fileB, B)) return 1;

    if (A.size() != B.size()) {
        cerr << "Matrices size mismatch" << endl;
        return 1;
    }

    size_t n = A.size();
    cout << "Multiplying " << n << "x" << n << " matrices..." << endl;
    
    auto start = high_resolution_clock::now();
    C = multiplyMatrices(A, B);
    auto end = high_resolution_clock::now();
    
    writeMatrix(fileResult, C);
    
    duration<double> elapsed = end - start;
    unsigned long long operations = 2ULL * n * n * n;
    
    cout << "\n=== RESULTS ===" << endl;
    cout << "Time: " << elapsed.count() << " seconds" << endl;
    cout << "Operations: " << operations << endl;
    cout << "Result saved to " << fileResult << endl;
    
    return 0;
}