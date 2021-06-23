"""Small compiler script to convert sass file to css"""
import sass
sassed = sass.compile(filename='style.sass')
with open('style.css', 'w') as css_file:
    css_file.write(sassed)