import re,sys

para_split_regex = re.compile("[\\s]*\n+[\\s]*")
raw_speeches = open(sys.argv[1]).read()
paras = para_split_regex.split(raw_speeches)

for i,para in enumerate(paras):
    open("fake-splits/fake-split-%i.txt"%i,"w").write(para)

