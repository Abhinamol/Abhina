
with open('words1.txt', 'r') as firstfile, open('demo.txt.txt', 'a') as secondfile:

    for line in firstfile:

        secondfile.write(line)
