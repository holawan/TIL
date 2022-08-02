### 저장소 세팅

```
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository universe
$ sudo apt-get update
```

### cerbot 설치

```
$ sudo apt-get update
$ sudo apt-get install certbot python3-certbot-nginx
```

### SSL 설정 -cerbot 이용 자동화

```
[SSL 설정]
sudo certbot --nginx -d [domain]
[갱신 테스트]
sudo certbot renew --dry-run
[인증서 만료일 확인]
certbot ceritificates
```

### 인증서 파일 위치

/etc/letsencrypt/live/domain



### Crontab을 이용한 SSL 자동 갱신

```
[Crontab 보기]
sudo crontab -l
[Crontab 편집]
sudo crontab -e
[Crontab 실행 로그]
view /var/log/syslog
```

```
매월 1일 새벽 3시에 갱신되도록 설정
0 18 1 * * /usr/bin/certbot renew --renew-hook="sudo systemctl restart nginx"
18이 새벽 3시인 이유 : 서버시간에 맞춰서 진행 (date로 서버시간 확인)
```



### Nginx 세팅

```
$ sudo vi /etc/nginx/site-avaliable/default
```

​		

```
server {
		listen 80 default_server;
		listen [::]:80 default_server;

		location / {
				root /var/www/html;
				index index.nginx-debvian.html;
		}
		server_name www.domain;
		return 301 https://www.domain$request_uri;
}

server {
            listen 443 ssl;
            listen [::]:443;
            server_name www.domain;
            ssl_certificate /etc/letsencrypt/live/domain/fullchain.pem; # managed by Certbot
            ssl_certificate_key /etc/letsencrypt/live/domain/privkey.pem; # managed by Certbot
            include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
            ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
            location / {
                #root /home/ubuntu/dist;
                root /var/www/html;
                index index.nginx-debian.html;
                }
location /demo {
            proxy_pass url;
            proxy_redirect off;
            charset utf-8;
            proxy_set_header X-Readl-IP $remote_addr;
            proxy_set_header X-Forwarded-For @proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-NginX-Proxy true;
	}
}
```



```
//nginx 서버 상태
sudo systemctl status nginx
//nginx 서버 켜기
sudo systemctl start nginx
//nginx 서버 중지
sudo systemctl stop nginx
//nginx 서버 재시작
sudo systemctl restart nginx
```

