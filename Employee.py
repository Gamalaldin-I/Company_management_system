class Employee:
    x=0

    def __init__(self) -> None:
      Employee.x+=1
      self.set_id(Employee.x)
      self.read()
      self.set_salary()

    def set_salary(self):
        self._salary=0

    def get_salary(self):
        return self._salary
    
    def setName(self,firstName:str,lastName:str):
        self.__name = firstName.capitalize()+ " " +lastName.capitalize()

    def getName(self):
        return self.__name
    def setSSN(self,ssn):
        self.SSN=ssn
    def getSSN(self):
        return self.SSN

    def setAge(self,MM,yyyy):
        currentYear = 124
        currentMonth = 3
        years=0
        months=0
        if MM < currentMonth :
            years = currentYear-(yyyy-1900)
        else:
            years = currentYear -(yyyy-1900+1)
        self.__age = years

    def getAge(self):
        age = str(self.__age) +' years'
        return age
    
    def setGender(self,gender):
        if gender == 0:
            self.__gender='male'
        else:
            self.__gender='female'

    def getGender(self):
        return self.__gender
    

    def set_id(self,id):
        self.id = id+1000

    def get_id(self):
        return self.id
    

    def set_phone(self,phone):
        self.__phone=phone

    def get_phone(self):
        line = self.__phone[0:3]
        if(line =='011'):
           line='Ettisalat'
        elif(line == '012'):
            line='Orange'
        elif(line == '010'):
            line ='Vodafone'
        elif(line =='015'):
            line = 'We'
        else:
            line = 'Unknown'
        return line,self.__phone
    
    def set_email(self,email):
        self.__email=email

    def get_email(self):
     b=self.__email.find('@')
     e=self.__email.find('.com')
     return self.__email[b+1:e], self.__email
    
    def set_address(self,country:str,government:str,city:str,st:str,n):
        self.__address=f'{n}- {st.capitalize()}.st {city.capitalize()} - {government.capitalize()} - {country.capitalize()}'

    def get_address(self):
        return self.__address
    

    def read(self):
        #input the firstname
        firstname=input('Enter your firstname : ')
        while(firstname.isdigit()):
            print('<< please enter valid fname >>')
            firstname=input('Enter your firstname : ')
        #input the lastname
        lastname=input('Enter your lastname : ')
        while(lastname.isdigit()):
            print('<< please enter valid lname >>')
            lastname=input('Enter your lastname : ')
        #set the name
        self.setName(firstname,lastname)
        #enter the SSN
        ssn=input('Enter the SSN number which consist 14 numbers')
        while(not len(ssn)== 14):
             ssn=input('Enter the SSN number which consist 14 numbers')
        self.setSSN(ssn)
        #input the date of birth
        print('Enter your birth day in this format dd mm yyyy')
        dd=int(input('Enter your day of birth : '))
        MM=int(input('Enter your Month of birth  :'))
        yyyy=int(input('Enter your Year of birth : '))
        while(not Employee.validBirthDay(dd,MM,yyyy)):
            print(' invalid date')
            print('Enter your birth day in this format dd mm yyyy')
            dd=int(input('Enter your day of birth : '))
            MM=int(input('Enter your Month of birth : '))
            yyyy=int(input('Enter your Year of birth : '))
        #set the age
        self.setAge(MM,yyyy)
        #input the gender
        gender=int(input('Male : 0 , female : 1  Enter your gender : '))
        while(not(gender==1 or gender==0)):
          print('retype the gender')
          gender=int(input('Male : 0 , female : 1  Enter your gender : '))
        #set the gender
        self.setGender(gender)
        #enter the phone number
        phone=input('Your phone number : ')
        while(phone.isalpha() or len(phone)>11):
          print('invalid phone number')
          phone=input('Your phone number : ')
        #set the phone number
        self.set_phone(phone)
        #enter the email
        email=input('Your  email : ')
        while(not(email.endswith('.com')) or email.find('@')==-1 ):
          print('invalid email number')
          email=input('Your email  : ')
        #set the email
        self.set_email(email)
        #enter the address
        country=input('Your country : ')
        gov=input('The name of your gov :  ')
        city=input('The name of your city  : ')
        st=input('The name of your street  : ')
        numberOfBuilding = input('Enter the number of your house  : ')
        self.set_address(country,gov,city,st,numberOfBuilding)

    def print(self):
        print(f'---------------- Employee : {self.get_id()} ----------------')
        self.info=f'''
Name   :  {self.getName()}
SSN    :  {self.getSSN()}
Age    :  {self.getAge()}
Gender :  {self.getGender()}
Phone  :  {self.get_phone()}
Email  :  {self.get_email()}
Address : {self.get_address()}
Salary :  {self.get_salary()} LE'''
        print(self.info)
    


    def splitBirthDay(dateOfBirth):
        dd= int(dateOfBirth[0])*10 +int(dateOfBirth[1])
        MM= int(dateOfBirth[3])*10 +int(dateOfBirth[4])
        yy= int(dateOfBirth[6])*10 +int(dateOfBirth[7])
        return dd,MM,yy
    
    def setDateOfBirth(self,dd,MM,yyyy):
        self.dateOfBirth=str(dd)+'-'+str(MM)+'-'+str(yyyy)
    def getDateOfBirth(self):
        return self.dateOfBirth

    def validBirthDay(dd,MM,yy):
        if (dd<0 or ((dd>28 and MM==2) or dd>31)) or (MM>12 or MM<1) or yy<1950:
            return False
        return True


