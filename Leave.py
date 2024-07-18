from datetime import datetime as dt
lt=["sick leave","earn leave","maternity leave","casual leave"]
userid='admin'
password='one'
l={
    1:{
        "name":"user1",
        "psw":"pwd1"
    },
    2:{
        "name":"user2",
        "psw":"pwd2"
    },
    3:{"name":"user3","psw":"pwd3"},
    4:{"name":"user4","psw":"pwd4"}
}
d={1:{"name":"user1","post":"asst professor","Dept":"CSE","sick leave":3,"earn leave":1,"maternity leave":0,"casual leave":2},
   2:{"name":"user2","post":"asst professor","Dept":"Civil","sick leave":4,"earn leave":3,"maternity leave":0,"casual leave":1},
   3:{"name":"user3","post":"asst professor","Dept":"EEE","sick leave":2,"earn leave":4,"maternity leave":0,"casual leave":2},
   4:{"name":"user4","post":"asst professor","Dept":"Mechanical","sick leave":1,"earn leave":5,"maternity leave":0,"casual leave":3}
}
p=["user1","user2","user3","user4"]

print('                           CBIT ONLINE LEAVE MANAGEMENT SYSTEM')
print('------------------------------------------------------------------------------------------------')
print()
print('''Choose:
    1.Admin Login
    2.User Login''')
print()


try:
    q=int(input('Enter your choice: '))
    print()
    if q==1:                             #admin
        print('***** ADMIN LOGIN *****')
        print()
        i = True
        while i:
            id = input('Enter id:')
            if id == userid:
                pwd = input('Enter password: ')
                if pwd != password:
                    print('Enter correct password.......')
                    print()
                else:
                    print('Logged in.......')
                    i = False
                    k = True
                    while k:
                        print()
                        print('1.To add  2.To delete  3.To modify  4. To view details of selected user 5.To quit')
                        print()
                        n = int(input('Choose: '))
                        print()
                        if n == 1:
                            d[len(d) + 1] = {}
                            d[len(d)]["name"] = input('Enter name: ')
                            if d[len(d)]["name"] in p:
                                print('User with given name exists already........')

                            else:
                                d[len(d)]["post"] = input('Enter post: ')
                                d[len(d)]["Dept"] = input('Enter department: ')
                                d[len(d)]["sick leave"] = int(input('Enter no.of sick leaves taken: '))
                                d[len(d)]["earn leave"]= int(input('Enter no.of earn leaves taken: '))
                                d[len(d)]["maternity leave"]=int(input('Enter no.of maternity leaves taken: '))
                                d[len(d)]["casual leave"]=int(input('Enter no.of casual leaves taken: '))
                                p.append(d[len(d)]["name"])
                                print('User Added.......')
                                f = open('user.txt', 'w')
                                for i in range(1, len(d) + 1):
                                    f.write(str(i) + ' ' + '=' + ' ' + repr(d[i]))
                                    f.write('\n')
                                f.close()
                                # create file and store data
                            print()
                        elif n == 2:
                            s = input('Enter element to delete: ')
                            for i in range(1, len(d) + 1):
                                if s == d[i]["name"]:
                                    d[i]["name"]=None
                                    d[i]["post"]=None
                                    d[i]["Dept"]=None
                                    d[i]["sick leave"]=None
                                    d[i]["earn leave"]=None
                                    d[i]["maternity leave"]=None
                                    d[i]["casual leave"]=None
                                    print('Deleted......')
                                    f = open('user.txt', 'w')
                                    for i in range(1, len(d) + 1):
                                        f.write(str(i) + ' ' + '=' + ' ' + repr(d[i]))
                                        f.write('\n')
                                    f.close()
                                    break

                            else:
                                print('Entered user doesnt exist.......')
                                # if selected then delete this from created file
                            print()
                        elif n == 3:
                            u = input('Enter which user data to be modified:')
                            print()
                            for i in range(1, len(d) + 1):
                                if u == d[i]["name"]:
                                    d[i]["name"] = input('Enter name:')
                                    d[i]["post"] = input('Enter post:')
                                    d[i]["Dept"] = input('Enter department:')
                                    d[i]["sick leave"] = int(input('Enter no.of sick leaves taken: '))
                                    d[i]["earn leave"] = int(input('Enter no.of earn leaves taken: '))
                                    d[i]["maternity leave"] = int(input('Enter no.of maternity leaves taken: '))
                                    d[i]["casual leave"] = int(input('Enter no.of casual leaves taken: '))
                                    print('Details modified.......')
                                    f = open('user.txt', 'w')
                                    for i in range(1, len(d) + 1):
                                        f.write(str(i) + ' ' + '=' + ' ' + repr(d[i]))
                                        f.write('\n')
                                    f.close()

                                    break
                            else:
                                print('Entered user doesnt exist.........')
                                # modify
                            # same here
                            print()
                        elif n==4:
                            w=input('Enter username of required user:')
                            print()
                            for i in range(1,len(d)+1):
                                if w == d[i]["name"]:
                                    if d[i]["name"] == None:
                                        print('Entered user details doesnt exist.......')
                                        break
                                    else:
                                        print('Name:', d[i]["name"])
                                        print('Post:', d[i]["post"])
                                        print('Department:', d[i]["Dept"])
                                        print('No.of sick leaves taken:', d[i]["sick leave"])
                                        print('No.of earn leaves taken:', d[i]["earn leave"])
                                        print('No.of maternity leaves taken:', d[i]["maternity leave"])
                                        print('No.of casual leaves taken:', d[i]["casual leave"])
                                        break
                            else:
                                print('Entered user doesnt exist.......')
                                print()
                                    
                        elif n == 5:
                            print('Logged out........')
                            quit()
                            print()
                        elif n>5:
                            print('Choose correct option.......')
                            print()
            else:
                print('Enter correct id........')
                print()
    elif q==2:
        print('****** USER LOGIN *******')
        print()
        i = True
        while i:
            u = input('Enter userid: ')
            j = 1

            while j <= len(l):
                if u == l[j]["name"]:
                    pd = input('Enter password: ')
                    if pd not in l[j]["psw"]:
                        print('Enter correct passowrd')
                        print()
                    else:
                        print('Logged in.......')

                        i = False
                        k = True
                        while k:
                            print()
                            print("1.To view details 2.To check no of leaves remaining 3. To apply for leave 4. To exit")
                            print()
                            n = int(input('Choose:'))
                            print()
                            if n == 1:
                                print('Name:',d[j]["name"])
                                print('Post:',d[j]["post"])
                                print('Department:',d[j]["Dept"])
                                print('No.of sick leaves taken:',d[j]["sick leave"])
                                print('No.of earn leaves taken:',d[j]["earn leave"])
                                print('No.of materinity leaves taken:',d[j]["maternity leave"])
                                print('No.of casual leaves taken:',d[j]["casual leave"])
                                print()
                            if n == 2:
                                print('No of sick leaves remaining: ',20-d[j]["sick leave"])
                                print('No of earn leaves remaining:', 6-d[j]["earn leave"])
                                print('No of maternity leaves remaining:', 180 - d[j]["maternity leave"])
                                print('No of casual leaves remaining:  ',20-d[j]["casual leave"])
                                print()
                            elif n == 3:
                                print('''choose leave option and check no.of leaves alloted for each leave type:
                                1. sick leave - 20 days per annum
                                2. earn leave - 6 days per annum
                                3. casual leave - 20 days per annum
                                4. maternity leave - 6 months''')
                                print()
                                m = int(input('Enter no of leaves:'))
                                p = input('Enter reason for leave:')
                                if p == "sick leave":
                                    if m + d[j]["sick leave"] > 20:
                                        print('Cant apply for leave.....')
                                    else:
                                        print('Leave application sent......')
                                elif p == "casual leave":
                                    if m + d[j]["casual leave"] > 20:
                                        print('Cant apply for leave.....')
                                    else:
                                        print('leave application sent......')
                                elif p == 'maternity leave':
                                    if m + d[j]["maternity leave"] > 180:
                                        print('Cant apply for leave......')
                                    else:
                                        print('Leave application sent......')
                                elif p == "earn leave":
                                    if m + d[j]["earn leave"] > 6:
                                        print('cant apply for leave......')
                                    else:
                                        print('Leave application sent.......')
                                else:
                                    print('Entered leave type doesnt exist')
                                print()
                            elif n == 4:
                                print('Logged out......')
                                quit()

                            elif n>4:
                                print('Choose correct option........')
                                print()
                    break
                j = j + 1
            else:
                print('Enter correct userid')
                print()
    else:
        print('Enter correct option......')
except (ValueError,KeyError):
    print('Enter correct value........')
          


