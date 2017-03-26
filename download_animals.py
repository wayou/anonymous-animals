#!/usr/bin/env pyhon3
import os
import shutil
import urllib.request

# the list comes from
# https://evert.meulie.net/faqwd/complete-list-anonymous-animals-on-google-drive-docs-sheets-slides/
iconList = ('Alligator', 'Anteater', 'Armadillo', 'Auroch', 'Axolotl',
            'Badger', 'Bat', 'Beaver', 'Buffalo', 'Camel', 'Capybara',
            'Chameleon', 'Cheetah', 'Chinchilla', 'Chipmunk', 'Chupacabra',
            'Cormorant', 'Coyote', 'Crow', 'Dingo', 'Dinosaur', 'Dolphin',
            'Duck', 'Elephant', 'Ferret', 'Fox', 'Frog', 'Giraffe', 'Gopher',
            'Grizzly', 'Hedgehog', 'Hippo', 'Hyena', 'Ibex', 'Ifrit', 'Iguana',
            'Jackal', 'Kangaroo', 'Koala', 'Kraken', 'Lemur', 'Leopard',
            'Liger', 'Llama', 'Manatee', 'Mink', 'Monkey', 'Moose', 'Narwhal',
            'NyanCat', 'Orangutan', 'Otter', 'Panda', 'Penguin', 'Platypus',
            'Pumpkin', 'Python', 'Quagga', 'Rabbit', 'Raccoon', 'Rhino',
            'Sheep', 'Shrew', 'Skunk', 'Squirrel', 'Tiger', 'Turtle', 'Walrus',
            'Wolf', 'Wolverine', 'Wombat')

dirname = 'icons'
if os.path.exists(dirname):
    shutil.rmtree(dirname)
os.makedirs(dirname)

html_icon_list = ''

for index, icon in enumerate(iconList):
    icon = icon.lower()
    filename = dirname + '/' + icon + '.png'
    url = 'https://ssl.gstatic.com/docs/common/profile/' + icon + '_lg.png'
    print('#%s\tfetching %s' % (index, url))
    try:
        html_icon_list = html_icon_list + '<li class="animal-item"><img src="' + filename + '" alt="' + icon + '" title="' + icon + '"></li>\n'
        urllib.request.urlretrieve(url, filename)
    except Exception:
        print('#%s\tfailed %s' % (index, url))

html_wrapper = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>anonymous animals from google docs</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body,ul,li{
                margin: 0;
                padding: 0;
            }
            body{
                background-color: #484343;
            }
            ul.animal-list{
                list-style: none;
                text-align: center;
            }
            .animal-item{
                width: 100px;
                display: inline-block;
            }
            .animal-item img{
                width: 100%%;
            }
        </style>
    </head>
    <body>
        <div id="app">
            <ul class="animal-list">%s</ul>
        </div>
    </body>
</html>
"""
html_str = html_wrapper % html_icon_list

Html_file = open("index.html", "w")
Html_file.write(html_str)
Html_file.close()
