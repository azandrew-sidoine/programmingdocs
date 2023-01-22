#include <string>
#include <map>
#include <iostream>

template<typename Key, typename Value, typename F>
void update(std::map<Key, Value>& m, F foo) {
    for (auto&& [key, value] : m ) value = foo(key);
}

template<typename ... T>
auto mean(T ... args) {
    return (args + ...) / sizeof...(args);
}

int main() {
    std::map<std::string, long long int> m {
        {"a", 1},
        {"b", 2},
        {"c", 3}
    };

    update(m, [](std::string key) {
        return std::hash<std::string>{}(key);
    });

    for (auto&& [key, value] : m) {
        std::cout << key << ":" << value << std::endl;
    }

    std::cout << "Mean -> " << mean(1,2,4,5) << std::endl;
}