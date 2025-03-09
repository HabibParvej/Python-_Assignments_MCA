def replace(s):
    result = s[0]  
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  
            result += '*'
        else:
            result += s[i]
    return result


txt = input("Enter a string: ")
print("output:", replace(txt))
