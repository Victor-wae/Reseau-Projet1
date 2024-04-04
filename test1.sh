gcc -o moveFile moveFile.c
./moveFile src KdriveRep
sleep 55

python3 modify.py KdriveRep/message.txt


sleep 10
./moveFile KdriveRep src
sleep 5
rm -f moveFile