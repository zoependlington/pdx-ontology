import csv
with open('../templates/pdx-cancer.tsv', 'rb') as f: #opens the template file
    reader = csv.reader(f, delimiter='\t') #reads it as a tsv
    l = list(reader) #makes a list from tsv

def extract(x): #extracts the ncit xrefs from the tsv id list
    global lst
    global lst2
    global xrefs
    xrefs = ('../ontology/results/ncit-xrefs.txt')
    lst = [item[x] for item in l] #takes the first value of each nested list (IDs)
    lst = lst[2:] #removes the two rows of "titles"
    lst = [y for y in lst if "PDXO:" not in y] #removes any PDXO: xrefs
    string = "http://purl.obolibrary.org/obo/"
    lst = [item.replace(":", "_") for item in lst]
    lst2 = [string + x for x in lst]
    with open (xrefs, "w") as output: #writes the result to the ncit-xrefs.txt file
        writer = csv.writer(output, lineterminator='\n') #writes each xref to new line
        for xref in lst2:
            writer.writerow([xref])

extract(0)
