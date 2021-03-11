#!/usr/bin/env python3
import requests
import json

data = requests.get('https://api.altmetric.com/v1/citations/1w?num_results=20')
json_pretty = json.loads(data.text)
json_obj = json.dumps(json_pretty, indent=2)
print('Total Results: ' + str(data.json()['query']['total']))
print('===============================\n\n')
for result in data.json()['results']:
  print("Title: " + result['title'] + '\n')
  if 'doi' in result.keys():
    print("doi: " + result['doi'] + '\n')
  if 'authors' in result.keys():
    if result['authors'][0].find(',') != -1:
      author_name = result['authors'][0].split(', ')
      author_name = [author_name[1], author_name[0]]
      author_name = ' '.join(author_name)
      print(str(len(result['authors'])) + " Authors // First: " + author_name + '\n' )
    else:
      print(str(len(result['authors'])) + " Authors // First: " + result['authors'][0] + '\n' )
  if 'abstract' in result.keys():
    print("Abstract: " + result['abstract'] + '\n')
  else:
    print("No Abstract Available\n")
  print('=====================================\n')