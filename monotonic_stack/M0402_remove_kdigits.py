# https://www.meta.ai/c/f9106977-1648-4125-86d2-64c8498200b7

def removeKdigits(num: str, k: int) -> str:
    stack = []
    for n in num:
        while k > 0 and stack and stack[-1] > n:
            stack.pop()
            k -= 1
        stack.append(n)
    # remove remaining k digits
    stack = stack[:-k] if k > 0 else stack
    # remove leading zeros
    return "".join(stack).lstrip("0") or "0"

print(removeKdigits("1432219", 2))
print(removeKdigits("1432987", 2))
print(removeKdigits("10200", 1))
