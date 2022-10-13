#ifndef utils_h
#define utils_h

template<typename T>
void swap(T& a, T& b);

template<typename T>
inline void swap(T& a, T& b)
{
    const auto temp = b;
    b = a;
    a = temp;
}

#endif