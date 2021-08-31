% Fourier representation
import AF.*
%dd = [0 1 1 1 1 1 1];

N = 7; % antennas
alpha = 0; %in deg

dd = [0.8 0.8 0.8 0.8 0.8 0.8 0.8]; %
dd1 = [0 0.711 1.019 0.868 0.98 0.772 0.747];
dd2 = [0.774 0.885 0.815 0.835 0.847];
amplitude = [1 1 1 1 1 1 1 1];

gcf = figure();
hold on
title('AF', 'FontSize',17)
xlabel('Degrees','FontSize', 16) 
ylabel('Amplitude Normalized (dB)','FontSize', 16) 
%legend({'Uniform','non-uniform'},'FontSize', 14)
grid on
AFF = AF(dd, amplitude, alpha, N);
axis([0 181 -50 0])
data = 20*log(abs(AFF)) - max(20*log(abs(AFF)));
plot(data(1:181))
AFF = AF(dd2, amplitude, alpha, 6);
axis([0 181 -50 0])
data = 20*log(abs(AFF)) - max(20*log(abs(AFF)));
plot(data(1:181))
AFF = AF(dd1, amplitude, alpha, N);
axis([0 181 -50 0])
data = 20*log(abs(AFF)) - max(20*log(abs(AFF)));
%plot(data(1:181))
legend({'Uniform','non-uniform', 'NU'},'FontSize', 14)

saveas(gcf,'GLZ2.emf')
saveas(gcf,'GLZ2.jpg')

%hold off
%padding = zeros(1,100);
%H = [1 1 1 1 1 1];
%HH = [H, padding];
%FF = [F,padding];
%h = ifft(FF);
%disp(F)
%gcf = figure;
%stem(h)
%hold on
%title('h(n)', 'FontSize',17)
%xlabel('Time','FontSize', 16) 
%ylabel('Amplitude', 'FontSize', 16) 
%stem(h)
%grid on
%saveas(gcf,'TEMTime.jpg')
%plot(abs(fft(h)))