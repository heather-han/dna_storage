#Comparative Genomics Project
#

#import tools
import binascii

#note that I simply use random names for variables, many times just
#adding letters until the full "word" is acheived

#open files for reading and writing (the files for writing are txt files
#containing the file of bits and the genome sequence file
beeth = open ('Beethoven_Sonata_Emin_op90_2nd_movement.ogg', 'rb')
bee = open('beethoven.txt', 'w')
beegen = open('beethoven_genomic.txt', 'w')
lec = open('L15singlecell.pdf', 'rb')
lect = open('lecture.txt', 'w')
lecgen = open('lecture_genomic.txt', 'w')

#open files for writing (these are the files being written
#into to re-create the original .x files; note to use 'wb')
sonatas = open('sonatas.ogg', 'wb')
classlectures = open('lecture.pdf', 'wb')


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


#write back to become the file you want (I commented out the genome sequence
#below for now to just ensure I can write back the file of bits into the
#original file format)
so = int(beethoven, 2)
son = hex(so)
sonata = bytearray.fromhex(son[2:])
sonatas.write(sonata)

cl = int(lecture, 2)
cla = hex(cl)
classlecture = bytearray.fromhex(cla[2:])
classlectures.write(classlecture)


###convert bits to nucleotides & write to files
##count = 0
##beethovengen = ''
##for i in beethoven:
##    if count == 0:
##        count += 2
##        continue
##    elif beethoven[(count-2):count] == '00':
##        beethovengen = beethovengen + 'A'
##        count += 2
##        continue
##    elif beethoven[(count-2):count] == '01':
##        beethovengen = beethovengen + 'C'
##        count += 2
##        continue
##    elif beethoven[(count-2):count] == '10':
##        beethovengen = beethovengen + 'G'
##        count += 2
##        continue
##    elif beethoven[(count-2):count] == '11':
##        beethovengen = beethovengen + 'T'
##        count += 2
##        continue
##beegen.write(beethovengen)
##
##counter = 0
##lecturegen = ''
##for i in lecture:
##    if counter == 0:
##        counter += 2
##        continue
##    elif lecture[(counter-2):counter] == '00':
##        lecturegen = lecturegen + 'A'
##        counter += 2
##        continue
##    elif lecture[(counter-2):counter] == '01':
##        lecturegen = lecturegen + 'C'
##        counter += 2
##        continue
##    elif lecture[(counter-2):counter] == '10':
##        lecturegen = lecturegen + 'G'
##        counter += 2
##        continue
##    elif lecture[(counter-2):counter] == '11':
##        lecturegen = lecturegen + 'T'
##        counter += 2
##        continue
##lecgen.write(lecturegen)




#close files
classlectures.close()
sonatas.close()
lecgen.close()
lect.close()
lec.close()
beegen.close()
bee.close()
beeth.close()
