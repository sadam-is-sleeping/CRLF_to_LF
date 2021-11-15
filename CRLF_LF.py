CRLF = b'\r\n'
LF = b'\n'

file_path = input(r'File Path: ')

with open(file_path, 'rb') as file:
    text = file.read()

text = text.replace(CRLF, LF)
# LF to CRLF
# text = text.replace(LF, CRLF)
with open(file_path, 'wb') as file:
    file.write(text)
