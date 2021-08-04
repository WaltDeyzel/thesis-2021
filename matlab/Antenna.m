classdef Antenna
   properties
      antennaArray
      Fitness {mustBeNumeric}
      f
      % DNA:
      % 1) Distance between elements.
      % 2) Amplitude of signals
      % 3) Phase shift of signals
      d 
   end
   methods
      % constructor
      function obj = Antenna(AA, freq, distance)
        if nargin == 3 % Number of function input arguments
            obj.antennaArray = AA;
            obj.Fitness = -1;
            obj.f = freq;
            obj.d = distance;
        end % end if
      end % end constructor
      function show(obj)
        patternAzimuth(obj, obj.f)
      end
   end % end methods
end