text = ""
hexadecimal_result = ''.join([hex(ord(char))[2:] for char in text])
print(hexadecimal_result)


hexadecimal_text = ""

def hex_to_text(hex_string):
    return bytes.fromhex(hex_string).decode('utf-8')

original_text = hex_to_text(hexadecimal_text)
print(original_text)


