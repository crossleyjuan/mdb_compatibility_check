# MongoDB Compatibility Checker

This repository contains scripts to check MongoDB compatibility for various versions (5.0, 6.0, and 8.0). The scripts analyze log entries to identify potential compatibility issues when upgrading MongoDB from 4.4 to version 8.0.

**Note: It's not checking commands that were introduced after version 4.4**

## Overview

The compatibility checker processes log entries and validates commands against the rules and changes introduced in MongoDB versions 5.0, 6.0, and 8.0. It identifies invalid parameters, removed commands, and other breaking changes.

## Checks Performed

### MongoDB 5.0 Compatibility (`check_50.py`)

- **Strict Parameter Validation**: Starting in MongoDB 5.0, commands raise errors for unrecognized parameters. The script validates the following commands:
  - `create`
  - `createIndexes`
  - `delete`
  - `drop`
  - `dropDatabase`
  - `dropIndexes`
  - `endSessions`
  - `explain`
  - `find`
  - `findAndModify`
  - `getMore`
  - `hello`
  - `insert`
  - `killCursors`
  - `listCollections`
  - `listDatabases`
  - `listIndexes`
  - `refreshSessions`
  - `update`

- **Removed Commands**: The following commands are flagged as removed:
  - `reseterror`
  - `geoSearch`
  - `shardConnPoolStats`
  - `unsetSharding`

- **Internal Parameters**: Internal parameters (e.g., `shardVersion`, `lsid`, `$`-prefixed keys) are removed before validation.

### MongoDB 6.0 Compatibility (`check_60.py`)

- **Unsupported Query Operators**: The following query operators are flagged as unsupported in version 5.1+ when using `find`:
  - `$explain`
  - `$comment`
  - `$hint`
  - `$max`
  - `$maxTimeMS`
  - `$min`
  - `$orderby`
  - `$query`
  - `$returnKey`
  - `$showDiskLoc`

- **Removed Commands**:
  - `reIndex` is flagged as removed in version 6.0+.

- **Behavioral Changes**:
  - `$mod` operator behavior has changed in version 6.0+.

- **Removed OpCodes**: The following opcodes are flagged as unsupported in version 5.1+:
  - `OP_INSERT`
  - `OP_DELETE`
  - `OP_UPDATE`
  - `OP_KILL_CURSORS`
  - `OP_GET_MORE`
  - `OP_QUERY`

### MongoDB 8.0 Compatibility (`check_80.py`)

- **Query Behavior Changes**:
  - Comparisons to `null` in equality match expressions no longer match `undefined` values. Queries containing `null` or `undefined` in filters are flagged.

## Usage

1. Place the logs to be analyzed in a directory.
2. Run the script using the following command:
   ```bash
   python main.py --log-path <path_to_logs>