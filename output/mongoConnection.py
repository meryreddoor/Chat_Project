import pymongo

#Conexión con la colección usuarios
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
user_mydb = myclient["emotions"]
user_mycol = user_mydb["users"]

#Conexión con la colección grupos
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
group_mydb = myclient["emotions"]
group_mycol = group_mydb["groups"]

#Conexion con la coleccion simpsons
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
simp_mydb = myclient["emotions"]
simp_mycol = group_mydb["simpsons"]