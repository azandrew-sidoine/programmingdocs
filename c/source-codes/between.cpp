#include <cstdlib>
#include <ctime>
#include <cstdio>

uint64_t between(uint64_t min, uint64_t max);

int main()
{
    // Seed random handler
    srand((unsigned)time(0));

    printf("Generated number value is : %d \n", between(10, 20));

    return EXIT_SUCCESS;
}

uint64_t between(uint64_t min, uint64_t max)
{
    // Seed the random
    return (rand() % (max - min + 1)) + min;
}