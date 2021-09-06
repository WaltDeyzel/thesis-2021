% Compare solution to uniform half wave spaced antennea array.

function compare(obj, steer)
        import uniformLinearArray.*
        dp = dipole('Width',0.001, 'Length', 0.5);
        %compare solution to uniform array.
        rb = uniformLinearArray(0.5, 90-steer);
        Adb = patternAzimuth(rb, 3e8);
        Adb_180 = Adb(1:180);
        % ------------------------------- 
        
        rb3 = linearArray;
        rb3.Element = [dp,dp,dp,dp,dp,dp];

        rb3.ElementSpacing = obj.antennaArray.ElementSpacing;
        rb3.PhaseShift = obj.antennaArray.PhaseShift;
        rb3.AmplitudeTaper = obj.antennaArray.AmplitudeTaper;

        Adb3 = patternAzimuth(rb3, 3e8);
        Adb3_180 = Adb3(1:180);
        
        figure 
        hold on
        grid on
        plot(flip(Adb_180-max(Adb_180)),'LineWidth',1)   % uniform solution.
        plot(flip(Adb3_180-max(Adb3_180)),'LineWidth',1)  % non-uniform solution.
        title('Beam steered ' + string(steer),'FontSize', 18)
        xlabel('Degrees','FontSize', 16) 
        ylabel('Amplitude (dB)','FontSize', 16) 
        legend({'Uniform','non-uniform'},'FontSize', 14)
        
      end