name="harry"
print(name[0])  # Output: h
print("Hello is your name ",name)#Output: Hello is your name  harry
#sen="He said "hi" to me"  # This line will cause a syntax error due to the unescaped double quotes
sen='He said "hi" to me'  # This line is correct and will not cause a syntax error
print(sen)  # Output: He said "hi" to me
#Multi-line string
multi_line='''This is a multi-line string.
It can span multiple lines.'''
print(multi_line)
print("\n lets use a for loop to print each character in the string\n")
for char in name:
    print(char)