#read in txt file and split on '|', note the space before and after the '|'

f = open("AviationData.txt", "r")
reader = f.read()
aviation_data = reader.split("\n")
aviation_list = [row.split(" | ") for row in aviation_data]

#playing with different search loops using code below as the search value
code = 'LAX94LA336'

#loop through each row and column for `code`.  This is O(n^2)
lax_code =[]
for i in range(len(aviation_list)):
    for j in range(len(aviation_list[i])):
        if aviation_list[i][j] == code:
            lax_code.append(aviation_list[i])

print('Data for {}:'.format(code),'\n',lax_code,'\n',25*'-','\n')

#perform linear search O(n)
lax_code2 = []
for row in aviation_list:
    for value in row:
        if value == code:
            lax_code2.append(row)

print('Data for {}:'.format(code),'\n',lax_code2,'\n',25*'-','\n')

#create dictionary where key is the column name and value is the columns values
aviation_dict_list = []
column_names = aviation_data[0].split(' | ')
aviation_data2 = aviation_data[1:]

for row in aviation_data2:
    split = row.split(' | ')
    dict = {}
    for i in range(len(split)):
        dict[column_names[i]] = split[i]
    aviation_dict_list.append((dict))

#search dictionary for code like about searches
lax_dict = []
for d in aviation_dict_list:
    if code in d.values():
        lax_dict.append(d)

print('Data for {} using dictionary search:'.format(code),'\n',lax_dict,'\n',25*'-','\n')

#count accidents by state and print top 3 states
from collections import Counter
import pandas as pd

aviation_df = pd.DataFrame(aviation_list[1:],columns=aviation_list[0])
aviation_us = aviation_df[aviation_df.Country == 'United States'].copy()
aviation_us['Location']=aviation_us['Location'].str.split()
aviation_us['Location']=aviation_us['Location'].str[-1]
counts = Counter(aviation_us['Location'])

print('Top three states with the most accidents:','\n',25*'-','\n',counts.most_common(3),'\n',25*'-','\n')

#Split date and keep only month and year MM/YYYY
aviation_us['Event Date'] = aviation_us['Event Date'].str.split('/').str[0] + '/' + aviation_us['Event Date'].str.split('/').str[-1]

#loop through unique months and calc serious, fatal, total injuries for each month
month_year = aviation_us['Event Date'].unique()
monthly_injuries = pd.DataFrame()
serious_tot = []
fatal_tot = []

#convert to integer
cols = ['Total Serious Injuries','Total Fatal Injuries']
for col in cols:
    aviation_us[col].replace({'':'0'},inplace=True)
    aviation_us[col]=aviation_us[col].astype('int')

for my in month_year:
    df = aviation_us[aviation_us['Event Date'] == my]
    serious = df['Total Serious Injuries'].sum()
    fatal = df['Total Fatal Injuries'].sum()
    serious_tot.append((serious))
    fatal_tot.append(fatal)
monthly_injuries['month_year'] = month_year
monthly_injuries['total_serious'] = serious_tot
monthly_injuries['total_fatal'] = fatal_tot
monthly_injuries['total_injuries'] = monthly_injuries['total_serious'] + monthly_injuries['total_fatal']

print('Top five months with highest total injuries','\n',25*'-','\n')
print(monthly_injuries.sort_values(by='total_injuries',ascending=False).head())