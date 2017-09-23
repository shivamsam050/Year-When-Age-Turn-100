import datetime
name= input("enter your name = ")
age= int(input("enter your age = "))
now = datetime.datetime.now()
current_year=now.year
if(age<100):
    extra_age=100-age
    desired_year=current_year+extra_age
    print("In ",desired_year," ",name," will be 100 year old")
else:
    print(name," age already more than 100 year")
