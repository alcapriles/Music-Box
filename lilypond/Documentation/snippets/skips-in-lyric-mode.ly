%% DO NOT EDIT this file manually; it is automatically
%% generated from LSR http://lsr.dsi.unimi.it
%% Make any changes in LSR itself, or in Documentation/snippets/new/ ,
%% and then run scripts/auxiliar/makelsr.py
%%
%% This file is in the public domain.
\version "2.16.0"

\header {
  lsrtags = "really-simple, rhythms, vocal-music"

  texidoc = "
The @code{s} syntax for skips is only available in note mode and chord
mode. In other situations, for example, when entering lyrics, using the
@code{\\skip} command is recommended.

"
  doctitle = "Skips in lyric mode"
} % begin verbatim


<<
  \relative c'' { a1 | a }
  \new Lyrics \lyricmode { \skip 1 bla1 }
>>