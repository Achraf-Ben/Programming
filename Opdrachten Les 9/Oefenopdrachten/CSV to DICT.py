with open('newfile.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('newfile_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
