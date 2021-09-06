% Fourier representation
import AF.*
%dd = [0 1 1 1 1 1 1];

N = 6; % antennas
alpha = [235.97873321 190.03847137 100.75352695   5.61344832 261.19869246  202.53565332]; %in deg
c = 5;
dd = [c c c c c c]; %
dd1 = [0.711 1.019 0.868 0.98 0.772 0.747];
dd2 = [0.48816526 0.54616767 0.43820411 0.58427123 0.36924341];
amplitude = [1 1 1 1 1 1 1];

gcf = figure();
hold on
title('AF', 'FontSize',17)
xlabel('Degrees','FontSize', 16) 
ylabel('Amplitude Normalized (dB)','FontSize', 16) 
legend({'Uniform','non-uniform'},'FontSize', 14)
grid on


AFF = AF(dd2, amplitude, alpha, N);
axis([0 181 -40 0])
data = 20*log(abs(AFF)) - max(20*log(abs(AFF)));
plot(data(1:181))


legend({'Uniform','non-uniform', 'NU'},'FontSize', 14)

%saveas(gcf,'GLZ2.emf')
%saveas(gcf,'GLZ2.jpg')


