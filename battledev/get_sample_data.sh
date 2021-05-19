#! /bin/bash

sampledatafile=$(ls -rt ~/Téléchargements/sample-*.zip | tail -1)
unzip ${sampledatafile}

mv $(basename ${sampledatafile} .zip) sample
rm ${sampledatafile}

for i in $(ls sample/input*.txt); do
    j=$i.old
    mv $i $j
    (cat $j && echo) > $i
    rm $j
done
