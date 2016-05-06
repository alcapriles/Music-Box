\version "2.17.6"
\header {
  texidoc = "Beams can be allowed to collide with grobs by overriding
the collision-interfaces property."
}

\relative c' {
  c8 [ des' ]
  \once \override Beam.collision-interfaces = #'(beam-interface
                                                   clef-interface
                                                   ;inline-accidental-interface
                                                   key-signature-interface
                                                   note-head-interface
                                                   time-signature-interface)
  c,8 [ des'! ]
  c, [ \key des \major d ]
  \once \override Beam.collision-interfaces = #'(beam-interface
                                                   clef-interface
                                                   inline-accidental-interface
                                                   ;key-signature-interface
                                                   note-head-interface
                                                   time-signature-interface)
  c [ \key c \major d ]
  g [ \grace { a [ d ] } g, ]
  \once \override Beam.collision-interfaces = #'(;beam-interface
                                                   clef-interface
                                                   inline-accidental-interface
                                                   key-signature-interface
                                                   note-head-interface
                                                   time-signature-interface)
  g [ \grace { a [ d ] } g, ]
}
