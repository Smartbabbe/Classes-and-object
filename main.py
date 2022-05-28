class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.track = tracks
        self.score = score
        pass

def change_name(self,new_name):
    self.name= new_name

def change_age(self,new_age):
    self.age= new_age

def change_tracks(self,new_tracks):
    self.tracks= new_tracks

def get_score(self):
    if isinstance(self.level,int):
        print(self.name,self.age,self.track,self.score)
    else:
        print("Age must be int. pls try again")





Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
