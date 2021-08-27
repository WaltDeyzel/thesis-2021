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
      gain
   end
   methods
      % constructor
      function obj = Antenna(AA, f, n, err)
        if nargin == 4 % Number of function input arguments
            obj.antennaArray = AA;
            obj.Fitness = err;
            obj.freq = f;
            obj.N = n;
            obj.gain = 0;
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
            if c == 1
                mutatePhase(obj);
            end
            if c == 2
                mutateSpacing(obj)
            end
            if c == 3
                mutateAmp(obj)
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
      
      function mutateAmp(obj)
           obj.antennaArray.AmplitudeTaper(randi([1 (obj.N)],1,1)) = rand;
      end % mutate spacing only
        
      function g = crossover(obj, obj1)
          % Average of spacing
            
           c = randi([1 3],1,1);
           if c == 1
               spacing = (obj.antennaArray.ElementSpacing + obj1.antennaArray.ElementSpacing)/2;
                obj.antennaArray.ElementSpacing(:) = round(spacing(:),3);
           end
           
           if c == 2
               amp = (obj.antennaArray.AmplitudeTaper + obj1.antennaArray.AmplitudeTaper)/2;
               obj.antennaArray.AmplitudeTaper(:) = round(amp(:),3);
           end
           
           if c == 3
               phaseShift = (obj.antennaArray.PhaseShift + obj1.antennaArray.PhaseShift)/2;
               obj.antennaArray.PhaseShift(:) = round(phaseShift(:),1);
           end
            g = obj;
      end % end crossover
      
      function f = fitness(obj, target)
      
            Adb_180 = patternAzimuth(obj.antennaArray, obj.freq, 0, 'Azimuth',0:1:180);
            tot = 0;
            Tot = 0;
            Tally = 1;
            tally = 1;
            peak_1 = 0;
            peak_2 = 0;
            M = 10^(Adb_180(target)/20);
            q = 10;
            for i = 1:180
                dbm = Adb_180(i); % in decibals
                
                % determine if current i is a peak
                if ((i > 1 && i < 180) && (Adb_180(i-1) < dbm) && (Adb_180(i+1) < dbm))
                    % second largest peak
                    if dbm > peak_1
                        peak_2 = peak_1;
                        peak_1 = dbm;
                    end
                end
                
                m = 10^(dbm/20);  
             
                % Outside main beam
                if (dbm > -10) && (i < target-q || i > target+q)
                    tally = tally + 1;
                    tot = tot + m;
                end
                % Within main beam
                if (i >= target-q && i <= target+q)
                    Tally = Tally + 1;
                    Tot = Tot + M;
                end
            end
            obj.Fitness = -(Tot*tally)/(tot*Tally);
            obj.gain = Adb_180(target);
            if(peak_1 - peak_2 <= 5) % second beam should at leat be 5db smaller.
                obj.Fitness = 100;
            end
            f = obj.Fitness;
      end % end fitness
      
      function y = HPBW(obj, target)
        Adb = patternAzimuth(obj.antennaArray, obj.freq); % Amplitude in dB
        Adb_180 = Adb(1:180);

        left = 0;
        right = 0;

        for i = 1:20
            if Adb_180(target-i) <= Adb_180(target) - 3
                left = target-i;
                break
            end
        end

        for i = 1:20
            if Adb_180(target+i) <= Adb_180(target) - 3
                right = target+i;
                break
            end
        end

        y = abs(left-right);
      end % end hpbw
      
      % DIFFERENT PLOT FOR ANTENNA ARRAY
      function Azimuth(obj)
        patternAzimuth(obj.antennaArray, obj.freq, 0, 'Azimuth',-0:1:180);
      end
      function Plot(obj)
          figure
          db = patternAzimuth(obj.antennaArray, obj.freq);
          plot(db)
      end
      function pattern(obj)
        pattern(obj.antennaArray, obj.freq)
      end
   end % end methods
end