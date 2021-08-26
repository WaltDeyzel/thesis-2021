
import readExcel.*
import uniformLinearArray.*
dp = dipole('Width',0.001, 'Length', 0.5);


rb = uniformLinearArray(0.5, 45);
Adb = patternAzimuth(rb, 3e8);
Adb_180 = Adb(1:180);
m_180 = 10.^(Adb_180/20);

% non-uniform

rb2 = linearArray;
rb2.Element = [dp,dp,dp,dp,dp,dp];


steer = 45;


for i = 1:1
    [a, b, c] = readExcel(1);
    rb2.ElementSpacing = a;
    rb2.PhaseShift = b;
    rb2.AmplitudeTaper = c;

    Adb2 = patternAzimuth(rb2, 3e8);
    Adb2_180 = Adb2(1:180) ;
    
    gcf = figure ;
    set(gcf,'position',get(0,'ScreenSize'))
    hold on
    
    plot(flip(Adb_180 - max(Adb)),'LineWidth',1)
    plot(flip(Adb2_180 - max(Adb2)),'LineWidth',1)
    
    title('Beam steered ' + string(steer) + '^{\circ}','FontSize', 18)
    xlabel('Degrees','FontSize', 16) 
    ylabel('Amplitude Normalized (dB)','FontSize', 16) 
    legend({'Uniform','non-uniform'},'FontSize', 14)
    grid on
    saveas(gcf,'graphs/NormalizedAmplitude.jpg')
    hold off
    
    gcf = figure;
    patternAzimuth(rb2, 3e8, 0, 'Azimuth',0:1:180)
    saveas(gcf,'graphs/patternAzimuth.jpg')
    
    %pattern(rb2, 3e8);
 
end