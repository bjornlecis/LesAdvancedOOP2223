from connectie import cursor

cursor.execute("SHOW COLUMNS FROM gemeentes.gemeente")
for gemeente in cursor:
    print(*gemeente)
