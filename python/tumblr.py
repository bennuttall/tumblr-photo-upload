from pytumblr import TumblrRestClient
from picamera import PiCamera
from datetime import datetime
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

PHOTOS_DIR = '/home/pi/photos'

def take_picture():
    with PiCamera() as camera:
        timestamp = datetime.now().isoformat()
        photo_path = '%s/%s.jpg' % (PHOTOS_DIR, timestamp)
        camera.capture(photo_path)
    return photo_path

def upload_picture(photo):
    success = False

    while not success:
        response = client.create_photo(username, data=photo)
        timestamp = datetime.now().isoformat()
        if 'id' in response:
            print("%s - Upload successful" % timestamp)
            success = True
        else:
            print("%s - Failed to upload picture. Trying again in 1 minute" % timestamp)
            sleep(60)

def main():
    photo = take_picture()
    upload_picture(photo)

if __name__ == '__main__':
    main()
