\version "2.17.6"

\header {
  texidoc = "@var{alignment-distances} applies to the toplevel
VerticalAlignment but not to BassFigureAlignment.  The 4 in
the bass figure line should be directly below the 6."
}

\score {
 <<
   \new Staff {
     \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details #'((alignment-distances . (15)))
     c'4
   }
   \new Staff <<
     { d'4 }
     \figures { <6 4>4 } >> >>
 }
