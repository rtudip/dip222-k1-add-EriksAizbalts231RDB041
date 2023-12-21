#Izmantojot teksta failā esošo informāciju nosākiet:
#Kurā gadā bija dibināts vecākais Omānas reģiona uzņēmums (informācija ir pieejama kolonnā Founded)?
result1=[]
with open('data.txt','r') as file:
    next(file)
    for line in file:
        row=line.rstrip().split(',')
        result1.append(row[6])
print(min(result1))

#Izmantojot teksta failā esošo informāciju nosākiet:
#Kāds ir darbinieku skaits, kas strādā Latvijā?
result2=[]
with open('data.txt','r') as file:
    next(file)
    substring = 'Latvia'
    for line in file:
        row=line.rstrip().split(',')
        if substring in row[4]:
           result2.append(row[8])
#print(result2)
int_result2 = [int(x) for x in result2]
print(sum(int_result2))

#Izmantojot teksta failā esošo informāciju nosākiet, 
#Kāds ir darbinieku skaits kas strādā telekomunikācijas jomā Latvijā.  (Industry = Telecommunications, Country = Latvia)?
result3=[]
with open('data.txt','r') as file:
    next(file)
    substring1 = 'Latvia'
    substring2 = 'Telecommunications'
    for line in file:
        row=line.rstrip().split(',')
        if substring1 in row[4]:
            if substring2 in row[7]:
               result3.append(row[8])
#print(result3)
int_result3 = [int(x) for x in result3]
print(sum(int_result3))

#Izmantojot teksta failā esošo informāciju nosākiet:
#Cik no datu bāze esošajiem Latvijas kompānijām ir SSL sertifikāts? (SSL sertifikāts ir kompānijām, kuram tīmekļa adrese sākas ar https://)
with open('data.txt','r') as file:
    next(file)
    substring11 = 'Latvia'
    substring22 = 'https://'
    res1 = 0
    for line in file:
        row=line.rstrip().split(',')
        if substring11 in row[4]:
            if substring22 in row[3]:
                res1 = res1 + 1
print(res1)

#Izmantojot teksta failā esošo informāciju nosākiet:
#Cik reizes datu bāzē tiek minēts domēna vārds .org reģionam Latvia?
with open('data.txt','r') as file:
    next(file)
    substring111 = 'Latvia'
    substring222 = '.org'
    res2 = 0
    for line in file:
        row=line.rstrip().split(',')
        if substring111 in row[4]:
            if substring222 in row[3]:
                res2 = res2 + 1
print(res2)