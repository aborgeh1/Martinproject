
from tkinter.filedialog import askopenfilename,asksaveasfilename
import pandas as pd
from Tacheometry import *
from Area_Calaculation import *
from Traversing_files import *
from tkinter import *

#Creating a class
class Surveying_calculations():
    def __init__(self,window):
        self.window=window
        self.stringvariable=StringVar()
        self.stringvariable.set('Data output')
        self.stringvariable1 = StringVar()
        self.stringvariable1.set('output')
        self.stringvariable2 = StringVar()
        self.stringvariable2.set('filepath')
        self.areavariable=StringVar()
        self.areavariable.set('filepath')
        self.areavariable1 = StringVar()
        self.areavariable1.set('filepath')
        self.Tacheovariable=StringVar()
        self.Tacheovariable.set('filepath')
        self.Tacheovariable1 = StringVar()
        self.Tacheovariable1.set('filepath')

    #Load path of file containing traverse data
    def Load_traverse_files(self):
        datafile=askopenfilename()
        return self.stringvariable2.set(datafile)

    #Calculate and output traverse computation results
    def calculate_Traverse(self):
        load_files=Traverse_label.get()
        Nortings = Northinsgs_calculations(Reading_Traverse_csv(load_files))
        travpointnames=Travpointnames(Reading_Traverse_csv(load_files))
        Eastings = Eastings_calculations(Reading_Traverse_csv(load_files))
        included_Angles=Included_angles(Reading_Traverse_csv(load_files))
        dataframe=pd.DataFrame({'Included Angles':included_Angles,'Northings':Nortings,'Easting':Eastings,'PointNames': travpointnames})
        dataframe1=dataframe.to_csv(Traverse_label_output.get())
        return self.stringvariable.set(f'{dataframe}'),dataframe.to_csv(Traverse_label_output.get())

    # Loading output path of computed traverse points
    def Traverse_output(self):
        Output=asksaveasfilename(filetypes=[('Comma Separated values','*.csv')])
        return self.stringvariable1.set(Output)

    # Loading path of file containing tacheometry data
    def Load_Tacheo_files(self):
        load_tacheo=askopenfilename()
        return self.Tacheovariable.set(load_tacheo)

    # calculating and returning out of computed Tacheometry points
    def Calculate_Tacheo(self):
        Tacheofile=Tacheo_label.get()
        northings=Northings_Coordinate_calcultion(Reading_Tacheo_csv(Tacheofile))
        eastings=Eastings_Coordinate_calculation(Reading_Tacheo_csv(Tacheofile))
        elevation1=Elevation(Reading_Tacheo_csv(Tacheofile))
        pointnames=left_right_pointnames(Reading_Tacheo_csv(Tacheofile))
        points=pd.DataFrame({'Northings':northings,'Eastings':eastings,'Elevation':elevation1,'Pointnames':pointnames})
        return self.stringvariable.set(points),points.to_csv(Tacheo_label_output.get())

    # Loading output path for saving tacheometry computed results
    def Tacheo_output(self):
        Tacheo_output=asksaveasfilename()
        return self.Tacheovariable1.set(Tacheo_output)

    # loading Area files from excel
    def Load_Area_files(self):
        area_data=askopenfilename()
        return self.areavariable.set(area_data)

    # calculate Area and output Area results
    def Calculate_Area(self):
        areafile=Area.get()
        return self.stringvariable.set(f'{Area_cal(Reading_files(areafile))}'),pd.DataFrame({'Area':[Area_cal(Reading_files(areafile))]}).to_csv(Area_label_output.get())

    # Load outputpath of file containing area of data
    def Area_output(self):
        areaoutput=asksaveasfilename()
        return self.areavariable1.set(areaoutput)


root=Tk()
Title=Label(root,text='Surveying calculations',font=('bold',12))
Title.pack(padx=50)
obj=Surveying_calculations(root)
root.geometry('350x350+10+10')

#CREATING WIDGETS FOR THE APP
#Creating OutPut Widgets
label = Label(root, height=30, width=50,bg='grey',bd=15)
label.place(x=450,y=250)
label = Label(root, textvariable=f'{obj.stringvariable}', height=28, width=45,bg='white',fg='black',bd=5)
label.place(x=479,y=280)

# Creating Traverse Widgets
Traverse_calculate_button=Button(root,text='calculate',height=2, width=15,bg='grey',command=obj.calculate_Traverse,fg='black')
Traverse_calculate_button.place(x=990,y=200)
Traverse_button=Button(root,height=2,width=4,text='open',bg='grey',command=obj.Load_traverse_files,fg='black')
Traverse_button.place(x=1230,y=85)
Traverse_button_output=Button(root,height=2,width=4,text='output',command=obj.Traverse_output,bg='grey',fg='black')
Traverse_button_output.place(x=1230,y=130)
Traverse_label=Label(root,width=50,bg='grey',bd=3)
Traverse_label.place(x=865,y=81,height=43)
Traverse_label=Entry(root,width=57,textvariable=obj.stringvariable2,bg='white',fg='black')
Traverse_label.place(x=870,y=87,height=30)
Traverse_label_output=Label(root,width=50,bg='grey')
Traverse_label_output.place(x=865,y=127,height=43)
Traverse_label_output=Entry(root,width=57,textvariable=obj.stringvariable1,bg='white',fg='black')
Traverse_label_output.place(x=870,y=133,height=30)
Traverse_heading_button=Label(root,text='TRAVERSE CALCULATION',height=2,width=30,bg='green',fg='white')
Traverse_heading_button.place(x=950,y=35)

#Creating Area Widgets
Area_button=Button(root,height=2,text='open',width=4,command=obj.Load_Area_files,bg='grey',fg='black')
Area_button.place(x=390,y=85)
Area=Label(root,width=50,bg='grey')
Area.place(x=22,y=81,height=43)
Area=Entry(root,width=57,textvariable=obj.areavariable,bg='white',fg='black')
Area.place(x=27,y=87,height=30)
Area_button_output=Button(root,height=2,text='output',command=obj.Area_output,width=4,bg='grey',fg='black')
Area_button_output.place(x=390,y=130)
Area_label_output=Label(root,width=50,bg='grey')
Area_label_output.place(x=22,y=127,height=43)
Area_label_output=Entry(root,width=57,textvariable=obj.areavariable1,bg='white',fg='black')
Area_label_output.place(x=27,y=133,height=30)
Area_Traverse_calculate_button=Button(root,text='calculate',height=2,command=obj.Calculate_Area, width=15,bg='grey',fg='black')
Area_Traverse_calculate_button.place(x=170,y=200)
Area_heading_button=Label(root,text='AREA CALCULATION',height=2,width=30,bg='green',fg='white')
Area_heading_button.place(x=100,y=35)

#Creating Tacheometry Widgets
Tacheo_heading_button=Label(root,text='TACKEOMETRY CALCULATION',height=2,width=30,bg='green',fg='white')
Tacheo_heading_button.place(x=530,y=35)
Tacheo_button2=Button(root,height=2,text='open',width=4,command=obj.Load_Tacheo_files,bg='grey',fg='black')
Tacheo_button2.place(x=810,y=85)
Tacheo_label=Label(root,width=50,bg='grey')
Tacheo_label.place(x=445,y=81,height=43)
Tacheo_label=Entry(root,width=57,textvariable=obj.Tacheovariable,bg='white',fg='black')
Tacheo_label.place(x=450,y=87,height=30)
Tacheo_calculate_button=Button(root,text='calculate',command=obj.Calculate_Tacheo,height=2, width=15,bg='grey',fg='black')
Tacheo_calculate_button.place(x=570,y=200)
Tacheo_button2_output=Button(root,height=2,text='output',command=obj.Tacheo_output,width=4,bg='grey',fg='black')
Tacheo_button2_output.place(x=810,y=130)
Tacheo_label_output1=Label(root,width=50,bg='grey')
Tacheo_label_output1.place(x=445,y=127,height=43)
Tacheo_label_output=Entry(root,width=57,textvariable=obj.Tacheovariable1,bg='white',fg='black')
Tacheo_label_output.place(x=450,y=133,height=30)

root.mainloop()







