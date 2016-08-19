#Entertainment
lines = open("testdata3.txt", "r").read().split('\n')
filet=open("entertainment1.txt","w")
for line in lines:

    sentence=line.split('||')
    if (sentence.__len__() <= 2):
            # print('> item number is wrong\n')
            #wrong = 1
            #sentence.append(' ')
            #sentence.append(' ')
        continue
    if "Entertainment" in sentence[2] :

        filet.writelines(line)
        filet.write('\n')
