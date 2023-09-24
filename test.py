from serverClass import Server
from myServerClass import MyServer

# Server class test code

database = Server(host = 'localhost', user = 'root', password = 'MCCTCRocks', database = 'ESPORTS')

database.createTable('PLAYERS', 
['PLAYER_ID','FIRST_NAME','LAST_NAME','PHONE_NUMBER','DISCORD_ID','ESPORT_GAME'],
['integer','text','text','text','text','text'],
['PRIMARY KEY AUTO_INCREMENT','NOT NULL','NOT NULL','','','']
)

database.createRow('PLAYERS', ['FIRST_NAME','LAST_NAME','PHONE_NUMBER','DISCORD_ID','ESPORT_GAME'], ['Karter','Crites','N/A','@TheGreatTurboski','Fortnite'])

# database.deleteRow('PLAYERS', 'PLAYER_ID', '2')
# database.deleteRow('PLAYERS', 'PLAYER_ID', '4')

database.alterRow("PLAYERS", 'PLAYER_ID', "1", 'ESPORT_GAME', 'Rocket League')

print(database.getTable("PLAYERS"))

database.executeQuery('SHOW TABLES;')

print(database.cursor.fetchall())

# MyServer class Test code
myDatabase = MyServer(host = 'localhost', user = 'root', password = 'MCCTCRocks', database = 'ESPORTS')

myDatabase.createTable('PLAYERS', 
['PLAYER_ID','FIRST_NAME','LAST_NAME','PHONE_NUMBER','DISCORD_ID','ESPORT_GAME'],
['integer','text','text','text','text','text'],
['PRIMARY KEY AUTO_INCREMENT','NOT NULL','NOT NULL','','','']
)

myDatabase.createRow('PLAYERS', ['FIRST_NAME','LAST_NAME','PHONE_NUMBER','DISCORD_ID','ESPORT_GAME'], ['Karter','Crites','N/A','@TheGreatTurboski','Fortnite'])

# myDatabase.deleteRow('PLAYERS', 'PLAYER_ID', '2')
# myDatabase.deleteRow('PLAYERS', 'PLAYER_ID', '4')

myDatabase.alterRow("PLAYERS", 'PLAYER_ID', "1", 'ESPORT_GAME', 'Rocket League')

print(myDatabase.getTable("PLAYERS"))

myDatabase.executeQuery('SHOW TABLES;')

print(myDatabase.cursor.fetchall())