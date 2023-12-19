# Custom model files

```sh
ollama create jdpllama-devops -f devops/Modelfile
ollama run jdpllama-devops
```

Examples:

```sh
ollama run jdpllama-devops "Summarize this file: $(cat README.md)"

ollama run jdpllama-devops 'Write a python function to generate the nth fibonacci number without using recursion.'

ollama run jdpllama-devops 'Write Python function that returns day of the week for a date'

ollama run jdpllama-devops '
Is there a bug in this function?

def calculate_fibonacci(n):
    "Calculate Fibonacci number"
    if n <= 0:
        return n
    else:
        return fib(n-1) + fib(n-2)
'

ollama run jdpllama-devops '
Write a unit test for this function.
Include imports and main.

def calculate_fibonacci(n):
    "Calculate Fibonacci number"
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
'

ollama run jdpllama-devops '# Python function to remove non-ASCII characters from a string:'

ollama run jdpllama-devops '<PRE> def return_most_frequent_character(x: str): <SUF>return result <MID>'

```