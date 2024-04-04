gcc -o moveFile moveFile.c
./moveFile src2 KdriveRep
sleep 10

python3 modify.py KdriveRep/message.txt

./moveFile KdriveRep src2
sleep 5

rm -f moveFile