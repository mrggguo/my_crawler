import pymysql
db=pymysql.connect(host='localhost',user='root',password='12345678',port=3306,db='spiders')
cursor=db.cursor()
# cursor.execute('SELECT VERSION()')
# data=cursor.fetchone()
# print('Database Version:',data)
# # 创建数据库
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
# db.close()
# 创建表单
sql='CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))'
cursor.execute(sql)
# 插入与更新数据：如果主键不存在则插入，否则更新
data={
    'id':'2021003',
    'name':'Tim',
    'age':19
}
table='students'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql="INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE ".format(table=table,keys=keys,values=values)
update=','.join(["{key}=%s".format(key=key) for key in data])
sql+=update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('Success!')
        db.commit()
except:
    print('Fail!')
    db.rollback()
# # 删除数据
# table='students'
# condition='age<20'
# sql='DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# 查询数据
sql='SELECT * FROM students WHERE age>=10'
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    row=cursor.fetchone()
    while row:
        print(row)
        row=cursor.fetchone()
except:
    print('Error!')
db.close()