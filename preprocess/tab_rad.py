import sys

argvs = sys.argv

f = open(argvs[1])
text = f.readlines()
f.close()

f_out = open('data/rad_words_ony.txt', 'w')

for te in text:
    f_out.write(te.strip('\n').split(',')[0])
    f_out.write('\n')

f_out.close()
