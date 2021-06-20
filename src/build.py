import os
import shutil
import re
import pprint
try:
    import markdown
except(Exception):
    print("\"Markdown\" ist nicht installiert.Bitte hole dies nach mit \"pip install -r requirements.txt\"")

def vorbereiten(pfad):

    # Verzeichnis docs aufräumen

    if os.path.exists(pfad):
        try:
            shutil.rmtree(pfad)
        except Exception:
            print("Es ist ein Fehler aufgetreten den Pfad \"" + pfad + "\" zu löschen.")
            exit(1)
        finally:
            print("Der Pfad \"" + pfad + "\" wurde erfolgreich gelöscht.")
    else:
        print("Der Pfad \"" + pfad + "\" musste nicht gelöscht werden.")

    
    
def scan(uhrsprung, ziel):
    dateinvorher = []
    dateinnachher = []
    for ordnerpfad, dateiname, dateipfad in os.walk(uhrsprung):
        for datei in dateipfad:
            os.path.join(ordnerpfad, datei)
            dateinvorher.append(os.path.join(ordnerpfad, datei))
            dateinnachher.append(os.path.join(ordnerpfad, datei).replace(uhrsprung, ziel))
            print(dateinvorher)
            print(dateinnachher)
    return(dateinvorher,dateinnachher)

def generiere(datei,ziel):
    print("Lade Header und Footer...")
    try:
        with open (os.path.join(arbeitspfad,"include","html","header.html"), "r", encoding="UTF-8") as f:
            header = f.read()
            f.close
        with open (os.path.join(arbeitspfad,"include","html","footer.html"), "r", encoding="UTF-8") as f:
            footer = f.read()
            f.close
    except(Exception):
        print("Die Header und Footer sind Fehlerhaft.")

    for oldfile,newfile in zip(datei,ziel):
        newfile = str(newfile).replace(".md",".html")
        print("Generiere: \"" + oldfile + "\" zu \"" + newfile + "\"")

        filepath= os.path.dirname(newfile)
        if not os.path.exists(filepath):
            os.makedirs(filepath)

        #Markdown
        with open(oldfile, 'r', encoding="utf8") as f:
            text = f.read()
            f.close
            md = markdown.markdown(text, extensions=['toc','meta','tables'])
            html = str(header) +"\n" + str(md) + "\n" +str(footer)

        

        #Html
        with open(newfile, 'w', encoding="UTF-8") as f:
            f.write(html)
            f.close()

def vars(htmlstring,pfadderdatei):
    """
    Ersetzt die variablen in dem header und footer.
    """

    vars= {
        "MAINCSSPATH":"",
        "MAINJSPATH":"",
        "MAINIMGPATH":"",
    }
    htmlstring.re

def cpdir(von,nach):
    """
    Kopiert ein Verzeichnis rekursiv (d.h. Den gesamten Inhalt inklusive Unterordner)
    """
    shutil.copytree(von,nach)
def logo():
    with open(os.path.join(arbeitspfad,"src","logo"), "r") as f:
        zeilen = f.readlines()        
        for zeile in zeilen:
            print(zeile.replace('\n',''))



def main():
    print("Starte bau der Website...")

    global arbeitspfad
    arbeitspfad = os.path.dirname(os.path.realpath('__file__'))
    
    logo()

    vorbereiten(os.path.join(arbeitspfad,"docs"))

    #Benötigte Datein wie CSS, Bilder und co. zu kopieren.
    cpdir(os.path.join(arbeitspfad,"include","public"),os.path.join(arbeitspfad,"docs"))

    #Verzeichise lesen
    tmp1, tmp2 =scan(os.path.join(arbeitspfad,"seiten"), os.path.join(arbeitspfad,"docs"))

    generiere(tmp1,tmp2)

    
    


    

if __name__ == '__main__':
    main()




import time
while True:
    try:
        logo()
        #input("Neugenerieren")
        time.sleep(3)
        main()
    except(Exception):
        print("Es ist ein Unbekannter Fehler aufgetreten")


