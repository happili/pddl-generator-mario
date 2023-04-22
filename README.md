# pddl-generator-mario

<h3>Problem generator for Super Mario Bros.</h3>

This generator uses a text database of the Super Mario Bros. (NES 1985) levels to generate Planning problems written in PDDL+. The problems are compatile with the domain formalisation associated written in PDDL+.

<h3>How to use</h3>

Clone the repository which contains most of the database of the levels (represent by the .txt files). You also need to have Pythom 3 installed. No further dependencies are necessary. 

To run the generator, run this command from the directory 

python generator.py world(integer)-level(integer) level-length level-height 

For example, to generate the first 10 by 20 tiles of the World 1-1 level, we run

python generator.py 1-1 20 10


The generator will then print out as output the problem.

Either copy paste it, or directly save it into a file with the > command as seen below. (This might cause issues).

python generator.py world(integer)-level(integer) level-length level-height > problem.pddl

