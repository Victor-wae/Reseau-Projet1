#ajoute des documents au répertoire Kdrive, lui laisse le temps de se synchroniser avec le répertoire en ligne, modifie le fichier message.txt, attend la synchronisation, puis supprime les documents ajoutés

gcc -o moveFile moveFile.c
./moveFile src KdriveRep

sleep 10

python3 modify.py KdriveRep/message.txt

sleep 10
./moveFile KdriveRep src
sleep 5
rm -f moveFile