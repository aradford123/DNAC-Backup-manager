# Backup tool

This tool will show or delete older automation backups on Cisco DNA Center.

****warning:  This uses internal Cisco DNAC Center API, so is not officially supported.***

Each automation backup on Cisco DNA Center is a complete copy.  If you backup everyday, it is easy to fill up the back up partition.  It is common to delete older backups. This tool can show the current backups, delete a specific backup by id, or delete all backups older than a certain time (the default is one week).



