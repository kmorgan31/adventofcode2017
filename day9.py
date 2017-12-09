def calc_score(stack):
    return stack.count('{')

def top(stack):
    if len(stack)==0:
        return ''
    return stack[-1]

def day9(filename):
    stack = []
    score = 0
    garbage_count = 0
    x=0

    with open(filename, 'r') as f:
        contents = f.read()

        while x < len(contents):
            if contents[x] == '!': # jump over next character
                x += 2
            else:
                if contents[x] in ('{', '<') and top(stack) != '<':
                    stack.append(contents[x])
                else:
                    if contents[x] == '}' and top(stack) == '{':
                        score += calc_score(stack)
                        stack.pop()
                    elif contents[x] == '>' and top(stack) == '<':
                        stack.pop()
        
                    if top(stack) == '<':
                        garbage_count += 1
                x += 1

    print garbage_count
    print score                                       
                
        
