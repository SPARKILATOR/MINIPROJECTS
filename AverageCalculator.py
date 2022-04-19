class Result:
    def __init__(self):
        self.length = int(input("ENTER NO. OF SUBJECTS IN THE EXAM :: "))
    def average(self):
        l = []
        print("\n")
        max_marks = int(input("MAX MARKS FOR EACH SUBJECT (SHOULD BE >= 10) : "))
        print("\n")
        if (max_marks < 10):
            print("PLEASE PUT VALID MAX_MARKS (VALUE SHOULD BE GREATER THAN 10)\n")
            max_marks = int(input("MAX MARKS FOR THE SUBJECT (SHOULD BE >= 10) : "))
        for i in range(0,self.length):
            a = int(input("ENTER MARKS  FOR SUBJECT (%r/%r) : " %(i+1,self.length)))
            if (a <= max_marks and a >= 0):
                l.append(a)
            else:
                print("\n")
                print("NOT A VALID INPUT, PLEASE INPUT VALUE IN BETWEEN 0 AND 100\n")
                a = int(input("ENTER MARKS  FOR SUBJECT (%r/%r) : " %(i+1,self.length)))
                l.append(a)
        for i in range(0,len(l)):
            if (l[i] < 33):
                print("\n***STUDENT FAILED***\n")
                print("FAILED ON THE SUBJECT -> %r/%r" %(l[i],len(l)))
                break
            if (i == (len(l)-1)):
                print("CONGRATULATION, STUDENT IS PASSED .....")
                print("\nAVERAGE/PERCANTAGE OF MARKS STUDENT GOT : %r" %(sum(l)/self.length))  
print("\n\n")
print("----------------------WELCOME TO GAANU RESULT MAKER PROGRAM-----------------------\n\n")
r = Result()
r.average()
