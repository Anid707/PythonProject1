import pytest
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class TestDbMongo:
    def connect_db(self):
        uri = "mongodb+srv://anid92:HappyPaw2023@happy-paws.frqylal.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.test
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        return db

    def test_new_user(self):
        db = self.connect_db()
        # insert_user = db.users.insert_one({"email": "Daysie1", "password": "pass111"})
        # print(insert_user)
        find_user = list(db.users.find({"email": "Daysie1"}))
        print(find_user[0])
        count_user = db.users.count_documents({"email": "Daysie1"})
        print(count_user)
        assert find_user[0]["email"] == "Daysie1"
        assert find_user[0]["password"] == "pass111"


    #print(list(db.users.find({"email": "Daysie"})))

# bulk_write(), as long as UpdateMany or DeleteMany are not included.
# delete_one()
# insert_one()
# insert_many()
# replace_one()
# update_one()
# find_one_and_delete()
# find_one_and_replace()
# find_one_and_update()
# find()
# find_one()
# aggregate() without $out
# distinct()
# count()
# estimated_document_count()
# count_documents()
# pymongo.collection.Collection.watch()
# list_indexes()
# pymongo.database.Database.watch()
# list_collections()
# pymongo.mongo_client.MongoClient.watch()
# list_databases()

# from pymongo import InsertOne, DeleteOne, ReplaceOne
# requests = [InsertOne({'y': 1}), DeleteOne({'x': 1}),
#             ReplaceOne({'w': 1}, {'z': 1}, upsert=True)]
# result = db.test.bulk_write(requests)
# result.inserted_count
# 1
# result.deleted_count
# 1
# result.modified_count
# 0
# result.upserted_ids

# def test_count_documents_in_collection():
#     db["users"].insert_one({"email": "Daysie", "password": "pass123"})

# import pyodbc
#
# server = '127.0.0.1'
# database = 'test'
# username = 'anid92'
# password = 'HappyPaw2023'
# driver = '{Devart ODBC Driver for MongoDB}'
# cnxn = pyodbc.connect(f"DRIVER={driver};SERVER={server};PORT=27017;DATABASE={database}")
# cursor = cnxn.cursor()
# cursor.execute("SELECT * from users")
# row = cursor.fetchone()
# while row:
#     print(str(row[0] + " " + str(row[1])))
#     row = cursor.fetchone()



    