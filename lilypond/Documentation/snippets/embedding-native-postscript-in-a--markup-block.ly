%% DO NOT EDIT this file manually; it is automatically
%% generated from LSR http://lsr.dsi.unimi.it
%% Make any changes in LSR itself, or in Documentation/snippets/new/ ,
%% and then run scripts/auxiliar/makelsr.py
%%
%% This file is in the public domain.
\version "2.16.0"

\header {
  lsrtags = "editorial-annotations, really-cool, specific-notation, text"

  texidoc = "
PostScript code can be directly inserted inside a @code{\\markup}
block.

"
  doctitle = "Embedding native PostScript in a \\markup block"
} % begin verbatim


% PostScript is a registered trademark of Adobe Systems Inc.

\relative c'' {
  a4-\markup { \postscript #"3 4 moveto 5 3 rlineto stroke" }
  -\markup { \postscript #"[ 0 1 ] 0 setdash 3 5 moveto 5 -3 rlineto stroke " }

  b4-\markup { \postscript #"3 4 moveto 0 0 1 2 8 4 20 3.5 rcurveto stroke" }
  s2
  a'1
}
