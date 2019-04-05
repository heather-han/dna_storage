#Applied Comparative Genomics Project


#import tools
#note that I technically did not use binascii in the code
#the parts commented out have the ability to just use the built in "string.hex()"
import binascii

#note that I simply use random names for variables, many times just
#adding letters until the full "word" is acheived
# i.e. for example: beeth -> beethov -> beethoven

#open files
beeth = open ('Beethoven_Sonata_Emin_op90_2nd_movement.ogg', 'rb')
bee = open('beethoven.txt', 'w')
beegen = open('beethoven_genomic.txt', 'w')
lec = open('L15singlecell.pdf', 'rb')
lect = open('lecture.txt', 'w')
lecgen = open('lecture_genomic.txt', 'w')

#read bits & write to files
with beeth:
    beethov = beeth.read()
##    hexa = binascii.hexlify(beethov)
    hexa = beethov.hex()
    dec = int(hexa, 16)
    beethoven = bin(dec)[2:].zfill(8)
bee.write(beethoven)


with lec:
    lectu = lec.read()
##    hexad = binascii.hexlify(lectu)
    hexad = lectu.hex()
    deca = int(hexad, 16)
    lecture = bin(deca)[2:].zfill(8)
lect.write(lecture)

#convert bits to nucleotides & write to files
count = 0
beethovengen = ''
for i in beethoven:
    if count == 0:
        count += 2
        continue
    elif beethoven[(count-2):count] == '00':
        beethovengen = beethovengen + 'A'
        count += 2
        continue
    elif beethoven[(count-2):count] == '01':
        beethovengen = beethovengen + 'C'
        count += 2
        continue
    elif beethoven[(count-2):count] == '10':
        beethovengen = beethovengen + 'G'
        count += 2
        continue
    elif beethoven[(count-2):count] == '11':
        beethovengen = beethovengen + 'T'
        count += 2
        continue
beegen.write(beethovengen)

counter = 0
lecturegen = ''
for i in lecture:
    if counter == 0:
        counter += 2
        continue
    elif lecture[(counter-2):counter] == '00':
        lecturegen = lecturegen + 'A'
        counter += 2
        continue
    elif lecture[(counter-2):counter] == '01':
        lecturegen = lecturegen + 'C'
        counter += 2
        continue
    elif lecture[(counter-2):counter] == '10':
        lecturegen = lecturegen + 'G'
        counter += 2
        continue
    elif lecture[(counter-2):counter] == '11':
        lecturegen = lecturegen + 'T'
        counter += 2
        continue
lecgen.write(lecturegen)



#close files
lecgen.close()
lect.close()
lec.close()
beegen.close()
bee.close()
beeth.close()
