#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#pragma GCC optimize("Ofast,unroll-loops")

static const int _ = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();

class Solution {
public:
    int numberOfSpecialChars(string word) {
        // Используем массивы фиксированного размера вместо векторов для скорости
        int lastLower[26];
        int firstUpper[26];
        
        // Инициализация -1 (не найдено)
        for (int i = 0; i < 26; ++i) {
            lastLower[i] = -1;
            firstUpper[i] = -1;
        }
        
        int n = word.length();
        for (int i = 0; i < n; ++i) {
            char c = word[i];
            if (c >= 'a' && c <= 'z') {
                lastLower[c - 'a'] = i; // Всегда обновляем на последнюю
            } else {
                int idx = c - 'A';
                if (firstUpper[idx] == -1) {
                    firstUpper[idx] = i; // Записываем только первую позицию
                }
            }
        }
        
        int count = 0;
        for (int i = 0; i < 26; ++i) {
            // Условие: обе найдены и порядок соблюден
            if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {
                count++;
            }
        }
        
        return count;
    }
};