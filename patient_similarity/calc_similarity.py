from scipy import linalg, mat, dot
import in_out
import os

def cos_similarity(a, b):
	return  dot(a,b.T)/linalg.norm(a)/linalg.norm(b)

def similarity_patients(patients, p_json):
	for patient_x in patients:
		for patient_y in patients:
			cos_similatiry(patient_x, patient_y)

if __name__ == "__main__":
	patients_data_dir = 'dic_output'
	files = os.listdir(patients_data_dir)

	patients = []
	for file in files:
    		patients.append(in_out.load_vector("%s/%s"%(patients_data_dir, file)))



	print patients[0][0]
	print patients[1][0]
	print cos_similarity(patients[0][0], patients[1][0])
	print cos_similarity(patients[0][0], patients[0][1])
