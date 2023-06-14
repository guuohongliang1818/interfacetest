# 姓名：郭宏亮
# 时间：2023/6/14 20:23
import pymysql


class MysqlUtil:

    # 封装建立连接的对象
    @classmethod
    def get_conn(cls):
        conn = pymysql.connect(
            host="litemall.hogwarts.ceshiren.com",
            port=13306,
            user="test",
            password="test123456",
            database="litemall",
            charset="utf8mb4"
        )
        return conn

    # 执行sql语句
    @classmethod
    def execute_sql(cls, sql):
        connect = cls.get_conn()
        cursor = connect.cursor()
        cursor.execute(sql)  # 执行SQL
        record = cursor.fetchone()  # 查询记录
        return record


if __name__ == '__main__':
    # 执行sql语句查询user123这个用户的购物车有一个名称为 hogwarts1 的商品
    print(MysqlUtil.execute_sql("SELECT * from litemall_goods where name = '轻奢纯棉刺绣水洗四件套'"))
