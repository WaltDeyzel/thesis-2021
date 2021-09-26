
import readExcel.*
import uniformLinearArray.*
import grpahNormdB.*
dp = dipole('Width',0.001, 'Length', 0.5);

steer = 90-24;
rb = uniformLinearArray(0.5, steer);
Adb = patternAzimuth(rb, 3e8);
Adb_180 = Adb(1:180);
m_180 = 10.^(Adb_180/20);

% non-uniform

rb2 = linearArray;
rb2.Element = [dp,dp,dp,dp,dp,dp];

i = 3;
[a, b, c] = readExcel(1);
rb2.ElementSpacing = a;
rb2.PhaseShift = b;
rb2.AmplitudeTaper = c;
gcf = figure;
hold on
Adb2 = patternAzimuth(rb2, 3e8);
Adb2_180 = Adb2(1:180) ;


plot(flip(Adb_180 - max(Adb)),'LineWidth',1)
plot(flip(Adb2_180 - max(Adb2)),'LineWidth',1)

title('GA vs Beam steered ' + string(steer) + '^{\circ}','FontSize', 18)
xlabel('Degrees','FontSize', 16) 
ylabel('Amplitude Normalized (dB)','FontSize', 16) 
legend({'Uniform','GA'},'FontSize', 14)
grid on
%saveas(gcf,'graphs/images/plot' + string(steer)+'deg_'+string(i)'+'.jpg')
%saveas(gcf,'graphs/images/plot' + string(steer)+'deg_'+string(i)'+'.emf')
%warning('off')
%gcf = figure;

%patternAzimuth(rb2, 3e8, 0, 'Azimuth',0:1:180)
%saveas(gcf,'graphs/images/pol' + string(steer)+'deg_'+string(i)'+'.jpg')
%saveas(gcf,'graphs/images/pol' + string(steer)+'deg_'+string(i)'+'.emf')
    

 
