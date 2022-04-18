# Each character in a string is stored internally as a so-called Unicode “code-point” which is an integer. 
# You can specify an exact code-point value using the following escape sequences:
a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FOR ALL}'   # d = '∀'

print(a, b, c, d)

# 1 byte string
# A string of 8-bit bytes, commonly encountered with low-level I/O, is written as follows:
data = b'Hello World\r\n'
print(data)
# By putting a little b before the first quotation, you specify that it is a byte string as opposed to a text string.
print(len(data))
print(data[0:5])
print(data.replace(b'Hello', b'Cruel'))
# Indexing is a bit different because it returns byte values as integers.
print(data[0])  # 72 (ASCII code for 'H')
# conversion to/from text strings
text = data.decode('utf-8')  # bytes -> text
print(text)
data = text.encode('utf-8')  # text -> bytes

# 2 raw strings
# Raw strings are string literals with an uninterpreted backslash. 
# They are specified by prefixing the initial quote with a lowercase “r”.
# Example: filename, regular expressions, etc.
rs = r'c:\Users\eason'
print(rs)

# 3 f-strings
name = 'eason'
shares = 100
price = 123.45
fs = f'{name:>10s} {shares:10d} {price:10.2f}'
print(fs)
fs2 = f'Cost = ${shares * price:.2f}'
print(fs2)

# 4 regular expressions
text = 'Today is 4/18/2022. Tomorrow is 4/19/2022.'
import re
# find all occurrences of a date
print(re.findall(r'\d+/\d+/\d+', text))
# replace all occurrences of a date with replacement text
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))


# commentaty
# dir() produces a list of all operations that can appear after the (.)
print(dir(text))