# -*- coding: utf-8 -*-
import json, random
import detection
import collections
import numpy as np

def read_json(filename):
        f = open(filename, 'r')
        jsonData = json.load(f,"utf-8")
        text = json.dumps(jsonData)
        f.close()
        return text, jsonData

def get_index(word, index):
        i = 0
	for w in index:
          if w == word:
            return i
          i += 1

def dictionarize_text(arr):
	#Need preprocessing of texts
        cl = collections.Counter(arr)
	from sklearn.feature_extraction import DictVectorizer
	v = DictVectorizer()
	count = v.fit_transform(cl)
        index = v.get_feature_names()
        return count, index

def get_cov(text, index):
	s_matrix = np.zeros((len(index), len(index)))
	for i_tex in xrange(len(text)):
          i = get_index(text[i_tex], index)
          if i_tex > 0:
              m1 = get_index(text[i_tex-1], index)
              s_matrix[i][m1] += 1
          if i_tex < len(text)-1:
              m2 = get_index(text[i_tex+1], index)
              s_matrix[i][m2] += 1
        return s_matrix


def load_sample():
        c = ['a', 'b', 'a', 'd', 'a']
        count, index = dictionarize_text(c)
	sm = get_cov(c, index)
        print c
        print sm
        return count, index

def find_similar_patients(matrix, N):
        import itertools
        combs = itertools.combinations(np.arange(N),2)
        min_val = 1000
        min_comb = [1,2]
        for comb in combs:
                tmp = matrix[comb[0]]-matrix[comb[1]]
                tmp = tmp*tmp
                tmp_all = tmp.sum()
                print "%s -- %s"%(comb, tmp_all)
                if min_val > tmp_all:
                        min_val = tmp_all
                        min_comb = comb
        return min_comb


def find_similar_patients_topic(matrix, N, topic_index):
	import itertools
	combs = itertools.combinations(np.arange(N),2)
	min_val = 1000
	min_comb = [1,2]
        for comb in combs:
		tmp = matrix[comb[0]]-matrix[comb[1]]
		tmp = tmp[topic_index,:]*tmp[topic_index,:]
		tmp_all = tmp.sum()
		print "%s -- %s"%(comb, tmp_all)
		if min_val > tmp_all:
			min_val = tmp_all
			min_comb = comb
	return min_comb		
	
def find_similar_label(arr):
	Num = len(arr)
	import itertools,math
        combs = itertools.combinations(np.arange(Num),2)
	min_val = 1000
	min_comb = [1,2]
	for comb in combs:
		tmp = math.fabs(arr[comb[0]]-arr[comb[1]])
		print "%s -- %s"%(comb, tmp)
		if min_val > tmp:
			min_val = tmp
			min_comb = comb
	return min_comb

if __name__ == "__main__":
        #count, index = load_sample()

	p_text, p_json = read_json("output/one_json_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)

	sm_patients = []
        order_labels = []

	#Making dictinary
	dic_arr = []
	for t in xrange(num_patients):
		#print str(t) + "----" + p_json["%s"%t]["0"]["A/P"]
		tmp = p_json["%s"%t]["0"]["A/P"].split(" ")
		tmp_cl = collections.Counter(tmp)
		dic_arr.append(tmp_cl)

	from sklearn.feature_extraction import DictVectorizer
	v = DictVectorizer()
	count = v.fit_transform(dic_arr)
	index = v.get_feature_names()

	#When writing json, you have to care "0" and "t"
        topic = p_json["0"]["0"]["A/P"].split(" ")
	topic_index = index.index(topic[0])
	#ここでの問題はトピックで索引しているのに、行列の引き算はすべての計算でやっているところ
	for t in xrange(num_patients):
        	texts = p_json["%s"%t]["0"]["A/P"].split(" ")
        	order_label = texts.index(topic)
		#count_m, index = dictionarize_text(texts)
		#Generate Matrix
		sm = get_cov(texts, index)
		sm_patients.append(sm)
		order_labels.append(order_label)

	###次元がsm行列のそれぞれ違う。それを揃える必要がある。
	print find_similar_patients_topic(sm_patients, num_patients, topic_index)
	print find_similar_label(order_labels)	
