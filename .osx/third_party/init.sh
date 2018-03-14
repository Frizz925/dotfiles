#!/bin/sh

URLS=""
URLS="${URLS} https://github.com/chriskempson/base16-iterm2"

for URL in ${URLS}; do
	git clone ${URL} --depth=1 &
done

