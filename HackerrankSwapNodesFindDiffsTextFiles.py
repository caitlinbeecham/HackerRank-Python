def findDiffsTextFiles(textfilename1,textfilename2):
    #will read each newline of each file into a list
    #and each space separated value from each line into elts of those lists
    #will first let us know if the num lists are the same
    #will  let us know if length of these lists are the same
    #then passing all that will return idxs where each of the list pairs elts
    #differ
    f1 = open(textfilename1,'r')
    f2 = open(textfilename2,'r')
    f1_lines = [line.strip().split(' ') for line in f1]
    f2_lines = [line.strip().split(' ') for line in f2]
    for i in range(len(f1_lines)):
        for j in range(len(f1_lines[i])):
            f1_lines[i][j] = int(f1_lines[i][j])
    for i in range(len(f2_lines)):
        for j in range(len(f2_lines[i])):
            f2_lines[i][j] = int(f2_lines[i][j])
    same_number_lines = (len(f1_lines) == len(f2_lines))
    same_number_elts = None
    ones_where_diff = None
    print("We have the same number of lines in each file.")
    print("Truth Value:")
    print(same_number_lines)
    if same_number_lines:
        same_number_elts = True
        for i in range(len(f1_lines)):
            if len(f1_lines[i]) != len(f2_lines[i]):
                same_number_elts = False
                break
        print("All lines have (pairwise between text files) the same number of elts.")
        print("Truth Value:")
        print(same_number_elts)
        print()
        if same_number_elts:
            #find list of lists of same dim f1_lines
            #where each elt if 0 if f1_lines[i][j] is same as f2_lines[i][j]
            #1 otherwise
            num_diff = 0
            ones_where_diff = [[0 for j in range(len(f1_lines[i]))] for i in range(len(f1_lines))]
            for i in range(len(f1_lines)):
                for j in range(len(f1_lines[i])):
                    if f1_lines[i][j] != f2_lines[i][j]:
                        ones_where_diff[i][j] = 1
                        num_diff += 1
            print("Number of Different Elts between expected and actual:")
            print(num_diff)
    else:
        print("We have a different number of lines in each file.")
        print("Num Lines in " + textfilename1 + ":")
        print(len(f1_lines))
        print("We have a different number of lines in each file.")
        print("Num Lines in " + textfilename2 + ":")
        print(len(f2_lines))
        print("So lets compare the lines up to the number of lines in the shorter list.")
        end_range = min(len(f1_lines),len(f2_lines))
        same_number_elts = True
        for i in range(end_range):
            if len(f1_lines[i]) != len(f2_lines[i]):
                same_number_elts = False
                break
        print("All lines have (pairwise between text files) the same number of elts.")
        print("Truth Value:")
        print(same_number_elts)
        print()
        if same_number_elts:
            #find list of lists of same dim f1_lines
            #where each elt if 0 if f1_lines[i][j] is same as f2_lines[i][j]
            #1 otherwise
            num_diff = 0
            ones_where_diff = [[0 for j in range(len(f1_lines[i]))] for i in range(len(f1_lines))]
            for i in range(len(f1_lines)):
                for j in range(len(f1_lines[i])):
                    if f1_lines[i][j] != f2_lines[i][j]:
                        ones_where_diff[i][j] = 1
                        num_diff += 1
            print("Number of Different Elts between expected and actual:")
            print(num_diff)
        
    return ones_where_diff



#okay so I found out mine is just not doing the last print inorder
#maybe my loop is 1 too short
#doubtful since this worked on other test cases
#my guess is my multiples of k indexing is off
findDiffsTextFiles('HackerrankSwapNodesTestCase10MyOutput.txt','HackerrankSwapNodesTestCase10Output.txt')

    
