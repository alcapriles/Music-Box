\header
{
  texidoc = "Beamlets in grace notes remain readable."
}

\version "2.17.28"
\layout {
  ragged-right = ##t
}

\relative c'
\context Staff {
  f1 \grace { a'8 f16 } g1
}
