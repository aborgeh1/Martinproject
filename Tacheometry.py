import  math as m
#Reading and cleaning file from excel
def Reading_Tacheo_csv(file):
    with open(file, 'r') as filename:
        data = filename.readlines()
        data_read = [data1.strip('\n').strip().split(',') for data1 in data]
        data_read.pop(0)
        data_read.pop(0)
        data_read.pop(0)
        data_read.pop(0)
        data_read.pop(1)
        data_read.pop(2)
        data_read.pop(2)
        data_read.pop(2)
    return data_read

#converting to decimal_degree
def decimal_hcr(read_data):
    return [float(d_hcr[1]) + (float(d_hcr[2]) / 60.0) + (float(d_hcr[3]) / 3600.0) for d_hcr in read_data]

#extracting left decimal degree
def extract_LEFT_HCR(Readfiles):
    LEft=[[Left[4],Left[6],Left[7],Left[8]] for Left in Readfiles if 'LL' in Left and Left[6]!='' and Left[7]!='' and Left[8]!='']
    return decimal_hcr(LEft)

#extracting right decimal degree
def extract_RIGHT_HCR(Readfile):
    RIGHT_HCR = [[RIGHT[4], RIGHT[6], RIGHT[7], RIGHT[8]] for RIGHT in Readfile if RIGHT[4] == 'RR' and RIGHT[6] != '' and RIGHT[7] != '' and RIGHT[8] != '']
    return decimal_hcr(RIGHT_HCR)

#calculating left included angle
def Left_included_angle(datafile):
    left_included_angle = []
    lefthcr = [[Left3[4], Left3[6], Left3[7], Left3[8],Left3[-1]] for Left3 in datafile if
             'LL' in Left3 and Left3[6] != '' and Left3[7] != '' and Left3[8] != '']
    ap_hcr=[]
    left_hcr=extract_LEFT_HCR(datafile)
    for hcr in zip(left_hcr,lefthcr):
        if hcr[1][-1]!='':
            ap_hcr.append(hcr[0])
            left_included_angle.append(hcr[0] - ap_hcr[-1])
        else:
            left_included_angle.append(hcr[0] - ap_hcr[-1])
    return left_included_angle[1:]

#calculating right included angle
def right_included_Angle(datafiles):
    right_included_angle = []
    ap_hcr1= []
    righthcr=[[RIGHT3[4], RIGHT3[6], RIGHT3[7], RIGHT3[8],RIGHT3[-1]] for RIGHT3 in datafiles if RIGHT3[4] == 'RR' and RIGHT3[6] != '' and RIGHT3[7] != '' and RIGHT3[8] != '']
    right_hcr1 = extract_RIGHT_HCR(datafiles)
    for hcr1 in zip(right_hcr1,righthcr):
        if hcr1[1][-1]!='':
            ap_hcr1.append(hcr1[0])
            right_included_angle.append(hcr1[0] - ap_hcr1[-1])
        else:
            right_included_angle.append(hcr1[0] - ap_hcr1[-1])
    return right_included_angle[1:]

#extracting left vertical circle reading
def extract_LEFT_VCR(Readfiles):
    LEFT_VCR=list([[left_vcr[4],left_vcr[10:13]] for left_vcr in Readfiles \
                    if left_vcr[4]=='LL' and left_vcr[10]!='' and left_vcr[11]!='' and left_vcr[12]!=''])
    LEFT_VCR1 = list(
        [float(left_vcr1[1][0]) + (float(left_vcr1[1][1]) / 60.0) + (float(left_vcr1[1][2]) / 3600.0) for left_vcr1 in
         LEFT_VCR])
    return LEFT_VCR1

#extracting right vertical circle reading
def extract_RIGHT_VCR(Readfiles):
    RIGHT_VCR = list([[right_vcr[4], right_vcr[10:13]] for right_vcr in Readfiles \
                     if right_vcr[4] == 'RR' and right_vcr[10] != '' and right_vcr[11] != '' and right_vcr[12] != ''])
    RIGHT_VCR1 = list(
        [float(right_vcr1[1][0]) + (float(right_vcr1[1][1]) / 60.0) + (float(right_vcr1[1][2]) / 3600.0) for right_vcr1 in
         RIGHT_VCR])
    return RIGHT_VCR1

#calcuting Left vertical angle
def Left_vertical_angle(left_vcr1_reading):
    left_vertical_angle = []
    for vcr in left_vcr1_reading:
        if vcr < float(90):
          left_vertical_angle.append(float(90)-vcr)
        elif float(90) < vcr <= float(270):
            left_vertical_angle.append(90.0-vcr)
        elif vcr > float(270):
            left_vertical_angle.append(vcr-float(270))
    return left_vertical_angle

#calculating right vertical angle
def Right_vertcal_angle(right_vcr1_reading):
    right_vertical_angle = []
    for vcr1 in right_vcr1_reading:
        if vcr1 < float(90):
          right_vertical_angle.append(float(90) - vcr1)
        elif vcr1 > float(90) and vcr1 < float(270):
            right_vertical_angle.append(90.0-vcr1)
        elif vcr1 > float(270):
            right_vertical_angle.append(vcr1 - float(270))
    return right_vertical_angle

#extracting left upper,middle and lower reading data
def extract_LEFT_STADIA(Readfiles):
    LEFT_STADIA=list([[left_stadia[4],left_stadia[14:17]] for left_stadia in Readfiles \
                      if left_stadia[4]=='LL' and left_stadia[14]!='' and left_stadia[15]!='' and left_stadia[16]!=''])
    LEFT_STADIA1=list([float(lft_stadia[1][0])-float(lft_stadia[1][2]) for lft_stadia in LEFT_STADIA])
    return LEFT_STADIA1

#extracting right upper,middle and lower reading data
def extract_RIGHT_STADIA(Readfiles):
    RIGHT_STADIA = list([[right_stadia[4], right_stadia[14:17]] for right_stadia in Readfiles \
                        if right_stadia[4] == 'RR' and right_stadia[14] != '' and right_stadia[15] != '' and right_stadia[
                            16] != ''])
    RIGHT_STADIA1 = list([float(rgt_stadia[1][0]) - float(rgt_stadia[1][2]) for rgt_stadia in RIGHT_STADIA])
    return RIGHT_STADIA1

#extracting intials
def extract_initials(Readfiles):
    init_dicts = {}
    init_dicts['k']=Readfiles[0][6]
    init_dicts['c']=[Readfiles[0][8]]
    init_dicts['Initial_bearing']=Readfiles[0][12:15]
    init_dicts['initial_northings']=Readfiles[0][18]
    init_dicts['initial_eastings']=Readfiles[1][16]
    init_dicts['initial_elevation']=Readfiles[1][11]
    return init_dicts

#calculating left vertical distance
def left_vertical_dist(initials,left_vert_angle,Left_stadia):
    return [(((float(initials['k'][0]))*item[0])+(float(initials['c'][0])))*m.sin(m.radians(item[1])) for item in list(zip(Left_stadia,left_vert_angle))]

#calculating right vertical distance
def right_vertical_dist(initials,right_vert_angle,Right_stadia):
    return [(((float(initials['k'][0])) * item1[0]) + (float(initials['c'][0]))) * m.sin(m.radians(item1[1])) for item1 in
         list(zip(Right_stadia, right_vert_angle))]

#calculating left horizontal distance
def left_horizontal_distance(reading_Files):
    initials=extract_initials(reading_Files)
    leftvertangle=Left_vertical_angle(extract_LEFT_VCR(reading_Files))
    left_stadia=extract_LEFT_STADIA(reading_Files)
    left_horizontal_dist = [(float(initials['k'][0]) * par7[0] * ((m.cos(m.radians(par7[1]))) ** 2)) + (
            (float(initials['c'][0])) * m.cos(m.radians(par7[1]))) for par7 in zip(left_stadia, leftvertangle)]
    return left_horizontal_dist

#calculating right horizontal distance
def right_horizontal_distance(reading_Files1):
    initials1=extract_initials(reading_Files1)
    rightvertangle=Right_vertcal_angle(extract_RIGHT_VCR(reading_Files1))
    right_stadia=extract_RIGHT_STADIA(reading_Files1)
    right_horizontal_dist = [(float(initials1['k'][0]) * par8[0] * ((m.cos(m.radians(par8[1]))) ** 2)) + (
            (float(initials1['c'][0])) * m.cos(m.radians(par8[1]))) for par8 in zip(right_stadia, rightvertangle)]
    return right_horizontal_dist

#calculating left bearing
def left_bearing_calculation(Read_data1):
    bearing_list = []
    temporary_Left_IA=[]
    bearing=extract_initials(Read_data1)['Initial_bearing']
    decimal_bearing=[float(bearing[0])+(float(bearing[1])/60.0)+(float(bearing[2])/3600.0)]
    bearing_list.append(decimal_bearing[0])
    Left_Included_Angle=Left_included_angle(Read_data1)
    for i,angle in enumerate(Left_Included_Angle):
        if angle==0.0:
            try:
                 tria=bearing_list[-2]+180

                 if 0.0 < tria < float(360):
                     bearing_list.append(tria)
                     decimal_bearing.append(tria)
                 elif float(360) < tria < float(720):
                     bearing_list.append(tria-float(360))
                     decimal_bearing.append(tria-float(360))
                 elif tria < 0.0:
                     bearing_list.append(tria+float(360))
                     decimal_bearing.append(tria+float(360))


            except IndexError:
                continue

        else:
            if 0.0 < angle <= float(360):
                actual_bearing = angle + decimal_bearing[-1]
                if 0.0 < actual_bearing <= 360:
                    bearing_list.append(actual_bearing)
                elif float(360) < actual_bearing <= 720:
                    bearing_list.append(actual_bearing - float(360))
            elif angle < 0.0:
                actual_bearing1 = (decimal_bearing[-1] - (float(360) - (angle + float(360))))
                if 0.0 < actual_bearing1 <= 360:
                    bearing_list.append(actual_bearing1)
                elif float(360) < actual_bearing1 <= 720:
                    bearing_list.append(actual_bearing1 - float(360))
            elif float(360) < angle <= float(720):
                actual_bearing2 = angle - float(360)
                if 0.0 < actual_bearing2 <= float(360):
                    bearing_list.append(actual_bearing2)
                elif float(360) < actual_bearing2 <= 720:
                    bearing_list.append(actual_bearing2 - float(360))
    return bearing_list

#calculating right bearing
def right_bearing_calculation(Read_data2):
    bearing_list1 = []
    bearing1 = extract_initials(Read_data2)['Initial_bearing']
    decimal_bearing1 = [float(bearing1[0]) + (float(bearing1[1]) / 60.0) + (float(bearing1[2]) / 3600.0)]
    bearing_list1.append(decimal_bearing1[0])
    Right_Included_Angle1 = right_included_Angle(Read_data2)
    for i, angle1 in enumerate(Right_Included_Angle1):
        if angle1 == 0:
            try:
                tria1 = bearing_list1[-2] + float(180)
                if 0.0 < tria1 < float(360):
                    bearing_list1.append(tria1)
                    decimal_bearing1.append(tria1)
                elif float(360) < tria1 < float(720):
                    bearing_list1.append(tria1 - float(360))
                    decimal_bearing1.append(tria1 - float(360))
                elif tria1 < 0.0:
                    bearing_list1.append(tria1 + float(360))
                    decimal_bearing1.append(tria1 + float(360))

            except IndexError:
                continue
        else:
            if 0.0 < angle1 <= float(360):
                actual_bearing = angle1 + decimal_bearing1[-1]
                if 0.0 < actual_bearing <= 360:
                    bearing_list1.append(actual_bearing)
                elif float(360) < actual_bearing <= 720:
                    bearing_list1.append(actual_bearing - float(360))
            elif angle1 < 0.0:
                actual_bearing1 = (decimal_bearing1[-1] - (float(360) - (angle1 + float(360))))
                if 0.0 < actual_bearing1 <= 360:
                    bearing_list1.append(actual_bearing1)
                elif float(360) < actual_bearing1 <= 720:
                    bearing_list1.append(actual_bearing1 - float(360))
            elif float(360) < angle1 <= float(720):
                actual_bearing2 = angle1 - float(360)
                if 0.0 < actual_bearing2 <= float(360):
                    bearing_list1.append(actual_bearing2)
                elif float(360) < actual_bearing2 <= 720:
                    bearing_list1.append(actual_bearing2 - float(360))
    return bearing_list1
print(left_bearing_calculation(Reading_Tacheo_csv('TACHEOMETRY_CALCULATION.csv')))
#calculating left latitude
def left_latitude_calculation(readdata):
    bearing_calculated=left_bearing_calculation(readdata)
    hor_dist=left_horizontal_distance(readdata)
    return [lat[0]*m.cos(m.radians(lat[1])) for lat in zip(hor_dist,bearing_calculated)]

#calculating left departure
def left_departure_calculation(readdata1):
    bearing_calculated1 = left_bearing_calculation(readdata1)
    hor_dist1 = left_horizontal_distance(readdata1)
    return [lat1[0] * m.sin(m.radians(lat1[1])) for lat1 in zip(hor_dist1, bearing_calculated1)]

#calculating left northings
def left_Northings_calulation(dataread):
    northings=[float(extract_initials(dataread)['initial_northings'])]
    leftlatitude=left_departure_calculation(dataread)
    northings.extend(northings[-1]+leftlat for leftlat in leftlatitude)
    return northings

#calculating left Eastings
def left_Eastings_calcualtion(dataread1):
    eastings = [float(extract_initials(dataread1)['initial_northings'])]
    leftdeoarture = left_departure_calculation(dataread1)
    eastings.extend(eastings[-1] + leftdep1 for leftdep1 in leftdeoarture)
    return eastings

#calculating right latitude
def right_latitude_calculation(readdata2):
    bearing_calculated3 = right_bearing_calculation(readdata2)
    hor_dist3 = right_horizontal_distance(readdata2)
    return [lat3[0] * m.cos(m.radians(lat3[1])) for lat3 in zip(hor_dist3, bearing_calculated3)]

#calculating right departure
def right_departure_calculation(readdata4):
    bearing_calculated4 = right_bearing_calculation(readdata4)
    hor_dist4 = right_horizontal_distance(readdata4)
    return [lat4[0] * m.sin(m.radians(lat4[1])) for lat4 in zip(hor_dist4, bearing_calculated4)]

#calculating right northings
def right_Northings_calulation(dataread6):
    northings1=[float(extract_initials(dataread6)['initial_northings'])]
    rightlatitude=right_latitude_calculation(dataread6)
    northings1.extend(northings1[-1]+rightlat for rightlat in rightlatitude)
    return northings1

#calculating right eastings
def right_Eastings_calcualtion(dataread7):
    eastings1 = [float(extract_initials(dataread7)['initial_northings'])]
    rightdeparture = right_departure_calculation(dataread7)
    eastings1.extend(eastings1[-1] + rightdepart for rightdepart in rightdeparture)
    return eastings1

#calculating final northings considering different different faces of hcr reading on field
def Northings_Coordinate_calcultion(clead_read_files):
    if clead_read_files[3][4]=='LL' and clead_read_files[4][4]=='LL':
        result1=left_Northings_calulation(clead_read_files)
    elif clead_read_files[3][4]=='RR' and clead_read_files[4][4]=='RR':
        result1=right_Northings_calulation(clead_read_files)
    elif (clead_read_files[3][4]=='LL' and clead_read_files[4][4]=='RR') or (clead_read_files[3][4]=='RR' and clead_read_files[4][4]=='LL') :
        print(left_Northings_calulation(clead_read_files))
        print(right_Northings_calulation(clead_read_files))
        result1= [(mean[0]+mean[1])/float(2) for mean in zip(left_Northings_calulation(clead_read_files),right_Northings_calulation(clead_read_files))]
    return result1

#calculating final eastings considering different different faces of hcr reading on field
def Eastings_Coordinate_calculation(clead_read_files1):
    if clead_read_files1[3][4] == 'LL' and clead_read_files1[4][4] == 'LL':
        result2 = left_Eastings_calcualtion(clead_read_files1)
    elif clead_read_files1[3][4] == 'RR' and clead_read_files1[4][4] == 'RR':
        result2=right_Eastings_calcualtion(clead_read_files1)
    elif (clead_read_files1[3][4] == 'LL' and clead_read_files1[4][4] == 'RR') or (
            clead_read_files1[3][4] == 'RR' and clead_read_files1[4][4] == 'LL'):
        result2 = [(mean1[0]+mean1[1])/float(2) for mean1 in
                   zip(left_Eastings_calcualtion(clead_read_files1), right_Eastings_calcualtion(clead_read_files1))]
    return result2

#calculating left middle reading
def left_middle_reading(read_file):
    left_m_reading=list([ lft_m_diddle_reading[15] for lft_m_diddle_reading in read_file[2::] if lft_m_diddle_reading[4]=='LL'])
    return left_m_reading

#calculating right middle reading
def right_middle_reading(read_file):
    right_m_reading = list(
        [rgt_m_diddle_reading[15] for rgt_m_diddle_reading in read_file[2::] if rgt_m_diddle_reading[4] == 'RR'])
    return right_m_reading

#calculating left elevating
def left_left_elev(read_files):
    Left_Vertical_Dist=left_vertical_dist(extract_initials(read_files),Left_vertical_angle(extract_LEFT_VCR(read_files)),extract_LEFT_STADIA(read_files))
    Left_middle_reading=left_middle_reading(read_files)
    trueheight=[]
    elev=[float(extract_initials(read_files)['initial_elevation'])]
    for dat in read_files:
        if dat[-3]=='CP':
            read_files.remove(dat)
    height=[Height[-1] for Height in read_files[2:]]
    for hyt in zip(height,Left_Vertical_Dist,Left_middle_reading):
        if hyt[0]!='':
            trueheight.append(hyt[0])
            elev.append(elev[-1] + float(hyt[0]) + hyt[1] - float(hyt[2]))
        else:
            elev.append(elev[-1] + float(trueheight[-1]) + hyt[1] - float(hyt[2]))
    return elev

#calculating right elevation
def right_right_elev(read_datafile):
    Right_Vertical_Dist=right_vertical_dist(extract_initials(read_datafile),Right_vertcal_angle(extract_RIGHT_VCR(read_datafile)),extract_RIGHT_STADIA(read_datafile))
    Right_middle_Reading=right_middle_reading(read_datafile)
    trueheight1 = []
    elev1 = [float(extract_initials(read_datafile)['initial_elevation'])]
    for dat1 in read_datafile:
        if dat1[-3] == 'CP':
            read_datafile.remove(dat1)
    height1 = [Height1[-1] for Height1 in read_datafile[2:]]
    for hyt1 in zip(height1, Right_Vertical_Dist, Right_middle_Reading):
        if hyt1[0] != '':
            trueheight1.append(hyt1[0])
            elev1.append(elev1[-1] + float(hyt1[0]) + hyt1[1] - float(hyt1[2]))
        else:
            elev1.append(elev1[-1] + float(trueheight1[-1]) + hyt1[1] - float(hyt1[2]))
    return elev1

# calculating elevation based on HCR face reading
def Elevation(data_read):
    if data_read[3][4]=='LL' and data_read[4][4]=='LL':
        result= left_left_elev(data_read)
    elif data_read[3][4]=='RR' and data_read[4][4]=='RR':
        result=right_right_elev(data_read)
    else:
        result= [(mean[0]+mean[1])/float(2) for mean in zip(left_left_elev(data_read),right_right_elev(data_read))]
    return result

#extracting left pointnames
def left_point_names(cleanfiles):
    point_names=[cleanfiles[2][0]]
    point=[pn for pn in cleanfiles[3:] if  pn[4]=='LL']
    for d in point:
        if d[1]!='' and d[2]=='' and d[3]=='':
            point_names.append(d[1])
        elif d[1]=='' and d[2]!='' and d[3]=='':
            point_names.append(d[2])
        elif d[1] == '' and d[2] == '' and d[3] != '':
            point_names.append(d[3])
    return point_names

#extracting right pointnames
def right_point_names(cleanfiles1):
    point_names1 = [cleanfiles1[2][0]]
    point1 = [pn1 for pn1 in cleanfiles1[3:] if pn1[4] == 'RR']
    for d1 in point1:
        if d1[1] != '' and d1[2] == '' and d1[3] == '':
            point_names1.append(d1[1])
        elif d1[1] == '' and d1[2] != '' and d1[3] == '':
            point_names1.append(d1[2])
        elif d1[1] == '' and d1[2] == '' and d1[3] != '':
            point_names1.append(d1[3])
    return point_names1

#naming points based on HCR reading
def left_right_pointnames(data):
    if data[3][4]=='LL' and data[4][4]=='LL':
        pointname=left_point_names(data)
    elif data[3][4] == 'RR' and data[4][4] == 'RR':
        pointname=right_point_names(data)
    elif (data[3][4] == 'LL' and data[4][4] == 'RR') or (
            data[3][4] == 'RR' and data[4][4] == 'LL'):
        pointname=left_point_names(data) or right_point_names(data)
    return pointname
print(left_right_pointnames(Reading_Tacheo_csv('TACHEOMETRY_CALCULATION.csv')))
def removecp(Iterabelies):

    for i in Iterabelies:
        if i[0][-1]=='b' and i[0][-1]=='b':
            print(i)

print(removecp(list(zip(left_right_pointnames(Reading_Tacheo_csv('TACHEOMETRY_CALCULATION.csv')),Eastings_Coordinate_calculation(Reading_Tacheo_csv('TACHEOMETRY_CALCULATION.csv')),Northings_Coordinate_calcultion(Reading_Tacheo_csv('TACHEOMETRY_CALCULATION.csv')),Elevation(Reading_Tacheo_csv('TACHEOMETRY_CALCULATION.csv'))))))


















