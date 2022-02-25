
def Reading_files(excel_file):
    with open(excel_file, 'r') as filename:
        data = filename.readlines()
        data_read = [data1.strip('\n').strip().split(',') for data1 in data]
        data_read.pop(0)
        return data_read
def Area_cal(reading_files):
    Northings=list(map(lambda y:y[0],reading_files))
    Eastings=list(map(lambda a:a[1],reading_files))
    NE=list(map(lambda x:float(x[0])*float(x[1]),zip(Northings[0:-1],Eastings[1:])))
    EN=list(map(lambda r:float(r[0])*float(r[1]),zip(Northings[1:],Eastings[0:-1])))
    return (abs(sum(NE)-sum(EN)))/2.000



