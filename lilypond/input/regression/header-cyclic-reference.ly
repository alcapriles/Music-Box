\version "2.16.0"
#(ly:set-option 'warning-as-error #f)
#(ly:expect-warning (_ "Recursive definition of property ~a detected!") 'header:title)
#(ly:expect-warning (_ "Recursive definition of property ~a detected!") 'header:composer)

\header {
  texidoc = "Cyclic references in header fields should cause a warning, but
not crash LilyPond with an endless loop"

  title = \markup {Cyclic reference to \fromproperty #'header:title }

  composer = \markup {Cyclic reference to \fromproperty #'header:temp }
  temp = \markup {Cyclic reference to \fromproperty #'header:composer }
}
\score {
  { c' d' e' f' }
}
