# MIT license https://opensource.org/licenses/MIT
# Copyright 2024 Infosys Ltd

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import shutil
import pymongo
import datetime,time
from docProcess.dao.DatabaseConnection import DB
from dotenv import load_dotenv
from docProcess.config.logger import CustomLogger
from gridfs import GridFS
from bson import objectid

load_dotenv()
log = CustomLogger()

class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


mydb=DB.connect()


class docDb:
    mycol = mydb["ResponseRegistery"]
    fs=GridFS(mydb)
    def findOne(id):
        values=docDb.mycol.find({"_id":id},{})[0]
        # print(values)
        values=AttributeDict(values)
        return values
    def findall(query):
        value_list=[]
        values=docDb.mycol.find(query,{})
        for v in values:

            v=AttributeDict(v)
            value_list.append(v)
        return value_list
    
    def create(value):
         value=AttributeDict(value)
         localTime = time.time()
         mydoc = {
        "_id":localTime,
        "docId":localTime,
        "userId":value.userId,
        "fileName":value.fileName,
        # "inputFileId":value.fileid,
        "categories":value.categories,
        "status":"Not Started",
        "type":value.type,
        "CreatedDateTime": datetime.datetime.now(),
        "LastUpdatedDateTime": datetime.datetime.now(),
         }
         docProccessData = docDb.mycol.insert_one(mydoc)
         return docProccessData.inserted_id
    
    def update(id,value:dict):
      
        newvalues = { "$set": value }
        docProccessData=docDb.mycol.update_one({"_id":id},newvalues)
        log.debug(str(newvalues)) 
        return docProccessData.acknowledged
    
    def delete(id):
        docDb.mycol.delete_many({"_id":id})
        # DocProcDtl.mycol.delete_many({})
        # Docpagedtl.mycol.delete_many({})
    
    
