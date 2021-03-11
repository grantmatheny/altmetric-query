#!/usr/bin/env python3
import requests
import json
import csv

data = requests.get('https://api.altmetric.com/v1/citations/1w?num_results=20')
json_pretty = json.loads(data.text)
json_obj = json.dumps(json_pretty, indent=2)

csv_data = [['Title', 'doi', 'Number of Authors', 'First Author', 'Abstract']]
print('Total Results: ' + str(data.json()['query']['total']))
print('===============================\n\n')
for result in data.json()['results']:
  
  print("Title: " + result['title'] + '\n')
  if 'doi' in result.keys():
    doi = result['doi']
    print("doi: " + doi + '\n')
  else:
    doi = 'No DOI provided'
  if 'authors' in result.keys():
    if result['authors'][0].find(',') != -1:
      author_name = result['authors'][0].split(', ')
      author_name = [author_name[1], author_name[0]]
      author_name = ' '.join(author_name)
    else:
      author_name = result['authors'][0]
    print(str(len(result['authors'])) + " Authors // First: " + author_name + '\n' )
  if 'abstract' in result.keys():
    abstract = result['abstract']
    print("Abstract: " + result['abstract'] + '\n')
  else:
    abstract = 'No Abstract Available'
    print("No Abstract Available\n")
  print('=====================================\n')
  csv_data.append([result['title'], doi, len(result['authors']), author_name, abstract])

with open('output.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(csv_data)