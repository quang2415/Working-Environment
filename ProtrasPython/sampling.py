from read_dataset import read_dataset
from proTras import proTras

dsName = 'ecoli2.dat'
data = read_dataset(dsName)

proTras(data)