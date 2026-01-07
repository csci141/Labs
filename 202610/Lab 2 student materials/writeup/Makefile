
COURSE=csci141_25f
TARGET=cslinux:/web/faculty/wehrwes/courses/$(COURSE)/

build:
	pandoc lab2.md -s --toc --toc-depth=2 --mathjax -c ../md.css --to=html5 -o index.html

publish: build
	rsync -avz index.html ../skel/*.py *.png linuxref.pdf $(TARGET)/lab2

