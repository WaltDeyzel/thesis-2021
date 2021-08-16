
dp = dipole('Width',0.001, 'Length', 0.5);
rb = linearArray;
rb.Element = [dp,dp,dp,dp,dp,dp];

%rb.NumElements = 4; antennaDesigner
rb.ElementSpacing = 0.5;

d = 0.5;            % uniform seperation.
f = 3e8;      % operating frequency
lamda= 3e8/f; % wave length
steering = 0;      % desired angle
a = 360*d*sin(steering *pi/180)/lamda;
rb.PhaseShift = [a*6 a*5 a*4 a*3 a*2 a*1];
patternAzimuth(rb, f); % Amplitude in dB
