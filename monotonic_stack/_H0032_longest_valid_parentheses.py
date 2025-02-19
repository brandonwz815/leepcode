def longestValidParentheses(s: str) -> int:
    stack = [-1]  # Base index to handle edge cases
    max_len = 0
    
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)  # Push the index of '(' onto the stack
        else:
            stack.pop()  # Pop the top (this should match the last '(')
            
            if stack:
                # Calculate the length of the valid substring
                max_len = max(max_len, i - stack[-1])
            else:
                # If the stack is empty, push the current index as the base for future calculations
                stack.append(i)
    
    return max_len
