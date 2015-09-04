# stringtree-python

[![Build Status](https://travis-ci.org/tomdionysus/stringtree-python.svg?branch=master)](https://travis-ci.org/tomdionysus/stringtree-python)
[![Coverage Status](https://coveralls.io/repos/tomdionysus/stringtree-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/tomdionysus/stringtree-python?branch=master)

StringTree is a fast forward-only tokeniser and partial string matcher, that is, it can:

* Load a dictionary of arbitarty size and record count - e.g. an actual dictionary, an english word list - where each record is associated with a key - e.g. a numeric identifier for the word.
* Parse an arbitary data string in a single pass, finding and storing instances of each item in the dictionary and storing their offsets and associated keys.
* Host a set of strings in such a way as to efficiently match partial input strings against the dictionary

This has become my 'hello world' over the years with any new language. I use it to get to know a language, as implementing it correctly involves many of the usual concepts needed get started coding from the hip (syntax, grammar, classes, public/private instance vars, statics, pass-by value/pass-by-reference etc.) not to mention usual code support skills like how to set up unit tests for this language and environment, etc.

## Testing

    PYTHONPATH=./ py.test

## Demo

    PYTHONPATH=./ python ./examples/demo.py

## Code of Conduct

The StringTree project is committed to the [Contributor Covenant](http://contributor-covenant.org). Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before making any contributions or comments.

## References

* http://docs.python.org
* http://en.wikipedia.org/wiki/Trie