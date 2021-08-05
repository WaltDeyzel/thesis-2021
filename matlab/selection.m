% Tournament selectrion
function g = selection(population, population_total)
    
    r1 = floor(rand*population_total)+1;
    r2 = floor(rand*population_total)+1;
    
    option_1 = population(r1);
    option_2 = population(r2);
    if option_1.Fitness > option_2.Fitness
        g = option_1;
        return
    end
    g = option_2;
end