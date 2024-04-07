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

  # Find all table rows with website data (adjust selector as needed)
  table_rows = soup.find_all('table', class_=['wikitable', 'sortable', 'jquery-tablesorter'])
  t_rows = table_rows[0]
  tb = t_rows.find('tbody')
  tr = tb.find_all('tr')

  # Skip the 2 header rows
  tr_data = tr[2:]

  # Extract website data and create lists
  title = []
  dName = []
  rSimWeb = []  # Assuming this data is present in the second column
  website = []
  rSamrush = []
  type = []
  company = []
  country = []
  # ... Add similar lists for other columns

  for row in tr_data:
    all_tds = row.find_all('td')
    if all_tds:
      dName.append(all_tds[0].text.strip())
      rSimWeb.append(all_tds[1].text.strip())  # Assuming this data is in the second column
      website.append(row.find('a').text.strip())
      rSamrush.append(all_tds[2].text.strip())  # Adjust index based on actual structure
      type.append(all_tds[3].text.strip())  # Adjust index based on actual structure
      company.append(all_tds[4].text.strip())  # Adjust index based on actual structure
      country.append(all_tds[5].text.strip())
      # ... Add similar logic for other columns

  # Create a pandas DataFrame
  df = pd.DataFrame({
      "Website": website,
      "Domain Name": dName,
      "Rank_SimilarWeb": rSimWeb,
      "Rank_Samrush": rSamrush,
      "Type": type,
      "Company": company,
      "Country": country
  })

  # Save the DataFrame to an Excel file
  df.to_excel("website_data.xlsx", index=False)  # Saves without index column
  print("Data saved to website_data.xlsx")

else:
  print("Failed to retrieve the webpage content.")
