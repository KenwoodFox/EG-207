# An example makefile to generate a pdf slideshow from markdown
# Uses pandoc, beamer
#
# Ideas from this video https://youtu.be/dum7q6UXiCE
#
# Team Gold, SNHU

# Get vars
hash := $(shell git describe --abbrev=8 --always --tags --dirty)
pwd = $(shell pwd)
builddir = $(pwd)/_build

# Do everything
all: generate_pres

# Generate artifacts and output binaries
generate_pres:
	# Premake relevant dirs
	mkdir -p $(builddir)/temp
	mkdir -p $(builddir)/pdf

	# Copy all presentations to _build
	cp -r presentations/* $(builddir)/temp

	# Update the build-hash
	find $(builddir)/temp -type f -name '*.md' -execdir sed -i "s/&hash/$(hash)/" {} \;

	# Convert all presentations to pdf
	find $(builddir)/temp -type f -name '*.md' -execdir pandoc {} -t beamer -o $(builddir)/pdf/{}.pdf \;

	# Clean presentaiton names 
	cd $(builddir)/pdf/ && prename '.md.pdf' '.pdf' *.md.pdf
