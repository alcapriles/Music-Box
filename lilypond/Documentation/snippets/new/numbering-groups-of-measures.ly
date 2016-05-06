\version "2.17.7"

\header {
  lsrtags = "contexts-and-engravers, editorial-annotations, repeats, staff-notation"

  texidoc = "
This snippet demonstrates the use of the @code{Measure_counter_engraver} to
number groups of successive measures.  Any stretch of measures may be numbered,
whether consisting of repetitions or not.

The engraver must be added to the appropriate context.  Here, a @code{Staff}
context is used; another possibility is a @code{Dynamics} context.

The counter is begun with @code{\\startMeasureCount} and ended with
@code{\\stopMeasureCount}.  Numbering will start by default with @code{1}, but
this behavior may be modified by overriding the @code{count-from} property.

When a measure extends across a line break, the number will appear twice, the
second time in parentheses.

"
  doctitle = "Numbering groups of measures"
}

\layout {
  \context {
    \Staff
    \consists #Measure_counter_engraver
  }
}

\new Staff {
  \startMeasureCount
  \repeat unfold 7 {
    c'4 d' e' f'
  }
  \stopMeasureCount
  \bar "||"
  g'4 f' e' d'
  \override Staff.MeasureCounter.count-from = #2
  \startMeasureCount
  \repeat unfold 5 {
    g'4 f' e' d'
  }
  g'4 f'
  \bar ""
  \break
  e'4 d'
  \repeat unfold 7 {
    g'4 f' e' d'
  }
  \stopMeasureCount
}
