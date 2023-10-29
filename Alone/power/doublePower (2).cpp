#include <iostream>

// تابع توان رساندن
double Power(double base, int exponent) {
    if (exponent == 0)
        return 1;
    else if (exponent < 0)
        return 1 / (base * Power(base, -exponent - 1));
    else
        return base * Power(base, exponent - 1);
}

// تابع بررسی نتیجه
void CheckResult(const std::string& testName, double result, double expectedResult) {
    std::cout << "Test: " << testName << std::endl;
    std::cout << "Result: " << result << std::endl;
    std::cout << "Expected Result: " << expectedResult << std::endl;
    std::cout << "Test " << (result == expectedResult ? "Passed" : "Failed") << std::endl;
    std::cout << std::endl;
}

// تابع اجرای تست کیس‌ها
void RunTests() {
    // تست توان رساندن
    double powerResult = Power(2, 3);
    CheckResult("Power Test", powerResult, 8);

    // تست توان رساندن با اعداد منفی
    powerResult = Power(-2, 3);
    CheckResult("Power Test with Negative Base", powerResult, -8);

    // تست توان رساندن با توان منفی
    powerResult = Power(2, -3);
    CheckResult("Power Test with Negative Exponent", powerResult, 0.125);
}

int main() {
    // اجرای تست کیس‌ها
    RunTests();

    // حلقه اجرای توان رساندن
    char choice;
    do {
        double base;
        int exponent;

        std::cout << "Enter the base number: ";
        std::cin >> base;

        std::cout << "Enter the exponent: ";
        std::cin >> exponent;

        double result = Power(base, exponent);

        std::cout << "Result: " << result << std::endl;

        std::cout << "Do you want to continue? (y/n): ";
        std::cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    return 0;
}
