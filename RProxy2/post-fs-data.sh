#!system/bin/sh
CADDY_PATH="/data/local/caddy2"
MODDIR=${0%/*}
LOCAL_PATH="${MODDIR}/caddy2"
if [ ! -d $CADDY_PATH ];then
 mkdir $CADDY_PATH
fi
 cp -f ${LOCAL_PATH}/caddy  $CADDY_PATH
cp -f ${LOCAL_PATH}/start.sh $CADDY_PATH
cp -f ${LOCAL_PATH}/steamcommunity.crt $CADDY_PATH
cp -f ${LOCAL_PATH}/steamcommunity.key $CADDY_PATH
cp -f ${LOCAL_PATH}/Caddyfile $CADDY_PATH
cp -f ${LOCAL_PATH}/5efe33a8.0 /system/etc/security/cacerts/ 




chmod 777 "${CADDY_PATH}/caddy"
chmod 777 "${CADDY_PATH}/start.sh"


