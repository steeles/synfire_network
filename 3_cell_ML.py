# morris_lecar_simple
# from Scholarpedia
# sara steele, 7/20
# phi had to be repeated in both tauw and in dw, so maybe it should be phi^2

from pylab import *
from numpy import *
from matplotlib.mlab import *


#def morris_lecar():  #V,w,Iapp):
def minf(V): 
	M_ss =  .5*(1 + tanh((V-v1)/v2)); return M_ss

def winf(V): 
	w_inf = .5*(1 + tanh((V-v3)/v4)); return w_inf

def tauw(V): 
	tau_w = 1/(Phi*cosh((V-v3)/(2*v4))); return tau_w

v_k, v_l, v_ca = -84, -60, 120
g_k, g_l, g_ca = 8, 2, 4.4

v1,v2,v3,v4 = -1.2,18,2,30

Phi = .04
C = 20

dt,T = .1, 500
tax = arange(dt,T,dt)
I = 100

EPSC = 80
nUnits = 3
weights = array([[0, 0, 0],[1, 0, 0],[0, 1, 0]]) * EPSC
thresh = 0

V = zeros((nUnits,len(tax))); V[:,0] = -16
#V[1,0] = 50
W = zeros((nUnits,len(tax))); W[:,0] = .4#.014915
I_app = zeros((nUnits,len(tax)));



for t in xrange(len(tax)-1):
	Istim = array([I,0,0])
	I_app[:,t] = dot(weights,V[:,t] > thresh) + Istim

	dv = dt/C * (I_app[:,t] - g_ca * minf(V[:,t]) * (V[:,t]-v_ca) - g_k * 
		W[:,t] * (V[:,t]-v_k) - g_l*(V[:,t]-v_l) )
	dw =  dt *(winf(V[:,t]) - W[:,t]) /tauw(V[:,t])

	V[:,t+1] = V[:,t] + dv
	W[:,t+1] = W[:,t] + dw




	#return V,w,tax

#(V,w,tax) = morris_lecar()
fig = figure()
for ind in xrange(nUnits):
	ax=fig.add_subplot(nUnits,1,ind+1)
	ax.plot(tax,V[ind,:]); 
	ax.plot(tax,W[ind,:]);
	title(str(ind+1)) 

show(block=False)

