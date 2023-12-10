def calc(expression):
    ops = {'плюс': (1, lambda x, y: x + y), 'минус': (1, lambda x, y: x - y),
           'умножить на': (2, lambda x, y: x * y), 'разделить на': (2, lambda x, y: x / y)}
    
    def parse_expression(expression):
        tokens = expression.split(' ')
        stack = []
        queue = []
        
        for token in tokens:
            if token in ops:
                while stack and ops[token][0] <= ops[stack[-1]][0]:
                    queue.append(stack.pop())
                stack.append(token)
            elif token == 'и':
                continue
            else:
                queue.append(float(token))
        
        while stack:
            queue.append(stack.pop())
        
        return queue
    
    def evaluate_expression(tokens):
        stack = []
        
        for token in tokens:
            if token in ops:
                y, x = stack.pop(), stack.pop()
                stack.append(ops[token][1](x, y))
            else:
                stack.append(token)
        
        return stack[0]
    
    parsed_expr = parse_expression(expression)
    result = evaluate_expression(parsed_expr)
    
    return str(result)


