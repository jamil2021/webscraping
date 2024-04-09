import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the target URL
url = "https://www.worldometers.info/coronavirus/"

# Send an HTTP GET request and store the response
response = requests.get(url)

# Check if the request was successful 
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.content, 'html.parser')

  # coronaVirus Cases
  co_cases = soup.find_all('h1', string='Coronavirus Cases:')
  co_casesNo = co_cases[0].find_next_sibling('div', class_='maincounter-number').find('span').text.strip()
  print(f"Coronavirus Cases: {co_casesNo}")

  # no of deaths
  deaths = soup.find_all('h1', string='Deaths:')
  deathsNo = deaths[0].find_next_sibling('div', class_='maincounter-number').find('span').text.strip()
  print(f"Deaths: {deathsNo}")

  # Recovered
  rec = soup.find_all('h1', string='Recovered:')
  recNo = rec[0].find_next_sibling('div', class_='maincounter-number').find('span').text.strip()
  print(f"Recovered: {recNo}")

  # Create a dictionary with the data
  data = {
    'active': [None, None, None, None, None],
    'recovered': [None, None, None, None, None]
  }

  # Create a DataFrame
  active_recovered_df = pd.DataFrame(data, index=['actClosedTotal', 'mildRec', 'mildRecPer', 'criticalDeaths', 'criticalDeathsPer'])

  # Rename the DataFrame
  active_recovered_df.columns = ['active', 'recovered']
  
  # Display the DataFrame
  print(active_recovered_df)

  # Total Active Cases and Closed Cases
  actClosedTotal = soup.find_all('div', class_='number-table-main')
  actTotal = actClosedTotal[0].text.strip()
  active_recovered_df.loc['actClosedTotal', 'active'] = actTotal
  closedTotal = actClosedTotal[1].text.strip()
  active_recovered_df.loc['actClosedTotal', 'recovered'] = closedTotal
  print(active_recovered_df)
  
  # in mild condition and Recovered Cases with percentages
  mildRec = soup.find_all('div', style='float:left; text-align:center')
  mild = mildRec[0].find('span', class_='number-table').text.strip()
  active_recovered_df.loc['mildRec', 'active'] = mild
  mildPer = mildRec[0].find('strong').text.strip()
  active_recovered_df.loc['mildRecPer', 'active'] = mildPer
  print(f"{mild} ({mildPer}%)")

  rec = mildRec[1].find('span', class_='number-table').text.strip()
  active_recovered_df.loc['mildRec', 'recovered'] = rec
  recPer = mildRec[1].find('strong').text.strip()
  active_recovered_df.loc['mildRecPer', 'recovered'] = recPer
  print(active_recovered_df)

  # Critical Cases and deaths with percentages
  criticalDeaths = soup.find_all('div', style='float:right; text-align:center')
  critical = criticalDeaths[0].find('span', class_='number-table').text.strip()
  active_recovered_df.loc['criticalDeaths', 'active'] = critical
  criticalPer = criticalDeaths[0].find('strong').text.strip()
  active_recovered_df.loc['criticalDeathsPer', 'active'] = criticalPer
  deaths = criticalDeaths[1].find('span', class_='number-table').text.strip()
  active_recovered_df.loc['criticalDeaths', 'recovered'] = deaths
  deathsPer = criticalDeaths[1].find('strong').text.strip()
  active_recovered_df.loc['criticalDeathsPer', 'recovered'] = deathsPer
  print(active_recovered_df)

# Find the table element with id 'main_table_countries_today'
table = soup.find('table', id='main_table_countries_today')

# Initialize lists to store data
data = {
    'No': [],
    'Country_other': [],
    'Total Cases': [],
    'New Cases': [],
    'Total Deaths': [],
    'New Deaths': [],
    'Total Recovered': [],
    'New Recovered': [],
    'Active Cases': [],
    'Serious Critical': [],
    'Tot. Cases/1M pop': [],
    'Deaths/1M pop': [],
    'Total Tests': [],
    'Tests/1M pop': [],
    'Population': []
}

# Find all rows in the table body
rows = table.find('tbody').find_all('tr')

# Iterate over each row and extract relevant data
for row in rows:
    # Find the cells in the row
    cells = row.find_all('td')
    
    # Extract data from each cell and append to respective lists
    data['No'].append(cells[0].text.strip())
    data['Country_other'].append(cells[1].text.strip())
    data['Total Cases'].append(cells[2].text.strip())
    data['New Cases'].append(cells[3].text.strip())
    data['Total Deaths'].append(cells[4].text.strip())
    data['New Deaths'].append(cells[5].text.strip())
    data['Total Recovered'].append(cells[6].text.strip())
    data['New Recovered'].append(cells[7].text.strip())
    data['Active Cases'].append(cells[8].text.strip())
    data['Serious Critical'].append(cells[9].text.strip())
    data['Tot. Cases/1M pop'].append(cells[10].text.strip())
    data['Deaths/1M pop'].append(cells[11].text.strip())
    data['Total Tests'].append(cells[12].text.strip())
    data['Tests/1M pop'].append(cells[13].text.strip())
    data['Population'].append(cells[14].text.strip())

# Create a DataFrame using the extracted data
df = pd.DataFrame(data)

# Drop the first 7 rows from the DataFrame
df = df.iloc[8:]

# Reset the index after dropping rows
df.reset_index(drop=True, inplace=True)

# Display the DataFrame
# print(df)

# Save the DataFrame to an Excel file
print(df.head(n=10))
# df.to_excel("corona_data.xlsx", index=False)  # Saves without index column


# Create a Pandas Excel writer using openpyxl
with pd.ExcelWriter('corona_data.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    # Get the Excel writer object from the Pandas Excel writer
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Adjust the column widths based on content length
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        # adjusted_width = (max_length + 2) * 1.2
        adjusted_width = (max_length + 0) * 1.2
        worksheet.column_dimensions[column_letter].width = adjusted_width

    # Save the Excel file
    writer._save()
print("Data saved to website_data.xlsx")
