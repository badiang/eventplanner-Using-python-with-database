import pymysql

""" Connect to database """
connection = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = '',
	db = 'event',


)

""" Add data to database """
def add_event(wat,wen,wer): 
    with connection.cursor() as cursor:
    	sql = "INSERT INTO `saveData` (`id`,`wat`,`wen`,`wer`) VALUES ( NULL, %s, %s, %s);"
    	try:
    		cursor.execute(sql, (wat,wen,wer))
    		print("Event Was Successfully Added")
    	except:
    		print("Access Denied!")
    connection.commit()
""" Read Data inside the database  """
def read_event(add_event):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `saveData`"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()

            print("\t\t--Event Planner Library--")
            print("")
            print("id\tWhat\t\tWhen\t\tWhere\n\t\t\t-Yr-M-D-")
            print("=======================================================================")
            for row in result:
                print('%s\t%s\t%s\t%s'%(str(row[0]),row[1],row[2],row[3]))
        except:
            print("Access Denied!")

    connection.commit()

""" Update Data inside the database """
def update_event(id):
    with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `saveData` WHERE  `id` = %s",id)
            cursor.fetchall()
            if cursor.rowcount > 0 :
                new_wat = raw_input("Enter New What: ")
                new_wen = raw_input("Enter New When: ")
                new_wer = raw_input("Enter New Where: ")
                cursor.execute("UPDATE saveData SET `wat`=%s, `wen`=%s, `wer`=%s WHERE `id` = %s",(new_wat,new_wen,new_wer,id))
                print("Successfully Update")
            else:
                print("ID'"+id+"' doesn't match")

    connection.commit()

""" Delete Data inside the database """
def delete_event(id):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `saveData` WHERE `id` = %s"
        try:
            cursor.execute(sql, id)
            if cursor.rowcount > 0 :
                del_event = "DELETE FROM `saveData` WHERE `id` = " + "'" + id + "'"
                cursor.execute(del_event)
                print ("Event Successfully Deleted")
            else:
                print "ID'"+id+"' is not Exist!"
        except:
            print ("Access Denied")

    connection.commit()

""" Choices """
loop = 1
while loop:
    print"\t\t--Event Planner--"
    print"Select ID Number"
    print"[1] Create"
    print"[2] Read"
    print"[3] Update"
    print"[4] Delete"
    print"[5] Exit\n"



    choice = raw_input("Enter your choice: ")

    if choice == '1':
        """ Enter All Required Information """
        wat              = raw_input('What: ')
        wen          	 = raw_input('When: ')
        wer         	 = raw_input('Where: ')
        
        
        add_event(wat,wen,wer)
        loop_2 = 1
    elif choice == '2':
        read_event(add_event)
        print("=======================================================================")
    elif choice == '3':
        id = raw_input("Enter ID that you whant to Update: ")
        update_event(id)
    elif choice == '4':
        id = raw_input("Enter ID that you whant to delete: ")
        delete_event(id)
    elif choice == '5':   
        print "\tThank You For Using Event Planner!!"
        print "\t\tGood Bye!!"

        break 
    else:
        print "Invalid Choice"

        """Looping To Continue The Activity"""

    loop_2 = 1
    while loop_2:
        cont = raw_input("\nDo you wish to continue ? [Y/N]: ").strip()
        if cont in 'Yy':
            loop_2 = 0
            loop = 1
        elif cont in 'Nn':
            print "\tThank You For Using Event Planner!!"
            print "\t\tGood Bye!!"
            loop_2 = 0
            loop = 0
        else:
            print 'Invalid Choice'
            loop_2 = 1
