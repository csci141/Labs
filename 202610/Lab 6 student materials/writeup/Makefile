
COURSE=csci141_25f
TARGET=cslinux:/web/faculty/wehrwes/courses/$(COURSE)/

build:
	pandoc lab6.md -s --toc --toc-depth=2 --mathjax -c ../md.css --to=html5 -o index.html

publish: build
	rsync -avz index.html *.png ../skeleton/sierpinski.py $(TARGET)/lab6

