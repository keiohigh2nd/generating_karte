
import sys, codecs

argvs = sys.argv

f = codecs.open(argvs[1], 'r','utf-16')
text = f.readlines()
f.close()


f_out = open('data/icd9_words_only.txt', 'w')

for te in text:
    f_out.write(te.strip('\n').encode('utf-8'))
    f_out.write('\n')

 
f_out.close()
