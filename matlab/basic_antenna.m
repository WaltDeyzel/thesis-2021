
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
%patternAzimuth(rb, f) 
n = 10000000;
u = zeros(10, 1);
for i = 1:n
    r = rand;
    if r > 0 && r <= 0.1
        u(1) = u(1)+1;
    end
    if r > 0.1 && r <= 0.2
        u(2) = u(2)+1;
    end
    if r > 0.2 && r <= 0.3
        u(3) = u(3)+1;
    end
    if r > 0.3 && r <= 0.4
        u(4) = u(4)+1;
    end
    if r > 0.4 && r <= 0.5
        u(5) = u(5)+1;
    end
    if r > 0.5 && r <= 0.6
        u(6) = u(6)+1;
    end
    if r > 0.6 && r <= 0.7
        u(7) = u(7)+1;
    end
    if r > 0.7 && r <= 0.8
        u(8) = u(8)+1;
    end
    if r > 0.8 && r <= 0.9
        u(9) = u(9)+1;
    end
    if r > 0.9 && r <= 1
        u(10) = u(10)+1;
    end
end
figure
title('Distribution of rand function for ' + string(n) + ' samples.','FontSize', 18)
xlabel('Frequency bins','FontSize', 16) 
ylabel('Normalised frequency','FontSize', 16) 
grid on
hold on
bar(u/n)