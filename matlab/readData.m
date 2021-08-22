
filename = 'test.txt';

y = readData2(filename);

function y = readData2(filename)
    
    fileID = fopen(filename,'r');
    a = 'a';
    while ischar(char(a))
        disp('gos')
    a = fscanf(fileID, '%f', 1);
    b = fscanf(fileID,'%f', 5);
    c = fscanf(fileID,'%f', 6);
    d = fscanf(fileID,'%f', 6);
    e = fscanf(fileID, '%f', 1);
    end
    fclose(fileID);
    y = a;
end