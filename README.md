synfire_network
===============

a synfire network that performs auditory grouping

This project simulates a neural network that receives external inputs over time corresponding to auditory tones at different frequencies. When the third neuron in the chain fires, it indicates that a grouped sequence was detected. When it fails to go off, it means that the sequence was not detected. Human sequence detection is sensitive to the rate at which the tones are presented (too fast, and the tones are not grouped) and to the difference in frequency between the tones (too high, and the tones are not grouped). This network shows the same sensitivity.

In the graphs produced, the red lines represent the stimulus, the blue lines represent the neurons' membrane voltage, and the cyan lines represent the synaptic signals from the other neurons. The top graph is the first neuron, the middle is the second, and the bottom is the third neuron. If the blue line one the bottom graph goes above 0, it means the sequence was detected.
