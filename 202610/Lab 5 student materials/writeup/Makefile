
COURSE=csci141_25f
TARGET=cslinux:/web/faculty/wehrwes/courses/$(COURSE)/

build:
	pandoc lab5.md -s --toc --toc-depth=2 --mathjax -c ../md.css --to=html5 -o index.html

publish: build
	rsync -avz index.html *.png ../solution/turtleshape_test.py $(TARGET)/lab5

