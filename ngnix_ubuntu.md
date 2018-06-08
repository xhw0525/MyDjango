##

#鑫彩
server {
    listen  80;
    server_name www.letgotry.site letgotry.site ;
    root /home/uxhw/xinload;
	index index.html;

}

#默认
server {
	listen 80 ;
	listen [::]:80  ipv6only=on;
	root /usr/share/nginx/html;
	index index.html index.htm;
	server_name localhost;
	location / {
		try_files $uri $uri/ =404;
	}
}



#MyDjango
server {
    listen 8081;
    listen [::]:8081;
    charset utf-8;
    server_name localhost;

#    root /var/www/example.com;
#    index index.html;

    access_log      /home/xhw/log/nginx/MyDjango_access.log;
    error_log       /home/xhw/log/nginx/MyDjango_error.log;

    client_max_body_size 75M;

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:1801;
        uwsgi_read_timeout 5;
    }
    location /static {
        expires 30d;
        autoindex on;
        add_header Cache-Control private;
        alias /home/xhw/MyDjango/static/;
     }
    location /media {
        alias /home/xhw/MyDjango/media/;
    }
}

#gogs
server {
    server_name localhost;
    listen 8082;
    # 或者 443，如果你使用 HTTPS 的话
    # ssl on; 是否启用加密连接
    # 如果你使用 HTTPS，还需要填写 ssl_certificate 和 ssl_certificate_key
    location / {
    # 如果你希望通过子路径访问，此处修改为子路径，注意以 / 开头并以 / 结束
        proxy_pass http://localhost:3000/;
    }
}


################################################以下是试例



# You may add here your
# server {
#	...
# }
# statements for each of your virtual hosts to this file

##
# You should look at the following URL's in order to grasp a solid understanding
# of Nginx configuration files in order to fully unleash the power of Nginx.
# http://wiki.nginx.org/Pitfalls
# http://wiki.nginx.org/QuickStart
# http://wiki.nginx.org/Configuration
#
# Generally, you will want to move this file somewhere, and start with a clean
# file but keep this around for reference. Or just disable in sites-enabled.
#
# Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
##

#server {
#	listen 80 default_server;
#	listen [::]:80 default_server ipv6only=on;
#
#	root /usr/share/nginx/html;
#	index index.html index.htm;
#
#	# Make site accessible from http://localhost/
#	server_name localhost;
#
#	location / {
#		# First attempt to serve request as file, then
#		# as directory, then fall back to displaying a 404.
#		try_files $uri $uri/ =404;
#		# Uncomment to enable naxsi on this location
#		# include /etc/nginx/naxsi.rules
#	}
#
#	# Only for nginx-naxsi used with nginx-naxsi-ui : process denied requests
#	#location /RequestDenied {
#	#	proxy_pass http://127.0.0.1:8080;
#	#}
#
#	#error_page 404 /404.html;
#
#	# redirect server error pages to the static page /50x.html
#	#
#	#error_page 500 502 503 504 /50x.html;
#	#location = /50x.html {
#	#	root /usr/share/nginx/html;
#	#}
#
#	# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#	#
#	#location ~ \.php$ {
#	#	fastcgi_split_path_info ^(.+\.php)(/.+)$;
#	#	# NOTE: You should have "cgi.fix_pathinfo = 0;" in php.ini
#	#
#	#	# With php5-cgi alone:
#	#	fastcgi_pass 127.0.0.1:9000;
#	#	# With php5-fpm:
#	#	fastcgi_pass unix:/var/run/php5-fpm.sock;
#	#	fastcgi_index index.php;
#	#	include fastcgi_params;
#	#}
#
#	# deny access to .htaccess files, if Apache's document root
#	# concurs with nginx's one
#	#
#	#location ~ /\.ht {
#	#	deny all;
#	#}
#}


# another virtual host using mix of IP-, name-, and port-based configuration
#
#server {
#	listen 8000;
#	listen somename:8080;
#	server_name somename alias another.alias;
#	root html;
#	index index.html index.htm;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}


# HTTPS server
#
#server {
#	listen 443;
#	server_name localhost;
#
#	root html;
#	index index.html index.htm;
#
#	ssl on;
#	ssl_certificate cert.pem;
#	ssl_certificate_key cert.key;
#
#	ssl_session_timeout 5m;
#
#	ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
#	ssl_ciphers "HIGH:!aNULL:!MD5 or HIGH:!aNULL:!MD5:!3DES";
#	ssl_prefer_server_ciphers on;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}

##########################################################

##下方代码开启https#
#server {
#    listen  80;
#    server_name  localhost;
#    # force redirect http to https
#    rewrite ^ https://$http_host$request_uri? permanent;
#    #return 301 https://$http_host$request_uri;
#    }
#server {
#	listen 443 ssl;
#	server_name localhost;
#
#	root html;
#	index index.html index.htm;
#
##	ssl on;
#	ssl_certificate /etc/nginx/ssl/nginx.crt;
#	ssl_certificate_key /etc/nginx/ssl/nginx.key;
#
#	ssl_session_timeout 5m;
##
##	ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
##	ssl_ciphers "HIGH:!aNULL:!MD5 or HIGH:!aNULL:!MD5:!3DES";
##	ssl_prefer_server_ciphers on;
##
#
#
#	location / {
#		# First attempt to serve request as file, then
#		# as directory, then fall back to displaying a 404.
#		try_files $uri $uri/ =404;
#		# Uncomment to enable naxsi on this location
#		# include /etc/nginx/naxsi.rules
#	}
#
#    keepalive_timeout   70;
#    server_tokens off; #隐藏nginx版本号
#
#    #强制用 HTTPS 访问?
#    #add_header Strict-Transport-Security "max-age=31536000; includeSubdomains";
#    #不知道下面2句啥用
#    #fastcgi_param   HTTPS               on;
#    #fastcgi_param   HTTP_SCHEME         https;
#
#    }