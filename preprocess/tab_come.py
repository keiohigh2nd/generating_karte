
import sys, codecs

argvs = sys.argv

f = codecs.open(argvs[1], 'r','utf-16')
text = f.readlines()
f.close()

del text[-1]
del text[-1]
del text[-1]

f_out = open('data/come_words_only.txt', 'w')

for te in text:
    f_out.write(te.split(',')[0].strip('\n').encode('utf-8'))
    f_out.write('\n')

 
f_out.close()
