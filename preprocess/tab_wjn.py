import sys

argvs = sys.argv

f = open(argvs[1])
text = f.readlines()
f.close()

f_out = open('data/wjn_words_ony.txt', 'w')

for te in text:
    f_out.write(te.split('\t')[1])
    f_out.write('\n')

f_out.close()
