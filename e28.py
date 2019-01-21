import random
import urllib.request
def downloadwebimag(url):
    name = random.randrange(1,1000)
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)
downloadwebimag("https://media3.picsearch.com/is?GvVZKZ1uFs5DedVM3V14bhpbyZQ7cy815XIPdK3lT-I&height=240")