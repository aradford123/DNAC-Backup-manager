# Backup tool

This tool will show or delete older automation backups on Cisco DNA Center.

****warning:  This uses internal Cisco DNAC Center API, so is not officially supported.  This is example code to show what is possible.***

Each automation backup on Cisco DNA Center is a complete copy.  If you backup everyday, it is easy to fill up the back up partition.  It is common to delete older backups. This tool can show the current backups, delete a specific backup by id, or delete all backups older than a certain time (the default is one week).


## Getting stated
First (optional) step, create a vitualenv. This makes it less likely to clash with other python libraries in future.
Once the virtualenv is created, need to activate it.
```buildoutcfg
python3 -m venv env3
source env3/bin/activate
```

Next clone the code.

```buildoutcfg
git clone https://github.com/aradford123/DNAC-Backup-manager.git
```

Then install the  requirements (after upgrading pip). 
Older versions of pip may not install the requirements correctly.
```buildoutcfg
pip install -U pip
pip install -r requirements.txt
```

Edit the dnac_vars file to add your DNAC and credential.  You can also use environment variables.

## Listing the backups
Run the manage_backup command with no arguments

```
./manage_backups.py 
Backup-id                               name                          timestamp                     time
70a0a277-8ff6-48b3-8a7b-832eef048c5a    testing                       1666243182.6503744            2022-10-20 16:19:42
```

## Deleting old backups
By default backups older than a week are deleted.  To delete a backup more recently, use the --older <secs> argument.  For example, older than 1 hour, you can use --older 3600
  
  ```
./manage_backups.py --older 3600
delete 70a0a277-8ff6-48b3-8a7b-832eef048c5a 2022-10-20 16:19:42
{'response': {'status': 'ok', 'message': "Deleted backup (backup_id='70a0a277-8ff6-48b3-8a7b-832eef048c5a')"}, 'version': '1.5.1'}
```
  
  ## Deleting a specific backup
  Provide a backup-id and just that back up will be deleted.
  
  ```
./manage_backups.py --delete 70a0a277-8ff6-48b3-8a7b-832eef048c5a
{'response': {'status': 'ok', 'message': "Deleted backup (backup_id='70a0a277-8ff6-48b3-8a7b-832eef048c5a')"}, 'version': '1.5.1'}
````
Note: This API call does not return an error if the backup does not exist.. so check carefully.
  
