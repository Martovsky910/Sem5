import os

path = os.path.join('file1.txt')
with open(path, 'r') as f:
    data = f.read()
    print(data)


def encode_rle(data: str):
    str_encode = ''
    prev_char = ''
    count = 1
    for char in data:
        if char != prev_char:
            if prev_char:
                str_encode += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        str_encode += str(count) + prev_char
    return str_encode

str_encode = encode_rle(data)
print(str_encode)


import os

path = os.path.join('file2.txt')
with open(path, 'r') as f:
    data = f.read()
    print(data)

def decode_rle(data: str):
    str_decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decode_rle(data)
print(str_decode)




