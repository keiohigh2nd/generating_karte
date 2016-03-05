#coding: utf-8
import os
import in_out
import numpy as np
import pickle
import json

def find_high_frequency(patients):
	row_sums = []
	for patient in patients:
		row_sums.append(np.sum(patient, axis=0))
	sums = np.sum(row_sums, axis=0)

	ids = []
	for x in xrange(7):
		tmp = np.argmax(sums)
		ids.append(tmp)
		sums[tmp] = 0
	return ids

def reference_dictionary(i):
	with open('tmp/dictionary_words.pickle', 'rb') as f:
		word_dict = pickle.load(f)
	return word_dict[i]

def dump_to_tree(words):
	js = {
 	"name": words[0],
 	"種類": [
  	{
   	"name": words[1],
   	"種類": [
    	{
     	"name": words[2],
     		"種類": [
      		{"name": words[3], "好き度": 10},
     		]
    	},
    	{
     	"name": words[4],
     	"種類": [
      		{"name": words[5], "好き度": 2},
      		{"name": words[6], "好き度": 10}
     		]
    	}
   	]
  	}
 	]
	}

	with open('view/tree_words.json', 'w') as f:
    		json.dump(js, f, ensure_ascii=True)

if __name__ == "__main__":

        #Get patients vetorization
        patients_data_dir = 'dic_output'
        files = os.listdir(patients_data_dir)
        patients = []
        for file in files:
                patients.append(in_out.load_vector("%s/%s"%(patients_data_dir, file)))

        print "Common words between Patients" 
        ids = find_high_frequency(patients)

	words = []
	for id in ids:
		words.append(reference_dictionary(id))
		print words
	dump_to_tree(words)
