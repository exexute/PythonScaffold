cat $2 | while read line;do if 7z e $1 -p"$line" 1>/dev/null 2>/dev/null;then echo "FOUND PASSWORD:"$line;break;fi;done
