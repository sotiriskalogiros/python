import datetime
year=int(input("give me the year:"))
month=int(input("give me the month:"))
if month==1:
    m="Jenuary"
elif month==2:
    m="February"
elif month==3:
     m="March"
elif month==4:
     m="April"
elif month==5:
     m="May"
elif month==6:
     m="June"
elif month==7:
     m="July"
elif month==8:
     m="August"
elif month==9:
     m="September"
elif month==10:
     m="October"
elif month==11:
     m="November"
elif month==12:
    m="December"
print(m,year)
print("S","M","T","W","T","F","S")
calendar={}
days=(datetime.date(year, month+1, 1) - datetime.date(year,month, 1) ).days
day1=datetime.date(year,month,1)
day1=day1.weekday()
if day1==0:
    print(' ','1',end=' ')
    x=2
elif day1==1:
    print(' ',' ','1',end=' ')
    x=3
elif day1==2:
    print(' ',' ',' ','1',end=' ')
    x=4
elif day==3:
     print(' ',' ',' ',' ','1',end=' ' )
     x=5
elif day==4:
    print(' ',' ',' ',' ',' ','1',end=' ')
    x=6
elif day==5:
    print(' ',' ',' ',' ',' ',' ','1',end=' ')
    x=7
elif day==6:
    print('1',end=' ' )

for i in range(2,days+1) :
    x+=1
    print(i,end=' ')
    if x%7==0 :
        print('\n')

     
