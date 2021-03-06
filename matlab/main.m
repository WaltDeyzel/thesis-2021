import Antenna.*
import selection.*
import write2excel.*
import genome.*
import compare.*

population_total = 100;
crossover_rate = 0.5;
mutation_rate = 0.15;
simulations = 20;
steer = 20;             % from horizontal anti clock wise
filename = '31Aug/GL1.xlsx';
% Empty arry to host antennas.
population = Antenna.empty(population_total, 0);

% Fill population array
for i = 1:population_total
    % Randomize la
    population(i) = genome();
end

fittest_antenna = population(1);
pop = zeros(simulations);
% Simulation - Gen 0
for a = 1:simulations
 
    disp("Generation " + string(a-1) )
    population_fitness = 0;
    
    for i = 1:population_total
        % calculate the fitness of each antenna.
       
        calc_fit = population(i).fitness(steer);
        population_fitness = population_fitness + calc_fit;
        if calc_fit < fittest_antenna.Fitness
            fittest_antenna = Antenna(population(i).getArray(), 3e8, 6, calc_fit);        
        end
    end % end calculate fitness
    
    pop_norm = population_fitness/population_total;
    % Create copy of populaton.
    population_copy = Antenna.empty(population_total, 0);
    write2excel('experiment/'+string(filename), fittest_antenna, a, steer, pop_norm);
    
    % Keep the best antenna. 
    population_copy(1) = fittest_antenna;
    % Display best antenna.
    fittest_antenna.Azimuth()
    disp('fit : ' + string(population_copy(1).getFitness))
    
    for i = 2:(population_total)
        selected_1 = selection(population(:), population_total);
        
        if rand < crossover_rate
            % crossover
            selected_2 = selection(population(:), population_total);
            selected_1 = selected_1.crossover(selected_2);
        end
        
        if rand < mutation_rate
            % mutation
            selected_1.mutate()
        end
        
        population_copy(i) = Antenna(selected_1.getArray(), 3e8, 6, 1000);
    end
    population(:) = population_copy(:);
    % Track population fitness
    disp('pop : ' + string(pop_norm))
   
end % end simulation

disp(fittest_antenna.Fitness);
disp(fittest_antenna.antennaArray);
compare(fittest_antenna, steer);
%[a, b, c, d, e] = hpbw(fittest_antenna.antennaArray);