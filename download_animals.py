#!/usr/bin/env pyhon3
import os
import shutil
import urllib.request

# the list comes from https://evert.meulie.net/faqwd/complete-list-anonymous-animals-on-google-drive-docs-sheets-slides/
iconList = ('Alligator', 'Anteater', 'Armadillo', 'Auroch', 'Axolotl', 'Badger', 'Bat', 'Bear', 'Beaver', 'Buffalo', 'Camel', 'Capybara', 'Chameleon', 'Cheetah', 'Chinchilla', 'Chipmunk', 'Chupacabra', 'Cormorant', 'Coyote', 'Crow', 'Dingo', 'Dinosaur', 'Dog', 'Dolphin', 'Duck', 'Elephant', 'Ferret', 'Fox', 'Frog', 'Giraffe', 'Gopher', 'Grizzly', 'Hedgehog', 'Hippo', 'Hyena', 'Ibex','Ifrit', 'Iguana', 'Jackal', 'Kangaroo', 'Koala', 'Kraken', 'Lemur', 'Leopard', 'Liger', 'Lion', 'Llama', 'Loris', 'Manatee', 'Mink', 'Monkey', 'Moose', 'Narwhal', 'Nyan Cat', 'Orangutan', 'Otter', 'Panda', 'Penguin', 'Platypus', 'Pumpkin', 'Python', 'Quagga', 'Rabbit', 'Raccoon', 'Rhino', 'Sheep', 'Shrew', 'Skunk', 'Squirrel', 'Tiger', 'Turtle', 'Walrus', 'Wolf', 'Wolverine', 'Wombat','Nyancat')

dirname = 'icons'
if os.path.exists(dirname):
    shutil.rmtree(dirname)
os.makedirs(dirname)

for index, icon in enumerate(iconList):
    icon = icon.lower()
    filename = dirname + '/' + icon + '.png'
    url = 'https://ssl.gstatic.com/docs/common/profile/' + icon + '_lg.png'
    print('#%s\tfetching %s' % (index, url))
    urllib.request.urlretrieve(url, filename)

# TODO: write all icons to index.html
