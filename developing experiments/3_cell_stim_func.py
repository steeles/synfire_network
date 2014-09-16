# 3_cell_ML_stimT
# from Scholarpedia with adjustments
# sara steele, 7/20
# phi had to be repeated in both tauw and in dw, so maybe it should be phi^2

from pylab import *
from numpy import *
from matplotlib.mlab import *


def morris_lecar(Phi,ITI,df):  #V,w,Iapp):
	def minf(V): 
		M_ss =  .5*(1 + tanh((V-v1)/v2)); return M_ss

	def winf(V): 
		w_inf = .5*(1 + tanh((V-v3)/v4)); return w_inf

	def tauw(V): 
		tau_w = 1/(Phi*cosh((V-v3)/(2*v4))); return tau_w

	v_k, v_l, v_ca = -84, -60, 120
	g_k, g_l, g_ca = 8, 2, 4.4

	v1,v2,v3,v4 = -1.2,18,2,30

	#Phi = .004
	C = 20

	dt,T = .1, 600
	tax = arange(dt,T,dt)
	Istim = 60

	EPSC = 40
	nUnits = 3
	weights = array([[0, 0, 0],[1, 0, 0],[-2, 1, 0]]) * EPSC
	thresh = -20

	V = zeros((nUnits,len(tax))); V[:,0] = -60
	#V[1,0] = 50
	W = zeros((nUnits,len(tax))); W[:,0] = .014915
	I_app = zeros((nUnits,len(tax)))
	Isyn = zeros((nUnits,len(tax)))

	execfile('stim_maker.py')

	
	stim = stim_maker(T,dt,nUnits,ITI,df) * Istim 
	noise = np.random.normal(0,1,stim.shape)
	stim = stim + noise
	
	exc_gain_n1 = array([1.3,1,1])


	for t in xrange(len(tax)-1):
		
		Isyn[:,t] = dot(weights,V[:,t] > thresh)
		I_app[:,t] = Isyn[:,t] + stim[:,t] * exc_gain_n1

		dv = dt/C * (I_app[:,t] - g_ca * minf(V[:,t]) * (V[:,t]-v_ca) - g_k * 
			W[:,t] * (V[:,t]-v_k) - g_l*(V[:,t]-v_l) )
		dw =  dt *(winf(V[:,t]) - W[:,t]) /tauw(V[:,t])

		V[:,t+1] = V[:,t] + dv
		W[:,t+1] = W[:,t] + dw

	fig = figure()
	title('ITI = ' + str(ITI) + ', Phi = ' + str(Phi) + ', df = ' + str(df))
	for ind in xrange(nUnits):
		ax=fig.add_subplot(nUnits,1,ind+1)
		ax.plot(tax,V[ind,:],'b'); 
		#ax.plot(tax,W[ind,:]* EPSC) ;
		ax.plot(tax,Isyn[ind,:],'c')
		ax.plot(tax,stim[ind,:],'r')
		#title(str(ind+1)) 

	show(block=False)
	if 0:
		fname = './figures/Phi_%d_df_%d_ITI_%d' %(Phi*1000,df,ITI)
		fig.savefig(fname)

	return tax,V,W,Isyn,stim

