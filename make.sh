# mkdir -p textbook
platex main
bibtex main
mendex main
platex main
platex main
dvipdfmx main.dvi
# latex2html -init_file latex2html-init -dir textbook textbook

# platex figures/tikz.tex
# dvipdfmx figures/tikz.tex
