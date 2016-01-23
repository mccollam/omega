opkg update
opkg install php5 php5-cgi
cat << EOL > /www/p.php
<?php
system("stty -F /dev/ttyUSB0 115200");
system("/root/projector.sh " . $_GET["c"]);
?>
EOL

cd /root
wget https://github.com/mccollam/VSControl/raw/master/projector.sh
chmod a+x projector.sh

sed -i "s/'Omega-.*'/'projector'/" /etc/config/system
sed -i "s/OnionOmega/projector/" /etc/config/network
