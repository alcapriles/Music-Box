\version "2.16.0"

\header {
  texidoc = "Having markup after a non-staff line doesn't confuse
the page layout engine."
}

#(set-default-paper-size "a6")

\book {
  \score {
  <<
     \new Staff <<
       \new Voice = "asdf" { c' d' e' f' }
     >>
     \new Lyrics \lyricsto "asdf" \lyricmode { a b c d }
  >>
  }
  \markup "next song"
  \score {
    <<
      \new Lyrics \lyricmode {la1 la }
      \new Staff \new Voice { a'1 a'1 }
  >>
  }
}

