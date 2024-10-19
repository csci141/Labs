
COURSE=csci141_23w
TARGET=cslinux:/web/faculty/wehrwes/courses/$(COURSE)/

build:
	pandoc lab4.md -s --toc --toc-depth=2 --mathjax -c ../md.css --to=html5 -o index.html

publish: build
	rsync -avz index.html *.png $(TARGET)/lab4

