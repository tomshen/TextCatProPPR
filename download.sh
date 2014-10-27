#!/bin/sh
wget http://qwone.com/~jason/20Newsgroups/20news-bydate-matlab.tgz
tar xvf 20news-bydate-matlab.tgz
mv 20news-bydate/matlab data
rm -rf 20news-bydate 20news-bydate-matlab.tgz
