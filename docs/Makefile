# An example makefile to generate a pdf slideshow from markdown
# Uses pandoc, beamer
#
# Ideas from this video https://youtu.be/dum7q6UXiCE
#
# Team Gold, SNHU

# Get vars
hash := $(shell git describe --abbrev=6 --always --tags --dirty)
builddate := $(shell date +"%m-%d-%y")
pwd = $(shell pwd)
builddir = $(pwd)/_build

# Do everything
all: generate_pres clean_filenames

# Generate artifacts and output binaries
generate_pres:
	# Premake relevant dirs
	mkdir -p $(builddir)/temp
	mkdir -p $(builddir)/pdf

	# Copy all presentations to _build
	cp -r presentations/* $(builddir)/temp

	# Update the build-hash
	find $(builddir)/temp -type f -name '*.md' -execdir sed -i "s/&hash/$(hash)/" {} \;

	# Update the date
	find $(builddir)/temp -type f -name '*.md' -execdir sed -i "s/&date/$(builddate)/" {} \;

	# Convert all presentations to pdf
	find $(builddir)/temp -type f -name '*.md' -execdir pandoc {} -t beamer -V colortheme:crane -o $(builddir)/pdf/{}.pdf \;

clean_filenames:
	# Clean presentaiton names 
	cd $(builddir)/pdf/ && rename 's/.md.pdf$$/.pdf/' *.md.pdf
