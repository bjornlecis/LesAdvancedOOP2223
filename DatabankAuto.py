import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd ="root",
    database ="dbauto"

)

def toon_menu():
    print("1: toon alle wagen")
    print("2: alle beschikbare merken")
    print("3: alle wagen jonger dan bouwjaar")
    print("4: voeg een wagen toe")
    print("5: verwijder een wagen")

def toon_alle_wagens():
    mycursor = db.cursor()
    mycursor.execute("select * from auto")
    for x in mycursor:
        print(*x)
def toon_alle_merken():
    mycursor = db.cursor()
    mycursor.execute("select distinct Merk from auto")
    for x in mycursor:
        print(*x)
def toon_alle_wagens_vanaf_bouwjaar():
    mycursor = db.cursor()
    bouwjaar = int(input("geef het bouwjaar ind"))
    sql = f"select * from auto where bouwjaar > {bouwjaar}"
    mycursor.execute(sql)
    for x in mycursor:
        print(*x)
def voeg_een_wagen_toe():
    merk = input("geef het merk in")
    model = input("geef het model in")
    bouwjaar = int(input("geef het bouwjaar in"))
    brandstof = input("geef brandstof in")

    mycursor = db.cursor()
    sql = "INSERT INTO auto (Merk, Model, Bouwjaar,Brandstof) VALUES (%s, %s, %s, %s)"
    val = (merk, model, bouwjaar,brandstof)
    mycursor.execute(sql,val)
    print("record toegevoegd")
    db.commit()

def verwijder_een_auto():
    toon_alle_wagens()
    wagen_id = input("geef het id van de wagen die je wenst te verwijderen")
    mycursor = db.cursor()
    sql = f"delete from auto where idauto = {wagen_id}"
    mycursor.execute(sql)
    print("wagen verwijderd")
    db.commit()
########################################"
#Hoofdprogramma
########################################

toon_menu()
invoer = input("geef je opdracht in")
while invoer != "stop":
    if invoer == "1":
        toon_alle_wagens()
    elif invoer == "2":
        toon_alle_merken()
    elif invoer == "3":
        toon_alle_wagens_vanaf_bouwjaar()
    elif invoer == "4":
        voeg_een_wagen_toe()
    elif invoer == "5":
        verwijder_een_auto()
    toon_menu()
    invoer = input("geef je opdracht")
