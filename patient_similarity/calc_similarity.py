from scipy import linalg, mat, dot
import numpy as np
import in_out
import os, itertools
import time_detection

def cos_similarity(a, b):
	print "---Cosine Similarity between Patients---"
	return  dot(a,b.T)/linalg.norm(a)/linalg.norm(b)

def distance_similarity(mat_a, mat_b):
	print "---Distance between Patients---"
	return np.linalg.norm(mat_a-mat_b)

def show_all_similarity(ids, combs):
        i = 0
        for comb in combs:
                print "Patients %s = %s" % (ids[i], distance_similarity(comb[0], comb[1]))
                i += 1

def validate_timepoints(patients, p_labels):
	i = 0
	for patient in patients:
		print p_labels["%s"%i]["change_point"]
		if p_labels["%s"%i]["change_point"] == time_detection.detection(patient):
			print "Detect Sucess"
		else:
			print "Detect Failed"
		i += 1

def validate_all_similarity(ids, patients, p_labels):

	N_patients = len(p_labels)

	min_id_lists = []
	for n in xrange(N_patients):
		print 'Patient-%s' % n
		min_value = 10000
		min_id = 0
		for id in ids:
			if id[0] == n:
				print '%s is %s' % (id, distance_similarity(patients[id[0]], patients[id[1]]))
				if min_value > distance_similarity(patients[id[0]], patients[id[1]]):
					min_value = distance_similarity(patients[id[0]], patients[id[1]])
					min_id = id[1]
		min_id_lists.append(min_id)		
	
	#Validation of dictionary
	for p in xrange(len(p_labels)):
		if p_labels["%s"%p]["dictionary_id"] == min_id_lists[p]:
			print "Dictionary Unmathced"
		else:
			print "Dictionary Matached"


def similarity_patients(patients, p_labels):
	id = list(itertools.combinations([x for x in range(len(patients))],2))
	
	#show_all_similarity(id, combs)
	validate_all_similarity(id, patients, p_labels)
        



if __name__ == "__main__":
	patients_data_dir = 'dic_output'
	files = os.listdir(patients_data_dir)

	patients = []
	for file in files:
    		patients.append(in_out.load_vector("%s/%s"%(patients_data_dir, file)))



