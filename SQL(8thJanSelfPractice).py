#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[4]:


import mysql.connector as conn


# In[5]:


mydb=conn.connect(host='localhost',user='root',password='Nikerebona13@')


# In[6]:


mydb


# In[7]:


cursor=mydb.cursor()


# In[8]:


cursor.execute('show databases') 


# In[9]:


cursor.fetchall()


# In[12]:


cursor=mydb.cursor()


# In[13]:


cursor.execute("create database test2")


# In[14]:


cursor.execute('create table test2.ineuron(studentid int(10),firtname varchar(50),lastname varchar(35),registration int(10),classname varchar(30))')


# In[15]:


cursor.execute('use test2')


# In[16]:


cursor.execute('show tables')


# In[17]:


cursor.fetchall()


# In[45]:


cursor.execute('insert into test1.ineuron values(1457,"ansh","singh",145245,"FSDS2.0")')
cursor.execute('insert into test1.ineuron values(123,"Raj","Kapoor",1258,"FSDS")')


# In[46]:


mydb.commit()


# In[47]:


cursor.execute("select * from test1.ineuron")


# In[48]:


cursor.fetchall()


# In[51]:


cursor.execute('create table test1.glassdata(col1 int(10),col2 float(10,5),col3 float(10,5),col4 float(10,5),col5 float(10,5),col6 float(10,5),col7 float(10,5),col8 float(10,5),col9 float(10,5),col10 float(10,5),col11 float(10,5))')


# In[52]:


cursor.execute("show tables")


# In[53]:


cursor.fetchall()


# In[60]:


ls


# In[65]:


file=open("glass.data",'r')


# In[66]:


file.read()


# In[71]:


import csv
with open("glass.data","r") as f:
    glass_data=csv.reader(f,delimiter='\n')
    for i in glass_data:
        print(i)


# In[73]:


cursor.execute('insert into test1.glassdata values(1,1.52101,13.64,4.49,1.10,71.78,0.06,8.75,0.00,0.00,1)')


# In[74]:


mydb.commit()


# In[75]:


cursor.execute('select * from test1.glassdata')


# In[76]:


cursor.fetchall()


# In[18]:


import csv
with open('glass.data','r') as f:
    glass_data=csv.reader(f,delimiter='\n')
    for i in glass_data:
        print(i)
        print(f"insert into glassdata values ({str(i[0])})")
        cursor.execute(f"insert into test1.glassdata values ({str(i[0])})")
mydb.commit()


# In[19]:


import pandas as pd


# In[20]:


pd.read_sql("select * from test1.glassdata",mydb )


# In[21]:


pd.read_sql("show databases",mydb)


# In[1]:


# 12th Jan 2023 [SQL Part2]
import mysql.connector as conn
mydb=conn.connect(host='localhost',user='root',password='Nikerebona13@')


# In[2]:


cursor=mydb.cursor()


# In[3]:


cursor.execute('show databases')
cursor.fetchall()


# In[ ]:




