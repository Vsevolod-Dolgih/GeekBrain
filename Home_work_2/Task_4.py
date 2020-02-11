sentence = input('Type any words or sentences:')
sentence = sentence.split()
line = 1
word = 0
for i in range (len(sentence)):
    w = sentence[word]
    print(line, w[0:10])
    line += 1
    word += 1
