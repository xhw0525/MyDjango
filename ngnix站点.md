##
server {
    listen 8081;
    listen [::]:8081;
    charset utf-8;
    server_name localhost;

#    root /var/www/example.com;
#    index index.html;

    access_log      /home/uxhw/nginx/MyDjango_access.log;
    error_log       /var/log/nginx/MyDjango_error.log;

    client_max_body_size 75M;

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8000;
        uwsgi_read_timeout 5;
    }
    location /static {
        expires 30d;
        autoindex on;
        add_header Cache-Control private;
        alias /home/uxhw/uftp/MyDjango/static/;
     }
    location /media {
        alias /home/uxhw/uftp/MyDjango/media/;
    }
}
