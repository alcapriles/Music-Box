/*
  This file is part of LilyPond, the GNU music typesetter.

  Copyright (C) 1997--2012 Han-Wen Nienhuys <hanwen@xs4all.nl>
  Jan Nieuwenhuizen <janneke@gnu.org>

  LilyPond is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  LilyPond is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with LilyPond.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <complex>

#include "misc.hh"
#include "offset.hh"
#include "warn.hh"

/*
  Return the 2-log, rounded down
*/
int
intlog2 (int d)
{
  assert (d);
  int i = 0;
  while ((d != 1))
    {
      d /= 2;
      i++;
    }

  assert (! (d / 2));
  return i;
}

double
log_2 (double x)
{
  return log (x) / log (2.0);
}

Real
directed_round (Real f, Direction d)
{
  if (d < 0)
    return floor (f);
  else
    return ceil (f);
}

/*
   0 at threshold,  1 at 0, with 1/x falloff.
 */
Real
peak_around (Real epsilon, Real threshold, Real x)
{
  if (x < 0)
    return 1.0;
  return max (- epsilon * (x - threshold) / ((x + epsilon) * threshold), 0.0);
}

/*
  0 at 0,  1 at standard_x, and increasing thereafter.
 */
Real
convex_amplifier (Real standard_x, Real increase_factor, Real x)
{
  return (exp (increase_factor * x / standard_x) - 1.0) / (exp (increase_factor) - 1.0);
}

string
camel_case_to_lisp_identifier (const string &in)
{
  vector<char> out;

  /* don't add '-' before first character */
  out.push_back (char (tolower (in[0])));

  for (size_t inpos = 1; inpos < in.size (); inpos++)
    {
      if (isupper (in[inpos]))
        out.push_back ('-');
      out.push_back ( char (tolower (in[inpos])));
    }

  string result (&out[0], out.size ());
  replace_all (&result, '_', '-');

  return result;
}

Offset
get_point_in_y_direction (Offset orig, Real slope, Real dist, Direction dir)
{
  if (slope == infinity_f)
    return orig + Offset (dir * dist, 0.0);

  Real x = slope == 0.0 ? 1.0 * dir : 1.0 * sign (slope) * dir;
  Real y = slope * x;
  Real angle = atan2 (y, x);

  complex<Real> orig_c (orig[X_AXIS], orig[Y_AXIS]);
  complex<Real> to_move = polar (dist, angle);
  complex<Real> res = orig_c + to_move;

  return Offset (real (res), imag (res));
}