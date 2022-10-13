#! /bin/sh

echo "Performing C-Styled For-Loop"
# C style loops
for ((i=0; i<=10; i++)); do
    echo "Step $i"
done

# While loop
i=1
echo "Performing a While-Loop"
while [ $i -le 10 ]; do
    echo "Step $i"
    ((i++))
done

echo ""
echo "Print list backward"
echo ""
while [ $i -gt 0 ]; do
    echo "Step $i"
    ((i--))
done

# Using break and continue
echo ""
echo "Loop with break statement"
echo ""
while [ $i -le 10 ]; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo "Step $i"
    ((i++))
done

i=1
echo ""
echo "Loop with continue statement for printing non-even numbers"
echo ""
while [ $i -le 10 ]; do
    result=$(( i % 2 ))
    if [ $result -eq 0 ]; then
        ((i++))
        continue
    else
        echo "Step $i"
        ((i++))
    fi
done