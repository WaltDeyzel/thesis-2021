
%m = monopole('Height', 0.001);
%m.GroundPlaneLength = 0.001;
%m.GroundPlaneWidth = 0.001;
%m.Width = 0.0001;
d = dipole('Width',0.001);
d.Length = 0.5;
rb = linearArray;
rb.Element = [d,d,d,d,d,d];

%rb.NumElements = 4; antennaDesigner
rb.ElementSpacing = 0.5;

%A = patternAzimuth(rb, 70e6); % Amplitude in dB
d = 0.5;            % uniform seperation.
f = 300000000;      % operating frequency
lamda= 300000000/f; % wave length
steering = 60;      % desired angle
a = 360*d*sin(steering *pi/180)/lamda;
rb.PhaseShift = [a*6 a*5 a*4 a*3 a*2 a*1];
% 270 270*2 270*3 270*4 270*5 270*6]; %30 degrees

%layout(rb);
%pattern(rb, 300e6)
patternAzimuth(rb, f) % 70 x 10 to the 6

