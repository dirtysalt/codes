#!/bin/bash

source common.sh

VAULT_NAME="${VAULT_NAME:-test-vault}"
VAULT_IMAGE="${VAULT_IMAGE:-hashicorp/vault:latest}"
VAULT_TOKEN="roottoken"

tmp_bash_file=$(mktemp)
ok=0
cleanup() {
    # docker rm -f $VAULT_NAME; echo-green "remove old docker container"    
    rm -f ${tmp_bash_file}
    if [ ok = 0 ]; then
        echo-red "[FAILED]"
    else
        echo-green "[PASSED]"
    fi
}

trap cleanup EXIT

wd=$(gen-working-dir test-vault)
cd $wd

echo-green "pull docker image: $VAULT_IMAGE"
docker pull $VAULT_IMAGE
docker rm -f $VAULT_NAME || echo-green "remove old docker container"

echo-green "create new docker container: $VAULT_NAME"
docker run --network host --cap-add=IPC_LOCK -e "VAULT_DEV_ROOT_TOKEN_ID=${VAULT_TOKEN}" -d --name=$VAULT_NAME ${VAULT_IMAGE} 

cat << EOF > ${tmp_bash_file}
set -e

export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="${VAULT_TOKEN}"

# don't know why, but have to stop here for a while??
sleep 1
vault login ${VAULT_TOKEN} && echo "[XXX] enable login..."

vault secrets enable database || echo "[XXX] enable database..."

echo "[XXX] write db..."
vault write database/config/my-mysql-database \
    plugin_name=mysql-database-plugin \
    connection_url="{{username}}:{{password}}@tcp(${FE_IP}:${FE_PORT})/" \
    allowed_roles="my-role" \
    username="${FE_USER}" \
    password="${FE_PASS}"

echo "[XXX] write role..."
vault write database/roles/my-role \
    db_name=my-mysql-database \
    creation_statements="CREATE USER '{{name}}'@'%' IDENTIFIED BY '{{password}}';GRANT root TO '{{name}}'; set default role root to '{{name}}'" \
    default_ttl="1h" \
    max_ttl="24h"


echo "[XXX] ask cred..."
vault read database/creds/my-role > /root/cred.txt
EOF
chmod +x ${tmp_bash_file}

cp ${tmp_bash_file} run.sh
docker cp ${tmp_bash_file} ${VAULT_NAME}:/root/run.sh
echo-green "docker exec -it ${VAULT_NAME} /bin/sh -c /root/run.sh"
docker exec -it ${VAULT_NAME} /bin/sh -c /root/run.sh
docker cp ${VAULT_NAME}:/root/cred.txt cred.txt

user=`grep username cred.txt | awk '{print$2}'`
pass=`grep password cred.txt | awk '{print$2}'`

echo-green "check mysqldb..."
mysql -h ${FE_IP} -P ${FE_PORT} -u ${user} -p${pass} << EOF
show users;
EOF

ok=1