

function data(filename, fittest_antenna)
    disp('fittest : ' + string(fittest_antenna.Fitness))
    disp(fittest_antenna.antennaArray.ElementSpacing)
    disp(fittest_antenna.antennaArray.PhaseShift)
    disp(fittest_antenna.antennaArray.AmplitudeTaper)
    
    fileID = fopen(filename,'a');
    fprintf(fileID, '%2.4f\n', fittest_antenna.Fitness);
    fprintf(fileID,'%1.4f %1.4f %1.4f %1.4f %1.4f\n', fittest_antenna.antennaArray.ElementSpacing);
    fprintf(fileID,'%3.1f %3.1f %3.1f %3.1f %3.1f %3.1f\n', fittest_antenna.antennaArray.PhaseShift);
    fprintf(fileID,'%1.4f %1.4f %1.4f %1.4f %1.4f %1.4f\n', fittest_antenna.antennaArray.AmplitudeTaper);
    fprintf(fileID, '%2.4f\n', 0);
    fclose(fileID);
end

