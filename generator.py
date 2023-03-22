import sys

with open('world1-1.txt') as f:
    lines = f.readlines()



if int(sys.argv[1]) > len(lines):
 level_length = len(lines)
else:
   level_length = int(sys.argv[1])

if int(sys.argv[2]) > 13 :
 level_height = 13
else:
   level_height = int(sys.argv[2])



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

#print(init)
# print(objects)
# print(air_blocks)
#print(level) ### print our level (with chosen size)

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
    print('       ' + element)

print('        (= (velocity-right) 0.0)\n\
        (= (velocity-left) 0.0)\n\
        ;(= (velocity-fall) 0.0)\n\
        (= (velocity-height) 0.0)\n\
        (= (y2) 2.0)\n\
        (= (x) 1.0)\n\
      \n\
        (= (d-jumped) 0.0)\n\
        (not (pressing-right))\n\
        (not (pressing-left))\n\
        (not (pressing-a))\n\
        (not (falling))\n\
        (not (reached))\n\
    )\n\
\n\
    (:goal\n\
        (and\n\
            (>= (x) 6.0)\n\
            (< (y2) 2.1) \n\
            (= (velocity-right) 0.0)\n\
            (= (velocity-left) 0.0)\n\
            (= (velocity-height) 0.0)\n\
        )\n\
    )\n\
\n\
)')