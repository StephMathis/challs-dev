#! /bin/bash
set -x

sampledatafile=$(ls -rt ~/Téléchargements/sample-*.zip | tail -1)
unzip ${sampledatafile}

#mv $(basename ${sampledatafile} .zip) sample
mv sample-* samples
rm ${sampledatafile}

for i in $(ls samples/*put*.txt); do
    j=$i.old
    mv $i $j
    (cat $j && echo) > $i
    rm $j
done

if [ ! -e soluce.py ]; then
  cp -r $(dirname $0)/templates/* $(dirname $0)/templates/.vscode .
  chmod +x soluce.py
fi
