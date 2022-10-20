import pandas as pd
import os
import numpy as np
import pickle
pd.set_option('display.max_columns', 15)


#Create new dataframe or load previous

if os.path.exists('Student_details.csv'):
    df_student=pd.read_csv('Student_details.csv')
else:
    df_student=pd.DataFrame(columns=['Name','Class','Roll Number','Admission Number','House',
                                 'DOB','DOJ','Address','Fee Status','Contact Number'])

if os.path.exists('marks.pkl'):
    with open('marks.pkl', 'rb') as f:
        mark = pickle.load(f)
else:
    mark=dict()

#Add new student
def addStudent(name,clas,rollno,admn,house,dob,doj,address,fee,contact):
    global df_student
    if admn in np.array(df_student['Admission Number']):
        print('Admission number already exists')
    else:
        df_student.loc[len(df_student)]=[name,clas,rollno,admn,house,dob,doj,address,fee,contact]
        df_student.to_csv('Student_details.csv',index=False)
        

#Delete student using admission number
def delStudentAdmn(admn):
    global df_student
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        idx=df_student[df_student['Admission Number']==admn].index[0]
        print('Deleted record:')
        print(df_student[df_student['Admission Number']==admn])
        df_student.drop(idx,inplace=True)
        df_student.reset_index(inplace=True)
        temp=df_student.pop('index')
        df_student.to_csv('Student_details.csv',index=False)
    


#Update name
def updateStudentName(admn,new_name):
    global df_student
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        idx=df_student[df_student['Admission Number']==admn].index[0]
        df_student.at[idx,'Name']=new_name   
        print('Updated Record:')
        print(df_student[df_student['Admission Number']==admn])
        df_student.to_csv('Student_details.csv',index=False)

def updateStudentContact(admn,new_contact):
    global df_student
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        idx=df_student[df_student['Admission Number']==admn].index[0]
        df_student.at[idx,'Contact Number']=new_contact   
        print('Updated Record:')
        print(df_student[df_student['Admission Number']==admn])
        df_student.to_csv('Student_details.csv',index=False)

def updateStudentRollNo(admn,new_rollno):
    global df_student
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        idx=df_student[df_student['Admission Number']==admn].index[0]
        df_student.at[idx,'Roll Number']=new_rollno
        print('Updated Record:')
        print(df_student[df_student['Admission Number']==admn])
        df_student.to_csv('Student_details.csv',index=False)

def updateStudentClass(admn,new_class):
    global df_student
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        idx=df_student[df_student['Admission Number']==admn].index[0]
        df_student.at[idx,'Class']=new_class
        print('Updated Record:')
        print(df_student[df_student['Admission Number']==admn])
        df_student.to_csv('Student_details.csv',index=False)
def updateStudentAddress(admn,new_address):
    global df_student
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        idx=df_student[df_student['Admission Number']==admn].index[0]
        df_student.at[idx,'Address']=new_address
        print('Updated Record:')
        print(df_student[df_student['Admission Number']==admn])
        df_student.to_csv('Student_details.csv',index=False)


def updateStudentHouse(admn,new_house):
    global df_student
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        idx=df_student[df_student['Admission Number']==admn].index[0]
        df_student.at[idx,'House']=new_house
        print('Updated Record:')
        print(df_student[df_student['Admission Number']==admn])
        df_student.to_csv('Student_details.csv',index=False)


def updateStudentFeeStatus(admn,new_feestatus):
    global df_student
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        idx=df_student[df_student['Admission Number']==admn].index[0]
        df_student.at[idx,'Fee Status']=new_feestatus
        print('Updated Record:')
        print(df_student[df_student['Admission Number']==admn])
        df_student.to_csv('Student_details.csv',index=False)

#Get record using name
def getStudentName(name):
    global df_student
    if name not in np.array(df_student['Name']):
        print('Name does not exist')
    else:
        print(df_student[df_student['Name']==name])

def getStudentRollno(rollno):
    global df_student
    if rollno not in np.array(df_student['Roll Number']):
        print('Roll Number does not exist')
    else:
        print(df_student[df_student['Roll Number']==rollno])
        
def getStudentClass(clas):
    global df_student
    if clas not in np.array(df_student['Class']):
        print('Class does not exist')
    else:
        print(df_student[df_student['Class']==clas])

def getStudentHouse(house):
    global df_student
    if house not in np.array(df_student['House']):
        print('House does not exist')
    else:
        print(df_student[df_student['House']==house])

def getStudentAdmn(admn):
    global df_student
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        print(df_student[df_student['Admission Number']==admn])

def getStudentDOB(dob):
    global df_student
    if dob not in np.array(df_student['DOB']):
        print('Date of birth does not exist')
    else:
        print(df_student[df_student['DOB']==dob])

def getStudentDOJ(doj):
    global df_student
    if doj not in np.array(df_student['DOJ']):
        print('Date of joining does not exist')
    else:
        print(df_student[df_student['DOJ']==doj])


def getStudentContact(cont):
    global df_student
    if cont not in np.array(df_student['Contact Number']):
        print('Contact Number does not exist')
    else:
        print(df_student[df_student['Contact Number']==cont])

def getStudentFee(fii):
    global df_student
    if fii not in np.array(df_student['Fee Status']):
        print('Fee Status does not exist')
    else:
        print(df_student[df_student['Fee Status']==fii])
        
#Enter student marks
def enterMarks(admn):
    global df_student,mark
    print(len(np.array(df_student['Admission Number'])))
    if admn not in np.array(df_student['Admission Number']):
        print('Admission Number does not exist')
    else:
        eng=float(input('Enter marks in English'))
        maths=float(input('Enter marks in Maths'))
        phy=float(input('Enter marks in Physics'))
        chem=float(input('Enter marks in Chemistry'))
        cs=float(input('Enter marks in CS'))
        mks=[eng,maths,phy,chem,cs]
        mark[admn]=mks        
        with open('marks.pkl', 'wb') as f:
            pickle.dump(mark, f)


#Get marks
def getMarks(admn):      
    global df_student,mark
    if admn in np.array(df_student['Admission Number']) and admn in mark.keys():
        print('English:',mark[admn][0])
        print('Maths:',mark[admn][1])
        print('Physics:',mark[admn][2])
        print('Chemistry:',mark[admn][3])
        print('Computer Science:',mark[admn][4])
    
    elif admn in np.array(df_student['Admission Number']) and admn not in mark.keys():
        print('No marks entered!')
    else:
        print('Admission Number does not exist')
#roll number list
def sortRollno():
    global df_student
    print(df_student.sort_values(by='Roll Number'))
    

#report card
def reportcard(admission):
        print(df_student[['Name','Admission Number','Roll Number','Class','House']][df_student['Admission Number']==admission])
        getMarks(admission)



def main():
    global df_student,marks
    print('Dataframe created')
    while True:
        print('1....add entry')
        print('2....update name')
        print('3....update class')
        print('4....update roll no')
        print('5....update house')
        print('6....update address')
        print('7....update fee status')
        print('8....update contact no')
        print('9....fetch record via admission number')
        print('10....fetch records via name')
        print('11....fetch records via class')
        print('12....fetch records via roll no')
        print('13....fetch records via house')
        print('14....fetch records via DOB')
        print('15....fetch records via DOJ')
        print('16....fetch records via fee status')
        print('17....fetch records via contact no')
        print('18....enter marks')
        print('19....get marks via admission number')
        print('20....Display')
        print('21....Report Card')
        print('22...Delete Record')
        print('23....Exit')
        
        ch=int(input('Enter your choice'))
        if ch==1:
            namo=input('Enter name ')
            classi=input('Enter class ')
            rollnum=int(input('Enter roll no '))
            admno=int(input('Enter Admission Number '))
            hehe=input('Enter house ')
            dobi=input('Enter DOB(DD/MM/YYYY) ')
            doji=input('Enter DOJ(YYYY) ')
            ad=input('Enter address ')
            fees=input('Enter fee status ')
            conta=input('Enter contact number ')
            
            addStudent(namo,classi,rollnum,admno,hehe,dobi,doji,ad,fees,conta)
            
        elif ch==2:
            admn=int(input('enter admission number'))
            new_name=input('enter new name')
            updateStudentName(admn,new_name)
        elif ch==3:
            admn=int(input('enter admission number'))
            cles=input('enter new class')
            updateStudentClass(admn,cles)
        elif ch==4:
            admn=int(input('enter admission number'))
            rickroll=int(input('enter new roll no'))
            updateStudentRollNo(admn,rickroll)
        elif ch==5:
            admn=int(input('enter admission number'))
            new_house=input('enter house')
            updateStudentHouse(admn,new_house)
        elif ch==6:
            admn=int(input('enter admission number'))
            add=input('enter address')
            updateStudentAddress(admn,add)
        elif ch==7:
            admn=int(input('enter admission number'))
            foo=input('enter fee status')
            updateStudentFeeStatus(admn,foo)
        elif ch==8:
            admn=int(input('enter admission number'))
            conti=input('enter contact no')
            updateStudentContact(admn,conti)
        elif ch==9:
            admn=int(input('enter admission number'))
            getStudentAdmn(admn)
            input()
        elif ch==10:
            n=input('enter name')
            getStudentName(n)
            input()
        elif ch==11:
            clas=input('enter class')
            getStudentClass(clas)
            input()
        elif ch==12:
            ro=int(input('enter roll number'))
            getStudentRollno(ro)
            input()
        elif ch==13:
            h=input('enter house')
            getStudentHouse(h)
            input()
        elif ch==14:
            dob=input('enter DOB')
            getStudentDOB(dob)
            input()
        elif ch==15:
            doj=int(input('enter DOJ '))
            getStudentDOJ(doj)
            input()
        elif ch==16:
            foo=input('enter fee status')
            getStudentFee(foo)
            input()
        elif ch==17:
            contu=int(input('enter Contact Number'))
            getStudentContact(contu)
            input()
        elif ch==18:
            admn=int(input('enter admission number'))
            enterMarks(admn)
            input()
        elif ch==19:
            admn=int(input('enter admission number'))
            getMarks(admn)
            input()
        elif ch==20:
            sortRollno()
            input()
        elif ch==21:
            admission=int(input('Enter admission number '))
            reportcard(admission)
            input()
        elif ch==22:
            admn=int(input('Enter Admission Number'))
            delStudentAdmn(admn)
        elif ch==23:
            print('Goodbye ')
            break
        else:
            print('not valid')
main()
