/*
  PROJECT: FlowerSoft C++ library
  FILE   : string-convert.hh
*/

#ifndef STRING_CONVERT_HH
#define STRING_CONVERT_HH

#include <cstdarg>
using namespace std;

#include "flower-proto.hh"

/** The functor string_convert handles all conversions to/from string
    (some time, anyway).  The class is quite empty from data view.  */
class String_convert
{
  static int hex2bin (string hex_string, string &bin_string_r);
  static int hex2nibble (Byte byte);
  static Byte nibble2hex_byte (Byte byte);
public:
  static string pad_to (const string &s, size_t length);
  static string bool_string (bool b);
  static string bin2hex (Byte bin_char);
  static string bin2hex (const string &bin_string);
  static int bin2int (const string &bin_string);
  static unsigned bin2unsigned (const string &bin_string);
  static string char_string (char c, int n);
  static int dec2int (const string &dec_string);
  static double dec2double (const string &dec_string);
  static string double_string (double f, char const *fmt = 0);
  static string form_string (char const *format, ...) __attribute__ ((format (printf, 1, 2)));
  static string vform_string (char const *format, va_list args);
  static string hex2bin (const string &str);
  static string int_string (int i, char const *fmt = 0);
  static string unsigned_string (unsigned);
  static string unsigned_long_string (unsigned long);
  static string long_string (long);
  static string int2hex (int i, size_t length_i, char ch);
  static string unsigned2hex (unsigned u, size_t length, char ch);
  static string int2dec (int i, size_t length_i, char ch);
  static string rational_string (Rational);
  static string pointer_string (void const *);
  static string precision_string (double x, int n);
  static string i64_string (I64, char const *fmt = 0);
  static string to_lower (string s);
  static string to_upper (string s);
  static string reverse (string s);
};

#endif // __STRING_CONVERT_HH //
