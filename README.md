# Parser Application

## Introduction
This Python program implements a simple recursive descent parser for parsing arithmetic expressions. The parser recognizes expressions involving addition, subtraction, multiplication, and division operations. It is designed to read expressions from an input file and determine whether they are syntactically correct according to a given grammar.

## Features
- **Parsing Arithmetic Expressions:** Parses arithmetic expressions involving addition, subtraction, multiplication, and division.
- **Error Handling:** Detects and reports syntax errors during parsing.
- **Interactive Console Output:** Provides detailed console output during the parsing process, indicating the production rules being applied and the current state of the parser.

## Usage
1. Ensure that the input file named `input.txt` containing arithmetic expressions is present in the same directory as the script.
2. Run the script `parser.py`.
    ```bash
    python parser.py
    ```
3. The parser will process the expressions in the input file and output the parsing results to the console.

## Grammar
The grammar for arithmetic expressions recognized by the parser is as follows:

G -> E

E -> T R

R -> + T R | - T R | ε

T -> F S

S -> * F S | / F S | ε

F -> ( E ) | M | N

M -> a | b | c | d

N -> 0 | 1 | 2 | 3


## Sample Input
The input file `input.txt` should contain arithmetic expressions separated by newline characters. Example content for `input.txt`:

(a + b) * c / (d - 1)

a + b * (c - d) / 2


## Output
The parser will output the parsing process and results to the console, indicating the production rules being applied and any syntax errors encountered during parsing.

## Contributions
Contributions to this project are welcome. If you have suggestions for improving the parser or extending its capabilities, please fork the repository and submit a pull request.

## License
This project is open-source and freely available under the MIT License.
