from scipy import linalg, mat, dot
import in_out, make_dictionary, calc
import os


if __name__ == "__main__":

	#Get patients vetorization
	patients_data_dir = 'dic_output'
	files = os.listdir(patients_data_dir)
	patients = []
	for file in files:
    		patients.append(in_out.load_vector("%s/%s"%(patients_data_dir, file)))

	#Get Labels
	documents, p_json = make_dictionary.read_json('make_dataset/sample/p_labels.json')
	print p_json["1"]

	#Calculation of Similarity
	calc.similarity_patients(patients, p_json)

	
