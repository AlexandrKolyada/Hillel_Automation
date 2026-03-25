import  requests

BASE_URL = "http://127.0.0.1:8080/upload"

try:
    with open("../mars_photo_1.jpg", "rb") as f:
        files = {"image": f}
        response = requests.post(BASE_URL, files=files)
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.json()}")

except FileNotFoundError:
    print("Error: File do not found. Check where is-  mars_photo_1.jpg in directory lesson_18")

full_url = response.json()["image_url"]

filename = full_url.split("/")[-1]

print(f"We have file name: {filename}")

get_url = f"http://127.0.0.1:8080/image/{filename}"

headers = {"Content-Type": "text"}
response_get = requests.get(get_url, headers=headers)

print(f"GET Status: {response_get.status_code}")
print(f"GET Response: {response_get.json()}")

remove_url = f"http://127.0.0.1:8080/delete/{filename}"
response_delete = requests.delete(remove_url)
print(f"Status: {response_delete.status_code}")
print(response_delete.json())