import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

response = requests.get(search_url, params=search_params)
data = response.json()
item = data['collection']['items']
first_item = data['collection']['items'][0]
nasa_id_1 = first_item['data'][0]['nasa_id']
next_item = data['collection']['items'][1]
nasa_id_2 = next_item['data'][0]['nasa_id']
print(nasa_id_1, nasa_id_2)

asset_url_1 = f"{BASE_URL}/asset/{nasa_id_1}"
response_1 = requests.get(asset_url_1)
asset_date_1 = response_1.json()

asset_url2 = f"{BASE_URL}/asset/{nasa_id_2}"
response_2 = requests.get(asset_url2)
asset_date_2 = response_2.json()

link_1 = asset_date_1['collection']['items']
link_2 = asset_date_2['collection']['items']

photo_url_1 = None
for item in asset_date_1['collection']['items']:
    if item['href'].endswith(".jpg"):
        photo_url_1 = item['href']
        break

photo_url_2 = None
for item in asset_date_2['collection']['items']:
    if item['href'].endswith(".jpg"):
        photo_url_2 = item['href']
        break

response_img1 = requests.get(photo_url_1)
with open("mars_photo_1.jpg", "wb") as file:
    file.write(response_img1.content)

response_img2 = requests.get(photo_url_2)
with open("mars_photo_2.jpg", "wb") as file_2:
    file_2.write(response_img2.content)