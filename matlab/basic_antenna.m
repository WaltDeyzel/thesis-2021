
import Antenna.*

dp = dipole('Width',0.001, 'Length', 0.5);
rb = linearArray;
rb.Element = [dp,dp,dp,dp,dp,dp];

%rb.NumElements = 4; antennaDesigner
rb.ElementSpacing = 0.5;
t = tiledlayout(3,6);
for q = -10:9
    disp('start')
    disp(q)
    d = 0.5;            % uniform seperation.
    f = 300000000;      % operating frequency
    lamda= 300000000/f; % wave length
    steering = q*10;      % desired angle
    a = 360*d*sin(steering *pi/180)/lamda;
    rb.PhaseShift = [a*6 a*5 a*4 a*3 a*2 a*1];
    rb.AmplitudeTaper = [1 1 1 1 1 1];
    % 270 270*2 270*3 270*4 270*5 270*6]; %30 degrees

    Adb = patternAzimuth(rb, f); % Amplitude in dB
    Adb_180 = Adb(181:361)';

    fit = zeros(180,1);
    fitt = 0;
    target = 30;
    for i = 1:180
        M = 10^(Adb_180(i)/20);
        if i >= target
            fit(i) = (M*cos(pi*abs(180-i - target)/180));
            fitt = fitt + (M*sin(pi*abs(i - target)/180))^2;
        end
        if target > i 
            fit(i) = (M*cos(pi*abs(target - 180-i)/180));
            fitt = fitt + (M*sin(pi*abs(target - i)/180))^2;
        end
    end
    plot(fit)
    title([q * 10, var(fit), fitt])
    nexttile
  end

%Adb_180 = [z Adb_180];
%polarplot(theta, Adb_180');
%layout(rb);
 %pattern(rb, 300e6)
%patternAzimuth(rb, f) 
