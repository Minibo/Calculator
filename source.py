OPERATORS = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x / y),
}

def calculator(input):
    '''
    This is calculator function
    '''
    def parse_input_str(input: str):
        mod_input = input.replace(' ', '')
        number = ''
        for character in mod_input:
            if character.isdigit() or character == '.':
                number += character
            elif number:
                yield(float(number))
                number = ''
            if character in OPERATORS or character in '()':
                yield character
        if number:
            yield float(number)

    def shunting_yard_algorithm(formula):
        stack = []
        for token in formula:
            if token in OPERATORS: 
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calculate(tokens):
        stack = []
        for token in tokens:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]
    
    output = calculate(shunting_yard_algorithm(parse_input_str(input)))
    return output