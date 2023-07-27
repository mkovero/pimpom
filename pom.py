import sys

def custom_binary_to_string(s):
    s = s.replace('uli', '1').replace('aaa', '0')
    binary_chars = [s[i:i+8] for i in range(0, len(s), 8)]
    return ''.join(chr(int(binary_char, 2)) for binary_char in binary_chars)

s = sys.stdin.read().strip()
print(custom_binary_to_string(s))

