# stim_maker

from pylab import *
from numpy import *
from matplotlib.mlab import *
import pdb

def stim_maker(T,dt,nUnits,ITI,df):

	tone_length = 30
	#exc_gain = 300
	tax = arange(0,T,dt) # ms 
	fq_axis = 440 * (2.**(1/12.))**arange(-12,13)
	tuning_curve = normpdf(linspace(-7,7,len(fq_axis)),0,3)
	tuning_curve/= max(tuning_curve) # rescale to equal 1
	tone_length = tone_length/dt
	#df = 5
	TRT = ITI/dt
	stim = zeros((nUnits,len(tax)-1))


	A_ind = 12; B_ind = A_ind - df
	#pdb.set_trace()
	stim[0,:tone_length] = tuning_curve[A_ind]
	stim[1,TRT:TRT+tone_length] = tuning_curve[B_ind]
	stim[2,2*TRT:2*TRT+tone_length] = tuning_curve[A_ind]

	# trip_activation = zeros(ITI*4)
	# trip_activation[:tone_length] = tuning_curve[A_ind]
	# trip_activation[ITI:ITI+tone_length] = tuning_curve[B_ind]
	# trip_activation[2*ITI:2*ITI+tone_length] = tuning_curve[A_ind]

	return stim