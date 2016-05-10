%% DO NOT EDIT this file manually; it is automatically
%% generated from LSR http://lsr.dsi.unimi.it
%% Make any changes in LSR itself, or in Documentation/snippets/new/ ,
%% and then run scripts/auxiliar/makelsr.py
%%
%% This file is in the public domain.
\version "2.17.6"

\header {
  lsrtags = "pitches, tweaks-and-overrides"

  texidoc = "
If you have more than one voice on the staff, setting octavation in one
voice will transpose the position of notes in all voices for the
duration of the ottava bracket. If the ottavation is only intended to
apply to one voice, the middleCPosition and ottava bracket may be set
explicitly.  In this snippet, the bass clef usually has middleCPosition
set to 6, six positions above the center  line, so in the 8va portion
middleCPosition is 7 positions (one octave) higher still.

"
  doctitle = "Adding an ottava marking to a single voice"
} % begin verbatim

{
  \clef bass
  << { <g d'>1~ q2 <c' e'> }
  \\
    {
      r2.
      \set Staff.ottavation = #"8vb"
      \once \override Staff.OttavaBracket.direction = #DOWN
      \set Voice.middleCPosition = #(+ 6 7)
      <b,,, b,,>4 ~ |
      q2
      \unset Staff.ottavation
      \unset Voice.middleCPosition
      <c e>2
    }
  >>
}