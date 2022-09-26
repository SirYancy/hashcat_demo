import hashlib

filename = "wordlist.txt"

input_file = open(filename, "r", encoding='utf-8')
output_file = open("hashes.txt", "w", encoding='utf-8')

for line in input_file:
    line = line.strip()
    result = hashlib.md5(str(line).encode('utf-8'))
    output_file.write(result.hexdigest())
    output_file.write('\n')
