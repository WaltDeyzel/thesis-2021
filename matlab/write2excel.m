% Write data to exel spreadsheet.

function write2excel(filename, fittest_antenna, generation, target, pop_norm) 
import hpbw.* 
xlswrite(filename, fittest_antenna.antennaArray.ElementSpacing  , 'Spacing', string(generation));
xlswrite(filename, fittest_antenna.antennaArray.PhaseShift      , 'Phase',   string(generation));
xlswrite(filename, fittest_antenna.antennaArray.AmplitudeTaper  , 'Amplitude', string(generation));
xlswrite(filename, hpbw(fittest_antenna.antennaArray)           , 'HPBW', string(generation));
xlswrite(filename, fittest_antenna.gain                         , 'Gain',  string(generation));
xlswrite(filename, fittest_antenna.Fitness                      , 'Fitness', string(generation));
xlswrite(filename, pop_norm                                     , 'Pop fit', string(generation));

end