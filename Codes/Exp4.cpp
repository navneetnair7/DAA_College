#include <bits/stdc++.h>
using namespace std;

void optimal_parantheses(int i, int j, int n, int* s, char& name){
    if(i == j){
        cout << name++;
        return;
    }
    else{
        cout << " ( ";
        optimal_parantheses(i, *((s + i * n) + j), n, s, name);
        optimal_parantheses(*((s + i * n) + j) + 1, j, n, s, name);
        cout << " ) ";
    }
}

void matrix_chain_mult(int p[], int n){
    int m[n][n];
    int s[n][n];

    for(int i = 1; i < n; i ++){
        m[i][i] = 0;
    }
    for(int l = 2; l < n; l++){
        for(int i = 1; i < n - l + 1; i ++){
            int j = i + l - 1;
            m[i][j] = INT_MAX;
            for(int k = i; k <= j - 1; k ++){
                int q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                if(q < m[i][j]){
                    m[i][j] = q;
                    s[i][j] = k;
                }
            }
        }
    }
    char name = 'A';
    cout << "The optimal parantheses are: " << endl;
    optimal_parantheses(1, n - 1, n, (int*)s, name);
}

int main(){
    int p[] = {40, 20, 30, 10, 30};
    int n = sizeof(p) / sizeof(p[0]);
    matrix_chain_mult(p, n);
    return 0;
}