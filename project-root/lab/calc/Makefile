demo: main.o add.o num_to_str.o read.o
	ld -macos_version_min 14.0.0 -o demo main.o add.o num_to_str.o read.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e main -arch arm64

main.o: src/main/main.s
	as -g -o main.o src/main/main.s  # Add -g flag here

add.o: src/features/math/shared/add.s
	as -g -o add.o src/features/math/shared/add.s  # Add -g flag here

num_to_str.o: src/features/shared/num_to_str.s
	as -g -o num_to_str.o src/features/shared/num_to_str.s  # Add -g flag here

read.o: src/features/io/read.s
	as -g -o read.o src/features/io/read.s  # Add -g flag here

clean:
	rm -f *.o demo
