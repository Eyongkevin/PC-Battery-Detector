import sqlite3

class Database(object):
	dbFile = 'setConfig'	
	
	def login(self):
		conn = sqlite3.connect(self.dbFile)
		curs = conn.cursor()
		return conn, curs
		
	def closeDatabase(self,conn):
		conn.close()
		
	def makedicts(self,cursor,query, params =()):
		cursor.execute(query, params)
		colnames = [desc[0] for desc in cursor.description]
		rowdicts = [dict(zip(colnames, row)) for row in cursor.fetchall()]  #---(2)
		return rowdicts

		
	def createDefaultTable(self):
		conn,curs = self.login()
		curs.execute("CREATE TABLE IF NOT EXISTS configDataDefault(alarmDisable int(1), alarmWhenDropTo int, disableSound int(1), notifyWhenFullyCharged int(1))")
		curs.execute('DELETE FROM configDataDefault')
		curs.execute("INSERT INTO configDataDefault VALUES(?,?,?,?)",(0,20,0,0))
		conn.commit()
		conn.close()
		
	def deleteConfigDataSetTable(self):
		conn,curs = self.login()
		curs.execute('DELETE FROM configDataSet')
		conn.commit()
		conn.close()
		
	def getData(self):
		conn,curs = self.login()
		curs.execute("CREATE TABLE IF NOT EXISTS configDataSet(alarmDisable int(1), alarmWhenDropTo int, disableSound int(1), notifyWhenFullyCharged int(1))")
		query = 'SELECT * FROM configDataSet'
		result = self.makedicts(curs,query)
		if not result:
			query = 'SELECT * FROM configDataDefault'
			result = self.makedicts(curs,query)
			conn.close()
			return result
		conn.close()
		return result

	def setDataToSetTable(self,alarmBatteryLevel,notifyWhenFullyCharged,alarmDisable,disableSound):
		conn,curs = self.login()
		curs.execute("CREATE TABLE IF NOT EXISTS configDataSet(alarmDisable int(1), alarmWhenDropTo int, disableSound int(1), notifyWhenFullyCharged int(1))")
		curs.execute('DELETE FROM configDataSet')
		curs.execute("INSERT INTO configDataSet VALUES(?,?,?,?)",(alarmDisable,alarmBatteryLevel,disableSound,notifyWhenFullyCharged))
		conn.commit()
		conn.close()
