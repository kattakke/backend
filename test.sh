

echo "Register Test"

curl -X "POST" \
  "${kattakke_host}/api/v0/users" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
"id": "string",
"password": "string"
}'

echo "Login Test"

token=$(curl -X "POST" \
  "${kattakke_host}/api/v0/auth/login" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "string",
  "password": "string"
}'  | python3 -c 'import sys, json; print(json.load(sys.stdin)["message"])')

echo "JWT Toekn: ${token}"

echo "Auth Me Test"
userId=$(curl -X "GET" \
  "${kattakke_host}/api/v0/auth/me" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}" | python3 -c 'import sys, json; print(json.load(sys.stdin)["userId"])')

echo "UUID: ${userId}"

echo "Logout Test"

curl -X "PATCH" \
  "${kattakke_host}/api/v0/auth/logout" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}"

echo "Logout Test 2"

curl -X "GET" \
  "${kattakke_host}/api/v0/auth/me" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}"

token=$(curl -X "POST" \
  "${kattakke_host}/api/v0/auth/login" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "string",
  "password": "string"
}'  | python3 -c 'import sys, json; print(json.load(sys.stdin)["message"])')

echo "JWT Toekn: ${token}"

echo "User DELETE Test"

curl -X "DELETE" \
  "${kattakke_host}/api/v0/users/${userId}" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}"

echo "User DELETE Test 2"

curl -X "GET" \
  "${kattakke_host}/api/v0/auth/me" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}"

echo "User DELETE Test 3"
curl -X "POST" \
  "${kattakke_host}/api/v0/auth/login" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "string",
  "password": "string"
}'

echo "Register New User"

curl -X "POST" \
  "${kattakke_host}/api/v0/users" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "string",
  "password": "string"
}'



token=$(curl -X "POST" \
  "${kattakke_host}/api/v0/auth/login" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "string",
  "password": "string"
}'  | python3 -c 'import sys, json; print(json.load(sys.stdin)["message"])')

echo "JWT Toekn: ${token}"

userId=$(curl -X "GET" \
  "${kattakke_host}/api/v0/auth/me" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}" | python3 -c 'import sys, json; print(json.load(sys.stdin)["userId"])')

echo "UUID: ${userId}"

curl -X "POST" \
  "${kattakke_host}/api/v0/books" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}" \
  -H "Content-Type: application/json" \
  -d '{
  "isbn": "123412341234",
  "title": "自然科学実験2020",
  "author": "北海道大学",
  "imagePath": "http://example.com/example.png"
}'

curl -X "POST" \
  "${kattakke_host}/api/v0/books" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}" \
  -H "Content-Type: application/json" \
  -d '{
  "isbn": "123412341235",
  "title": "自然科学実験2021",
  "author": "北海道大学",
  "imagePath": "http://example.com/example.png"
}'

curl -X "POST" \
  "${kattakke_host}/api/v0/books" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}" \
  -H "Content-Type: application/json" \
  -d '{
  "isbn": "123412341236",
  "title": "自然科学実験2022",
  "author": "北海道大学",
  "imagePath": "http://example.com/example.png"
}'



bookid=$(curl -X "POST" \
  "${kattakke_host}/api/v0/books" \
  -H "accept: application/json" \
  -H "Authorization: Bearer ${token}" \
  -H "Content-Type: application/json" \
  -d '{
  "isbn": "123412341236",
  "title": "自然科学実験2023",
  "author": "北海道大学",
  "imagePath": "http://example.com/example.png"
}'  | python3 -c 'import sys, json; print(json.load(sys.stdin)["bookId"])')

curl -X "GET" \
  "${kattakke_host}/api/v0/books/${bookid}" \
  -H "accept: application/json"

curl -X "PATCH" \
  "${kattakke_host}/api/v0/books/${bookid}" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
  "isbn": "123412341237",
  "title": "自然科学実験2023",
  "author": "北海道大学",
  "imagePath": "http://example.com/example.png"
}'

curl -X "GET" \
  "${kattakke_host}/api/v0/books/${bookid}"\
  -H "accept: application/json"

curl -X "GET" \
  "${kattakke_host}/api/v0/users/${userId}/shelf?title=asdf&tag=asdf&isbn=asdf" \
  -H "accept: application/json"