from ATM_DB import DBHelper
import pandas as pd

class History(DBHelper):

    def Details(self):
        query="create table  if not exists Details like customer"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    '''def ALTER(self):

        query="""ALTER TABLE Details MODIFY COLUMN userid int(11) NOT NULL, 
                    DROP PRIMARY KEY, ENGINE = MyISAM, ADD action VARCHAR(8) DEFAULT 'insert' FIRST, 
                    ADD revision INT(6) NOT NULL AUTO_INCREMENT AFTER action,
                    ADD dt_datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP AFTER revision,
                    ADD PRIMARY KEY (userid, revision)"""
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()'''

    def DropTrigInsertion(self):
        query="DROP TRIGGER IF EXISTS Insertion"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def DropTrigUpdation(self):
        query="DROP TRIGGER IF EXISTS Updation"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def TrigInsert(self):
        #self.DropTrigUpdation(cur)
        query="""CREATE TRIGGER Insertion AFTER INSERT ON customer FOR EACH ROW
                    INSERT INTO Details SELECT 'insert', NULL, NOW(), d.* 
                    FROM customer AS d WHERE d.userid = NEW.userid"""
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def TrigUpdate(self):
        #self.DropTrigUpdation(cur)
        query="""CREATE TRIGGER Updation AFTER UPDATE ON customer FOR EACH ROW
                    INSERT INTO Details SELECT 'update', NULL, NOW(), d.*
                    FROM customer AS d WHERE d.userid = NEW.userid;
                    """
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    '''def CreateView(self):
        query="""CREATE VIEW data_history_changes AS 
                    SELECT t2.dt_datetime, t2.action, t1.userid as 'row id'
                    FROM Details as t1 INNER join Details as t2 on t1.userid = t2.userid 
                    WHERE (t1.revision = 1 AND t2.revision = 1) OR t2.revision = t1.revision+1
                    ORDER BY t1.userid ASC, t2.revision ASC"""
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()'''


    ''' def ViewHistory(self):
        db_cursor = self.con.cursor()
        db_cursor.execute('SELECT * FROM Details')

        table_rows = db_cursor.fetchall()

        df = pd.DataFrame(table_rows)'''
    