cat /usr/share/wordlists/rockyou.txt | while read line;do if ssh-keygen -p -P $line -N $line -f /tmp/test/id_rsa 1>/dev/null 2>/dev/null;then echo "PASSWORD FOUND : "$line;break;fi;done;
