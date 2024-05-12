#include <iostream>
#include <vector>

int main() {
    int n, i = 0, count = 0;
    long long int sum = 0;  
    std::cin >> n;

    std::vector<int> carneiros(n);
    std::vector<int> estrelas_atacadas(n, 0);

    for (int j = 0; j < n; ++j) {
        std::cin >> carneiros[j];
    }

    while (0 <= i && i < n) {
        estrelas_atacadas[i] = 1;
        if (carneiros[i] % 2 == 0) {
            carneiros[i] = carneiros[i] > 0 ? carneiros[i] - 1 : 0;
            i -= 1;
        } else {
            carneiros[i] = carneiros[i] > 0 ? carneiros[i] - 1 : 0;
            i += 1;
        }
    }

    for (int j = 0; j < n; ++j) {
        count += estrelas_atacadas[j];
        sum += carneiros[j];  
    }

    std::cout << count << " " << sum << std::endl;  

    return 0;
}