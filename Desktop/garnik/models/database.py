import mysql.connector


class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=self.dbname
        )
        self.cursor = self.db.cursor(dictionary=True, buffered=True)

    def insert(self, table, data):
        # print (data.keys())
        # print(tuple(data.keys()))
        # print(list(data.keys()))
        keys = ', '.join(list(data.keys()))
        # values=data.values()
        values = (tuple(data.values()))
        query = f"""INSERT INTO {table} ({keys}) VALUE {values}"""
        # print(query)
        # print(keys)
        # print(values)
        self.cursor.execute(query)
        self.db.commit()
        # print(f"INSERTED ITEM {self.cursor.rowcount}")

    def get(self, table):
        query1 = f"SELECT * FROM {table}"
        self.cursor.execute(query1)
        d1 = self.cursor.fetchall()
        return d1
        # for i in d1:
        #     print(i['name'])

    def login(self, table, email):
        query7 = f"SELECT * FROM {table} WHERE email = '{email}'"
        self.cursor.execute(query7)
        d7 = self.cursor.fetchone()
        return d7

    def Delete(self, table, data):
        d2 = ""
        for key in data:
            d2 += " {} = '{}' AND ".format(key, data[key])
            # print(key, data[key])
        # print(d)
        query2 = f'DELETE  FROM {table} WHERE {d2[:-4]}'
        self.cursor.execute(query2)
        self.db.commit()
        # print(query2)

    def find(self, table, id):
        query3 = f"SELECT * FROM {table} WHERE id = {id}"
        self.cursor.execute(query3)
        d3 = self.cursor.fetchone()
        return d3

    def findAll(self, table, id):
        query15 = f"SELECT * FROM {table} WHERE user_id = {id}"
        self.cursor.execute(query15)
        d10 = self.cursor.fetchall()
        return d10

    # def update1(self, table, where):
    #     query4 = f"UPDATE {table} SET name = {where['name']}, surname = {where['surname']}" \
    #             f" WHERE id = {where['id']} AND age = {where['age']}"
    #     self.cursor.execute ( query4 )
    #     self.db.commit ()
    #     print ( f"INSERTED ITEM {self.cursor.rowcount}" )

    def update(self, table, data, where):
        data_set = ""
        data_where = ""

        for key in data:
            data_set += "{} = '{}', ".format(key, data[key])
        data_set = data_set[:-2]

        for key in where:
            data_where += "{} = '{}' AND ".format(key, where[key])
        data_where = data_where[:-4]

        sql = "UPDATE {} SET {} WHERE {}".format(table, data_set, data_where)
        self.cursor.execute(sql)
        self.db.commit()

    # def first(self,table,where):
    #     query5 = f"SELECT * FROM {table} WHERE {where}"
    #     self.cursor.execute ( query5 )
    #     d = self.cursor.fetchone ()
    #     print(d)

    def first(self, table, where):
        data_where = ""
        for key in where:
            data_where += "{} = '{}' AND ".format(key, where[key])
        data_where = data_where[:-4]

        query5 = f"SELECT * FROM {table} WHERE {data_where}"
        self.cursor.execute(query5)
        d = self.cursor.fetchone()
        # print(d)

    def word(self, table):
        query6 = f"SELECT id , hay FROM {table}"
        self.cursor.execute(query6)
        p = self.cursor.fetchall()
        return p

    def photo(self, table, id):
        query11 = f"SELECT * FROM {table} WHERE user_id={id} "
        self.cursor.execute(query11)
        d16 = self.cursor.fetchall()
        return d16

    def serch(self, table, name):
        # print(table)
        # print(name)
        query10 = f" SELECT * FROM {table} WHERE name LIKE '{name}%' "
        self.cursor.execute(query10)
        d17 = self.cursor.fetchall()
        return d17

    def add(self, id):
        query11 = f"""SELECT * FROM user 
            JOIN addFrend ON addFrend.from_id = user.id 
            WHERE to_id = {id}"""
        self.cursor.execute(query11)
        d18 = self.cursor.fetchall()
        return d18

    def getFrend(self, id):
        query12 = f""" SELECT * FROM user WHERE id IN (SELECT user_2_id FROM drug WHERE user_1_id={id} UNION
                        SELECT user_1_id FROM drug WHERE user_2_id={id})"""
        # print(query12)
        self.cursor.execute(query12)
        d19 = self.cursor.fetchall()
        # print(d19)
        return d19
    # ------------
    def friends(self, data):
        sql = f"""
        SELECT * FROM Login WHERE id in (SELECT user1_id FROM friend WHERE user2_id = {data} 
        UNION SELECT user2_id FROM friend WHERE user1_id = {data})"""
        # print(sql)
        self.cursor.execute(sql)
        d20 = self.cursor.fetchall()
        return d20

    def messenger(self, my_id, frend_id):
        slq = f""" SELECT messages.*, user.name, user.surname, user.photo FROM messages
                join  user ON user.id = messages.from_id
        WHERE (from_id={my_id} AND to_id={frend_id}) OR  (from_id={frend_id} AND to_id={my_id}) 
        order by  messages.id"""
        # print(slq)
        self.cursor.execute(slq)
        d21 = self.cursor.fetchall()
        # print(d21)
        return d21

