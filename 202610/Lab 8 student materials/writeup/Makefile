
COURSE=csci141_25f
TARGET=cslinux:/web/faculty/wehrwes/courses/$(COURSE)/

build:
	pandoc lab7.md -s --toc --toc-depth=2 --mathjax -c ../md.css --to=html5 -o index.html

publish: build
	rsync -avz index.html *.png ../skeleton/plot_earthquakes.py ../skeleton/earth.png ../skeleton/earthquakes.csv ../skeleton/words.txt $(TARGET)/lab7

