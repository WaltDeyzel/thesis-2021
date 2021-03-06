

%LAA = [1 1 1 1 1 1];
%d = [0 0.5 1 1.5 2 2.5];
%N = 100;

%LAA = ones(1,N);
%d = linspace(0, 6);
%gcf = figure();
%hold on
%title('Uniform Linear Antenna Array', 'FontSize',17)
%xlabel('Element Spacing [\lambda]','FontSize', 16) 
%ylabel('Amplitude Taper','FontSize', 16) 
%legend({'Uniform','non-uniform'},'FontSize', 14)
%grid on
%stem(d, LAA)

%saveas(gcf,'ULAASPACING100.emf')
%saveas(gcf,'ULAASPACING100.jpg')

%hold off
%N = 100;
%d = 6/N;                    % uniform seperation.
%f = 3e8;                    % operating frequency
%lamda= 3e8/f;               % wave length
%steering = 45;              % desired angle
%theta = 360*d*cos(steering *pi/180)/lamda ;

amp0 = [1 1 1 1 1 1 1 1 1 1 1];
amp1 = [1.2587 2.1013  3.270 4.2912 4.8872 4.8872 4.2912 3.2707 2.1013 1.2587]/4.8872;
amp2 = [1 9 36 84 126 126 84 36 9 1]/126;
amp3 = [0.16145804 0.32647378 0.54452268 0.74505314 0.8648596  0.8648596 0.74505314 0.54452268 0.32647378 0.16145804];

d = 1;
gcf = figure();
hold on
title('Amplitude Tapering ULA.', 'FontSize',17)
xlabel('Degrees','FontSize', 16) 
ylabel('Amplitude Normalized (dB)','FontSize', 16) 

grid on

 radians = 0:0.00001:pi;
    
resolution = length(radians);   
space = AF(d, amp0);    

plot(180*(1:resolution)/resolution, 20*log10(abs(space))-max(20*log10(abs(space))),'LineWidth',1)
space = AF(d, amp1);    
plot(180*(1:resolution)/resolution,20*log10(abs(space))-max(20*log10(abs(space))),'LineWidth',1)
space = AF(d, amp2);    
plot(180*(1:resolution)/resolution, 20*log10(abs(space))-max(20*log10(abs(space))),'LineWidth',1)
space = AF(d, amp3);    
plot(180*(1:resolution)/resolution, 20*log10(abs(space))-max(20*log10(abs(space))),'LineWidth',1)
axis([0 180 -50 0 ])
legend({'Uniform', 'Dolph', 'Binomial', 'GA'}, 'FontSize', 14)
saveas(gcf,'AmpALL.emf')
%saveas(gcf,'AmpALL.jpg')
h = chebwin(6);
%stem(h)

hold off
N = 50;
LAA = ones(1,N);
z = zeros(1, 20);
sig = [z LAA z];
Sig = fft(sig, 1000);
SIG = fftshift(Sig);
x = -200:0.001:200;
s = sinc(x)+sinc(x+20)+sinc(x+40)+sinc(x+60)+sinc(x+80)+sinc(x+100);

y = conv(LAA, s);
%plot(y)

%plot(s)
%set(gca,'XTick',[], 'YTick', [])

%plot(linspace(10,20, 1000), sinc(linspace(-10,10, 1000)))
% window
%plot(linspace(-1,1,140),sig)
% dirac comb
%stem(LAA)


% sampled window
%stem(linspace(-1.2,1.2, 46),sig)
%axis([-1 1 0 1.2])

function y = AF(d, amp)
    radians = 0:0.00001:pi;
    k = 2*pi;
    N = 10;
    resolution = length(radians);
    space = zeros(1, resolution);
    y = 1; 
    for r = radians
        tot = 0;
        for m = 0:N-1
            tot = tot + amp(m+1)*exp(1i*k*m*d*cos(r));
        end
      
        space(y) = tot;
        y = y + 1;
    end
    y = space;
end