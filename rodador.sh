#!/bin/bash


max=160

echo "C-ij"
echo "C-ij" >> saida.txt

for i in $(seq 0 $max); do
	x=$((100*i))
	./matmul $x 0 >> saida.txt
done

echo "C-ji"
echo "C-ji" >> saida.txt

for i in $(seq 1 $max); do
        x=$((100*i))
        ./matmul $x 1 >> saida.txt
done

echo "Fortran-ij"
echo "Fortran-ij" >> saida.txt

for i in $(seq 0 $max); do
        x=$((100*i))
        ./matmulf $x 0 >> saida.txt
done

echo "Fortran-ji"
echo "Fortran-ji" >> saida.txt

for i in $(seq 0 $max); do
        x=$((100*i))
        ./matmulf $x 1 >> saida.txt
done

echo "pronto"
















