import requests

url = "http://127.0.0.1:5000/predict"
image_path = r"C:\Users\HP\Downloads\w1.jpg"  # Option 1: Raw string

# OR use escaped backslashes
# image_path = "C:\\Users\\HP\\Downloads\\w1.jpg"

with open(image_path, "rb") as img:
    files = {"file": img}
    response = requests.post(url, files=files)
    print(response.json())
