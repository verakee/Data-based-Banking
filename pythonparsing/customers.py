import requests
file1 = open('customerdata','w')
response = requests.get("http://api.reimaginebanking.com/enterprise/customers?key=c086a83a35926b58caea74268ee585e2")
data = response.json()
count = 0
for entry in data["results"]:
    if count > 10000:
        break
    try:
        stnum = (str(entry['address']['street_number'])).strip()
        stname = (str(entry['address']['street_name'])).strip()
        city = (str(entry['address']['city'])).strip()
        file1.write(str(entry['_id'])+ ',')
    except:
        continue
    response2 = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={}+{},\
    +{}&key=AIzaSyDPkaBMJaE5iJ8tDSyGf8rOwh-2w8xKirg".format(stnum,stname,city).replace(' ','+'))
    data2 = response2.json()
    try:
        for entry2 in data2["results"][0]["address_components"]:
            if entry2["types"][0] == "administrative_area_level_2":
                file1.write(str(entry2["long_name"]) + ',')
            if entry2["types"][0] == "administrative_area_level_1":
                file1.write(str(entry2["long_name"]) + '\n')
    except:
        continue
    count +=1
file1.close()
