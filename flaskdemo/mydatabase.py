import sqlite3
class MyDatabase:
    def __init__(self):
        self.con=sqlite3.connect('mydatabase.db')
        print("connected")
        self.cur=self.con.cursor()
        print("created cursor object")
        sql="create table if not exists company(id integer primary key autoincrement,tit varchar(1000),desc varchar(1000),date DATE NOT NULL);"
        self.cur.execute(sql)
        print("table created")
        self.cur.execute("select * from company")
        print(self.cur.fetchall())

    def insert(self,sql):
        self.cur.execute(sql)
        self.con.commit()
        print("inserted")


    def view(self):
        self.cur.execute('select * from company')
        data=self.cur.fetchall()
        return data

    def update(self,sql):
        self.cur.execute(sql)
        self.con.commit()

    def delete(self,sql):
        self.cur.execute(sql)
        self.con.commit()



    

    # def ins_del_up(self,sql):
    #     self.cur.execute(sql)
    #     self.con.commit()

     
    # def selectall(self,sql):
    #     self.cur.execute(sql)
    #     data=self.cur.fetchone()

    
    def selectone(self,sql):
        self.cur.execute(sql)
        
        d=self.cur.fetchone()
        print(d)
        return d
mydb=MyDatabase()
