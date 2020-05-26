from bs4 import BeautifulSoup
import requests

#Scraping the countries data table from this site
URL = 'https://www.worldometers.info/coronavirus/#countries'

page = requests.get(URL)

if page.status_code != 200:
	print('Error with scraping data')

#Gets html code for the entire page
soup = BeautifulSoup(page.content,'html.parser')

#Get only the table's html code
results = soup.find(id='main_table_countries_today')

#Filters results down to only table values
content = results.find_all('td')

countries = []
total_cases = []
new_cases = []
total_deaths = []
new_deaths = []
total_recovered = []
active_cases = []
total_tests = []

#Every country has 15 rows in content, so the following code splits the data acc to category
i=1
for entry in content:
	if i%15 == 2:
		countries.append(entry.text.strip())
	if i%15 == 3:
		total_cases.append(entry.text.strip())
	if i%15 == 4:
		new_cases.append(entry.text.strip())
	if i%15 == 5:
		total_deaths.append(entry.text.strip())
	if i%15 == 6:
		new_deaths.append(entry.text.strip())
	if i%15 == 7:
		total_recovered.append(entry.text.strip())
	if i%15 == 8:
		active_cases.append(entry.text.strip())
	if i%15 == 12:
		total_tests.append(entry.text.strip())
	i+=1

#This function detect if the entered word matches any country name, and then returns 3 things:
# 1. a dictionary of all info for that country
# 2. the same dictionary in string format
# 3. found flag that is set if entered word matches a country name
def find_data_for_country(country):
	if country not in countries:
		return 0,0,0
	idx =  countries.index(country)
	#print('Country name: {}'.format(countries[idx]))

	output_dict = {
		'Total Cases':total_cases[idx],
		'New Cases':new_cases[idx],
		'Total Deaths':total_deaths[idx],
		'New Deaths':new_deaths[idx],
		'Total Recovered':total_recovered[idx],
		'Active Cases':active_cases[idx],
		'Total Tests':total_tests[idx]
	}

	output_str = "Here are today's stats for {}".format(country)
	output_str += '\n' + 'Total Cases: {}'.format(total_cases[idx])
	output_str += '\n' + 'New Cases: {}'.format(new_cases[idx])
	output_str += '\n' + 'Total Deaths: {}'.format(total_deaths[idx])
	output_str += '\n' + 'New Deaths: {}'.format(new_deaths[idx])
	output_str += '\n' + 'Total Recovered: {}'.format(total_recovered[idx])
	output_str += '\n' + 'Active Cases: {}'.format(active_cases[idx])
	output_str += '\n' + 'Total Tests: {}'.format(total_tests[idx])
	
	return output_dict,output_str,1