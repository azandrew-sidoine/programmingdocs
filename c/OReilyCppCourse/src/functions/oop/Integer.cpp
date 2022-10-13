#include "Integer.hpp"
#include <cstdio>
#include <utility>

Integer::Integer(const Integer &source) { SetValue(source.GetValue()); }

Integer::Integer(Integer&& source) {
  value_ = std::move(source.value_);
  source.value_ = nullptr;
}

int Integer::GetValue() const { return *value_; }

void Integer::SetValue(int value) { value_ = new int(value); }

Integer::Integer(int value) { SetValue(value); }

Integer::~Integer() {
  if (value_ != nullptr) {
    delete value_;
    value_ = nullptr;
  }
}
