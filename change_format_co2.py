import numpy

## OPEN DATASET ## 
f = open('C02_emissions.csv','r')
data = []
for line in f:
    data.append(line) 
f.close()

## WRITE DATA TO LIST: CO2 emissions data ##
'''
This for loop also puts the country names as a single string in order to have all the rows with equal length 
'''

new_data  = []
for i in range(len(data)):
    f = data[i].split(',')[:-1]
    #print len(f)
    if len(f) == 38:
        f[3] = f[4][1:-1] + ' ' + f[3][1:]
        f.pop(4)
    new_data.append(f)     
             
## A BETTER HEADER ##        
header = ["Rank 2009","Rank 2008","Rank 2006","Country","ISO country code","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","% change from 2008 to 2009","% change from 2000 to 2009"]

## DATA ARRAY SO THAT WE CAN SLICE DATA BY COLUMN ## 
data_array = numpy.array((new_data[1:]))

## CLEANING CO2 DATA ##
country = data_array[:,3]
CO2_1980 = data_array[:,5]
new_CO2_1980 = numpy.zeros((len(CO2_1980)))
for i in range(len(CO2_1980)):
    ele = CO2_1980[i]
    if ele == '--':
        new_CO2_1980[i] = '0.0'
    elif ele == 'NA':
        new_CO2_1980[i] = '0.0'
    else:
        new_CO2_1980[i] = ele

## WRITING ONE SLICE OF DATA MATRIX TO FILE ##         
f = open('CO2_data_country_1980.txt','w')

for i in range(len(country)):
    f.write('%s,%0.f\n' % (country[i],new_CO2_1980[i]))
f.close() 
