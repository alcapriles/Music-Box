\version "2.16.0"
#(ly:set-option 'warning-as-error #f)
#(ly:expect-warning (_ "unterminated tie"))
#(ly:expect-warning (_ "unterminated tie"))

\header
{

  texidoc =
  "when @code{tieWaitForNote} is set, the right-tied note does not
 have to follow the lef-tied note directly. When @code{tieWaitForNote}
 is set to false, any tie will erase all pending ties."
  
}

\paper { ragged-right =  ##t }
\relative c' {
  c~ e~ g~ <c, e g>
  \set tieWaitForNote = ##t
  c~ e~ g~ <c, e g>

  <c c'> ~

  \set tieWaitForNote = ##f
  <c e> ~
  <c e c'>

}
