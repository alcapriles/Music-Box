%% DO NOT EDIT this file manually; it is automatically
%% generated from LSR http://lsr.dsi.unimi.it
%% Make any changes in LSR itself, or in Documentation/snippets/new/ ,
%% and then run scripts/auxiliar/makelsr.py
%%
%% This file is in the public domain.
\version "2.17.6"

\header {
  lsrtags = "rhythms, tweaks-and-overrides"

  texidoc = "
Sometimes, a time signature should not print the whole fraction (e.g.
7/4), but only the numerator (7 in this case). This can be easily done
by using @code{\\override Staff.TimeSignature.style = #'single-digit}
to change the style permanently. By using @code{\\revert
Staff.TimeSignature.style}, this setting can be reversed. To apply
the single-digit style to only one time signature, use the
@code{\\override} command and prefix it with a @code{\\once}.

"
  doctitle = "Time signature printing only the numerator as a number (instead of the fraction)"
} % begin verbatim


\relative c'' {
  \time 3/4
  c4 c c
  % Change the style permanently
  \override Staff.TimeSignature.style = #'single-digit
  \time 2/4
  c4 c
  \time 3/4
  c4 c c
  % Revert to default style:
  \revert Staff.TimeSignature.style
  \time 2/4
  c4 c
  % single-digit style only for the next time signature
  \once \override Staff.TimeSignature.style = #'single-digit
  \time 5/4
  c4 c c c c
  \time 2/4
  c4 c
}
