# Unittest Demo

## Part 1: Setup

### Dependencies

This repo requires no external dependencies. If you have Python 3, you're good.

### Installation

From the command line: fork/clone this repo and change into the new directory.

```zsh
git clone https://github.com/ajtran303/unittest_demo.git
cd unittest_demo
```
### Run the tests

Run individual test cases by invoking the spec as a module:

```zsh
python3 -m specs.test_imaginary_friend
```

To run all tests, invoke the unittest module with options:

```zsh
python3 -m unittest discover -s specs
```

Either command will invoke a test runner whose daemon should report `Ran 8 tests` and `FAILED (errors=8)`. If you don't see this, make sure to send the correct command.