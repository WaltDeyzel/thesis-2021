classdef Antenna < handle
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
      function obj = Antenna(AA, f, n, err)
        if nargin == 4 % Number of function input arguments
            obj.antennaArray = AA;
            obj.Fitness = err;
            obj.freq = f;
            obj.N = n;
        end % end if
      end % end constructor
      function y = getFitness(obj)
        y = obj.Fitness;
      end
      
      function y = getArray(obj)
        y = copy(obj.antennaArray);
      end % return antenna array
   
      function mutate(obj)
            if rand < 0.5
                obj.antennaArray.PhaseShift(randi([1 (obj.N-1)],1,1)) = round(rand*360);
            end
            if rand > 0.5
                r = randi([1 (obj.N-1)],1,1);
                a = rand();
                obj.antennaArray.ElementSpacing(r) = a;
                obj.antennaArray.ElementSpacing(obj.N - r) = a;
            end
      end % end mutate
        
      function g = crossover(obj, obj1)
          % Average of spacing 
          tot = obj.Fitness + obj1.Fitness;
          t1  = abs(obj.Fitness/tot);
          t2  = abs(obj1.Fitness/tot);
          
          spacing = (obj.antennaArray.ElementSpacing * t1 + obj1.antennaArray.ElementSpacing * t2);
          %spacing = (obj.antennaArray.ElementSpacing + obj1.antennaArray.ElementSpacing)/2;
          obj.antennaArray.ElementSpacing(:) = spacing(:);
        
        %amp = (obj.antennaArray.AmplitudeTaper * t1 + obj1.antennaArray.AmplitudeTaper * t2);
        %obj.antennaArray.AmplitudeTaper(:) = amp(:);
        
        phaseShift = (obj.antennaArray.PhaseShift * t1 + obj1.antennaArray.PhaseShift * t2);
        obj.antennaArray.PhaseShift(:) = phaseShift(:);
        
        g = obj;
      end
      
      function f = fitness(obj)
      
            Adb = patternAzimuth(obj.antennaArray, obj.freq); % Amplitude in dB
            Adb_180 = Adb(181:361);
            %fitt = 0;
            fit = zeros(180,1);
            target = 30;
            %tot = 0;
            flag = 0;
            prev = Adb_180(1);
            for i = 1:180
                %M = 10^(Adb_180(i)/20);
                if Adb_180(i) >= prev
                    prev = Adb_180(i);
                    flag = 0;
                end
                if Adb_180(i) < prev && flag == 0 && i ~= target
                    %disp('walt' + string(prev)); 
                    fit(i) = 10^(prev/20)^2;
                    flag = 1;
                    prev = Adb_180(i);
                end
                if flag == 1
                    prev = Adb_180(i);
                end
                %tot = tot + M;
                %fit(i) = M*exp(-abs(target-i));
            end
            obj.Fitness = -(10^(Adb_180(target)/20)^2 - (sum(fit) + 10^(Adb_180(180)/20)));
            f = obj.Fitness;
            
      
      end % end fitness
      
      function show(obj)
        patternAzimuth(obj.antennaArray, obj.freq)
      end
   end % end methods
end