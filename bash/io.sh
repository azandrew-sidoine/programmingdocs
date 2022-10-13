#! /bin/sh

path=/Users/azandrewsidoine/Workspace/code-testing/bash/text.txt


echo "Checking if file exist..."

if [[ -f "$path" ]]; then
    echo ''
    echo "$path exists"
else
    echo ''
    echo "$path does not exists"
    echo ''
    echo "Creating file..."
    touch "text.txt"
    echo "Hello World!" > "text.txt"
fi

DIR=$HOME/Downloads

echo ''
echo 'Testing if a directory exists'

if [[ -d "$DIR" ]]; then
    echo "$DIR exists"
else
    echo "$DIR does not exists"
fi