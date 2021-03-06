import os
from peewee import *

arq = "animal.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Animal(BaseModel):
	nome_dono = CharField()
	tipo_animal = CharField()
	raca = CharField()
	nome_animal = CharField()

		def __str__(self):
			return self.tipo_animal, self.raca, self.nome_dono, self.nome_animal

class Consulta(BaseModel):
	data = CharField()
	servidor = CharField()
	horario = CharField()
	animal = ForeignKeyField(Animal)
	confirma = CharField()
	myID = CharField()

	def __str__(self):
		return self.servico, self.data, self.horario, self.confirma, self.myID, str(self.animal)

if __name__ == "__main__":
	arq = "animal.db"
	if os.path.exists(arq):
		os.remove(arq)

	try:
		db.connect()
		db.create_tables([Animal, Consulta])

	except OperationError as erro:
		print("erro ao criar as tabelas: "+str(erro))

	print("teste do animal")
	a1 = Animal(nome_dono="Gustavo", tipo_animal="cachorro", raca="linguicinha", nome_animal="Sarchixa")
	a1.save()
	print(a1)
	print("teste da consulta")
	c1 = Consulta(data="2019-06-05", servico="Consulta", horario="14:00", animal=a1, confirma="sim", myID="3425576687sdf436")
	

	todos = Animal.select()
	for i in todos:
		print(i)