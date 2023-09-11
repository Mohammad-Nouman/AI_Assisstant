import mysql.connector

class Connector:
    __myDb = None
    __myCursor = None
    databaseName = "PersonalAssistant"
    @classmethod
    def connect(cls):
        cls.__myDb = mysql.connector.connect(host="localhost",
                           user="root",
                           passwd="admin",
                           database=Connector.databaseName)

        cls.__myCursor = cls.__myDb.cursor()

    @classmethod
    def insertCommand(cls,index,fword,lword):
        command = f"select idCommand from {Connector.databaseName}.command order by idCommand desc limit 1;"
        cls.__myCursor.execute(command)
        if cls.__myCursor.fetchone() == None:
            id = 0
        else: id = cls.__myCursor.fetchone()
        count = int(id[0])
        count = count+1
        command = f"INSERT INTO `{Connector.databaseName}`.`command`" \
                  f" (`idCommand`,`fword`,`lword`,`detail`)" \
                  f" VALUES({count},'{fword}','{lword}','{index}');"
        cls.__myCursor.execute(command)
        cls.__myDb.commit()


    @classmethod
    def searchFword(cls,word):
        command = f"select detail from {Connector.databaseName}.command where fword = '{word}'"
        index = cls.searchCommand(command)
        return index

    def searchLword(cls,word):
        command = f"select detail from {Connector.databaseName}.command where lword = '{word}'"
        index = cls.searchCommand(command)
        return index

    @classmethod
    def searchCommand(cls,command):
        cls.__myCursor.execute(command)
        result = cls.__myCursor.fetchall()
        # print(result)
        # index = None
        # if len(result) != 0:
        #     tuplpl1 = result[0]
        #     index = tuplpl1[0]
        cls.__myDb.commit()
        return result
        # result = cls.myCursor.fetchone()

    @classmethod
    def showTable(cls,name):
        command = f"select * from {name}"
        cls.__myCursor.execute(command)
        result = cls.__myCursor.fetchall()
        cls.__myDb.commit()
        return result