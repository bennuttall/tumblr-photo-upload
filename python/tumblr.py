from pytumblr import TumblrRestClient
from time import sleep
from auth import (
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret
)

client = TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret
)

info = client.info()

try:
    username = info["user"]["name"]
except KeyError:
    raise RuntimeError("Could not connect to Tumblr. Check auth keys.")

def main():
    photo = "/home/ben/tumblr/photo.jpg"
    success = False

    while not success:
        response = client.create_photo(username, data=photo)
        if 'id' in response:
            print("Upload successful")
            success = True
        else:
            print("Failed to upload picture. Trying again in 1 minute")
            sleep(60)

if __name__ == '__main__':
    main()
