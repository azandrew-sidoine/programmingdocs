# Modern C++ (Regular Expression) <regex>

Previous to C++11, we make use of `boost` regex library. C++11 introduced the `std::regex` in the language core for parsing regular expression and matching strings.

- std::regex

Regular expression provided by C++11, operates on `std::string` object and patterns are constructed and parsed by tge `std::regex` object.

- std::regex_match

It is used to match regular expression in C++11 and foward

> std::regex_match(std::string, std::regex)

```cpp
#include <string>
#include <regex>

int main()
{
    std::string names{"foo.txt", "bar.txt", "test", "a0.txt", "AAA.txt"};

    // **Note** As \ is uses to escape character, \\ must be used in regex string to escape special characters
    std::regex txt_regex{"[a-z]+\\.txt"};

    for (const auto& name : names)
        std::cout << name << ": " << std::regex_match(name, txt_regex) << std::endl;
}
```

> std::regex_match(std::string, std::smatch, std::regex)

**Note**
std::smatch -> It's a container object, that hold the list of matches (similar to &matches array passed in PHP).
The first element of the `std::smatch` is the entire string matching the regular expression, while susequent elements matches the group matches when `()` is used in the regex.


```cpp
int main()
{
    std::regex my_regex{"([a-z]+)\\.txt"};
    std::smatch mataches;

    for (const auto& name : names) {
        if (std::regex_match(name, matches, my_regex)) {
            if (matches.size() === 2) {
                std::string base = matches[1].str();
                std::cout << "sub-match[0]: " << matches[0].str() << std::endl;
                std::cout << name << "sub-match[1]: " << base << std::endl;
            }    
        }
    }
}
```
