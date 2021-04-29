import random
import urllib.request


def pic_download(url):

  name = random.randrange(1, 1000)
  Final_Name = str(name) + ".jpg"
  urllib.request.urlretrieve(url, Final_Name)


pic_download("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6-HMIgg0auh3xX_qz8yK2bP-I24CdZFirkZjer2SMVPhJo7u-")
a = input("Enter the link")
pic_download(str(a))
