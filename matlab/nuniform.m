% Radiation pattern for non-uniform antenna array.
import fitnessFunction.*

dp = dipole('Width',0.001, 'Length', 0.5);
rb = linearArray;
rb.Element = [dp,dp,dp,dp,dp,dp];
rb2 = linearArray;
rb2.Element = [dp,dp,dp,dp,dp,dp];

rb.ElementSpacing = [0.5 0.5 0.5 0.5 0.5];
rb.PhaseShift = [90.8 180.0 270.0 360 90 180];
rb.AmplitudeTaper = [1    1    1    1   1    1];

rb2.ElementSpacing = [0.6403    0.6656    0.6646    0.6656    0.6403];
rb2.PhaseShift = [161.3346  166.4949  163.4810  178.1219  183.4636  186.6479];
rb2.AmplitudeTaper = [1    1    1    1   1    1];

Adb = patternAzimuth(rb, 3e8);
Adb2 = patternAzimuth(rb2, 3e8);

disp(fitnessFunction(Adb_180))

figure 
plot(Adb)
hold on 
plot(Adb2)
