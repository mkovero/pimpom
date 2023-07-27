import sys

def string_to_custom_binary(s):
    return ''.join(''.join('aaa' if bit == '0' else 'uli' for bit in format(ord(c), '08b')) for c in s)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pim.py <input_string>")
    else:
        s = sys.argv[1]
        print(string_to_custom_binary(s))

