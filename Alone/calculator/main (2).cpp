#include <iostream>

// ماشین حساب ساده
class Calculator {
public:
    int Add(int a, int b) {
        return a + b;
    }

    int Subtract(int a, int b) {
        return a - b;
    }

    void RunTests() {
        // تست جمع
        int addResult = Add(2, 3);
        CheckResult("Add Test", addResult, 5);

        // تست کاهش
        int subtractResult = Subtract(5, 3);
        CheckResult("Subtract Test", subtractResult, 2);
    }

private:
    // تابع بررسی نتیجه
    void CheckResult(const std::string& testName, int result, int expectedResult) {
        std::cout << "Test: " << testName << std::endl;
        std::cout << "Result: " << result << std::endl;
        std::cout << "Expected Result: " << expectedResult << std::endl;
        std::cout << "Test " << (result == expectedResult ? "Passed" : "Failed") << std::endl;
        std::cout << std::endl;
    }
};

int main() {
    Calculator calculator;
    calculator.RunTests();

    return 0;
}
