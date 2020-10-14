#!/usr/bin/env python

LOWER_ALPHA = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHA = LOWER_ALPHA.upper()
ALPHA = LOWER_ALPHA + UPPER_ALPHA

LOWER_ACCENTS = "âêîôûäëïöüàùèéç"
UPPER_ACCENTS = LOWER_ACCENTS.upper()
ACCENTS = LOWER_ACCENTS + UPPER_ACCENTS

LOWER_ACCENTS_TRANS = str.maketrans(LOWER_ACCENTS, "aeiouaeiouaueec")
UPPER_ACCENTS_TRANS = str.maketrans(UPPER_ACCENTS, "AEIOUAEIOUAUEEC")
ACCENTS_TRANS = LOWER_ACCENTS_TRANS | UPPER_ACCENTS_TRANS

NUMS = "0123456789"
PUNCTS = ".,:;?!"
QUOTES = "\"'`"
BRACKETS = "(){}[]"

# \n -> line feed (LF)
# \r -> carriage return (CR)
# \t -> tab (TAB)
# \v -> vertical tab (VT)
# \f -> formfeed (FF)
# \b -> backspace (BS)
SPACES = " \n\r\t\v\f\b"