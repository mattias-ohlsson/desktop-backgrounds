# Makefile for source rpm: desktop-backgrounds
# $Id: Makefile,v 1.1 2004/09/09 04:07:00 cvsdist Exp $
NAME := desktop-backgrounds
SPECFILE = $(firstword $(wildcard *.spec))

TARGETS = generate-default-background

.PHONY :: generate-default-background

generate-default-background:
	cp default-background-fc.png default-background.png
	if echo $(COLLECTION) | grep -q -e "^dist-[^-]*E\($$\|-\)"; then cp default-background-rhel.png default-background.png; fi

include ../common/Makefile.common
