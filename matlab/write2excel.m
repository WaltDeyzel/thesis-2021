% Write data to exel spreadsheet.

function write2excel(filename, fittest_antenna, generation) 
 
xlswrite(filename, fittest_antenna.antennaArray.ElementSpacing  , 'Sheet1', string(generation));
xlswrite(filename, fittest_antenna.antennaArray.PhaseShift      , 'Sheet2', string(generation));
xlswrite(filename, fittest_antenna.antennaArray.AmplitudeTaper  , 'Sheet3', string(generation));
xlswrite(filename, fittest_antenna.HPBW(90)                     , 'Sheet4', string(generation));
xlswrite(filename, fittest_antenna.Fitness                      , 'Sheet5', string(generation));

end