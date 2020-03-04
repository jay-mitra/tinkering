mkdir testing
cd testing/
touch test.txt
ls -la
echo "line1" >> test.txt
echo "line2" >> test.txt
cat test.txt
for i in {3..12}; do echo "line$i" >> test.txt ; done
cat test.txt
head -n 3 test.txt
tail -n 5 test.txt
wc -l test.txt
