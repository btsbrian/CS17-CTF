#!/bin/bash

while [ 1 -eq 1 ]; do
fil=`ls`

filtype=`file $fil | cut -d" " -f 2`

case "$filtype" in
	gzip)
		mv $fil $fil.gz
		gunzip $fil.gz
		;;
	LZMA)
		mv $fil $fil.lzma
		lzma -d $fil.lzma
		;;
	rzip)
		mv $fil $fil.rz
		rzip -d $fil.rz
		;;
	7-zip)
		mv $fil $fil.7z
		p7zip -d $fil.7z
		;;
	Zip)
		mv $fil $fil.zip
		unzip $fil.zip
		rm $fil.zip
		;;
	bzip2)
		mv $fil $fil.bz
		bzip2 -d $fil.bz
		;;
	ARC)
		mv $fil $fil.arc
		unar $fil.arc
		rm $fil.arc
		;;
	*)
		echo Unknown file type: $fil -- $filtype
		exit 1
esac

done
