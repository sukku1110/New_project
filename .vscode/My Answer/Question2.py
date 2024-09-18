import re
class Class2:
    def password_compliance(self,input):
        """Regex to comply with the password anomalies"""
        regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        for i in input:
            match1=re.match(regex,i)
            """Checking if the value of match was True or False accordingly an answer will be generated """
            if match1 :
                print("The answer for Second Question is :")
                print(i)

