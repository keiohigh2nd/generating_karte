#coding: UTF-8
import json 
import codecs
import collections
import calc_similarity
import in_out
import numpy as np
from sklearn.feature_extraction import DictVectorizer

def read_json(filename):
        #f = open('tmp/json_time_series_patient.json', 'r')
        f = open(filename, 'r')
        jsonData = json.load(f,"utf-8")
        text = json.dumps(jsonData)
        f.close()
        return text, jsonData

def preprocess(text):
	return	

def vectorization(text):
	texts = text.strip("\r")
	tmp = collections.Counter(texts)
	return tmp

def check_vectorization():
	sample = "a b c"
	sample1 = "a b c d"
	print vectorization(sample)
	print vectorization(sample1)

def file_open(file_name):
	f= codecs.open(file_name, "r", "utf-8")
	text = f.read()
	f.close()
	return text

def make_dictionary():
	file1 = "data/icd9_words_only.txt" 
	file2 = "data/rad_words_only.txt" 
	file3 = "data/come_words_only.txt" 
	file4 = "data/wjn_words_only.txt" 

	text1 = file_open(file1)
	text2 = file_open(file2)
	text3 = file_open(file3)
	text4 = file_open(file4)

	tmp_1 = text1.split("\r\n")
	tmp_1[-1] = tmp_1[-1].strip("\n")

	tmp_3 = text3.split("\r\n")
        tmp_3[-1] = tmp_3[-1].strip("\n")

	tmp_24 = text2 + text4
	tmp_24 = tmp_24.split("\n")
	del tmp_24[-1]

        return collections.Counter(tmp_1 + tmp_24 + tmp_3)

if __name__ == "__main__":
	#number of patients !!!
	N = 3
        file_name = 'make_dataset/sample/json_time_series_patient.json'

	dic_texts = make_dictionary()
        documents, p_json  = read_json(file_name)

	
	v_list = []
	for t in xrange(len(p_json)):	
		v_tmp = []
		for pat in xrange(len(p_json["%s"%t])):
			v_tmp = vectorization(p_json["%s"%t]["%s"%pat]["MDcomments"])
			v_list.append(v_tmp)

	v_list.append(dic_texts)
	v = DictVectorizer()
        dd = v.fit_transform(v_list).toarray()

	#delete dictionary vector 
	dd = np.delete(dd, -1, 0)

	#split per patient
	dd = np.vsplit(dd, N)


	i = 0
	for d in dd:
		print d.shape
		in_out.save_vector(d, "sample_patient-%s"%i)
		i += 1

	"""	
	for t in xrange(len(p_json)):
		print calc_similarity.cos_similarity(dd[t],dd[t+1])
	"""
		
