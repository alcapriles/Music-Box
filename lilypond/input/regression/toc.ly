\version "2.16.0"

\header {
  texidoc = "A table of contents is included using
@code{\\markuplist \\table-of-contents}. The toc items are added with
the @code{\\tocItem} command. In the PDF backend, the toc items are linked
to the corresponding pages."
}

#(set-default-paper-size "a6")

\book {
  \markuplist \table-of-contents
  \pageBreak

  \tocItem \markup "The first score"
  \score {
    { 
      c'1 \pageBreak
      \mark "A" \tocItem \markup "Mark A"
      d'
    }
  }
  \pageBreak
  \tocItem \markup "The second score"
  \score {
    { e' }
    \header { piece = "Second score" }
  }
}
