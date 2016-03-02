import os
import in_out
import numpy as np
 
def detection(patient):
	max_value = 0
	time_stamp = 0
	for t in xrange(len(patient)):
		try:
			tmp = patient[t+1]-patient[t]
		except:
			continue
		sum_tmp = np.sum(np.fabs(tmp))
		if int(max_value) < int(sum_tmp):
			max_value = sum_tmp
			time_stamp = t

	print "The change point is %s" % (time_stamp + 1)
	return time_stamp

if __name__ == "__main__":

        #Get patients vetorization
        patients_data_dir = 'dic_output'
        files = os.listdir(patients_data_dir)
        patients = []
        for file in files:
                patients.append(in_out.load_vector("%s/%s"%(patients_data_dir, file)))
	
	print "Number of Patients = %s" % len(patients)
	for patient in xrange(patients):
		detection(patient)
	
