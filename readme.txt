Commands:

$ sudo apt-get update
$ sudo apt install python3-pip
$ pip3 install -r requirements.txt

$ sudo apt install nginx

$ cd /etc/nginx/sites-enabled/
$ sudo nano fastapi_nginx

server {    
   listen 80;    
   server_name server_name;    
   location / {        
     proxy_pass http://127.0.0.1:8000;    
   }
}

$ sudo rm /etc/nginx/sites-enabled/default

$ sudo service nginx restart
$ python3 -m uvicorn main:app
