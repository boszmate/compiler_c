# Python to C language compiler

## Description
This is the Python App to compile Python files to C language. The compiler supports basic properties of Python language like e.g. variables, if statement, print function, expressions and comparisons. Look into [ToDo](##ToDo) section to more information what will be added to this app.


## Installation guide
#### 1. Download
```
$ git clone https://github.com/boszmate/compiler_c.git
$ cd compiler_c
```
#### 2. Install required packages
```
$ sudo apt install python3
```
#### 3. Run
```
$ python ./main.py {py input}
```
For example:
```
$ python ./main.py tests/input.py 
```

## Output files in C
Output C files are in the `tests` directory.

## ToDo
To add:
- loops (e.g. for, while),
- classes and functions,
- standard libraries (e.g. file operations),
- more types (e.g. float, boolean, string),
- arrays,
- logical operators,
- tests (e.g unit tests),
- validator to check the correctness of the generated C code (e.g. additional bash script).