import sqlite3


class MySqlite3:
    """
    数据库通用类
    """

    _conn = None

    def __init__(self, database):
        """
        构造函数\n
        初始数据库连接
        """
        self._conn = sqlite3.connect(database)

    def __del__(self):
        """
        析构函数\n
        关闭数据库连接
        """
        if self._conn:
            self._conn.close()

    def _dict_factory(self, cursor, row):
        """
        将查询的数据集转为字典\n
        cursor 游标\n
        row 数据行
        """
        d = {}
        for index, col in enumerate(cursor.description):
            d[col[0]] = row[index]
        return d

    def execute(self, sql, args=[], result_dict=True, commit=True)->list:
        """
        执行数据库操作的通用方法\n
        参数：\n
        sql:sql语句\n
        result_dict:已字典格式返回\n
        commit:是否提交事务\n
        返回值：\n
        list 列表
        """
        if result_dict:
            self._conn.row_factory = self._dict_factory
        else:
            self._conn.row_factory = None

        #获取游标
        _cursor = self._conn.cursor()
        #执行SQL获取结果
        _cursor.execute(sql, args)
        if commit:
            self._conn.commit()
        data = _cursor.fetchall()
        _cursor.close()
        return data
