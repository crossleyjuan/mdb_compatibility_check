import json

def check_find_parameters(entry):
    flat = json.dumps(entry)

    unsupported_query_operators = [
        "$explain", 
        "$comment",
        "$hint",
        "$max",
        "$maxTimeMS",
        "$min",
        "$orderby",
        "$query",
        "$returnKey",
        "$showDiskLoc"
    ]

    for operator in unsupported_query_operators:
        if operator in flat:
            raise Exception(f"{operator} is not supported in version 5.1+ when using find")
    
def check_command(command, entry):
    if "find" in command:
        check_find_parameters(entry)

    if "reIndex" in command:
        raise Exception("reIndex is not supported in version 6.0+")
    
    if "$mod" in json.dumps(entry):
        raise Exception("$mod has changed in version 6.0+, review the documentation https://www.mongodb.com/docs/manual/release-notes/6.0-compatibility/#-mod-error-behavior")

def check_op_codes_removed(entry):
    unsupported_op_codes = [
        "OP_INSERT",
        "OP_DELETE",
        "OP_UPDATE",
        "OP_KILL_CURSORS",
        "OP_GET_MORE",
        "OP_QUERY"
    ]
    for op_code in unsupported_op_codes:
        if op_code in entry:
            raise Exception(f"{op_code} is not supported in version 5.1+")

def check(entries):
    errors = []
    for entry in entries:
        jentry = json.loads(entry)
        try:
            if jentry["c"] == "COMMAND" and "command" in jentry["attr"]:
                command = jentry["attr"]["command"]
                check_command(command, jentry)
            check_op_codes_removed(entry)
        except Exception as e:
            errors.append(str(e))

    return { "errors": errors }