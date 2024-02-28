import requests

url = input('enter a URL:')

with requests.get(url) as response:
    print("\nRESPONSE HEADER")
    for key, value in response.headers.items():
        print(f"{key:30s} {value}")
    server = response.headers.get('Server')
    if server:
        print(f'The server is :{server}')
    else:
        print('No server found')
    
    cookies = response.cookies


    if cookies:
        for cookie in cookies:
            expired = cookie.expires
            print(f"The cookie is :{cookie.name}={cookie.value} and expires: {expired}")
    else:
        print('No cookies found')
