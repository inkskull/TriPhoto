import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil
saisons={
        '01':'4 hiver',
        '02':'4 hiver',
        '03':'1 printemps',
        '04':'1 printemps',
        '05':'1 printemps',
        '06':'2 ete',
        '07':'2 ete',
        '08':'2 ete',
        '09':'3 automne',
        '10':'3 automne',
        '11':'3 automne',
        '12':'4 hiver'}

cible=r'/home/eric/Images'
source=r'/home/eric/Images/atrier'

def enumerateur(racine):
    return

def datephoto(chemin):
    data=get_exif(chemin)
    if 'DateTime' not in data:
        mois='00'
        annee='0000'
        return annee,mois
    mois=data['DateTime'][5:7]
    annee=data['DateTime'][:4]
    return annee,mois

def choisirepertoire(annee,mois):
    if mois=='00':
        nomdoss=os.path.join(cible,'nonclasse')
        return nomdoss
    if mois=='12':
        nomdoss=os.path.join(cible,annee+'-'+str(int(annee)+1)+r' '+saisons[mois])
        return nomdoss
    if mois=='01' or mois=='02':
        nomdoss=os.path.join(cible,str(int(annee)-1)+'-'+annee+r' '+saisons[mois])
        return nomdoss
    nomdoss=os.path.join(cible,annee+r' '+saisons[mois])
    return nomdoss


def copiephoto(repertoire):
    return

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

if __name__ == "__main__":

    for dirname, dirnames, filenames in os.walk(source):
        print (dirname, dirnames , filenames)
        for filename in filenames:
            print(filename)
            (nom,extension)=os.path.splitext(filename)
            if os.path.normcase(extension)=='.JPG':
                annee,mois = datephoto(os.path.join(dirname,filename))
                nomdoss=choisirepertoire(annee,mois)
                print(nomdoss)

                if not(os.path.exists(nomdoss)):
                    os.makedirs(nomdoss)
                if not(os.path.exists(os.path.join(nomdoss,filename))):
                    shutil.move(os.path.join(dirname,filename),nomdoss)
                elif not(os.path.exists(os.path.join(cible,'double',filename))):
                    shutil.move(os.path.join(dirname,filename),os.path.join(cible,'double'))
            else:
                if not(os.path.exists(os.path.join(cible,'nonclasse',filename))):
                    shutil.move(os.path.join(dirname,filename),os.path.join(cible,'nonclasse'))
                elif not(os.path.exists(os.path.join(cible,'double',filename))):
                    shutil.move(os.path.join(dirname,filename),os.path.join(cible,'double'))
