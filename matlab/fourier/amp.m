% Different amplitude taper for window.
samples = 10;
n = 0:samples;
z = zeros(1, 100);

y1 = ones(1,samples+1);
sig1 = [z y1 z];

y2 = sin(2*pi*0.5/samples * n);
sig2 = [z y2 z];

y3 = triangularPulse(0, 5, 10, 0:10);
sig3 = [z y3 z];


y4 = [1 10 45 120 210 252 210 120 45 10 1];
sig4 = [z y4 z];


%plot(y1/max(y1),'LineWidth',1)
hold on
%plot(y2/max(y2),'LineWidth',1)
%plot(y3/max(y3),'LineWidth',1)
%plot(y4/max(y4),'LineWidth',1)


%plot(abs(fftshift(fft(sig1)))/max(abs(fftshift(fft(sig1))) ))
hold on
%plot(abs(fftshift(fft(sig2)))/max(abs(fftshift(fft(sig2))) ))
%plot(abs(fftshift(fft(sig3)))/max(abs(fftshift(fft(sig3))) ))
%plot(abs(fftshift(fft(sig4)))/max(abs(fftshift(fft(sig4))) ))
%plot(abs(fftshift(fft(sig5)))/max(abs(fftshift(fft(sig5))) ))
%stem(y3)
set(gca,'XTick',[], 'YTick', [])
legend({'Uniform','Sin(x)','Triangle', 'Binomial'}, 'Fontsize', 14)
%title('FT of window.', 'FontSize',17)
axis([0 10 0 1.1 ])