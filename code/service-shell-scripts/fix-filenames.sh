ls -v | cat | while read f; do mv -n "$f" $(echo "$f" | sed -e 's/[^A-Za-z0-9._-]/_/g'); done
