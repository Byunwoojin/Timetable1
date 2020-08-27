lec={}
choose=0
class Lecture():
    def __init__(self,lecname,professor,limit,place) :
        self.name =lecname
        self.professor =professor
        self.limit =limit
        self.place =place

    def changeLimitOfStudent(self,new_limit):
        lec[lecname].limit=new_limit
    def changePlace(self,new_place):
        lec[lecname].place=new_place
    def printInfo(self):
        print("Professor : ", lec[lecname].professor)
        print("Number of students : ", lec[lecname].limit)
        print("Place: ", lec[lecname].place)
            
            
while True:
    print("********************************")
    print("           Time table           ")
    print("********************************")
    print("  1.Open new class")
    print("  2.Change limit of students")
    print("  3.Change calssroom")
    print("  4.Print lecture info")
    print("  5.Exit")
    print("********************************")
    print()
    choose=int(input("Choose >>"))
    if choose==1:
        lecname=input("Lecture name : ")
        professor=input("Professor : ")
        limit=int(input("Limit of student :"))
        place=input("Place : ")
        lec[lecname]=Lecture(lecname,professor,limit,place)
    elif choose==2:
        lecname=input("Enter lecture name : ")
        new_limit=int(input("Enter new limit of students : "))
        lec[lecname].changeLimitOfStudent(new_limit)
    elif choose==3:
        lecname=input("Enter lecture name : ")
        new_place=input("Enter new classroom :")
        lec[lecname].changePlace(new_place)
    elif choose==4:
        lecname=input("Enter lecture name : ")
        lec[lecname].printInfo()
    elif choose==5:
              break
