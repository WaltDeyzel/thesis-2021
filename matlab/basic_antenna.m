
import Antenna.*

dp = dipole('Width',0.001, 'Length', 0.5);
rb = linearArray;
rb.Element = [dp,dp,dp,dp,dp,dp];

%rb.NumElements = 4; antennaDesigner
rb.ElementSpacing = 0.5;


d = 0.5;            % uniform seperation.
f = 300000000;      % operating frequency
lamda= 300000000/f; % wave length
steering = 30;      % desired angle
a = 360*d*sin(steering *pi/180)/lamda;
rb.PhaseShift = [a*6 a*5 a*4 a*3 a*2 a*1];
% 270 270*2 270*3 270*4 270*5 270*6]; %30 degrees

%A = patternAzimuth(rb, 70e6); % Amplitude in dB
%layout(rb);
%pattern(rb, 300e6)
patternAzimuth(rb, f) 


t = Antenna(rb,3e8, 0.5);

