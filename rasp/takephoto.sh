content=`cat /sys/class/net/wlan0/address`
id=`grep "$content" /home/pi/rasp/id_list | cut -d , -f 2`
if [ "$id" = "" ]
then
    raspistill -vf -o /home/pi/rasp/photo/ERRORID.jpg
else
    raspistill -vf -o /home/pi/rasp/photo/photo_"$id"_$(date +"%Y%m%d_%H%M%S").jpg
fi