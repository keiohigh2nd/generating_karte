import sys
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml
import string
import random
import shelve
import numpy as np 
import scipy.sparse as sparse
import cPickle as pickle
from collections import defaultdict, namedtuple

def randomString(length=16):
	return "".join([random.choice(string.letters) for _ in xrange(length)])

def token((disp, repr)):
	return {'disp':disp, 'repr':repr}

def randomText(length, words):
	return " ".join([random.choice(words) for _ in xrange(length)])

def remove_prefix(w):
	if '_' in w:
		return w.split('_', 1)[1]
	else:
		return w

def word_shuffle(words_list):
	random.shuffle(words_list)
	words_list = words_list[:500]
	vocab_list = set(words_list)
        return words_list
 
random.seed(2014)

wjn_words = file('data/wjn_words_only.txt').read().splitlines()
rad_words = file('data/rad_words_only.txt').read().splitlines()
icd9_words = file('data/icd9_words_only.txt').read().splitlines()
come_words = file('data/come_words_only.txt').read().splitlines()

wjn_words = word_shuffle(wjn_words)
rad_words = word_shuffle(rad_words)
icd9_words = word_shuffle(icd9_words)
come_words = word_shuffle(come_words)


def randomPatient():
	global vocab
	pat = {}
	pat['index'] = randomString()
        dig_code = randomText(2, icd9_words)
	ChiefComplaint = pat['ChiefComplaint'] = dig_code
        ana_pos = randomText(10, rad_words)
	TriageAssessment = pat['TriageAssessment'] = dig_code + ana_pos + randomText(10, wjn_words)
	MDcomments = pat['MDcomments'] = dig_code + ana_pos + randomText(50, come_words)
	Age = pat['Age'] = str(np.random.choice(range(20,80)))
	Sex = pat['Sex'] = np.random.choice(['M', 'F'])[0]
        return {'visit':pat}

if __name__ == "__main__":

    try:
        n = int(sys.argv[1])
    except:
        print "usage: python generate_patients.py numPatients"
        sys.exit()

    xml_str = ""
    for _ in xrange(n):
        pat = randomPatient()
        #print pat
        xml = dicttoxml(pat, attr_type=False, root=False)
        dom = parseString(xml)
        pat = '\n'.join(dom.toprettyxml().split('\n')[1:])
        xml_str += pat
    print xml_str
