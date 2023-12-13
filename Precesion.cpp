#include <iostream>
#include <iomanip>

using namespace std;

void preciseDivision(float a, float b) {
    // Perform the division
    float result = a / b;

    // Print the result with and without decimal precision
    cout << fixed << setprecision(5) << result << " " << fixed << setprecision(3) << result << endl;
}

int main() {
    // Example usage
    float a = 5.43;
    float b = 2.653;

    preciseDivision(a, b);

    return 0;
}
