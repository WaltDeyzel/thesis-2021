
function [spacing,phase,amplitude] = readExcel(i)
    filename = 'graphs/graph.xlsx';
    sheet = 1;
    
    xlRange1 = 'A' +string(i)+':E'+string(i);
    xlRange2 = 'G' +string(i)+':L'+string(i);
    xlRange3 = 'N' +string(i)+':S'+string(i);
    
    spacing = xlsread(filename,sheet,xlRange1); 
    phase = xlsread(filename,sheet,xlRange2); 
    amplitude = xlsread(filename,sheet,xlRange3); 
end