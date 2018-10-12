#please use python 3.x version
#Required packages are csv and geopy
#input file should be named as input_file.csv and should be in same directory as the script
#output will be generated in out_of_tolerance.csv file in same directory as script
import csv
import geopy.distance

rows =[]
with open('input_file.csv','r') as file:
    data = csv.reader(file)
    for row in data:
        rows.append(row)

row_no=0
for row in rows:
    if row_no ==0:
        row_no +=1
        continue
    else:
        #Testing if input is good
        if len(row[0].split(',')) != 5:
            print('Values missing for this row',row)
            continue
        eid, lat1, long1, lat2, long2 = row[0].split(',')
        try:
            source = (int(lat1)/1000000, int(long1)/1000000)
            dest = (int(lat2)/1000000, int(long2)/1000000)
        except ValueError:
            print('latitude or longitude is not an integer value for eid: ',eid)
            continue
        if source[0] > 90 or source[1] < -90 or dest[0] >90 or dest[1] < -90:
            print('Wrong input for this EID: ',eid)
            continue
        elif geopy.distance.vincenty(source,dest).meters > 5000:
            with open('out_of_tolerance.csv','a') as File:
                File.writelines(eid+'\n')
        row_no +=1




