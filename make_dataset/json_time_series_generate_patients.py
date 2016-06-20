# coding: UTF-8

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
import codecs, json

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
	#words_list = words_list[:500]
	#words_list = words_list[:500]
	vocab_list = set(words_list)
        return words_list

def read_file(filename):
	f = codecs.open(filename,"r","utf-8")
	text = f.read()
	f.close()
	return text
 
random.seed(2014)

icd9_words = read_file('data/icd9_words_only.txt')
rad_words = read_file('data/rad_words_only.txt')
wjn_words = read_file('data/wjn_words_only.txt')
come_words = read_file('data/come_words_only.txt')


icd9_words = icd9_words.split("\r\n")
icd9_words[-1] = icd9_words[-1].strip("\n")
print len(icd9_words)

come_words = come_words.split("\r\n")
come_words[-1] = come_words[-1].strip("\n")

rad_words = rad_words.split("\n")
wjn_words = wjn_words.split("\n")
print len(rad_words)
print len(wjn_words)


"""
wjn_words = file('data/wjn_words_only.txt').read().splitlines()
rad_words = file('data/rad_words_only.txt').read().splitlines()
icd9_words = file('data/icd9_words_only.txt').read().splitlines()
come_words = file('data/come_words_only.txt').read().splitlines()
"""

wjn_words = word_shuffle(wjn_words)
rad_words = word_shuffle(rad_words)
icd9_words = word_shuffle(icd9_words)
come_words = word_shuffle(come_words)


def randomPatient():
	global vocab
	p_dict = {}
	#pat['index'] = randomString()
        tmp = ''
	pat_id = randomString()
        #時系列ごとに疾患が増えて行 -> MD commentの所に加えて行く
        for t in xrange(10):
		random_int = random.randint(1,10)
        	dig_code = randomText(random_int, icd9_words)
        	ana_pos = randomText(random_int, rad_words)
		tmp_Triage = dig_code + ana_pos + randomText(random_int, wjn_words)
                tmp += tmp_Triage
                t_dict = {}
		t_dict = { 
				"patient_id": pat_id,
				"ChiefComplaint" : dig_code,
				"TriageAssessment" : tmp_Triage,
				"MDcomments" : tmp + randomText(random_int, come_words),
				"Age" : str(np.random.choice(range(20,80))),
				"Sex" : np.random.choice(['M', 'F'])[0],
				"Time" : t
		}
		p_dict[t] = t_dict
                
        return p_dict

def generate_patients(n):
    for _ in xrange(n):
        pat = randomPatient()

    jsonstring = json.dumps(pat, ensure_ascii=False)
    return jsonstring

if __name__ == "__main__":

    try:
        n = int(sys.argv[1])
    except:
        print "usage: python generate_patients.py numPatients"
        sys.exit()

    pat_dics = {}
    for t in xrange(n):
        pat_dics[t] = randomPatient()


    jsonstring = json.dumps(pat_dics, ensure_ascii=False)

    f = codecs.open("tmp/json_time_series_patient.json","w","utf-8")
    #f = open("tmp/json_time_series_patient.json", "w")
    json.dump(pat_dics, f, ensure_ascii=False)

    
