import numpy as np

def save_vector(v, name):
	np.save('dic_output/%s.npy' % name, v)
	#np.savetxt('%s.npy' % name, v, delimiter=',')

def load_vector(name):
	return np.load(name)
	#return np.loadtxt(name, delimiter=',')
