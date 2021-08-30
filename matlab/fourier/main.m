% Fourier representation

f = 3e8;
c = 3e8;
lamda = 1;
k = 2*pi*f/c;

d = 0.5; 
dd = [0.5 0.5 0.5 0.5 0.5 0.5];
AF2 = zeros(361, 0);
N = 6; % antennas

alpha = 0; %in deg
%  0: 0
% 30: 90
% 45: 127.279
% 60: 155.88457
spaced = [1 2 3];
amplitude = [1 1 1 1 1 1];

%gcf = figure();
hold on
title('Binomial AF, uniformly spaced array :' + string(d)+'\lambda', 'FontSize',17)
xlabel('Degrees','FontSize', 16) 
ylabel('Amplitude Normalized (dB)','FontSize', 16) 
%legend({'Uniform','non-uniform'},'FontSize', 14)
grid on
F = zeros(1, N);

    for q = 1:361
        AF = 0;
        %d = 0;
        for m = 0:N-1
            
            if m < 5
            %    d = d + dd(m+1);
                A = amplitude(m+1);
            end

            zeta = k*d*cos(q*pi/180) + alpha*pi/180;
            temp = A*exp(1i*m*zeta);
            AF = AF + temp;
            F(m+1) = temp;
        end
        AF2(q) = AF; 
    end
    axis([0 181 -50 0])
    data = 20*log(abs(AF2)) - max(20*log(abs(AF2)));
    %plot(data(1:181))

%saveas(gcf,'BinomialAF1.emf')
%saveas(gcf,'BinomialAF1.jpg')

hold off
padding = zeros(1,100);
H = [1 1 1 1 1 1];
HH = [H, padding];
FF = [F,padding];
h = ifft(FF);
disp(F)
gcf = figure;
%stem(h)
hold on
title('h(n)', 'FontSize',17)
xlabel('Time','FontSize', 16) 
ylabel('Amplitude', 'FontSize', 16) 
stem(h)
grid on
saveas(gcf,'TEMTime.jpg')
%plot(abs(fft(h)))