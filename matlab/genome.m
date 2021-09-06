%Create a random solution 

function y = genome()
    
    % Half wave dipole antenna.
    dp = dipole('Width',0.001, 'Length', 0.5);
    
    la = linearArray;
    
    % Antenna design. - linear array of 6.
    la.Element = [dp,dp,dp,dp,dp,dp];
    
    %S1 = rand;
    %S2 = rand;
    %S3 = rand;
    a = 1;
    la.ElementSpacing = [0.488 0.546 0.438 0.584 0.369];%[rand*a rand*a rand*a rand*a rand*a];       % Symetrically spaced
    a = 10;
    la.AmplitudeTaper = [1 1 1 1 1 1]; %[rand*a rand*a rand*a rand*a rand*a rand*a];
    a = 360; % degrees
    la.PhaseShift = [236 190 101 6 261  203];%[round(rand*a) round(rand*a) round(rand*a) round(rand*a) round(rand*a) round(rand*a)];
    y = Antenna(la, 3e8, 6, 1000);
end