from autos import process_file

def insert_autos(infile, col):
    autos = process_file(infile)
    col.insert_many(autos)
    # Your code here. Insert the data in one command
    # autos will be a list of dictionaries, as in the example in the previous video
    # You have to insert data in a collection 'autos'



if __name__ == "__main__":

    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples
    col = db.autos

    insert_autos('autos-small.csv', col)
