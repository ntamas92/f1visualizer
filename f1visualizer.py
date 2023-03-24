import urllib.request
import json

#url = 'https://ergast.com/api/f1/2023/drivers.json'
#result = json.load(urllib.request.urlopen(url))

#driver_table = result['MRData']['DriverTable']

#season = driver_table['season']
#drivers = driver_table['Drivers']

#filtereddrivers = drivers[0:3]

#for driver in filtereddrivers:
   #print(driver['familyName'],driver['givenName'],driver['permanentNumber'])

url2 = 'https://ergast.com/api/f1/2021/5/results.json'
result = json.load(urllib.request.urlopen(url2))

race_table = result['MRData']['RaceTable']    
season = race_table['season']
round =  race_table['round']
races =  race_table['Races']
year = races[0]['season']
weekend = races[0]['round']
weekendname = races[0]['raceName']
print(weekendname)

results = races[0]['Results']
podium = results[0:3]
for pos in podium:
   print(pos['position'],'.',pos['Driver']['givenName'],pos['Driver']['familyName'],pos['points'],"points")

#print(results[0]['position'],'.',results[0]['Driver']['givenName'],results[0]['Driver']['familyName'],results[0]['points'],"points")
#print(results[1]['position'],'.',results[1]['Driver']['givenName'],results[1]['Driver']['familyName'],results[1]['points'],"points")
p#rint(results[2]['position'],'.',results[2]['Driver']['givenName'],results[2]['Driver']['familyName'],results[2]['points'],"points")

#
