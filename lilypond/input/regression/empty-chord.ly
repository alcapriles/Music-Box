\version "2.16.0"

\header { texidoc = "Empty chords accept articulations, occupy no time,
                     and leave the current duration unchanged."
        }

\relative c' {
  r4 e8( g <>) ^"sul D" \f \> \repeat unfold 8 { c-. } <>\sfz
  <>\downbow \repeat unfold 2 { c g } c1\> <>\enddecr
}
