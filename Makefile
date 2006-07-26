# Makefile for source rpm: desktop-backgrounds
# $Id: Makefile,v 1.2 2004/09/30 16:00:01 alexl Exp $
NAME := desktop-backgrounds
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
