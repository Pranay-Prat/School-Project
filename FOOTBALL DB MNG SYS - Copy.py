while True:
  from mysql import connector
  from prettytable import from_db_cursor
  import matplotlib.pyplot as plt
  import numpy as np
  mydb=connector.connect(host='localhost',user='root',passwd='Pranay',auth_plugin='mysql_native_password',database='Project')
  if mydb.is_connected()==False:
      print("Connection Error")
  mycursor=mydb.cursor()

#Functions
  def youngplayers():
      ay=int(input("Enter the age below which you want the names of the players:-"))
      mycursor.execute("select * from leagues where Age<{} order by Age ".format(ay))
      x=from_db_cursor(mycursor)
      print(x)
      mydb.close()

  def oldplayers():
      ao=int(input("Enter the age above which you want the names of the players:-"))
      mycursor.execute("select * from leagues where Age>{} order by Age DESC".format(ao))
      x=from_db_cursor(mycursor)
      print(x)
      mydb.close()

  def nationplayers():
      nation1=input("Enter the team whose players you want:-")
      mycursor.execute("select * from leagues where Nationality = '{}'".format(nation1))
      x=from_db_cursor(mycursor)
      print(x)
      mydb.close()

  def teamplayers():
      team1=input("Enter the team whose players you want:-")
      mycursor.execute("select * from leagues where Club = '{}'".format(team1))
      x=from_db_cursor(mycursor)
      print(x)
      mydb.close()

  def valueplayersabove():
      value1=int(input("Enter the value in million euros above which you want the names of the players:-"))
      mycursor.execute("select * from leagues where Value_In_Million_Euros >{} order by Value_In_Million_Euros".format(value1))
      x=from_db_cursor(mycursor)
      print(x)
      mydb.close()

  def valueplayersbelow():
      value2=int(input("Enter the value in million euros below which you want the names of the players:-"))
      mycursor.execute("select * from leagues where Value_In_Million_Euros < {} order by Value_In_Million_Euros ".format(value2))
      x=from_db_cursor(mycursor)
      print(x)
      mydb.close()

  def sumvalclubs():
      L=[]
      A=[]
      mycursor.execute("select sum(Value_In_Million_Euros) from Leagues group by Club")
      for i in mycursor:
          L+=i
      mycursor.execute("select Club from Leagues group by Club")
      for j in mycursor:
          A+=j
      plt.barh(A,L, color="Turquoise")
      plt.xticks([120, 240, 360, 480, 600, 720, 840,960])
      plt.show()
      mydb.close()

  def sumvalnation():
      L=[]
      A=[]
      mycursor.execute("select sum(Value_In_Million_Euros) from Leagues group by Nationality")
      for i in mycursor:
          L+=i
      mycursor.execute("select Nationality from Leagues group by Nationality")
      for j in mycursor:
          A+=j
      plt.barh(A,L, color="Pink")
      plt.xticks([120, 240, 360, 480, 600, 720, 840,960,1080,1200,1320])
      plt.show()
      mydb.close()

  def avgageclub():
      L=[]
      A=[]
      mycursor.execute("select avg(Age) from Leagues group by Club")
      for i in mycursor:
          L+=i
      mycursor.execute("select Club from Leagues group by Club")
      for j in mycursor:
          A+=j
      plt.barh(A,L, color="#7851a9")
      plt.xticks([5,10,15,20,25,30,35,40])
      plt.show()
      mydb.close()

  def avgagenat():
      L=[]
      A=[]
      mycursor.execute("select avg(Age) from Leagues group by Nationality")
      for i in mycursor:
          L+=i
      mycursor.execute("select Nationality from Leagues group by Nationality")
      for j in mycursor:
          A+=j
      plt.barh(A,L, color="#DC143C")
      plt.xticks([5,10,15,20,25,30,35,40])
      plt.show()
      mydb.close()
      
  def indstat():
      name1=input("Enter the name of the Player-")
      mycursor.execute("select * from leagues where Name = '{}'".format(name1))
      x=from_db_cursor(mycursor)
      print(x)
      mydb.close()

#Menu
  print("                                                                WELCOME TO FOOTY DATA")
  print("FOOTY DATA is a Football Stats Database Management useful for Football Leagues and Boards to keep a track of all the details of footballers playing in various leagues across the world.")
  print("Here are the operations you can perform:-")
  print("1.Enter new record")
  print("2.Delete record")
  print("3.Update record")
  print("4.Sort Statistics")
  print("5.Team Statistics")



  choice=int(input("Enter the operation you want to perform(serial number):"))

#New Record
  if choice==1:
      name=input("Enter the name of the player:-")
      age=int(input("Enter the age of the player:-"))
      club=input("Enter the club for which the player plays:-")
      nat=input("Enter the nationality of the player:-")
      pos=input("Enter the player's position on the field:-")
      lig=input("Enter the league in which the player plays:-")
      mil=int(input("Enter the value of the player(in millions):-"))
      mycursor.execute("insert into leagues values('{}',{},'{}','{}','{}','{}',{})".format(name,age,club,nat,pos,lig,mil))
      print("New Record added successfully.")
      ch=input("Do you want to see the record? YES or No-")
      if ch=='Yes' or 'yes':
          mycursor.execute("select * from leagues where Name = '{}'".format(name))
          x=from_db_cursor(mycursor)
          print(x)
      else:
          print("Okay")
      mydb.commit()
      mydb.close()

#Delete Record
  if choice==2:
      name1=input("Enter the name of the player whose record you want to delete: ")
      mycursor.execute("Delete from leagues where Name='name1'")
      mydb.commit() 
      print("Record deleted successfully.")
      

#Update Record    
  if choice==3:
      name1=input("Enter the name of the player whose data you want to update-")
      ch=input("What do you want to update-")
      if ch=='Name':
          n=input("Enter the new name of the player-")
          mycursor.execute("UPDATE Leagues SET Name = '{}' WHERE Name='name1'".format(n))
      if ch=='Age':
          n=int(input("Enter the new Age of the player-"))
          mycursor.execute("UPDATE Leagues SET Age = {} WHERE Name='name1'".format(n))
      if ch=='Club':
          n=input("Enter the new Club of the player-")
          mycursor.execute("UPDATE Leagues SET Club = '{}' WHERE Name='name1'".format(n))
      if ch=='Position':
          n=input("Enter the new Position of the player-")
          mycursor.execute("UPDATE Leagues SET Position = '{}' WHERE Name='name1'".format(n))
      if ch=='League':
          n=input("Enter the new League of the player-")
          mycursor.execute("UPDATE Leagues SET League = '{}' WHERE Name='name1'".format(n))
      if ch=='Value':
          n=int(input("Enter the new Value of the player-"))
          mycursor.execute("UPDATE Leagues SET Value_In_Million_Euros = {} WHERE Name='name1'".format(n))
      else:
          print("Not a valid Option")
      mydb.commit()
      print("The record has been updated successfully.")
      mydb.close()      
    
    
#Sort Statistics
  if choice==4:
      print("How do you want to sort the data from the table?")
      print("Your options are--")
      print("a.Sort by age- players younger than a particular age")
      print("b.Sort by age- players older than a particular age")
      print("c.Sort by the Nationality ")
      print("d.Sort by the Team from which the players plays")
      print("e. Sort by value of a player- above a particular value")
      print("f.Sort by value of a player- below a particular value")
      print("g.Individual Player Stats")
      choosing=input("Enter the desired function- serial alphabet(a,b,c,d,e,f or g-);-")
      if choosing=='a':
          youngplayers() 
      if choosing=='b':
          oldplayers()
      if choosing=='c':
          nationplayers()
      if choosing=='d':
          teamplayers()
      if choosing=='e':
          valueplayersabove()
      if choosing=='f':
          valueplayersbelow()
      if choosing=='g':
          indstat()

#Team Statistics
  if choice==5:
      print("How do you want to sort the data from the table?")
      print("Your options are-")
      print("a.Total Value of Clubs")
      print("b.Total Value of Nations")
      print("c.Average Age of players of Clubs")
      print("d.Average Age of Players Of Nation")
      choosing=input("Enter the desired function serial alphabet(a,b,c or d)-")
      if choosing=='a':
          sumvalclubs()
      if choosing=='b':
          sumvalnation()
      if choosing=='c':
          avgageclub()
      if choosing=='d':
          avgagenat()

  ch=input("Do you want to perform other operation? Type Yes or No-")
  if ch=='no'or ch=='NO' or ch=='No' or ch=='nO':
      break    
print("Thank you for using FOOTY DATA")    
    
    
    

    
    
    
