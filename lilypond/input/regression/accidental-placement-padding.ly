\version "2.17.6"

\header {
  texidoc = "Accidental padding works for all accidentals, including
those modifying the same pitch."
}

\relative c' {
  \override Staff.AccidentalPlacement.padding = #2
  <ces cis>1
  <ces des>1
}
