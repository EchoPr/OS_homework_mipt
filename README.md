## Homework 1
### Task1
Using ```python3 main.py <comands_list_file>```

```comands_list_file``` example:
```
3 echo "Printed after 3 seconds after starting prgramm"
1 echo "Printed after 1 second after starting prgramm"
2 echo "Printed after 2 seconds after starting prgramm"
```

Expected behaviour:
```
Printed after 1 second after starting prgramm
Printed after 2 seconds after starting prgramm
Printed after 3 seconds after starting prgramm
```
---

### Task2
Using ```python3 main.py <source_directory> <target_backup_directoy>```

Expected behaviour:
When processing the next file, if it has been changed, then the following message is displayed
```
SAVING: <processing_file_name> TO: <processing_file_name.gz>
```
Otherwise it will be missed