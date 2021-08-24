% Radiation pattern for antenna array

dp = dipole('Width',0.001, 'Length', 0.5);
rb = linearArray;
rb.Element = [dp,dp,dp,dp,dp,dp];

rb.ElementSpacing = 0.7;

d = 0.5;            % uniform seperation.
f = 3e8;      % operating frequency
lamda= 3e8/f; % wave length
steering = 30;      % desired angle
a = 360*d*sin(steering *pi/180)/lamda;
rb.PhaseShift = [a*6 a*5 a*4 a*3 a*2 a*1];

Adb = patternAzimuth(rb, 3e8);
Adb_180 = flip(Adb(1:180));
m_180 = 10.^(Adb_180/20);

% non-uniform

rb2 = linearArray;
rb2.Element = [dp,dp,dp,dp,dp,dp];

rb2.ElementSpacing = [0.6683    0.7595    0.6592    0.7595    0.6683];
rb2.PhaseShift = [142.1451  177.0818  142.9742  160.0963  189.7535  187.3016];
rb2.AmplitudeTaper = [3.1677    6.3839    6.1488    4.9763    6.8816    4.8793];

Adb2 = patternAzimuth(rb2, 3e8);

rb3 = linearArray;
rb3.Element = [dp,dp,dp,dp,dp,dp];

rb3.ElementSpacing = [0.4863    0.4610    0.5675    0.4610    0.4863];
rb3.PhaseShift = [184  136  172  172  136  184];
rb3.AmplitudeTaper = [1    1    1    1   1    1];

Adb3 = patternAzimuth(rb3, 3e8);

theta = linspace(0,pi,180);
rho = (Adb_180/max(Adb));
figure 
hold on
plot(Adb/max(Adb))
%plot(Adb2/max(Adb2))
%plot(Adb3/max(Adb3))

%figure 
%polarplot(theta,rho) 
%rlim([-10,2])
