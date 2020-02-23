import requests
sum = 0
sum2 = 0
file1 = open("atmdata2","w")
for page in range(1,10000):
    response = requests.get("http://api.reimaginebanking.com/atms?lat=39.8283&lng=-98.5795&rad=10000&key=c086a83a35926b58caea74268ee585e2&page=" + str(page))
    data = response.json()
    if len(data['data']) == 0:
        break
    for item in data['data']:
        file1.write(str(item['name'])+ ',')
        file1.write(str(item['geocode']['lat'])+ ',')
        file1.write(str(item['geocode']['lng']) + ',')
        lat = str(item['geocode']['lat'])
        lng = str(item['geocode']['lng'])
        response2 = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyDPkaBMJaE5iJ8tDSyGf8rOwh-2w8xKirg".format(lat,lng))
        data2 = response2.json()
        for item2 in data2["results"][0]["address_components"]:
            if item2["types"][0] == "administrative_area_level_2":
                file1.write(str(item2["long_name"]) + ',')
            if item2["types"][0] == "administrative_area_level_1":
                file1.write(str(item2["long_name"]) + '\n')
        if item["address"]["state"] == "DC":
            sum2+=1
        sum += 1
    #print("end of page" + str(page))
print(sum)
print(sum2)
file1.close()
