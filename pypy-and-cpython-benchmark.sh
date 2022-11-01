echo "PyPy And CPython Benchmark"
echo "--------------------------"
echo ""

echo "KERNEL VERSION"
uname -a
echo ''

echo "PYTHON VERSION"
python3 --version
echo ''

echo "PyPy VERSION"
pypy --version
echo ''

echo "---- Python ----"
for var in 5 10 15 20 25 30 35 40
do
echo "Fibonacci for $var"
python3 fibonacci.py $var
echo ''
done

echo "----  PyPy  ----"
for var in 5 10 15 20 25 30 35 40
do
echo "Fibonacci for $var"
pypy fibonacci.py $var
echo ''
done