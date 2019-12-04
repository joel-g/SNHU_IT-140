# Joel Guerra
# IT-140
# 12-3-2019
# Project 4


import re

#Paragraph provided for search and replace
lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

# prints number of non-alphanumeric characters
occurrance_non_alpha = re.findall(r"/W", lorem_ipsum) 
print(len(occurrance_non_alpha)) 

# prints number occurances of sit-amet or sit:amet
occurrance_sit_amet = re.findall(r"(sit[-:]amet)", lorem_ipsum)
print(len(occurrance_sit_amet)) 

# replace all occurances of sit-amet or sit:amet with sit-amet
replace_results = re.sub(r"(sit[-:]amet)", "sit amet", lorem_ipsum)

# print out number of occurances of "sit amet"
occurrance_sit_amet = re.findall(r"(sit amet)", replace_results)
print(len(occurrance_sit_amet))
