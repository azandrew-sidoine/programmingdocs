#include <cstdio>
#include <cstdlib>

int Add(int a, int b) {
    return a + b;
}

void Printf(int& value)
{
    printf("Print(L-VALUE) Reference: %d\n", value);
}

void Printf(const int& value)
{
    printf("Print(CONST L-VALUE) Reference: %d\n", value);
}

void Printf(int&& value)
{
    printf("Print(R-VALUE) Reference: %d\n", value);
}


int main(int argc, char const *argv[])
{
    Printf(Add(2, 4));
    Printf(4);

    int x = 10;

    Printf(x);
    return 0;
}
