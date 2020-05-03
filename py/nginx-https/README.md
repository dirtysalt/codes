- http.py # represents backend http service.
- server.conf # configuration file for nginx.
- 生成 server.key, server.crt # [How to create a self-signed Certificate](http://www.akadia.com/services/ssh_test_certificate.html)
- install server.crt # [How to create a self-signed Certificate](http://askubuntu.com/questions/73287/how-do-i-install-a-root-certificate)

生成server.key/server.crt 可以参考下面命令
```
# . 可以留空. 如果希望匹配所有子域名的话，需要使用wildcard表示如*.xxx.com
openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr
# 下面这步骤是自己做签名认证。正规的流程是在第三方机构做签名认证
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```
