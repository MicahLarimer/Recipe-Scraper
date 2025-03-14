import requests

# Start a session
session = requests.Session()

# Set the User-Agent header
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
})

url = "https://minimalistbaker.com/creamy-tuscan-shrimp-pasta-dairy-free/"
response = session.get(url)

print(response.status_code)
print(response.text[:500])
