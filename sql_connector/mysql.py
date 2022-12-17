'''
Above Script will be used to connect to the mysqlDB,
             querying the DB table to get the data stored in it,
             storing the data in the form of dictionary with emp_id as key 
             and other data associated with the id will be stored as value (nested dictionary)
'''
import mysql.connector as mysql
#used to connect to the Database
mydb = mysql.connect(host = "localhost", user = "root", passwd = "****", database='emp', auth_plugin='mysql_native_password')
sql_query = "select * from emp_detail"
mycursor = mydb.cursor()
mycursor.execute(sql_query)
# dictionary storing table data for future usage
res_dict = {}
#used to get column name
column_name = mycursor.description
result = mycursor.fetchall()
for i in range(len(result)):
    # hold data to get into the dictionary
    l = []
    for j in range(1,len(column_name)):
        l.append({column_name[j][0]:result[i][j]})
    res_dict[result[i][0]] = l
print("DATA ::: %r" %(res_dict))
'''
Table has been posted as attachement to this folder from which the data has been extracted as a dictionary
Result for the above code
DATA ::: 
{68319: [{'emp_name': 'ARYAN'}, {'job_name': 'PRESIDENT'}, {'manager_id': 0}, {'hire_date': '1991-08-12'}, {'salary': 6000}, {'commission': 0}, {'dep_id': 1001}], 
66928: [{'emp_name': 'BLAZE'}, {'job_name': 'MANAGER'}, {'manager_id': 68319}, {'hire_date': '1991-085-12'}, {'salary': 2750}, {'commission': 0}, {'dep_id': 3001}], 
67832: [{'emp_name': 'CLARKE'}, {'job_name': 'MANAGER'}, {'manager_id': 68319}, {'hire_date': '1991-08-11'}, {'salary': 2950}, {'commission': 0}, {'dep_id': 2001}], 
65646: [{'emp_name': 'RASH'}, {'job_name': 'MANAGER'}, {'manager_id': 68319}, {'hire_date': '1991-05-11'}, {'salary': 2650}, {'commission': 0}, {'dep_id': 1001}], 
67858: [{'emp_name': 'PALI'}, {'job_name': 'ANALYST'}, {'manager_id': 65646}, {'hire_date': '1995-05-11'}, {'salary': 2650}, {'commission': 0}, {'dep_id': 1001}], 
63679: [{'emp_name': 'SAND'}, {'job_name': 'CLERK'}, {'manager_id': 69062}, {'hire_date': '1996-05-11'}, {'salary': 650}, {'commission': 0}, {'dep_id': 2001}], 
64989: [{'emp_name': 'ADELYN'}, {'job_name': 'SALESMAN'}, {'manager_id': 66928}, {'hire_date': '1995-05-11'}, {'salary': 1650}, {'commission': 110}, {'dep_id': 2001}], 
65271: [{'emp_name': 'KARA'}, {'job_name': 'SALESMAN'}, {'manager_id': 66928}, {'hire_date': '1993-05-11'}, {'salary': 1350}, {'commission': 10}, {'dep_id': 3001}], 
66564: [{'emp_name': 'RAKA'}, {'job_name': 'SALESMAN'}, {'manager_id': 66928}, {'hire_date': '1996-05-11'}, {'salary': 1650}, {'commission': 1660}, {'dep_id': 3001}], 
68545: [{'emp_name': 'BABA'}, {'job_name': 'SALESMAN'}, {'manager_id': 66928}, {'hire_date': '1996-06-11'}, {'salary': 1330}, {'commission': 1160}, {'dep_id': 3001}], 
68736: [{'emp_name': 'VISHNU'}, {'job_name': 'CLERK'}, {'manager_id': 67858}, {'hire_date': '1993-06-11'}, {'salary': 1130}, {'commission': 0}, {'dep_id': 2001}], 
69000: [{'emp_name': 'AARU'}, {'job_name': 'CLERK'}, {'manager_id': 66928}, {'hire_date': '1999-06-11'}, {'salary': 730}, {'commission': 0}, {'dep_id': 1001}]}
'''
