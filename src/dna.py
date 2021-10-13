

def dna_check(DNAText):
    may = False # flag to double check
    mut = 0 # how many mutants lines are
    dict = {'A':0, 'T':0, 'C':0, 'G':0}

    for row in DNAText: # loop th in rows
        for word in row: # loop every word
            sl = len(row) # get the len
            if word == 'A' or word == 'T' or word == 'C' or word == 'G': # check every word
                dict[word] += 1 #increases dict

    for wd in dict: #loop dict
        if dict[wd] >= 4: # if dict is over 4, may be mutant
            may = True
            break

    # print(dict)
    if may: # if may be
        for wd in dict: # loop again
            if dict[wd] >= 4: # if is over 4, dig
                for row in DNAText: # loop th in rows
                    if row.find(wd*4) >= 0: # check horizontal
                        mut += 1
                        # print('h' + wd)
                for i in range(sl): # check vertical
                    cant = 0 # initial val
                    for row in DNAText: # loop th in rows
                        if wd == row[i]: # check word in i pos
                            cant += 1 # incr
                            if cant == 4: # if touch 4 is mutant
                                mut += 1
                                # print('v' + wd)
            cant = 0
            for i in range(sl): # check diag
                if DNAText[i][i] == wd:
                    cant += 1
                    if cant == 4:
                        mut += 1
                        # print('d' + wd)
    return True if mut >= 2 else False

# if __name__ == '__main__':
#     print('Mutant' if dna_check(["AXXXXX","CAXXXX","TTAXXX","AGAAXX","CCCXAA","TCACTA"]) else 'NoMutant')
#     print('Mutant' if dna_check(["AXGCGA","XAGTGC","XXATGT","AGAAGG","CCXXTA","TCACTX"]) else 'NoMutant')
#     print('Mutant' if dna_check(["AAAAXX","XXXXXX","XXXXXX","XXXXXX","XXXXXX","XXXXXX"]) else 'NoMutant')
#     print('Mutant' if dna_check(["ACCG","CACX","CCAG","JKXA"]) else 'NoMutant')