# Backup tool

This tool will show or delete older automation backups on Cisco DNA Center.

****warning:  This uses internal Cisco DNAC Center API, so is not officially supported.***

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

