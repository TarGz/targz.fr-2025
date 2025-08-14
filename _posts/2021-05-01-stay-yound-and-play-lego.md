---
layout: post
title: "Stay yound and play Lego"
seo-title: "Stay yound and play Lego - Digital Art & Experiments | Targz"
description: "Created: June 13, 2022 10:08 AM"
keywords: "digital art, stay yound and play lego, experimental art, creative coding"
date: 2021-05-01
category: bits
tags: [digital-art, experimental]
image: /assets/images/stay_yound_and_play_lego_001.png
redirect_from:
  - /stay-yound-and-play-lego/
  - /stay-yound-and-play-lego
---

Created: June 13, 2022 10:08 AM
Categorie: personnal, practice
date: April 28, 2013
tag: lego

I made a motivational Lego poster that remind me to keep playing Lego

<img src="{{ '/assets/images/stay_yound_and_play_lego_004.png' | relative_url }}" alt="Stay yound and play Lego" style="width: 100%; max-width: 800px; margin: 1rem 0;" />

After having working of my [](https://targz.fr/keepcalm/)I feel inspired to create a Lego version. I wanted to create a poster with a size close to the original [Kepp calm poster](https://www.notion.so/Keep-Calm-8c350f5755c944af80869550d78ecb81?pvs=21). I have build four of this one, 1 for my home, 1 for my office, 1 have been build for my boss at DigitasLbi and 1 for Michael Chaize for his Adobe office.

[Keep Calm](https://www.notion.so/Keep-Calm-8c350f5755c944af80869550d78ecb81?pvs=21)

### FRAME

As no such Lego plate of this size exist I had to find a way. I had an option to build the frame using bricks and plates but it will have been very expensive and heavy. So I choosed to use a piece of wood and blue base plates, they are 32X32 knobs and 25x25 cm so using 3 for the height and 2 for the with gave me a 50x75 frame wich is close enougth to my objective and doesn't require any cuting.

<img src="{{ '/assets/images/stay_yound_and_play_lego_002.png' | relative_url }}" alt="Stay yound and play Lego" style="width: 100%; max-width: 800px; margin: 1rem 0;" />

### COST

Once the design was made I tried to optimize the number of bricks because that can make a big difference in term of price. I'm using [Lego pick a brick](http://shop.lego.com/en-FR/Pick-A-Brick-ByTheme) to order the bricks. Concidering a "pixel" from the design as a 1x1 plate. A 1x1 Lego white plate cost 0,08 € where a 2X10 Lego white plate cost 0,26€. That give a cost per pixel of 0,013€ wich is much affordable. The design as 1720 colored pixel, if I had use 1x1 bricks the total cost of the bricks will have been around 140€.

### PRICE OPTIMISATION

Figuring out what could be the best size of bricks and where to use them was tricky so I have write a script to sort this out. The script load an image of the design where each pixel represent an 1x1 brick, then he loop throuh a list of bricks and recursivly starting by the largest brick and try to fit them is the design. Next he move to a smaller brcik and so on till the smallest brick of the list. This minize the number of bricks and by concequence the final price of the frame. Using this technics I have reduce the number of bricks from 1720 to 273.

<img src="{{ '/assets/images/stay_yound_and_play_lego_003.png' | relative_url }}" alt="Stay yound and play Lego" style="width: 100%; max-width: 800px; margin: 1rem 0;" />

### BUILD YOUR OWN

I'm open sourcing a part of the projet so anybody can build his own. The script is not part of the source because it's still buggy and miss some features. The BOM, the instruction and the [LeoCad](http://www.leocad.org/trac) sources are free to [download and published on github.](https://github.com/TarGz/stay-young-and-play-lego) It's published under "Creative Commons Attribution-NonCommercial 4.0 International Public License" meaning you can use the design but never use it in any commercial maner. If you build one please mention me and please point to the git repository, I would appreciate if you tweet me a pict of your finished frame.

[https://www.notion.so](https://www.notion.so)


<img src="{{ '/assets/images/stay_yound_and_play_lego_004.png' | relative_url }}" alt="Stay yound and play Lego" style="width: 100%; max-width: 800px; margin: 1rem 0;" />

Source files available on GitHub [https://github.com/TarGz/stay-young-and-play-lego](https://github.com/TarGz/stay-young-and-play-lego)