# @Time : 2022-03-29 10:48 
# @Author : 金枝
import pymysql


class MySql:
    def __init__(self, host, user,  password):
        """数据库链接"""
        self.connect = pymysql.connect(
            host=host,
            user=user,
            password=password,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def select(self, sql):
        cursor = self.connect.cursor()  # 拿到数据集
        cursor.execute(sql)
        data = cursor.fetchall()  # 获取查询结果
        self.connect.commit()  # 提交数据，这样才能保证下次查询的是最新数据
        cursor.close()
        return data

    def updata(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()

    def insert(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()

    def close(self):
        if self.connect is not None:
            self.connect.close()


if __name__ == '__main__':
    mysql = MySql(host='localhost', user='root', password='root')
    user = mysql.select('SELECT *FROM flask_study.flask_user')
    print(user[0]['username'])





