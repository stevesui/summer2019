import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="brian",
    passwd="brian",
    database = "terrordb",
    port=8889
)
echo "ugh!"

mycursor = mydb.cursor()

#mycursor.execute('SELECT id, org FROM `groups`')
mycursor.execute('SELECT org_id, org, year, num_kills, num_allies, num_attacks2 FROM `activity`')


myresult = mycursor.fetchall()

#result = mycursor.execute('truncate table groups')
#print ("truncate result = "+result)


for org_id, org, year, kills, allies, attacks in myresult:
    #org = org.lstrip();
    #org = org.rstrip();
    print(org_id)
    print(org)
    print(kills)
    print(allies)
    print(attacks)
    #org = org.strip()
    #mycursor.execute("Update `groups` set org = \""+org+"\" where id =" +str(id) )
    #mydb.commit()
    #print(org)
    #print("\n")
    #print(len(org))
    #mycursor.execute("select org_id, org from terrordb.activity where org = \"" + org + "\"")
    #selectRslt = mycursor.fetchall();
    #print(selectRslt)
    #mycursor.execute("UPDATE `activity` set org_id ="  + str(id) + " where org = \"" + org + "\"")
    #mydb.commit()
    

    
