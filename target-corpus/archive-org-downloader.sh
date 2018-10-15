wget -r -H -nc -np -nd -nH -c -A .txt \
    -e robots=off -l1 -i item-ids-pulp.csv \
    -B 'http://archive.org/download/' -P pulpmagazinearchive/
