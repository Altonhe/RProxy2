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
cp -f ${LOCAL_PATH}/cert.key $CADDY_PATH
cp -f ${LOCAL_PATH}/cert.crt $CADDY_PATH




chmod 777 "${CADDY_PATH}/caddy"
chmod 777 "${CADDY_PATH}/start.sh"

sleep 20
su -c "/data/local/caddy2/start.sh"


