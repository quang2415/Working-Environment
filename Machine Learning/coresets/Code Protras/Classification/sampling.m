clear
close all
mkdir(date);
disp('Change datasets name in the line below, auto version is comming soon...');
dsName  = 'ecoli2.dat';
data = read_dataset(dsName);
[Ty,T,S] = proTraS(data);
