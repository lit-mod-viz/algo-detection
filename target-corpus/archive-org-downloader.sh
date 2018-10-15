wget -r -H -nc -np -nd -nH -A .txt \
    -R .tar,.zip -e robots=off -l1 -i item-ids-pulp.csv \
    -B 'http://archive.org/download/' -P pulpmagazinearchive/
