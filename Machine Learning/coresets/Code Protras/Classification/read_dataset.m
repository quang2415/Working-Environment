function [Data] = read_dataset(dsName)
    datasetPath = 'Datasets/imb_IRlowerThan9/';
    fullPath = [datasetPath,dsName];
    disp('fullpath dataset:');
    disp(fullPath);
    T  = readtable(fullPath);
    
    Data = table2array(T(:,1:end-1));
end