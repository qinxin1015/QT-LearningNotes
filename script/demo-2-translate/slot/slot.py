
class CollectSlot:

    @staticmethod
    def to_mysql(conn, word, means):
        """
            接收3个参数：
                conn：数据库连接对象
                word：单词
                means：意思（翻译结果）
        """
        try:
            with conn.cursor() as cur:
                # 查询单词是否存在单词本中
                sql = 'select id from wordbook where word="%s"' % word
                if cur.execute(sql):
                    return

                # 存入
                sql = 'insert into wordbook(word, means) values("%s", "%s")' % (word, means)
                cur.execute(sql)

            conn.commit()
        except:
            conn.rollback()


class DictionarySlot:

    @staticmethod
    def to_mysql(conn, word, means):
        """
            要接收3个参数：
                conn：数据库连接对象
                word：单词
                means：意思（翻译结果）
        """

        try:
            with conn.cursor() as cur:
                # 查询单词是否存在单词本中
                sql = 'select id from dictionary where word="%s"' % word
                if cur.execute(sql):
                    return

                # 存入
                sql = 'insert into dictionary(word, means) values("%s", "%s")' % (word, means)
                cur.execute(sql)

            conn.commit()
        except:
            conn.rollback()


class GetWord:
    """获取单词"""
    @staticmethod
    def from_mysql(conn, page=1):
        """
            接收2个参数：
                conn：数据库连接对象
                page：(int or str) 页数 每页8个
        """
        data = ()
        # -------------- 容错处理 ---------------- #
        if isinstance(page, str):
            page = int(page)
        if not(isinstance(page, int) or isinstance(page, str)):
            return data
        # -------------------------------------- #

        try:
            with conn.cursor() as cur:
                # 在数据库库中查询 8 条数据
                sql = 'select word,means from dictionary where is_delete=0 and id>%s limit 8' % ((page - 1)*8)
                cur.execute(sql)
                data = cur.fetchall()

            conn.commit()
        except:
            conn.rollback()

        return data


    @staticmethod
    def all_count(conn):
        """
            接收1个参数：
                conn：数据库连接对象
        """
        count = 0
        try:
            with conn.cursor() as cur:
                # 查询单词
                sql = 'select count(id) from dictionary where is_delete=0'
                cur.execute(sql)
                count = cur.fetchone()[0]
            conn.commit()
        except:
            conn.rollback()

        return count


class UpdateMean:
    """修改单词意思"""
    @staticmethod
    def update(conn, means, word):
        """
            接收3个参数：
                conn：数据库连接对象
                word：单词
                means：意思（翻译结果）
        """
        status = 0      # 修改失败，status的值就仍然是 0 
        try:
            with conn.cursor() as cur:
                # 修改数据库表格，修改单词的意思
                sql = 'update dictionary set means="%s" where word="%s"' % (means, word)
                status = cur.execute(sql)
            conn.commit()
        except:
            conn.rollback()

        return status


class DeleteWord:
    """删除单词"""
    @staticmethod
    def delete(conn, word):
        """
            接收2个参数：
                conn：数据库连接对象
                word：单词
        """
        status = 0
        try:
            with conn.cursor() as cur:
                # 查询单词
                sql = 'update dictionary set is_delete = 1 where word="%s"' % word
                status = cur.execute(sql)
            conn.commit()
        except:
            conn.rollback()

        return status


class ReciteWord:
    """背单词"""
    @staticmethod
    def from_mysql(conn, n=0):
        """
            接收2个参数：
                conn：数据库连接对象
                n：每次请求的数据个数 (32 * n)
        """
        data = ()
        try:
            with conn.cursor() as cur:
                # 查询单词是否存在单词本中
                sql = 'select word,means from wordbook where is_delete=0 and id>%s limit 32' % (n*32)
                cur.execute(sql)
                data = cur.fetchall()
            conn.commit()
        except:
            conn.rollback()

        return data


class AnswerCheck:
    """验证答案"""
    @staticmethod
    def check(conn, word, answer):
        """
            接收3个参数：
                conn：数据库连接对象
                word：单词
                answer：答案
        """
        status = 0
        try:
            with conn.cursor() as cur:
                # 查询单词
                sql = 'select id from wordbook where word="%s" and means="%s"' % (word, answer)
                status = cur.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        return status


class AnswerGet:
    """获取答案"""
    @staticmethod
    def get(conn, word):
        """
            接收2个参数：
                conn：数据库连接对象
                word：单词
        """
        answer = ''
        try:
            with conn.cursor() as cur:
                # 查询单词
                sql = 'select means from wordbook where word="%s" and is_delete=0' % word
                cur.execute(sql)
                answer = cur.fetchone()[0]
            conn.commit()
        except:
            conn.rollback()
        return answer


class WordKill:
    """删除单词"""

    @staticmethod
    def kill(conn, word):
        """
            接收2个参数：
                conn：数据库连接对象
                word：单词
        """
        status = 0
        try:
            with conn.cursor() as cur:
                # 查询单词
                sql = 'update wordbook set is_delete=1 where word="%s"' % word
                status = cur.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        return status