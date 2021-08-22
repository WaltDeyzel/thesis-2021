
import Antenna.*

dp = dipole('Width',0.001, 'Length', 0.5);
rb = linearArray;
rb.Element = [dp,dp,dp,dp,dp,dp];

%rb.NumElements = 4; antennaDesigner
rb.ElementSpacing = 0.5;
t = tiledlayout(3,6);

%for q = -10:9
  
    disp('start')
    d = 0.5;            % uniform seperation.
    f = 300000000;      % operating frequency
    lamda= 300000000/f; % wave length
    steering = 0;      % desired angle
    a = 360*d*sin(steering *pi/180)/lamda;
    rb.PhaseShift = [a*6 a*5 a*4 a*3 a*2 a*1];
    rb.AmplitudeTaper = [1 1 1 1 1 1];
    % 270 270*2 270*3 270*4 270*5 270*6]; %30 degrees

    Adb = patternAzimuth(rb, f); % Amplitude in dB
    Adb_180 = Adb(181:361)';

    fit = zeros(180,1);
    scores = zeros(20,1);
    fitt = 0;
    target = 90;
   
    for i = 1:180
        M = 10^(Adb_180(i)/20);
        %if i >= target
        %    fit(i) = M*cos(deg2rad(i - target));
        %    fitt = fitt + (M*sin(deg2rad((i - target)*1.5)))^2;
        %end
        
        %if i < target
        %    fit(i) = M*cos(deg2rad(target - i));
        %    fitt = fitt + (M*sin(deg2rad((target - i)*1.5)))^2;
        %end
        %fit(i) = (M*(1-abs(target-i)/(target)))^2 - (M*(abs(target-i)/(target)))^2;
        %fit(i) = M*(cos(abs(target-i)*pi/180)- sin(abs(target-i)*pi/180));
        %fit(i) = (M*(1-abs(target-i)/(100)))^1 - (M*(1+abs(i-target)/(100)))^1;
        %fit(i) = M*exp(-abs(target-i));
        %fit(i) = M*exp(-0.5*abs(target-i)) - (M*exp(0.015*abs(target-i) + M));
    end
    plot(fit)
    %patternAzimuth(rb, f); % Amplitude in dB
    %plot(Adb)
    %title([q * 10, sum(fit)])
    nexttile
 %end

%Adb_180 = [z Adb_180];
%polarplot(theta, Adb_180');
%layout(rb);
 %pattern(rb, 300e6)
patternAzimuth(rb, f) 
