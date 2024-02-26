import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input('enter a URL:')  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    #html = response.text
    #more(html)
    print("\nRESPONSE HEADER")
    for key, value in response.headers.items():
        print(f"{key:30s} {value}")
    server = response.headers.get('Server')
    if server:
        print(f'The server is :{server}')
    else:
        print('No server found')
    
    cookies = response.cookies.get('Set-Cookie')
    if cookies:
        print(f'The server is :{cookies}')
    else:
        print('No cookies found')