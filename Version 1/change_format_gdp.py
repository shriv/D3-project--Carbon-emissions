import numpy

## OPEN DATASET ## 
f = open('GDP_country.csv','r')
data = []
for line in f:
    data.append(line) 
f.close()

## WRITE DATA TO LIST: GDP emissions data ##
'''
This for loop also makes (i) the country names more systematic and (ii) makes all the rows of equal length 
'''

new_data  = []
for i in range(len(data)):
    f = data[i].split(',')[:-1]
    print len(f)
    if len(f) == 55:
        f[0] = f[1][1:-1] + ' ' + f[0][1:]
        f.pop(1)
    new_data.append(f)     
    
## DATA ARRAY SO THAT WE CAN SLICE DATA BY COLUMN ## 
data_array = numpy.array((new_data[1:]))

## HEADER ## 
header = new_data[0]
## CLEANING GDP DATA ##
country = data_array[:,0]
ind = numpy.where([x == '1980' for x in header])[0][0]
GDP_1980 = data_array[:,ind]
new_GDP_1980 = numpy.zeros((len(GDP_1980)))

for i in range(len(GDP_1980)):
    ele = GDP_1980[i]
    if ele == '':
        new_GDP_1980[i] = '0.0'
    elif ele == 'NA':
        new_GDP_1980[i] = '0.0'
    else:
        new_GDP_1980[i] = ele

## WRITING ONE SLICE OF DATA MATRIX TO FILE ##         
f = open('GDP_data_country_1980.txt','w')

for i in range(len(country)):
    f.write('%s,%0.f\n' % (country[i],new_GDP_1980[i]))
f.close()     