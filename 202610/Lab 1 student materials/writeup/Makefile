
COURSE=csci141_25f
TARGET=cslinux:/web/faculty/wehrwes/courses/$(COURSE)/

build:
	pandoc lab1.md -s --toc --toc-depth=2 -c ../md.css --to=html5 -o index.html

publish: build
	rsync -avz index.html *.png $(TARGET)/lab1

