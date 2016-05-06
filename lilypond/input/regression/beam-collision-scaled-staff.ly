\version "2.17.6"
\header {
  texidoc = "Beam collisions are resistant to scaled down staves."
}

\new Staff \with {
  fontSize = #-3
  \override StaffSymbol.staff-space = #(magstep -3)
  \override StaffSymbol.thickness = #(magstep -3) }
<<
  \relative c'' { e16[ f] }
  \\
  \relative c''' { \autoBeamOff g b }
>>
