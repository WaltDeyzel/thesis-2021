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
            c = randi([1 3],1,1);
            if c == 5
                obj.antennaArray.PhaseShift(randi([1 (obj.N-1)],1,1)) = round(rand*360);
            end
            if c == 2
                r = randi([1 (obj.N-1)],1,1);
                a = rand();
                obj.antennaArray.ElementSpacing(r) = a;
                obj.antennaArray.ElementSpacing(obj.N - r) = a;
            end
            if c == 5
                obj.antennaArray.AmplitudeTaper(randi([1 (obj.N-1)],1,1)) = rand*10;
            end
      end % end mutate
      
      function mutatePhase(obj)
          obj.antennaArray.PhaseShift(randi([1 (obj.N-1)],1,1)) = round(rand*360);
      end % mutate phase only
      
      function mutateSpacing(obj)
           r = randi([1 (obj.N-1)],1,1);
           a = rand();
           obj.antennaArray.ElementSpacing(r) = a;
           obj.antennaArray.ElementSpacing(obj.N - r) = a;
      end % mutate spacing only
        
      function g = crossover(obj, obj1)
          % Average of spacing
          
           spacing = (obj.antennaArray.ElementSpacing + obj1.antennaArray.ElementSpacing)/2;
           obj.antennaArray.ElementSpacing(:) = spacing(:);
        
           amp = (obj.antennaArray.AmplitudeTaper + obj1.antennaArray.AmplitudeTaper)/2;
           obj.antennaArray.AmplitudeTaper(:) = amp(:);

           phaseShift = (obj.antennaArray.PhaseShift + obj1.antennaArray.PhaseShift)/2;
           obj.antennaArray.PhaseShift(:) = phaseShift(:);

            g = obj;
      end % end crossover
      
      function f = fitness(obj)
      
            Adb = patternAzimuth(obj.antennaArray, obj.freq); % Amplitude in dB
            Adb_180 = Adb(1:180);
            fit = flip(zeros(180,1));
            tot = 0;
            Tot = 0;
            Tally = 1;
            tally = 1;
            target = 60;
            M = 10^(Adb_180(target)/20);
            q = 5;
            for i = 1:180
                dbm = Adb_180(i);
          
                m = 10^(dbm/20);
                fit(i) = m;
                
                if (dbm > 0) && (i < target-q || i > target+q)
                    tally = tally + 1;
                    tot = tot + m*1.5;
                end
                if (i >= target-q && i <= target+q)
                    Tally = Tally + 1;
                    Tot = Tot + M;
                end
            end
            obj.Fitness = -(Tot*tally)/(tot*Tally);
            f = obj.Fitness;
      end % end fitness
      
      function fitness2(obj)
            target = 60;
            Adb = patternAzimuth(obj.antennaArray, obj.freq); % Amplitude in dB
            Adb_180 = Adb(1:180);
            q = 10;
            peak = 0;
            for i = 1:180
                dbm = Adb_180(i);
                if (i < target-q || i > target+q)
                    if dbm > peak
                        peak = dbm;
                    end
                end
            end
            
            if Adb_180(target) - peak < 3
                obj.Fitness = 10;
            end
      end % end fitness
      
      function Azimuth(obj)
        patternAzimuth(obj.antennaArray, obj.freq)
      end
      function Plot(obj)
          figure
          db = patternAzimuth(obj.antennaArray, obj.freq);
          plot(db)
      end
   end % end methods
end