% uniform antenna array

% Radiation pattern for antenna array
function y = uniformLinearArray(spaced, steer)
    dp = dipole('Width',0.001, 'Length', 0.5);
    ULA = linearArray;
    ULA.Element = [dp,dp,dp,dp,dp,dp];

    ULA.ElementSpacing = spaced;

    d = 0.5;                    % uniform seperation.
    f = 3e8;                    % operating frequency
    lamda= 3e8/f;               % wave length
    steering = steer;           % desired angle
    a = 360*d*sin(steering *pi/180)/lamda;
    disp(a)
    ULA.PhaseShift = [a*6 a*5 a*4 a*3 a*2 a*1];
    y = ULA;
end