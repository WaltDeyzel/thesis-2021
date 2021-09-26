dp = dipole('Width',0.001, 'Length', 0.5);
steer = 63;
rb = uniformLinearArray(0.5, steer);
Adb = patternAzimuth(rb, 3e8);
Adb_180 = Adb(1:180);

patternAzimuth(rb, 3e8, 0, 'Azimuth',0:1:180);

gcf = figure ;
hold on

plot(flip(Adb_180 - max(Adb)),'LineWidth',1)


title('Beam steered ' + string(steer) + '^{\circ}','FontSize', 18)
xlabel('Degrees','FontSize', 16) 
ylabel('Amplitude Normalized (dB)','FontSize', 16) 
legend({'Uniform','non-uniform'},'FontSize', 14)
grid on