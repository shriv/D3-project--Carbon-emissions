import numpy

f = open('GDP_data_country_1980.txt','r')
gdp = []
for line in f:
    gdp.append(line)
f.close()

f = open('CO2_data_country_1980.txt','r')
co2 = []
for line in f:
    co2.append(line)   
f.close()

f = open('population_data_country_1980.txt','r')
population = []
for line in f:
    population.append(line)   
f.close()

country_gdp = []
for line in gdp:
    country_gdp.append(line.split(',')[0])
    
country_co2 = []
for line in co2:
    country_co2.append(line.split(',')[0])
    
country_population = []
for line in population:
    country_population.append(line.split(',')[0])
    
union = set(country_gdp).intersection(set(country_co2))
union = list(union)
common_set = []
for i in range(len(union)):
    country = union[i]
    ind_co2 = numpy.where([x == country for x in country_co2])[0][0]
    ind_gdp = numpy.where([x == country for x in country_gdp])[0][0]
    ind_population = numpy.where([x == country for x in country_population])[0][0]
    row = [country,population[ind_population].split(',')[1][:-1],co2[ind_co2].split(',')[1][:-1],gdp[ind_gdp].split(',')[1][:-1]]
    common_set.append(row)
    
    
f = open('population_CO2_GDP_1980.csv','w')
f.write('Country,Population,CO2,GDP\n')
for line in common_set:
    f.write('%s,%s,%s,%s\n' %(line[0],line[1],line[2],line[3]))
    
f.close()