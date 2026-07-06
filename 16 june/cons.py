class student:
    c_name = "xyz"
    #lass method
    @classmethod

    def change_name(cls):
        return "class method"
    
    @classmethod
    def change_c_name(cls, new_name):
        cls.c_name = new_name
        return f"updated value is {cls.c_name}"
    print(student.change_name())
    print(student.change_c_name1("abc"))