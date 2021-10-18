
import readExcel.*
import uniformLinearArray.*
import grpahNormdB.*
dp = dipole('Width',0.001, 'Length', 0.5);

steer = 90-37;
rb = uniformLinearArray(0.5, steer);
Adb = patternAzimuth(rb, 3e8);
Adb_180 = Adb(1:180);
m_180 = 10.^(Adb_180/20);

% non-uniform

rb2 = linearArray;
rb2.Element = [dp,dp,dp,dp,dp,dp];
gcf = figure;
hold on
plot(flip(Adb_180 - max(Adb)),'LineWidth',1) %
for i = 1:3
[a, b, c] = readExcel(i);
rb2.ElementSpacing = a;
rb2.PhaseShift = b;
rb2.AmplitudeTaper = c;

hold on
%axis([0 180 -30 0])
Adb2 = patternAzimuth(rb2, 3e8);
Adb2_180 = Adb2(1:180) ;
A = 10.^(Adb_180/20);
A2 = 10.^(Adb2_180/20);
disp('HERE Directivity')
disp(A(180-(90-steer))/mean(A))
%disp(A2(180-(90-steer))/mean(A2))
disp('DONE')
%pattern(rb, 3e8, 0:1:180, -100:1:100,  'Normalize', true);

%pattern(rb, 3e8, 'Type', 'efield', 'Normalize', true);
%pattern(rb, [50e6:10e6:500e6], 0, 1:1:360, 'PlotStyle', 'waterfall','CoordinateSystem', 'rectangular');
plot(flip(Adb2_180 - max(Adb2)),'LineWidth',1)%

%patternAzimuth(rb2, 3e8, 0, 'Azimuth',0:1:180)
%saveas(gcf,'graphs/images/pol' + string(steer)+'deg_'+string(i)'+'.jpg')
%saveas(gcf,'graphs/images/pol' + string(steer)+'deg_'+string(i)'+'.emf')

end
%set(gcf, 'Position',  [100, 100, 600, 300])
%title('Beam steered : ' + string(90-33) +' ^\circ','FontSize', 18)

xlabel('Degrees','FontSize', 16) 
ylabel('Amplitude Normalized (dB)','FontSize', 16) 
%legend({'Uniform','s1', 's2','s3'},'Location','southwest','FontSize', 14)
grid off

%saveas(gcf,'../plots/SLA' + string(steer)+'deg'+'.jpg')
%saveas(gcf,'../plots/SLA' + string(steer)+'deg'+'.emf')
%saveas(gcf,'../plots/SLA' + string(steer)+'deg'+'.fig')