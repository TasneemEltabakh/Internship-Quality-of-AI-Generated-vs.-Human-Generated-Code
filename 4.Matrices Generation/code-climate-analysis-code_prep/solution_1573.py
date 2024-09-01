import numpy
data = numpy.asarray([ [10,20,30], [40,50,60], [70,80,90] ])
numpy.savetxt("test.csv", data, delimiter=",")
