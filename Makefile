# Makefile for source rpm: desktop-backgrounds
# $Id$
NAME := desktop-backgrounds
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
