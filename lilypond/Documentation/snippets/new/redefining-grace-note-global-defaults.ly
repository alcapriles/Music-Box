\version "2.17.6"

\header {
  lsrtags = "rhythms"

  texidoc = "
The global defaults for grace notes are stored in the identifiers
@code{startGraceMusic}, @code{stopGraceMusic},
@code{startAcciaccaturaMusic}, @code{stopAcciaccaturaMusic},
@code{startAppoggiaturaMusic} and @code{stopAppoggiaturaMusic}, which
are defined in the file @code{ly/grace-init.ly}.  By redefining them
other effects may be obtained.

"
  doctitle = "Redefining grace note global defaults"
}

startAcciaccaturaMusic = {
  <>(
  \override Flag.stroke-style = #"grace"
  \slurDashed
}

stopAcciaccaturaMusic = {
  \revert Flag.stroke-style
  \slurSolid
  <>)
}

\relative c'' {
  \acciaccatura d8 c1
}

