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


# Nginx Configuration Examples

This document provides common and practical examples of Nginx configurations. These configurations are suitable for various scenarios including static resource hosting, reverse proxying, load balancing, and more.

---

## **1. Static Resource Hosting**

Serve static files such as HTML, CSS, JavaScript, or images.

```nginx
server {
    listen 80;
    server_name example.com;

    root /var/www/example.com;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Cache static files like images, CSS, and JS
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|ttf|svg|eot|otf|html)$ {
        expires 30d;
        access_log off;
    }
}
```

---

## **2. Reverse Proxy**

Forward requests to a backend service.

```nginx
server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://127.0.0.1:3000; # Backend service address
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

---

## **3. HTTPS Configuration**

Enable HTTPS using Let's Encrypt certificates.

```nginx
server {
    listen 80;
    server_name example.com;

    # Redirect HTTP to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;

    # SSL certificate paths
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        root /var/www/example.com;
        index index.html;
    }
}
```

---

## **4. Load Balancing**

Distribute traffic to multiple backend servers.

```nginx
upstream backend {
    server 192.168.1.10;
    server 192.168.1.11;
    server 192.168.1.12;
}

server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

---

## **5. Path-Based Reverse Proxy**

Route requests based on specific paths to different backend services.

```nginx
server {
    listen 80;
    server_name example.com;

    location /api/auth {
        proxy_pass http://127.0.0.1:4000; # Authentication service
    }

    location /api/data {
        proxy_pass http://127.0.0.1:5000; # Data service
    }

    location / {
        root /var/www/example.com;
        index index.html;
    }
}
```

---

## **6. Dynamic DNS Backend**

Forward requests to a dynamically resolved DNS backend, such as Kubernetes services.

```nginx
http {
    resolver 8.8.8.8 1.1.1.1 valid=300s;
    resolver_timeout 5s;

    server {
        listen 80;
        server_name example.com;

        location / {
            proxy_pass http://dynamic-service.example.com;
            proxy_ssl_server_name on; # Enable HTTPS backend
        }
    }
}
```

---

## **7. Caching Proxy**

Cache backend responses for improved performance.

```nginx
proxy_cache_path /tmp/cache keys_zone=my_cache:10m levels=1:2 inactive=60m;

server {
    listen 80;
    server_name example.com;

    location / {
        proxy_cache my_cache;
        proxy_cache_valid 200 302 10m;
        proxy_cache_valid 404 1m;
        proxy_pass http://127.0.0.1:3000;
    }
}
```

---

## **8. Rate Limiting**

Limit the number of requests per second to prevent abuse.

```nginx
http {
    limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;

    server {
        listen 80;
        server_name example.com;

        location / {
            limit_req zone=one burst=20 nodelay;
            proxy_pass http://127.0.0.1:3000;
        }
    }
}
```

---

## **9. WebSocket Proxy**

Enable WebSocket support through Nginx.

```nginx
server {
    listen 80;
    server_name example.com;

    location /ws/ {
        proxy_pass http://127.0.0.1:4000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

---

## **10. SPA (Single Page Application) Support**

Handle frontend frameworks with client-side routing, such as React or Vue.js.

```nginx
server {
    listen 80;
    server_name example.com;

    root /var/www/example.com;
    index index.html;

    location / {
        try_files $uri /index.html;
    }
}
```

---

## **11. Optimized File Download**

Enhance file download performance for large files.

```nginx
server {
    listen 80;
    server_name example.com;

    location /downloads/ {
        root /var/www/files;
        sendfile on;
        tcp_nopush on;
    }
}
```

---

## **12. Prevent Hotlinking**

Restrict other websites from directly linking your image resources.

```nginx
server {
    listen 80;
    server_name example.com;

    location /images/ {
        root /var/www/example.com;
        valid_referers none blocked example.com *.example.com;
        if ($invalid_referer) {
            return 403;
        }
    }
}
```

---

## Conclusion
These examples cover common use cases for Nginx configurations. You can use them as templates and adapt them to your specific needs. If you have any unique requirements, feel free to extend these configurations!

