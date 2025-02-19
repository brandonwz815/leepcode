# https://www.meta.ai/c/f878bf6d-7a29-4f03-b86c-7271b5f820f5

def stockSpan(prices):
    n = len(prices)
    span = [1] * n
    stack = []
    
    for i in range(n):
        # Pop all indices from the stack where price is less than or equal
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        # If stack is not empty, update span
        if stack:
            span[i] = i - stack[-1]
        else:
            span[i] = i + 1
        
        # Push current index to the stack
        stack.append(i)
    
    return span

# Example usage
prices = [10, 4, 5, 90, 120, 80]
print(stockSpan(prices))  # Output: [1, 1, 2, 4, 5, 1]