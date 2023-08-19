### 8.  Create Contact.csv file which contain name,contact. Use "|" as Delimiter.
### Search particular contact by entering person name . 

import csv

with open("C://22BCA206//python//contact_file1.csv",'w',newline='') as fileobj:
    obj=csv.writer(fileobj)
    field=['NAME','CONTACT NUMBER']
    obj.writerow(field)
    # 5 records insert directly
    records=[['Jay',9923456786],['Shree',9923356796],['Ram',6323456786],['Shiv',7923456786],['Krishna',6683456786]]
    obj.writerows(records)

with open("C://22BCA206//python//contact_file.csv",'r',newline='') as ob:
    data=csv.reader(ob)
    for i in data:
        print("{:^10} {:^10}".format(i[0],i[1]))
   

with open("C://22BCA206//python//contact_file1.csv",'r',newline='') as o:
    heading=next(o)
    data=csv.reader(o)
    name=input('Enter Name Whose Record You Want :')
    print('\n\n--------------------------------------------------')
    print('\n\t\t SEARCHED REACORD\n--------------------------------------------------')
    print("{:^10} {:^10}".format('NAME','CONTACT NUMBER'))
    for re in data:
        if re[0]==name:
             print("{:^10} {:^10}".format(re[0],re[1]))





