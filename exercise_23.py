# File Overlapping

overlap_list = []

with open('primenumbers.txt', 'r') as prime_file:
    prime_line = prime_file.readline()
    while prime_line:
        prime_line = prime_line.strip()
        with open('happynumbers.txt', 'r') as happy_file:
            happy_text = happy_file.read()
            happy_text = happy_text.split()
        if prime_line in happy_text:
            overlap_list.append(prime_line)
        prime_line = prime_file.readline()

print(overlap_list)

