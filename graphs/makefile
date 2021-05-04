DOT := $(wildcard *.dot)
TEX := $(patsubst %.dot, %.tex, $(DOT))

all: $(TEX)

%.tex: %.dot
	dot2tex $*.dot -o $*.tex --figonly --autosize
