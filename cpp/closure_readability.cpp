/* Small program to show how simple closures in C++ may improve readability.
 * Compiles under C++14, C++17, and C++20, but not C++11.
 */

#include <iostream>


class Counter {
public:
	explicit Counter(long start = 0): count{start} {}

	long operator()() {
		return ++count;
	}
private:
	long count;
};

auto NewCounterClosure(long count = 0) {
	return [count]() mutable {
		return ++count;
	};
}

int main() {
	Counter counter1;
	Counter counter2{};
	auto counter3(NewCounterClosure());
	auto counter4{NewCounterClosure()};
	auto counter5 = NewCounterClosure();

	std::cout << counter1() << counter1() << counter1() << std::endl;
	std::cout << counter2() << counter2() << counter2() << std::endl;
	std::cout << counter3() << counter3() << counter3() << std::endl;
	std::cout << counter4() << counter4() << counter4() << std::endl;
	std::cout << counter5() << counter5() << counter5() << std::endl;

	std::cout << "sizeof(Counter) = " << sizeof(Counter) << std::endl;
	std::cout << "sizeof(NewCounterClosure()) = " << sizeof(NewCounterClosure()) << std::endl;

	return 0;
}
