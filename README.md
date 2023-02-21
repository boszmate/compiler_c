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

## Tests
#### 1. Manual tests
You can run manual tests due to providing input file to python command line (look into `3. Run` in previous README section). The app return output C files are in the `tests` directory.

#### 2. Unit tests
Unit tests are available with following command line:
```
$ python -m unittest {path to unit test}
```
For example to run single test:
```
$ python -m unittest tests/unittests/test_print.py
```
For example to run all tests:
```
$ python -m unittest tests/unittests/*.py
```


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