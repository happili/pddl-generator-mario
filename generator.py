import sys

#print if command is not in the correct format and size

if len(sys.argv) < 4:
   print("Run the file as follows : {} <world(integer)-level(integer)> <level-length> <level-height> > <problem-file-name>.pddl")
   sys.exit(-1)

world = "world" + str(sys.argv[1]) + ".txt"

### take data from the comand line and the .txt file

with open(world) as f:
    lines = f.readlines()



if int(sys.argv[2]) > len(lines):
 level_length = len(lines)
else:
   level_length = int(sys.argv[2])

if int(sys.argv[3]) > 13 :
 level_height = 13
else:
   level_height = int(sys.argv[3])



level = []
cols = []


blockcount = 1 
aircount = 1

objects = []
air_blocks = []

init = []



# stores in 2D array our level / iterate through level (with chosen size)

for i in range(level_length):
    for j in range(level_height):  
        cols.append(lines[i][j])
        if lines[i][j] == 'g' or lines[i][j] == 'k':
            continue
        elif lines[i][j] == '.':
            air_blocks.append('a'+str(aircount))
            init.append('(= (block-x a'+str(aircount)+') '+str(i+1)+'.0)')
            init.append('(= (block-y a'+str(aircount)+') '+str(j+1)+'.0)')
            aircount += 1
        else:
            objects.append('b'+str(blockcount))
            init.append('(= (block-x b'+str(blockcount)+') '+str(i+1)+'.0)')
            init.append('(= (block-y b'+str(blockcount)+') '+str(j+1)+'.0)')
            blockcount += 1


    level.append(cols)
    cols = []

##### we print the problem with simple print statements (and we use the arrays created above to print out the initialised states)


print('(define (problem problem_name)\n\
    (:domain supermario_nes)\n\
    (:objects'
      )
print('       ', end = ' ')
for element in air_blocks:
    print(element, end = ' ')
print('- air')
print('       ', end = ' ')
for element in objects:
    print(element, end = ' ')
print('- blocks')
print('    )\n\
    (:init')

for element in init:
    print('        ' + element)

print('        (= (velocity-right) 0.0)\n\
        (= (velocity-left) 0.0)\n\
        (= (velocity-height) 0.0)\n\
        (= (y2) 3.0)\n\
        (= (x) 1.0)\n\
      \n\
        (= (d-jumped) 0.0)\n\
        (not (pressing-right))\n\
        (not (pressing-left))\n\
        (not (pressing-a))\n\
        (not (falling))\n\
        (not (reached))\n\
    )\n\
    (:goal\n\
        (and\n\
            (> (x) '+str(level_length - 1)+')\n\
            ;(< (y2) 2.1) \n\
            (= (velocity-right) 0.0)\n\
            (= (velocity-left) 0.0)\n\
            (= (velocity-height) 0.0)\n\
        )\n\
    )\n\
)',end='')