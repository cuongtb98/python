import pymongo
from config.setting import CONNECT

def connect():
    try:
        client = pymongo.MongoClient(f"mongodb+srv://{CONNECT['user']}:{CONNECT['password']}@shop.rpgea.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        print("Connect success")
    except NameError:
        print("Connect error: ", NameError)
        exit()
    db_cources = client['cources']
    cl_software_engineer = db_cources['software_engineer']
    return cl_software_engineer

