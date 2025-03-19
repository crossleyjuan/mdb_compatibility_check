import json

def check_find_parameters(command):
    if "filter" in command:
        filter = command["filter"]
        flat = json.dumps(filter)
        if "null" in flat or "undefined" in flat:
            raise Exception(f"Warn: Starting in MongoDB 8.0, comparisons to null in equality match expressions don't match undefined values. Review the documentation https://www.mongodb.com/docs/manual/release-notes/8.0-compatibility/#queries-for-null-don-t-match-undefined-fields to check if you are affected by this change. The following query might be affected by this {flat}")

def check_command(command, jentry):
    if "find" in command:
        check_find_parameters(command)


def check(entries):
    errors = set()
    for entry in entries:
        jentry = json.loads(entry)
        if jentry["c"] == "COMMAND" and "command" in jentry["attr"]:
            command = jentry["attr"]["command"]
            try:
                check_command(command, jentry)
            except Exception as e:
                errors.add(str(e))

    return { "errors": errors }    