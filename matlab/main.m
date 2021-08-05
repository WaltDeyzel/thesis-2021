import Antenna.*
import selection.*

population_total = 100;
crossover_rate = 0.3;
mutation_rate = 0;
simulations = 10;

% Empty arry to host antennas.
population = Antenna.empty(population_total, 0);

% Antenna design. - linear array of 6.
% Half wave dipole antenna.
dp = dipole('Width',0.001, 'Length', 0.5);


% Fill population array
for i = 1:population_total
    % Randomize la
    la = linearArray;
    la.Element = [dp,dp,dp,dp,dp,dp];
    la.ElementSpacing = [1 1 1 1 1]; % symetrical?
    %la.AmplitudeTaper = [rand rand rand rand rand rand];
    a = 360*rand; % degrees
    la.PhaseShift = [a*6 a*5 a*4 a*3 a*2 a*1];
    population(i) = Antenna(la, 3e8, 6);
end
fittest_antenna = population(1);
% Simulation - Gen 0
for a = 1:simulations
    population_fitness = 0;
    
    for i = 1:population_total
        % calculate the fitness of each antenna.
        calc_fit = population(i).fitness;
        disp(calc_fit)
        population_fitness = population_fitness + calc_fit;
        if calc_fit > fittest_antenna.Fitness
            fittest_antenna = population(i);
        end
    end % end calculate fitness
    disp(fittest_antenna.Fitness)
    % Create copy of populaton.
    population_copy = Antenna.empty(population_total, 0);
    % Keep the best antenna. 
    population_copy(1) = fittest_antenna;
    
    for i = 2:(population_total)
        selected_1 = selection(population, population_total);
        %population(floor(rand*population_total)+1);
        
        if rand < crossover_rate
            % crossover
            selected_2 = selection(population, population_total);
            selected_1 = selected_1.crossover(selected_2);
        end
        
        if rand < mutation_rate
            % mutation
            selected_1.mutate
        end
        
        population_copy(i) = selected_1;
    end
    population = population_copy;
    disp(a)
end % end simulation
