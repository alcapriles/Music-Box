\version "2.16.0"

\header {
  lsrtags = "rhythms"
  texidoc = "
Beat grouping within a measure is controlled by the context property
@code{beatStructure}.  Values of @code{beatStructure} are
established for many time signatures in
@file{scm/time-signature-settings.scm}.  Values of @code{beatStructure}
can be changed or set with @code{\set}.
Alternatively, @code{\time} can be used to both
set the time signature and establish the beat structure.
For this, you specify the internal grouping of beats in a measure
as a list of numbers (in Scheme syntax) before the time signature.

@code{\time} applies to the @code{Timing} context, so it will not
reset values of @code{beatStructure} or @code{baseMoment} that are set
in other lower-level contexts, such as @code{Voice}.

If the @code{Measure_grouping_engraver} is included
in one of the display contexts, measure grouping signs will be
created.  Such signs ease reading rhythmically complex modern music.
In the example, the 9/8 measure is grouped in two different
patterns using the two different methods, while the 5/8 measure
is grouped according to the default setting in
@file{scm/time-signature-settings.scm}:
"
  doctitle = "Conducting signs, measure grouping signs"
}


\score {
  \new Voice \relative c'' {
    \time 9/8
    g8 g d d g g a( bes g) |
    \set Timing.beatStructure = #'(2 2 2 3)
    g8 g d d g g a( bes g) |
    \time #'(4 5) 9/8
    g8 g d d g g a( bes g) |
    \time 5/8
    a4. g4 |
  }
  \layout {
    \context {
      \Staff
      \consists "Measure_grouping_engraver"
    }
  }
}