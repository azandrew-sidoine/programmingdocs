#! /bin/sh

base_str='Hello World'

echo "Base string ${base_str}"

# Substring
echo "Substring between index 0 and 4: ${base_str:0:4}"

# Replace
echo "Replacing pattern: ${base_str/[e]/a}"

# Base string length
echo "String length is: ${#base_str}"

# Split string implementation

function str_split
{
    local DEFAULT_IFS="$IFS"
    IFS=$2
    read -ra "$3" <<< "$1"
    IFS="$DEFAULT_IFS"
}

# Here We pass in the string to split, the character to use to split the string
# and the output variable
str_split "Hello, Welcome to KodeKloud" ' ' 'arr'

echo ''
echo 'Printing list values:'
for part in "${arr[@]}"; do
    echo "$part"
done

printf '%s' '> '
read string

str_split "$string" ' ' 'arr'

echo ''
echo 'Printing list values:'
for part in "${arr[@]}"; do
    echo "$part"
done