export token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InZpc2hhbCIsImV4cCI6MTU5NDE0NDA0MywiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTU5MzcxMjA0M30.HkFF_bJ2nwYboiNhovl1qrry2PPEs5JR52hPgGXzm2I"

echo "Service will only work for 7 days due to exceed number of rows than assigned quota i.e 127,234/10,000"
echo
echo 

# Get bank details with given ifsc
echo
echo
echo "**********Bank details for ifsc=ABHY0065050*************"
echo

curl -X GET \
  https://bankifsccoderestapi.herokuapp.com/api/bank/ABHY0065015/ \
  -H "Authorization: TOKEN $token" \



# Get bank details with given name and city
echo
echo
echo "************ All the banks details for name='ALLAHABAD BANK' and city='DELHI' with limit=4 and offset=3 ******"
echo

curl -X GET \
  'https://bankifsccoderestapi.herokuapp.com/api/bank?name=ALLAHABAD%20BANK&city=DELHI&limit=4&offset=3' \
  -H "Authorization: TOKEN $token" \
  
echo

# Get all the bank details 

echo "********* All the banks details limit=4 and offset=3 ****************"
echo

curl -X GET \
  'https://bankifsccoderestapi.herokuapp.com/api/bank/?limit=4&offset=3' \
  -H "Authorization: TOKEN $token" \
