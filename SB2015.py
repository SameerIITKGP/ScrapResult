import urllib2
import mechanize
import numpy as np

ihrolllist, sbrolllist, mnamelist  = np.loadtxt('data.csv',delimiter=',',unpack=True,dtype=str)

br = mechanize.Browser()
br.set_handle_robots(False)
f = open("final.csv","w")
f.write("Roll No., State Board Roll No., Name, Marks out of 650, P, C, M, English, Electronics, CS, EM, IT, BIO, Socio, Hindi, Marathi, Sanskrit, EVS\n")


response = br.open('http://mahresult.nic.in/hsc2015/hsc2015.htm')

for k in xrange(0,473):

    if((len(sbrolllist[k])==7) and (mnamelist[k]!="")):
        br.form = list(br.forms())[0]

        br.form["regno"]=sbrolllist[k]
        br.form["mname"]=mnamelist[k]

        response1 = br.submit()
        table = response1.read()
        table=table.split('\n')


        j=0

        index = 0
        indexn = 0
        indexp = 0
        indexm = 0
        indexc = 0
        indexMarathi = 0
        indexSanskrit = 0
        indexHindi = 0
        indexEnglish = 0
        indexElectronics = 0
        indexEM = 0
        indexCS = 0
        indexEVS = 0
        indexSocio = 0
        indexIT = 0
        indexBIO = 0

        foundMarathi = False
        foundSanskrit = False
        foundHindi = False
        foundEnglish = False
        foundElectronics = False
        foundEM = False
        foundCS = False
        foundEVS = False
        foundSocio = False
        foundIT = False
        foundBIO = False
        foundcpi = False
        foundname = False
        foundchem = False
        foundphy = False
        foundmath = False

        for line in table:

            if "<b>Total Marks:</b>" in line and foundcpi==False:
                index=j+2
                foundcpi = True
            elif "<td>54</td>" in line and foundphy==False:
                indexp=j+2
                foundphy = True
            elif "<p><b>Name</b>" in line and foundname==False:
                indexn=j+1
                foundname = True
            elif "<td>55</td>" in line and foundchem==False:
                indexc=j+2
                foundchem = True
            elif "<td>40</td>" in line and foundmath==False:
                indexm=j+2
                foundmath = True
            elif "<td>01</td>" in line and foundEnglish==False:
                indexEnglish=j+2
                foundEnglish = True
            elif "<td>02</td>" in line and foundMarathi==False:
                indexMarathi=j+2
                foundMarathi = True
            elif "<td>04</td>" in line and foundHindi==False:
                indexHindi=j+2
                foundHindi = True
            elif "<td>33</td>" in line and foundSanskrit==False:
                indexSanskrit=j+2
                foundSanskrit = True
            elif "<td>45</td>" in line and foundSocio==False:
                indexSocio=j+2
                foundSocio = True
            elif "<td>56</td>" in line and foundBIO==False:
                indexBIO=j+2
                foundBIO = True
            elif "<td>97</td>" in line and foundIT==False:
                indexIT=j+2
                foundIT = True
            elif "<td>A1</td>" in line and foundEM==False:
                indexEM=j+2
                foundEM = True
            elif "<td>C2</td>" in line and foundElectronics==False:
                indexElectronics=j+2
                foundElectronics = True
            elif "<td>D9</td>" in line and foundCS==False:
                indexCS=j+2
                foundCS = True
            elif "<td>31</td>" in line and foundEVS==False:
                indexEVS=j+2
                foundEVS = True

            j=j+1

        a=[]
        a.append(ihrolllist[k])
        a.append(sbrolllist[k])
        a.append(table[indexn].strip())
        a.append(table[index].strip())
        a.append(table[indexp].strip())
        a.append(table[indexc].strip())
        a.append(table[indexm].strip())
        a.append(table[indexEnglish].strip())
        a.append(table[indexElectronics].strip())
        a.append(table[indexCS].strip())
        a.append(table[indexEM].strip())
        a.append(table[indexIT].strip())
        a.append(table[indexBIO].strip())
        a.append(table[indexSocio].strip())
        a.append(table[indexHindi].strip())
        a.append(table[indexMarathi].strip())
        a.append(table[indexSanskrit].strip())
        a.append(table[indexEVS].strip())

        i=0
        for x in a:
            if "<!DOCTYPE html>" in x:
                a[i] = "NA"
            if "<td>" in x:
                a[i] = x.replace("<td>", "").replace("</td>", "")
            i+=1

        a[3] = a[3][:3]

        result = a[0]+","+a[1]+","+a[2]+","+a[3]+","+a[4]+","+a[5]+","+a[6]+","+a[7]+","+a[8]+","+a[9]+","+a[10]+","+a[11]+","+a[12]+","+a[13]+","+a[14]+","+a[15]+","+a[16]+","+a[17]+"\n";
        f.write(result)

        response1=br.back()

    else:
        result = ihrolllist[k] + "NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP,"+"NAP," + "NAP\n";



    print k
f.close()
