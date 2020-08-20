/* Small program to show how simple closures in C++ may improve readability.
 * Compiles under C++14, C++17, and C++20, but not C++11.
 */

#include <iostream>


class Counter {
public:
  explicit Counter(long start = 0): count(start) {}

  void operator()() {
    std::cout << ++count << std::endl;
  }
private:
  long count;
};

auto NewCounterClosure(long count = 0) {
  return [=]() mutable {
    std::cout << ++count << std::endl;
  };
}

int main() {
  long start;
  std::cin >> start;

  Counter counter1{start};
  Counter counter2{start};
  auto counter3 = NewCounterClosure(start);
  auto counter4 = NewCounterClosure(start);

  counter1(); counter1(); counter1();
  counter2(); counter2(); counter2();
  counter3(); counter3(); counter3();
  counter4(); counter4(); counter4();

  std::cout << "sizeof(counter1) = " << sizeof(counter1) << std::endl;
  std::cout << "sizeof(counter2) = " << sizeof(counter2) << std::endl;
  std::cout << "sizeof(counter3) = " << sizeof(counter3) << std::endl;
  std::cout << "sizeof(counter4) = " << sizeof(counter4) << std::endl;

  return 0;
}
