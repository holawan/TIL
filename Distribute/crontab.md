## 인증서 갱신

- certbot은 인증서 확인 후, 컨테이너가 중지되므로, 해당 컨테이너를 주기적으로 실행해주면 됨
- --dry-run 옵션으로 충분히 테스트 후, 다음과 같이 --force-revewal을 넣어줌 

```
  certbot:
    depends_on:
      - nginxproxy 
    image: certbot/certbot
    container_name: certbot
    volumes:
      - ./certbot-etc:/etc/letsencrypt
      - ./myweb:/usr/share/nginx/html
    command: certonly --webroot --webroot-path=/usr/share/nginx/html --email test@test.com --agree-tos --no-eff-email --keep-until-expiring -d familyzoa.com -d www.familyzoa.com --force-renewal 

```

### crontab 설정

- 리눅스나 맥에서 주기적으로 명령을 실행하는 것 

```
crontab -e
```

```
PATH=/usr/local/bin

* * * * * docker-compose -f /home/ubuntu/09_HTTPS_NGINX/docker-compose.yml restart certbot >> /home/ubuntu/09_HTTPS_NGINX?cron.log 2>&1
```

#### Crontab 주요 명령

- crontab -e
  - 크론탭 설정 입력 파일(텍스트 에디터 사용 태스크 추가/수정/삭제)
- crontab -l
  - 현재 크론탭에 설정되어 있는 내용 확인

#### Crontab 설명

- \* 5개로 이뤄져 있음

  ```(
  *         *        *        *        *
  분(0~59) 시간(0~23) 일(1~31) 월(1~12) 요일(0~7)
  ```

  - 요일에서 0과 7은 일요일 1~6은 월요일에서 토요일 

- 특정시간에 실행 -매주 월요일 오전 6시 40분에 실행

  ```
  40 6 * * 1 /root/scripts/status_check.sh
  ```

- 반복 실행 - 매일 매시간 0분, 20분, 40분에 실행

  ```
  0,20,40 * * * * /root/scripts/status_check.sh
  ```

- 범위 실행 - 매일 오전 6시 10분부터 40분까지 매분 실행

  ```
  10-40 6 * * * /root/scripts/status_check.sh
  ```

- 간격 실행 - 매 20분마다 실행

  ```
  */20 * * * * /root/scripts/status_check.sh
  ```

- 특정 여러 시각 실행 - 10일에서 12일까지 4시,5시,6시 매 20분마다 실행

  ```
  */20 4,5,6 10-20 * * /root/scripts/status_check.sh
  ```

#### crontab 실행 팁

- 로그 남겨두기
- 단, 로그가 많이 쌓이면, 저장공간이 꽉 차게 되고, 컴퓨터 다운 또는 비정상동작을 보일 수 있으므로, 주기적으로 삭제 

```
*/20 * * * * /root/scripts/status_check.sh >> /var/log/status_check.log 2>&1
* * 1 * * rm -rf /var/log/status_check.log 2>&1
```

