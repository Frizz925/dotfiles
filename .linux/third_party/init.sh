#!/bin/sh

URLS=""
URLS="${URLS} https://github.com/aaron-williamson/base16-gnome-terminal"

for URL in ${URLS}; do
	git clone ${URL} --depth=1 &&
done

