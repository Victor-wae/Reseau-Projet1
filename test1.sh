./moveFile src KdriveRep
sleep 10

python3 modify.py KdriveRep/message.txt

./moveFile KdriveRep src
sleep 5