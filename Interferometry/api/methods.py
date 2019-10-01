"""
This file is the main API to use Interferometry without the UI.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt 

sys.path.append('..')

from core.evaluate import min_max_method, cff_method, fft_method, cut_gaussian, gaussian_window , ifft_method, spp_method, args_comp
from core.edit_features import savgol, find_peak, convolution, cut_data, find_closest
from core.generator import generatorFreq, generatorWave
# from core.cff_fitting import FitOptimizer, cos_fit1, cos_fit2, cos_fit3, cos_fit5, cos_fit4


class DatasetError(Exception):
	pass


class Generator(object):
	def __init__(self, start, stop, center, delay=0, GD=0, GDD=0, TOD=0, FOD=0, QOD=0, resolution=0.1, delimiter=',',
		         pulseWidth=10, includeArms=False):
		self.start = start
		self.stop = stop
		self.center = center
		self.delay = delay
		self.GD = GD
		self.GDD = GDD
		self.TOD = TOD
		self.FOD = FOD
		self.QOD = QOD
		self.resolution = resolution
		self.delimiter = delimiter
		self.pulseWidth = pulseWidth
		self.includeArms = includeArms
		self.x = np.array([])
		self.y = np.array([])
		self.ref = np.array([])
		self.sam = np.array([])

	def generate_freq(self):
		self.x, self.y, self.ref, self.sam = generatorFreq(self.start, self.stop, self.center, self.delay, self.GD,
															    self.GDD, self.TOD, self.FOD, self.QOD,
						   										self.resolution, self.delimiter, self.pulseWidth, self.includeArms)
		if len(self.ref) != 0:
			self.y =  (self.y - self.ref - self.sam)/(2*np.sqrt(self.sam*self.ref))


	def generate_wave(self):
		self.x, self.y, self.ref, self.sam = generatorWave(self.start, self.stop, self.center, self.delay, self.GD,
															    self.GDD, self.TOD, self.FOD, self.QOD,
						   										self.resolution, self.delimiter, self.pulseWidth, self.includeArms)
		if len(self.ref) != 0:
			self.y =  (self.y - self.ref - self.sam)/(2*np.sqrt(self.sam*self.ref))
			
	def show(self):
		plt.figure()
		plt.plot(self.x, self.y, 'r')
		plt.grid()
		plt.show()

	def save(self, name, path=None):
		if path == None:
			np.savetxt('{}.txt'.format(name), np.transpose([self.x, self.y, self.ref, self.sam]))
		else:
			np.savetxt('{}/{}.txt'.format(path, name), np.transpose([self.x, self.y, self.ref, self.sam]))


class Dataset(object):
	def __init__(self, x, y, ref=None, sam=None):
		self.x = x
		self.y = y
		if self.ref is None:
			self.ref = []
		else:
			self.ref = ref
		if self.sam is None:
			self.sam = []
		else:
			self.sam = sam
		self._is_normalized = False
		if not isinstance(self.x, np.ndarray):
			try:
				self.x = np.array(self.x)
				self.x.astype(float)
			except:
				raise DatasetError
		if not isinstance(self.y, np.ndarray):
			try:
				self.y = np.array(self.y)
				self.y.astype(float)
			except:
				raise DatasetError
		if not isinstance(self.ref, np.ndarray):
			try:
				self.ref = np.array(self.ref)
				self.ref.astype(float)
			except:
				pass
		if not isinstance(self.sam, np.ndarray):
			try:
				self.sam = np.array(self.sam)
				self.sam.astype(float)
			except:
				pass
		if len(self.ref) == 0:
			self.y_norm = self.y
		else:
			self.y_norm = (self.y - self.ref - self.sam)/(2*np.sqrt(self.sam*self.ref))
			self._is_normalized = True

	
	def __str__(self):
		string = "{}, {}, {}, {}\n{}, {}, {}, {}".format(self.x[0], self.y[0], self.ref[0], self.sam[0], self.x[1], self.y[1], self.ref[1], self.sam[1])
		return string

	@property
	def is_normalized(self):
		return self._is_normalized
	
	def savgol_fil(self, window=101, order=3):
		self.x, self.y_norm = savgol(self.x, self.y, self.ref, self.sam, window = window, order = order)
		self.ref = []
		self.sam = []

	def cut(self):
		pass

	def convolution(self):
		pass

	def detect_peak(self):
		pass

	def show(self):
		plt.figure()
		plt.plot(self.x, self.y_norm)
		plt.grid()
		plt.show()


class MinMaxMethod(Dataset):
	def __init__(self, reference_point, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.xmin = []
		self.xmax = []
		self.reference_point = reference_point


	def calculate(self, fit_order, show_graph = False):
		dispersion, dispersion_std, fit_report = min_max_method(
			self.x, self.y, self.ref, self.sam, ref_point = self.reference_point,
			maxx = self.xmax, minx = self.xmin, fitOrder = fit_order, showGraph = show_graph
			)
		return dispersion, dispersion_std, fit_report


class CosFitMethod(Dataset):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class SPPMethod(Dataset):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class FFTMethod(Dataset):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#making sure it's not normalized
		if self._is_normalized:
			self.y_norm = self.y
			self._is_normalized = False
		


