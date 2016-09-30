sudo apt-get install pure-ftpd

sudo su
#TYPE PASSWORD

groupadd ftpgroup

useradd ftpuser -g ftpgroup -s /sbin/nologin -d /dev/null

exit
#TO EXIT FROM THAT

sudo mkdir /home/pi/FTP

sudo chown -R ftpuser:ftpgroup /home/pi/FTP
#-R FOR READ ACCESS ONLY

sudo pure-pw useradd upload -u ftpuser -g ftpgroup -d /home/pi/FTP -m
#IT MAY ASK PASSWORD

sudo pure-pw mkdb
#IT MAY ASK PASSWORD

ln -s /etc/pure-ftpd/conf/PureDB
#IF THIS DOESNT WORK TYPE BELOW COMMAND
#ln -s /etc/pure-ftpd/conf/PureDB /etc/pure-ftpd/auth/60puredb



sudo service pure-ftpd restart
#FOR RESTARTING THE SERVICE

sudo service pure-ftpd stop
#TO STOP

sudo service pure-ftpd start
#TO START



