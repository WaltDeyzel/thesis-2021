classdef BasicClass
   properties
      Value {mustBeNumeric}
   end
   methods
       % constructor
      function obj = BasicClass(val)
        if nargin == 1
            obj.Value = val;
        end % end if
      end % end constructor
   end % end methods
end