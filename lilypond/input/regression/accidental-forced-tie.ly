\version "2.16.0"

\header {
  texidoc = "Accidentals can be forced with ! and ? even if the
notes are tied.  Cautionary accidentals applied to tied notes
after a bar line are valid for the whole measure.
"
}

\layout {
  ragged-right = ##t
}

\relative c'' {
  gis4 ~ gis!~ gis? r4
  fis1 ~
  fis!2 fis ~
  fis?2 fis
}

