class student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"name is{self.name}\nroll is {self.roll}\n marks {self.marks}")