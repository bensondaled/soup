import numpy 
import numpy as np

def mode(inputData, axis=None, dtype=None):
	"""
	Robust estimator of the mode of a data set using the half-sample mode.
	
	.. versionadded: 1.0.3
	"""
	
	if axis is not None:
		fnc = lambda x: mode(x, dtype=dtype)
		dataMode = numpy.apply_along_axis(fnc, axis, inputData)
	else:
		# Create the function that we can use for the half-sample mode
		def _hsm(data):
			if data.size == 1:
				return data[0]
			elif data.size == 2:
				return data.mean()
			elif data.size == 3:
				i1 = data[1] - data[0]
				i2 = data[2] - data[1]
				if i1 < i2:
					return data[:2].mean()
				elif i2 > i1:
					return data[1:].mean()
				else:
					return data[1]
			else:
				wMin = data[-1] - data[0]
				N = int(data.size/2 + data.size%2 )
				for i in range(0, N):
					w = data[i+N-1] - data[i] 
					if w < wMin:
						wMin = w
						j = i
				return _hsm(data[j:j+N])
				
		data = inputData.ravel()
		if type(data).__name__ == "MaskedArray":
			data = data.compressed()
		if dtype is not None:
			data = data.astype(dtype)
			
		# The data need to be sorted for this to work
		data = numpy.sort(data)
		
		# Find the mode
		dataMode = _hsm(data)
		
	return dataMode

def cohens_d(x,y):
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    return (np.mean(x) - np.mean(y)) / np.sqrt(((nx-1)*np.std(x, ddof=1) ** 2 + (ny-1)*np.std(y, ddof=1) ** 2) / dof)
