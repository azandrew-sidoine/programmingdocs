#include "math.hpp"

int sum(int values[], size_t length) {

  int result{};

  for (int i = 0; i < length; i++) {
    result += values[i];
  }
  
  return result;
  
}