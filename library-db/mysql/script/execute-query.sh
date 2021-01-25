# 第一引数のクエリを library-db に実行するスクリプト
# bash script/execute-query.sh "select * from users"
# みたいにして呼び出す
docker exec -it mysql_host mysql -u root -proot -D library -e "$1"