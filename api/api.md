# Api Routes

## inventory routes
`/inventory` </br>
method: POST </br>
body: {"steamid":str, "update": bool} </br>
return: steam inv, json </br>

`/inventory/delete` </br>
method: POST </br>
body: {"steamid":str, "update": bool} </br>
return: success

`/inventory/history` </br>
method: POST </br>
body: {"steamid":str, "update": bool} </br>
return: inventory history

`/inventory/stats` </br>
method: POST </br>
body: {"steamid":str, "update": bool} </br>
return: inventory stats