import json
# Starting in MongoDB 5.0, certain database commands raise an error if passed a parameter not explicitly accepted by the command. In MongoDB 4.4 and earlier, unrecognized parameters are silently ignored.
create_valid_parameters = '''
{
   create: <collection or view name>,
   capped: <true|false>,
   timeseries: {
      timeField: <string>,
      metaField: <string>,
      granularity: <string>
   },
   expireAfterSeconds: <number>,
   autoIndexId: <true|false>,
   size: <max_size>,
   max: <max_documents>,
   storageEngine: <document>,
   validator: <document>,
   validationLevel: <string>,
   validationAction: <string>,
   indexOptionDefaults: <document>,
   viewOn: <source>,
   pipeline: <pipeline>,
   collation: <document>,
   writeConcern: <document>,
   comment: <any>
}'''

createIndexes_valid_parameters = '''
db.runCommand(
  {
    createIndexes: <collection>,
    indexes: [
        {
            key: {
                <key-value_pair>,
                <key-value_pair>,
                ...
            },
            name: <index_name>,
            <option1>,
            <option2>,
            ...
        },
        { ... },
        { ... }
    ],
    writeConcern: { <write concern> },
    commitQuorum: <int|string>,
    comment: <any>
  }
)'''

delete_valid_parameters = '''
 db.runCommand(
    {
      delete: <collection>,
      deletes: [
         {
           q : <query>,
           limit : <integer>,
           collation: <document>,
           hint: <document|string>
         },
         ...
      ],
      comment: <any>,
      let: <document>, // Added in MongoDB 5.0
      ordered: <boolean>,
      writeConcern: { <write concern> },
      maxTimeMS: <integer>
   }
)'''

drop_valid_parameters = '''' \
db.runCommand(
   {
     drop: <collection_name>,
     writeConcern: <document>,
     comment: <any>
   }
)'''

dropdatabase_valid_parameters = '''' \
db.runCommand(
   {
     dropDatabase: 1,
     writeConcern: <document>,
     comment: <any>
   }
)
'''

dropIndexes_valid_parameters = '''' \
db.runCommand(
   {
     dropIndexes: <string>,
     index: <string|document|arrayofstrings>,
     writeConcern: <document>, comment: <any>
   }
)'''

endSessions_valid_parameters = '''
db.runCommand(
   {
     endSessions: [ { id : <UUID> }, ... ]
   }
)'''

explain_valid_parameters = '''' \
db.runCommand(
   {
     explain: <command>,
     verbosity: <string>,
     comment: <any>
   }
)'''

find_valid_parameters = '''
db.runCommand(
   {
      find: <string>,
      filter: <document>,
      sort: <document>,
      projection: <document>,
      hint: <document or string>,
      skip: <int>,
      limit: <int>,
      batchSize: <int>,
      singleBatch: <bool>,
      comment: <any>,
      maxTimeMS: <int>,
      readConcern: <document>,
      max: <document>,
      min: <document>,
      returnKey: <bool>,
      showRecordId: <bool>,
      tailable: <bool>,
      oplogReplay: <bool>,
      noCursorTimeout: <bool>,
      awaitData: <bool>,
      allowPartialResults: <bool>,
      collation: <document>,
      allowDiskUse : <bool>,
      let: <document> // Added in MongoDB 5.0
   }
)'''

findAndModify_valid_parameters = '''' \
db.runCommand(
   {
     findAndModify: <collection-name>,
     query: <document>,
     sort: <document>,
     remove: <boolean>,
     update: <document or aggregation pipeline>,
     new: <boolean>,
     fields: <document>,
     upsert: <boolean>,
     bypassDocumentValidation: <boolean>,
     writeConcern: <document>,
     maxTimeMS: <integer>,
     collation: <document>,
     arrayFilters: <array>,
     hint: <document|string>,
     comment: <any>,
     let: <document> // Added in MongoDB 5.0
   }
)'''

getMore_valid_parameters = '''' \
db.runCommand(
   {
      getMore: <long>,
      collection: <string>,
      batchSize: <int>,
      maxTimeMS: <int>,
      comment: <any>
   }
)'''

hello_valid_parameters = '''
db.runCommand(
   {
     hello: 1
   }
)'''

insert_valid_paramters = '''
db.runCommand(
   {
      insert: <collection>,
      documents: [ <document>, <document>, <document>, ... ],
      ordered: <boolean>,
      maxTimeMS: <integer>,
      writeConcern: { <write concern> },
      bypassDocumentValidation: <boolean>,
      comment: <any>
   }
)'''

killCursors_valid_parameters = '''' \
db.runCommand(
   {
     killCursors: <collection>,
     cursors: [ <cursor id1>, ... ], comment: <any>
   }
)
''' 
def check_killCursors_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("killCursors", None)
    command.pop("cursors", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for killCursors command: {command}")

listCollections_valid_parameters = '''
db.runCommand(
   {
     listCollections: 1,
     filter: <document>,
     nameOnly: <boolean>,
     authorizedCollections: <boolean>,
     comment: <any>
   }
)'''
def check_listCollections_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("listCollections", None)
    command.pop("filter", None)
    command.pop("nameOnly", None)
    command.pop("authorizedCollections", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for listCollections command: {command}")

listDatabases_valid_parameters = '''
db.adminCommand(
   {
     listDatabases: 1,
     filter: <document>,
     nameOnly: <boolean>,
     authorizedDatabases: <boolean>,
     comment: <any>
   }
)'''
def check_listDatabases_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("listDatabases", None)
    command.pop("filter", None)
    command.pop("nameOnly", None)
    command.pop("authorizedDatabases", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for listDatabases command: {command}")

listIndexes_valid_paramters = '''db.runCommand (
   {
      listIndexes: "<collection-name>",
      cursor: { batchSize: <int> },
      comment: <any>
   }
)
'''
def check_listIndexes_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("listIndexes", None)
    command.pop("cursor", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for listIndexes command: {command}")

refreshSessions_parameters = '''db.runCommand(
   {
     refreshSessions: [
       { id : <UUID> }, ...
     ]
   }
 )'''
def check_refreshsessions_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("refreshSessions", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for refreshSessions command: {command}")

update_valid_parameters = '''db.runCommand(
   {
      update: <collection>,
      updates: [
         {
           q: <query>,
           u: <document or pipeline>,
           c: <document>, // Added in MongoDB 5.0
           upsert: <boolean>,
           multi: <boolean>,
           collation: <document>,
           arrayFilters: <array>,
           hint: <document|string>,
           sort: <document>
         },
         ...
      ],
      ordered: <boolean>,
      maxTimeMS: <integer>,
      writeConcern: { <write concern> },
      bypassDocumentValidation: <boolean>,
      comment: <any>,
      let: <document> // Added in MongoDB 5.0
   }
)'''
def check_update_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("update", None)
    command.pop("updates", None)
    command.pop("ordered", None)
    command.pop("maxTimeMS", None)
    command.pop("writeConcern", None)
    command.pop("bypassDocumentValidation", None)
    command.pop("comment", None)
    command.pop("let", None)
    command.pop("stmtIds", None)

    for update in command.get("updates", []):
        update.pop("q", None)
        update.pop("u", None)
        update.pop("c", None)
        update.pop("upsert", None)
        update.pop("multi", None)
        update.pop("collation", None)
        update.pop("arrayFilters", None)
        update.pop("hint", None)
        update.pop("sort", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for update command: {command}")

commands_check_parameters = [
    "abortTransaction",
    "aggregate",
    "authenticate",
    "collMod",
    "commitTransaction",
    "create", 
    "createIndexes",
    "delete",
    "drop",
    "dropDatabase",
    "dropIndexes",
    "endSessions",
    "explain",
    "find",
    "findAndModify",
    "getMore",
    "hello",
    "insert",
    "killCursors",
    "listCollections",
    "listDatabases",
    "listIndexes",
    "ping",
    "refreshSessions",
    "update",
]

removed_commands = [
    "reseterror"
    "geoSearch",
    "shardConnPoolStats",
    "unsetSharding"
]

def check_ping_parameters(entry):
    command = entry["attr"]["command"]
    del command["ping"]
    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for ping command: {command}")

def check_abortTransaction_parameters(entry):
    command = entry["attr"]["command"]
    del command["abortTransaction"]

    remove_internal_parameters(command)

    if command:
        raise Exception(f"Invalid parameters for abortTransaction command: {command}")

def remove_internal_parameters(command):
    to_remove = []
    for k in command.keys():
        if k.startswith("$"):
            to_remove.append(k)
    for k in to_remove:
        del command[k]

    command.pop("shardVersion", None)
    command.pop("lsid", None)
    command.pop("txnNumber", None)
    command.pop("fromMongos", None)
    command.pop("runtimeConstants", None)
    command.pop("needsMerge", None)
    command.pop("clientOperationKey", None)


def check_aggregate_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("aggregate", None)
    command.pop("pipeline", None)
    command.pop("cursor", None)
    command.pop("explain", None)
    command.pop("allowDiskUse", None)
    command.pop("bypassDocumentValidation", None)
    command.pop("collation", None)
    command.pop("comment", None)
    command.pop("hint", None)
    command.pop("maxTimeMS", None)
    command.pop("maxAwaitTimeMS", None)
    command.pop("readConcern", None)
    command.pop("readPreference", None)
    command.pop("writeConcern", None)
    command.pop("session", None)
    command.pop("let", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for aggregate command: {command}")

# TODO: confirm this command    
def check_authenticate_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("authenticate", None)
    command.pop("user", None)
    command.pop("mechanism", None)
    command.pop("db", None)
    command.pop("pwd", None)
    command.pop("digestPassword", None)
    command.pop("mechanismProperties", None)
    command.pop("client", None)
    command.pop("clientFirst", None)
    command.pop("speculativeAuthenticate", None)
    command.pop("authSource", None)
    command.pop("authMechanism", None)
    command.pop("authMechanismData", None)
    command.pop("authMechanismProperties", None)
    command.pop("saslSupportedMechs", None)
    command.pop("saslContinue", None)
    command.pop("saslStart", None)
    command.pop("saslStart", None)
    command.pop("saslContinue", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for authenticate command: {command}")

def check_collMod_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("collMod", None)
    command.pop("index", None)
    command.pop("validator", None)
    command.pop("validationLevel", None)
    command.pop("validationAction", None)
    command.pop("viewOn", None)
    command.pop("pipeline", None)
    command.pop("expireAfterSeconds", None)
    command.pop("comment", None)
    command.pop("w", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for collMod command: {command}")

def check_commitTransaction_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("commitTransaction", None)
    command.pop("writeConcern", None)
    command.pop("txnNumber", None)
    command.pop("autocommit", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for commitTransaction command: {command}")

def check_create_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("create", None)
    command.pop("capped", None)
    command.pop("timeseries", None)
    command.pop("expireAfterSeconds", None)
    command.pop("autoIndexId", None)
    command.pop("size", None)
    command.pop("max", None)
    command.pop("storageEngine", None)
    command.pop("validator", None)
    command.pop("validationLevel", None)
    command.pop("validationAction", None)
    command.pop("indexOptionDefaults", None)
    command.pop("viewOn", None)
    command.pop("pipeline", None)
    command.pop("collation", None)
    command.pop("writeConcern", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for create command: {command}")

def check_createIndexes_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("createIndexes", None)
    command.pop("indexes", None)
    command.pop("writeConcern", None)
    command.pop("commitQuorum", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for createIndexes command: {command}")
    
def check_delete_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("delete", None)
    command.pop("deletes", None)
    command.pop("comment", None)
    command.pop("let", None)
    command.pop("ordered", None)
    command.pop("writeConcern", None)
    command.pop("maxTimeMS", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for delete command: {command}")

def check_drop_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("drop", None)
    command.pop("writeConcern", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for drop command: {command}")

def check_dropDatabase_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("dropDatabase", None)
    command.pop("writeConcern", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for dropDatabase command: {command}")

def check_dropIndexes_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("dropIndexes", None)
    command.pop("index", None)
    command.pop("writeConcern", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for dropIndexes command: {command}")

def check_endSessions_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("endSessions", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for endSessions command: {command}")

def check_explain_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("explain", None)
    command.pop("verbosity", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for explain command: {command}")

def check_find_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("find", None)
    command.pop("filter", None)
    command.pop("sort", None)
    command.pop("projection", None)
    command.pop("hint", None)
    command.pop("skip", None)
    command.pop("limit", None)
    command.pop("batchSize", None)
    command.pop("singleBatch", None)
    command.pop("comment", None)
    command.pop("maxTimeMS", None)
    command.pop("readConcern", None)
    command.pop("max", None)
    command.pop("min", None)
    command.pop("returnKey", None)
    command.pop("showRecordId", None)
    command.pop("tailable", None)
    command.pop("oplogReplay", None)
    command.pop("noCursorTimeout", None)
    command.pop("awaitData", None)
    command.pop("allowPartialResults", None)
    command.pop("collation", None)
    command.pop("allowDiskUse", None)
    command.pop("let", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for find command: {command}")
    
def check_findAndModify_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("findAndModify", None)
    command.pop("query", None)
    command.pop("sort", None)
    command.pop("remove", None)
    command.pop("update", None)
    command.pop("new", None)
    command.pop("fields", None)
    command.pop("upsert", None)
    command.pop("bypassDocumentValidation", None)
    command.pop("writeConcern", None)
    command.pop("maxTimeMS", None)
    command.pop("collation", None)
    command.pop("arrayFilters", None)
    command.pop("hint", None)
    command.pop("comment", None)
    command.pop("let", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for findAndModify command: {command}")

def check_getMore_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("getMore", None)
    command.pop("collection", None)
    command.pop("batchSize", None)
    command.pop("maxTimeMS", None)
    command.pop("comment", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for getMore command: {command}")

def check_hello_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("hello", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for hello command: {command}")

def check_insert_parameters(entry):
    command = entry["attr"]["command"]
    command.pop("insert", None)
    command.pop("documents", None)
    command.pop("ordered", None)
    command.pop("maxTimeMS", None)
    command.pop("writeConcern", None)
    command.pop("bypassDocumentValidation", None)
    command.pop("comment", None)
    command.pop("stmtIds", None)

    remove_internal_parameters(command)
    if command:
        raise Exception(f"Invalid parameters for insert command: {command}")
    
def check_command_parameters(command, jentry):
    if "ping" in command:
        check_ping_parameters(jentry)
    if "abortTransaction" in command:
        check_abortTransaction_parameters(jentry)
    if "aggregate" in command:
        check_aggregate_parameters(jentry)
    if "authenticate" in command:
        check_authenticate_parameters(jentry)
    if "collMod" in command:
        check_collMod_parameters(jentry)
    if "commitTransaction" in command:
        check_commitTransaction_parameters(jentry)
    if "create" in command:
        check_create_parameters(jentry)
    if "createIndexes" in command:
        check_createIndexes_parameters(jentry)
    if "delete" in command:
        check_delete_parameters(jentry)
    if "drop" in command:
        check_drop_parameters(jentry)
    if "dropDatabase" in command:
        check_dropDatabase_parameters(jentry)
    if "dropIndexes" in command:
        check_dropIndexes_parameters(jentry)
    if "endSessions" in command:
        check_endSessions_parameters(jentry)
    if "explain" in command:
        check_explain_parameters(jentry)
    if "find" in command:
        check_find_parameters(jentry)
    if "findAndModify" in command:
        check_findAndModify_parameters(jentry)
    if "getMore" in command:
        check_getMore_parameters(jentry)
    if "hello" in command:
        check_hello_parameters(jentry)
    if "insert" in command:
        check_insert_parameters(jentry)
    if "killCursors" in command:
        check_killCursors_parameters(jentry)
    if "listCollections" in command:
        check_listCollections_parameters(jentry)
    if "listDatabases" in command:
        check_listDatabases_parameters(jentry)
    if "listIndexes" in command:
        check_listIndexes_parameters(jentry)
    if "refreshSessions" in command:
        check_refreshsessions_parameters(jentry)
    if "update" in command:
        check_update_parameters(jentry)

def check(entries):
    errors = set()
    for entry in entries:
        for check_command in commands_check_parameters:
            jentry = json.loads(entry)
            if jentry["c"] == "COMMAND" and "command" in jentry["attr"]:
                command = jentry["attr"]["command"]
                try:
                    check_command_parameters(command, jentry)
                except Exception as e:
                    errors.add(str(e))

                if any(cmd in command for cmd in removed_commands):
                    errors.add(f"Command {list(command.keys())[0]} is in the list of removed commands.")

    return { "errors": errors }