import math as m
# extracting and cleaning file from excel
def Reading_Traverse_csv(file):
    with open(file, 'r') as filename:
        data = filename.readlines()
        data_read = [data1.strip('\n').strip().split(',') for data1 in data]
        data_read.pop(1)
        data_read.pop(2)
        data_read.pop(2)
        data_read.pop(2)
        fileread=data_read
    return fileread

#extracting face left hcr reading and converting to decimal degree
def Left_group_hcr(read_data):
    LEFT = [[value[3],value[4],value[5],value[6]] for value in read_data[2:] if
                     value[3] == 'LL' and value[4] != '' and value[5] != '' and value[6] != '']
    return LEFT

#extracting face right reading and converting to decimal degree
def Right_group_hcr(read_data):
    RIGHT = [[value1[3], value1[4], value1[5], value1[6]] for value1 in read_data[2:] if
                value1[3] == 'RR' and value1[4] != '' and value1[5] != '' and value1[6] != '']
    return RIGHT

#calculating mean inclued angles
def Included_angles(read_files):
    left_hcr=Left_group_hcr(read_files)
    right_hcr=Right_group_hcr(read_files)
    LEFT_LEFT_HCR = [float(data3[1]) + float(data3[2]) / 60 + float(data3[3]) / 3600 for data3 in left_hcr]
    RIGHT_RIGHT_HCR= list([float(data4[1]) + float(data4[2]) / 60 + float(data4[3]) / 3600 for data4 in right_hcr])
    zipped_right_right=list(zip(RIGHT_RIGHT_HCR[0::2],RIGHT_RIGHT_HCR[1::2]))
    zipped_Left_left=list(zip(LEFT_LEFT_HCR[0::2],LEFT_LEFT_HCR[1::2]))
    LEFT_HIA = []
    RIGHT_HIA = []
    if read_files[3][3] == 'LL':
        for FACE_LEFT in zipped_Left_left:
            a = FACE_LEFT[1] - FACE_LEFT[0]
            if a > float(360):
                LEFT_HIA.append(a - float(360))
            elif a < 0:
                LEFT_HIA.append(a + float(360))
            elif a < float(360):
                LEFT_HIA.append(a)
        for FACE_RIGHT in zipped_right_right:
            b = FACE_RIGHT[0] - FACE_RIGHT[1]
            if b > float(360):
                RIGHT_HIA.append(b - float(360))
            elif b < 0:
                RIGHT_HIA.append(b + float(360))
            elif b < float(360):
                RIGHT_HIA.append(b)
    elif read_files[3][3]=='RR':
        for FACE_RIGHT in zipped_right_right:
            if FACE_RIGHT[1] - FACE_RIGHT[0] > float(360):
                RIGHT_HIA.append((FACE_RIGHT[1] - FACE_RIGHT[0]) - float(360))
            elif FACE_RIGHT[1] - FACE_RIGHT[0] < 0:
                RIGHT_HIA.append((FACE_RIGHT[1] - FACE_RIGHT[0]) + float(360))
            elif FACE_RIGHT[1] - FACE_RIGHT[0] < float(360):
                RIGHT_HIA.append(FACE_RIGHT[1] - FACE_RIGHT[0])
        for FACE_LEFT in zipped_Left_left:
            if FACE_LEFT[0] - FACE_LEFT[1] > float(360):
                LEFT_HIA.append((FACE_LEFT[0] - FACE_LEFT[1]) - float(360))
            elif FACE_LEFT[0] - FACE_LEFT[1] < 0:
                LEFT_HIA.append((FACE_LEFT[0] - FACE_LEFT[1]) + float(360))
            elif FACE_LEFT[0] - FACE_LEFT[1] < float(360):
                LEFT_HIA.append(FACE_LEFT[0] - FACE_LEFT[1])
    zipped_left_right=list(zip(LEFT_HIA,RIGHT_HIA))
    final_HIA=[(HIA[0]+HIA[1])/float(2) for HIA in zipped_left_right]
    return final_HIA

#calculating Bearing
def Bearing_calculation(readdata):
    included_angles=Included_angles(readdata)
    initial_bearing=float(readdata[0][2])
    bearing_list=[initial_bearing]
    for angle in included_angles:
        angle1=angle+float(180)+bearing_list[-1]
        if angle1 < float(360):
            bearing_list.append(angle1)
        elif angle1 > float(360) and angle1<float(720):
            bearing_list.append(angle1 - float(360))
        elif angle1>float(720):
            bearing_list.append(angle1-float(720))
    return bearing_list[1:]

#Calculating latitude
def Latitude(datafiles):
    Bearing=Bearing_calculation(datafiles)
    Distance=[dist[-1] for dist in datafiles if dist[-1]!='']
    return [float(lat[0])*m.cos(m.radians(lat[1]))for lat in zip(Distance,Bearing)]

#calculating departure
def Departure(datafiles1):
    Bearing1 = Bearing_calculation(datafiles1)
    Distance1 = [dist[-1] for dist in datafiles1 if dist[-1]!='']
    return [float(dep[0]) * m.sin(m.radians(dep[1])) for dep in zip(Distance1,Bearing1)]

#Calculating Northing coordinates
def Northinsgs_calculations(Read_data):
    latitude=Latitude(Read_data)
    intial_northings=float(Read_data[0][-2])
    Lat_list=[intial_northings]
    for lat in latitude[1::]:
        Lat_list.append(lat+Lat_list[-1])
    return Lat_list

#calculating easting coordinates
def Eastings_calculations(Read_data):
    departure=Departure(Read_data)
    initial_Eastings=float(Read_data[1][2])
    Dep_list=[initial_Eastings]
    for dep in departure[1::]:
        Dep_list.append(dep + Dep_list[-1])
    return Dep_list

#Assigning pointnames to points
def Travpointnames(data):
    return [pn[0] for pn in data[2:] if pn[0]!='']











