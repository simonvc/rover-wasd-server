#mjpg_streamer -i "/usr/lib/input_uvc.so -d /dev/video0  -r 320x240 -f 28" -o "/usr/lib/output_http.so -p 8090 -w /var/www"
#mjpg_streamer -i "/usr/lib/input_uvc.so  -d /dev/video0  -r 640x360 -f 60" -o "/usr/lib/output_http.so -p 8090 -w /var/www"
mjpg_streamer -i "/usr/lib/input_uvc.so  -d /dev/video0  -r 320x240 -q 50 -f 30" -o "/usr/lib/output_http.so -p 8090 -w /var/www"

