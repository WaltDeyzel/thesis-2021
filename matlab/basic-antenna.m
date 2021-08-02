rb = linearArray('NumElements',4);
%rb.NumElements = 4; antennaDesigner
rb.ElementSpacing = [1, 0.5, 1];

A = patternAzimuth(rb, 70e6); % Amplitude in dB
rb.PhaseShift = [45 90 0 30];

layout(rb);
pattern(rb, 70e6)
patternAzimuth(rb, 70e6) % 70 x 10 to the 6
patternElevation(rb, 70e6)

for a = 1:10
   patternAzimuth(rb, 70e6);
   rb.PhaseShift = [30 30*a 30*2*a 30*3*a];
   pause(5);
end
