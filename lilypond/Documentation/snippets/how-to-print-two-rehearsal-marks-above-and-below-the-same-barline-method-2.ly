%% DO NOT EDIT this file manually; it is automatically
%% generated from LSR http://lsr.dsi.unimi.it
%% Make any changes in LSR itself, or in Documentation/snippets/new/ ,
%% and then run scripts/auxiliar/makelsr.py
%%
%% This file is in the public domain.
\version "2.17.6"

\header {
  lsrtags = "editorial-annotations, expressive-marks, staff-notation, tweaks-and-overrides"

  texidoc = "
This method prints two 'rehearsal marks' - one above the stave and one
below, by creating two voices, adding the Rehearsal Mark engraver to
each voice - without this no rehearsal mark is printed - and then
placing each rehearsal mark UP and DOWN in each voice respectively.

This method (as opposed to method 1) is more complex, but allows for
more flexibility, should it be needed to tweak each rehearsal mark
independently of the other.

"
  doctitle = "How to print two rehearsal marks above and below the same barline (method 2)"
} % begin verbatim


\score {
  \relative c'
  <<
    \new Staff {
      <<
        \new Voice \with {
          \consists Mark_engraver
          \consists "Staff_collecting_engraver"
        }
        { c4 d e f
          \mark \markup { \box A }
          c4 d e f
        }
        \new Voice \with {
          \consists Mark_engraver
          \consists "Staff_collecting_engraver"
          \override RehearsalMark.direction = #DOWN
        }
        { s4 s s s
          \mark \markup { \circle 1 }
          s4 s s s
        }
      >>
    }
  >>
  \layout {
    \context {
      \Score
      \remove "Mark_engraver"
      \remove "Staff_collecting_engraver"
    }
  }
}