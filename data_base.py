# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:34:18 2020
@author: hp
"""

import pymysql
conn = pymysql.connect(
        host = 'x',
        port = 3306,
        user = 'admin',
        password = 'x',
        db = 'x'
        
        )
 
#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Details (id varchar(200), username varchar(200),password varchar(200) )

# """
# cursor.execute(create_table)


# def insert_details(id,username,password):
#     cur=conn.cursor()
#     cur.execute("INSERT INTO Details (id, username, password) VALUES (%d,%s,%s)", (id,username,password))
#     conn.commit()

# def get_details():
#     cur=conn.cursor()
#     cur.execute("SELECT *  FROM Details")
#     details = cur.fetchall()
#     return details
