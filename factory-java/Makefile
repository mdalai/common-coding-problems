
# https://www.tutorialspoint.com/design_pattern/factory_pattern.htm

# Option-1: build all source code into build/ dir
# and run by pointing the main entry
build1:
	javac -d build src/com/mingat/libshape/*.java
run1:
	java -cp .:build:**/*.class FactoryDemo


# Option-2: build all source code into build/ dir 
# create a JAR, libshape.jar, in the lib/ dir
# build TestFactory which depends on the JAR in the bin/ dir
# and run by pointing the main entry
build2:
	javac -d build src/com/mingat/libshape/*.java
	cd build/  &&  jar cvf ../lib/libshape.jar .
	javac -cp .:lib/libshape.jar -d bin src/TestFactory.java

run2:
	cd bin/  &&  java -cp .:../lib/libshape.jar TestFactory


clean:
	rm -rf build/*
	rm -rf lib/*