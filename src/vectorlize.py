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

if __name__ == "__main__":
        count, index = load_sample()
	"""
	p_text, p_json = read_json("make_dataset/small/small_json_time_series_patient.json")
	collection = collections.Counter(p_text)
        #Unidentified two spaces
        tmp = p_json["0"]["3"]["Plan"].split("  ")
	collection = collections.Counter(tmp)

        from sklearn.feature_extraction import DictVectorizer
	v = DictVectorizer()
	#print v.fit_transform(collection)
        #print collection


        #Shuffle
	#print tmp
        old_tmp = tmp  #dictionary
        random.shuffle(tmp)
        #print tmp

	from sklearn.feature_extraction import DictVectorizer
        v = DictVectorizer()
        print v.fit_transform(collection)

        #Prepare s_matrix
        M = len(collection)
        s_matrix = np.zeros((M, M)) 

        for i in xrange(len(tmp)):
            j = return_index(tmp[i], old_tmp)
            if i > 0:
              m1 = return_index(tmp[i], old_tmp)
              s_matrix[j][m1] += 1
            if i < len(tmp):
	      m2 = return_index(tmp[i], old_tmp)
              s_matrix[j][m2] += 1
              
        print s_matrix 
	"""
