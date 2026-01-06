
COURSE=csci141_25f
TARGET=cslinux:/web/faculty/wehrwes/courses/$(COURSE)/
CSS=https://facultyweb.cs.wwu.edu/~wehrwes/md.css
build:
	pandoc lab3.md -s --toc --toc-depth=2 --mathjax -c ${CSS} --to=html5 -o index.html

publish: build
	rsync -avz index.html *.png $(TARGET)/lab3

