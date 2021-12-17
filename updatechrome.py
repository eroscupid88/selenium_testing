import requests
import wget
import zipfile
import os

# get the latest chrome driver version number
url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
response = requests.get(url)
version_number = response.text
print(version_number)

# build the donwload url
download_url = "https://chromedriver.storage.googleapis.com/" + \
    version_number + "/chromedriver_mac64.zip"

# # download the zip file using the url built above
latest_driver_zip = wget.download(download_url, 'chromedriver.zip')

# extract the zip file
with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    # you can specify the destination folder path here
    zip_ref.extractall('/Users/dillonvu/chromeDriver')
# delete the zip file downloaded above
os.remove(latest_driver_zip)
os.chmod("/Users/dillonvu/chromeDriver/chromedriver", 0o0755)
