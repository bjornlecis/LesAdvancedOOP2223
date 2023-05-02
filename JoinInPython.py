from connectie import cursor

sql = f"SELECT naam,voetbalploeg,gemeente.gem_naam FROM gemeentes.persoon " \
      f"JOIN gemeente on gemeente = gemeente.gem_id"

ploeg = input("geef je ploeg")
sql2 = f"SELECT naam,voetbalploeg,gemeente.gem_naam FROM gemeentes.persoon " \
       f"JOIN gemeente on gemeente = gemeente.gem_id " \
       f"WHERE voetbalploeg !=\"{ploeg}\";"

cursor.execute(sql2)


print("Naam","Ploeg","Gemeente")
for line in cursor:
    print(*line)
