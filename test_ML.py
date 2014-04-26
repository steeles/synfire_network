# test_ML

from pylab import *
from numpy import *
from matplotlib.mlab import *
import pdb

execfile('3_cell_stim_func.py')
execfile('stim_maker.py')

test_dfs = arange(3,12,2)
#test_Phis = logspace(.001,.02,5)
#test_Phis = test_Phis[1:]
test_Phis = array([.0021])#, .0022])

test_ITIs = linspace(30,130,5)

detect_map = zeros((len(test_dfs),len(test_Phis)))
suppress_map = zeros((len(test_dfs),len(test_Phis)))


dind = 0 #p = 0;
#Vresult = zeros((3,5999,len(test_ITIs)))
Phi = 0

for dind in xrange(len(test_dfs)):

	for pind in xrange(len(test_Phis)):
		
		Phi = test_Phis[pind]

		b_sDetect = False
		b_sSuppress = False

		for ind in xrange(len(test_ITIs)):
			[tax,V,W,Isyn,stim] = morris_lecar(
				Phi,test_ITIs[-ind-1],test_dfs[dind])
				#Vresult[:,:,ind] = V

			# I would like an easy way to test that changing phis doesn't
			#get me spurious stim firing, but i'm lazy right now. 
			#later i can update fxn to eliminate ff weights

			if any(V[2,:]>0) & ~b_sDetect:
				detect_map[dind,pind] = test_ITIs[-ind-1]
				b_sDetect = True

			if ~any(V[2,:]>0) & b_sDetect & ~b_sSuppress:
				suppress_map[dind,pind] = test_ITIs[-ind-1]
				b_sSuppress = True


np.set_printoptions(precision=2)
figure()
title('TRT of first detected sequence')
imshow(detect_map,interpolation='nearest',
	extent=[test_Phis[0],test_Phis[-1],test_dfs[0],
	test_dfs[-1]],cmap='gray')
xscale('log')
xlabel('Phi')
ylabel('df')
colorbar()
xticks(test_Phis,test_Phis)
show(block=False)


figure()
title('TRT of first suppressed sequence')
imshow(suppress_map,interpolation='nearest',
	extent=[test_Phis[0],test_Phis[-1],test_dfs[0],
	test_dfs[-1]],cmap='gray')
xscale('log')
xlabel('Phi')
ylabel('df')
colorbar()
xticks(test_Phis,test_Phis)
show(block=False)

	#pdb.set_trace()




