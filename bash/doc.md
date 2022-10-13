# Bash scripting

Like python bash statement lays on a single line and are not `;` terminated.

## Shbang declaration

> #! /bin/sh

This declaration is required at top of the file for it to be recongnized as bash or shell script.

## Basics

* Script output

> echo < `content` > [>]|[>>] [output]

Write the provided string to the output buffer. By default it write it to the execution environment a.k.a terminal.

* Commands

Shell script has access to binary in the currently executing in the environmment the can be called as calling them directly in the terminal.

```sh
cat >> "./path/to/file
```

* Comments

Comments in shell scripting start with the `#` operator.

Multi line comments can be add using PHP EOT syntax:

```sh
<< EOT
Multi line comments goes like this
comment
EOT
```

## Conditions

Here is a list of operators based on the purpose:

-- Integer operators

> -eq    =========> Integer equality
> -ne    =========> Integer inequality
> -lt    =========> Integer less than
> -le    =========> Integer less than or equal to
> -gt    =========> Integer greater than
> -ge    =========> Integer greater than or equal to

-- Strings operators

> = (also =)    =========>  String equality
> !=    =========>  String inequality
> <     =========>  String lexiographic comparison (before)
> `>` =========>  String lexiographic comparison (after)
> =~    =========>  String regular expression match (bash 3 only, not currently allowed in ebuilds)

-- Strings Test

-z "string" ==========> String has zero length
-n "string" ==========> String has non-zero length

-- File descriptor testing

> -a file ========>   Exists (use -e instead)
> -b file ========>   Exists and is a block special file
> -c file ========>   Exists and is a character special file
> -d file ========>   Exists and is a directory
> -e file ========>   Exists
> -f file ========>   Exists and is a regular file
> -g file ========>   Exists and is set-group-id
> -h file ========>   Exists and is a symbolic link
> -k file ========>   Exists and its sticky bit is set
> -p file ========>   Exists and is a named pipe (FIFO)
> -r file ========>   Exists and is readable
> -s file ========>   Exists and has a size greater than zero
> -t fd   ========>   Descriptor fd is open and refers to a terminal
> -u file ========>   Exists and its set-user-id bit is set
> -w file ========>   Exists and is writable
> -x file ========>   Exists and is executable
> -O file ========>   Exists and is owned by the effective user id
> -G file ========>   Exists and is owned by the effective group id
> -L file ========>   Exists and is a symbolic link
> -S file ========>   Exists and is a socket
> -N file ========>   Exists and has been modified since it was last read

Note: For operator precedence, use `( )`

use `[[ condition ]]` instead of `[ condition ]` whenever possible as the first is bash way of testing condition while the second is internal command. But also know that first syntax does not evaluate multiple expression.

* if ... then ... [elif] ... [else] ... fi

Here is the syntax:

```sh
if [ $variable -eq 10 ]; then
    echo "Variable greather than 10"
fi
```

Note: You should be aware that the space between opening `[` and closing `]` are required.
To evaluate a variable between `[]`, developper must precede variable name with `$`

* Conditions chaining with && and ||

`&&` anf `||` are used to.

> && or -a

```sh
if [ $age -ge 18 ] && [ $age -lt 40 ]; then
    echo 'You are adult but not old'
else
    echo 'You are young or Too old'
fi
```

## Bash Iterative Structures

There are a few simple iterative structures available from within bash. The most useful of these is a for loop. This can be used to perform the same task upon multiple items.

```sh
# Basic for loop
for (( i = 1 ; i <= 10 ; i++ )) ; do
    einfo "i is ${i}"
done

# Basic while loop
while hungry ; do
    # Call function eat_cookies while condition is true
    eat_cookies
done

# Iterating over files
while read myline ; do
    einfo "It says ${myline}"
done < some_file
```

## Variables, Template string & String variables

* Arithmetic Expansion

The $(( expression )) construct can be used for integer arithmetic evaluation. expression is a C-like arithmetic expression. The following operators are supported (the table is in order of precedence, highest first).

> var++, var--    ==========> Variable post-increment, post-decrement
> ++var, --var    ==========> Variable pre-increment, pre-decrement
> -, +    ==========> Unary minus and plus
> !, ~    ==========> Logical negation, bitwise negation
> **  ==========> Exponentiation
> *, /, % ==========> Multiplication, division, remainder
> +, -    ==========> Addition, subtraction
> <<, >>  ==========> Left, right bitwise shifts
> <=, >=, <, >    ==========> Comparison: less than or equal to, greater than or equal to, strictly less than, strictly greater than
> ==, !=  ==========> Equality, inequality
> &   ==========> Bitwise AND
> ^   ==========> Bitwise exclusive OR
> |   ==========> Bitwise OR
> &&  ==========> Logical AND
> ||  ==========> Logical OR
> expr ? expr : expr  ==========> Conditional operator

=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=    =========> Assignment

* Declaring a variable

> variable=value

```sh
length=10

greetings="Hello"
```

* Null coalescing operator

> length=${missingVar:-10} -> Set length to 10 if missingVar is unset

or

> length:=missingVar

Here:

> ${var:?messateString} - Display messageString to stderr if var is missing

Template string works the same way as of PHP.

```sh
# Declaring age variable and set it value to 10
age=10

template="Your actual age is ${age}" # Access age variable to create a template string
```

* Obtaining length of string

> ${#stringVar}

```sh
myString="This is my string"
length=${#myString}
```

* Substring Extraction
The `${var:offset}` and `${var:offset:length} ` constructs can be used to obtain a substring. Strings are zero-indexed. Both offset and length are arithmetic expressions.

The first form with a positive offset returns a substring starting with the character at offset and continuing to the end of a string. If the offset is negative, the offset is taken relative to the end of the string.

```sh
base_str="Hello World"

substr=${base_str:0:4}
```

* String Replacements

There are three basic string replacement forms available:

> ${var#pattern} - Delete content from the start of the string
> ${var%pattern} - Delete content from end of string
> ${var/pattern/replacement}. -  The third is used to replace a match with different content.
> sed -i 's/pattern/replacement/' <FILENAME> - Replace pattern with replacement in the filename specified

* Splitting a string

The shell variable, `$IFS` is used to assign the character that will be used for dividing the string data.

`read` is a command or a function for reading input from a given source, either from shell argument, or strings.

```bash
```

## Arrays

Arrays are list of values. Array in bash are zero-based indexed.

> ${arr[*]}         # All of the items in the array
> ${!arr[*]}        # All of the indexes in the array
> ${#arr[*]}        # Number of items in the array
> ${#arr[0]}        # Length of item zero

```bash
arr=(1,2,3,4,5)

#Count the total elements of the array
total=${arr[*]}

# Accessing all element of an array
for element in arr[@];do
    printf 'Element :%d\n' $value
done
```

## Functions

Declaring a function using:

```bash
function func_name()
{
    # Function contents
}
```

or:

```bash
func_name()
{
    # Function contents
}
```

-- Variable scopes in function

Using the `local` keyword on a variable declared in a function scope, variable is local to the function.

-- Function with arguments

`$1`, `$2` ... `$n` represent the first, second ... nth arguments to a function.

```bash
function sum()
{
   return $(($1 + $2))
}
```

In order to get the returned value of a function we use the `$?` operator

```bash
function sum()
{
    # Function that returns
}

#Execute the function
sum 1 2 3
#Getting the returned value
echo "Result=$?"
```

Note: `unset command`

`unset` is used to remove variable or function reference from script execution.

To remove a function we:

```bash
function delete()
{
    # Function definition
}

unset -f delete
```

## Files & Directories

-- Checking if file exists

Using the test command:

> test -f "$PATH" && <WHAT_TO_EXECUTE_IF_FILE_EXISTS>

Using bash if conditions:

```bash
path=$HOME/path/to/file

if [[ -f $path ]]; then
    echo "Path exists"
else
    echo "Path does not exists"
fi
```

-- Checking if directory exists

Using the test command:

> test -d "$PATH" && <WHAT_TO_EXECUTE_IF_FILE_EXISTS>

Using bash if conditions:

```bash
path=$HOME/path/to/file

if [[ -d $path ]]; then
    echo "Path exists"
else
    echo "Path does not exists"
fi
```

-- Reading file line by line

```bash

INPUT=/path/to/file

while read -r line; do
    echo "$line"
done < INPUT
```

-- Appending data to file

Using `>` we write to file and `>>` to append to files.

Note the output of any command can be indirect to a given file path instead of the standard output.

> echo -e <TEXT_CONTENT> >> $PATH
> cat << EOF >> $PATH - Open an interactive terminal for appending data to file.

Using the tee command:

> echo <STRING_CONTENT> | tee -a $FILENAME > /dev/null

## Input & Outputs && Redirection

## Command line arguments
