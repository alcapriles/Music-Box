\version "2.16.0"

\header{
  texidoc="Beams in unnatural direction, have shortened stems, but do not look too short."
}
\layout{ ragged-right = ##t }


\relative c'{
  \stemUp
  f'4  f8[ f]  f16[ f]  f32[ f]  f64[ f]  f128[ f] 
}
