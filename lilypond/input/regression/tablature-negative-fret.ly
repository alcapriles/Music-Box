\version "2.16.0"
#(ly:set-option 'warning-as-error #f)
#(ly:expect-warning (_ "Requested string for pitch requires negative fret: string ~a pitch ~a") 1 "#<Pitch c' >")
#(ly:expect-warning (_ "Ignoring string request and recalculating."))
#(ly:expect-warning (_ "Negative fret for pitch ~a on string ~a") "#<Pitch c' >" 1)
#(ly:expect-warning (_ "Requested string for pitch requires negative fret: string ~a pitch ~a") 1 "#<Pitch c' >")
#(ly:expect-warning (_ "Ignoring note in tablature."))



% #(ly:expect-warning (ly:translate-cpp-warning-scheme "Markup depth exceeds maximal value of %d; Markup: %s") 1024 "recursive-explosion-markup")

\header {

  texidoc = "
Negative fret numbers calculated due to assigning a string number
can be displayed, ignored, or recalculated.  Here we should have
all three cases demonstrated.
"

}

myMusic = \relative c'  {
  <c\1>1 ^\markup { recalculate }
  \set TabStaff.handleNegativeFrets = #'include
  <c\1>1 ^ \markup { include }
  \set TabStaff.handleNegativeFrets = #'ignore
  <c\1>1 ^ \markup { ignore }
}

\score {
  <<
    \new Staff {
      \clef "treble_8"
      \textLengthOn
      \myMusic
    }
    \new TabStaff {
      \myMusic
    }
  >>
}
