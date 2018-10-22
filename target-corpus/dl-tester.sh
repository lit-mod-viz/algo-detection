wget -r -H -nc -np -nd -nH -c -nc -A .txt \
    -R .tar,.zip -e robots=off -l1 -i test-id.csv \
    -B 'http://archive.org/download/' -P test-dl/
