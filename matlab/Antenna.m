classdef Antenna
   properties
      antennaArray
      Fitness {mustBeNumeric}
      freq
      % DNA:
      % 1) Distance between elements.
      % 2) Amplitude of signals
      % 3) Phase shift of signals
      N
   end
   methods
      % constructor
      function obj = Antenna(AA, f, n)
        if nargin == 3 % Number of function input arguments
            obj.antennaArray = AA;
            obj.Fitness = 1;
            obj.freq = f;
            obj.N = n;
        end % end if
      end % end constructor
      
      function mutate(obj)
         
            r = randi([1 (obj.N-1)],1,1);
            a = rand;
            obj.antennaArray.ElementSpacing(r) = a;
            obj.antennaArray.ElementSpacing(obj.N - r) = a;    
      end % end mutate
      
      function g = crossover(obj, obj1)
          % Average of spacing 
          tot = obj.Fitness + obj1.Fitness;
        %spacing = (obj.antennaArray.ElementSpacing * obj.Fitness/tot + obj1.antennaArray.ElementSpacing * obj1.Fitness/tot)/2;
        %obj.antennaArray.ElementSpacing = spacing;
        
        %amplitude = (obj.antennaArray.AmplitudeTaper * obj.Fitness/tot + obj1.antennaArray.AmplitudeTaper * obj1.Fitness/tot)/2;
        %obj.antennaArray.AmplitudeTaper = amplitude;
        
        phaseShift = (obj.antennaArray.PhaseShift * obj.Fitness/tot + obj1.antennaArray.PhaseShift * obj1.Fitness/tot)/2;
        obj.antennaArray.PhaseShift = phaseShift;
        g = obj;
      end
      
      function f = fitness(obj)
      
            Adb = patternAzimuth(obj.antennaArray, obj.freq); % Amplitude in dB
            Adb_180 = Adb(181:361)';
            fit = zeros(180,1);
            target = 90;
            for i = 1:180
                M = 10^(Adb_180(i)/20);
                fit(i) =  (M*sin(pi*abs(i - target)/180))^2;
            end
            obj.Fitness = 1/var(fit);
            f = obj.Fitness;
      
      end % end fitness
      
      function show(obj)
        patternAzimuth(obj.antennaArray, obj.freq)
      end
   end % end methods
end