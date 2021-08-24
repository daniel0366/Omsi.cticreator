ctiname = input('Please enter the name of CTI file')
doclist = [ctiname] 
texture = 1


while  True: 
    n = input('Please enter the names of documents to use in order. Enter STOP to stop.')
    if n=="STOP":
        break
    else:
        doclist.append(n)

print (doclist)
print (len(doclist))
with open(doclist[0] + '.cti', 'w') as f:
    f.write(    "\n")
    f.write("***************************************\n")
    f.write(doclist[0]+"\n")
    f.write("***************************************\n")
    while texture < len(doclist):
        if len(doclist) == 0:
            break
        else:
            print (texture)
            f.write(    "\n")
            f.write("[item]\n")
            f.write(doclist[0]+"\n")
            f.write("farcschema_tex"+str(texture)+"\n")
            f.write(doclist[texture]+"\n")
            texture = texture + 1

    else:
        print("done!")