import requests
sum = 0
file1 = open('bankdata','w')
response = requests.get("http://api.reimaginebanking.com/branches?key=c086a83a35926b58caea74268ee585e2")
data = response.json()
for entry in data:
    file1.write(str(entry['name'])+ ',')
    file1.write(str(entry['geocode']['lat'])+ ',')
    file1.write(str(entry['geocode']['lng']) + ',')
    lat = str(entry['geocode']['lat'])
    lng = str(entry['geocode']['lng'])
    response2 = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyDPkaBMJaE5iJ8tDSyGf8rOwh-2w8xKirg".format(lat,lng))
    data2 = response2.json()
    for entry2 in data2["results"][0]["address_components"]:
        if entry2["types"][0] == "administrative_area_level_2":
            file1.write(str(entry2["long_name"]) + ',')
        if entry2["types"][0] == "administrative_area_level_1":
            file1.write(str(entry2["long_name"]) + '\n')
    sum += 1
print(sum)
file1.close()
