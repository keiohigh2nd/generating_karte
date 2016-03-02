from scipy import linalg, mat, dot
import in_out, make_dictionary, calc_similarity
import os


if __name__ == "__main__":

	#Get patients vetorization
	patients_data_dir = 'dic_output'
	files = os.listdir(patients_data_dir)
	patients = []
	for file in files:
    		patients.append(in_out.load_vector("%s/%s"%(patients_data_dir, file)))

	#Get Labels
	documents, p_labels = make_dictionary.read_json('make_dataset/sample/p_labels.json')

	#Calculation of Similarity
	#calc_similarity.similarity_patients(patients, p_labels)

	#Validate Timepint
	calc_similarity.validate_timepoints(patients, p_labels)

		
