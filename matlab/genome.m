%Create a random solution 

function y = genome()
    
    % Half wave dipole antenna.
    dp = dipole('Width',0.001, 'Length', 0.5);
    
    la = linearArray;
    
    % Antenna design. - linear array of 6.
    la.Element = [dp,dp,dp,dp,dp,dp];
    
    l1 = rand*2;
    l2 = rand*2;
    l3 = rand*2;
    la.ElementSpacing = [l1 l2 l3 l2 l1];
    l1 = rand*2;
    l2 = rand*2;
    l3 = rand*2;
    la.AmplitudeTaper = [1 1 1 1 1 1];
    a = 360; % degrees
    la.PhaseShift = [round(rand*a) round(rand*a) round(rand*a) round(rand*a) round(rand*a) round(rand*a)];
    y = Antenna(la, 3e8, 6, 1000);
end