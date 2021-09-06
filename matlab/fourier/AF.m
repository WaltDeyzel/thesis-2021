% uniform 0.5 lambda alpha for steer
%  0: 0
% 30: 90
% 45: 127.279
% 60: 155.88457

function y = AF(spacing, amplitude, alpha, N)
    f = 3e8;
    c = 3e8;
    k = 2*pi*f/c;
    
    F = zeros(1, N);
    AF2 = zeros(361, 0);
    d = 0;
    ph =0;
    for q = 1:361
        AF = 0;
        for m = 0:N-1
            
            if m < N-1
                d = d + spacing(m+1);
                A = amplitude(m+1);
                ph = alpha(m+1);
                
            end
            zeta = k*d*cos(q*pi/180) + ph*pi/180;
            temp = A*exp(1i*zeta);
            AF = AF + temp;
            F(m+1) = temp;
        end
        AF2(q) = AF; 
    end
    y = AF2(:);
end