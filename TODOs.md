# TODOS:

- es muss ein Token übergeben werden, der diesen Teil autorisiert, wenn dieser nicht stimmt wird der teil nicht gecallt -> redirect zur db json call route

- neue Method erstellen die du Uhrzeit checkt und den Programm teil um0:01 triggert ODER wenn es viele ids in der DB gibt, jede Stunde denprogrammteil mit einer anderen ID triggert (for loop durch die IDs) ->wenn Prozess fertig: Email an Nutzer.

- Nutzer kann sich sein INV in einem PDF doc runterladen (Items             werdenaufgeführt: `mengex Itemname`, am Ende steht der Heutige          Cashoutbetrag, welcher auch auf den Startbildschirm des Nutzer (bei         loginstehen soll)) -> Aufbau wie bei einer Rechnung (FF; Unterschrift       alsjoke am Ende)

- Advanced Function: item per Steam api verkaufen über eigenen APItoken, bei login muss der USer seinen eigenen Api token angeben: wennlogin -> Programm benutzt diesen Api token!

- Todays cashout mit lowest_price berechnen

- Währung ändern über body request

### PDF layout
                                        Datum
Hello -Name-
- Menge x Name   Preis

- Your Today cashout-TOTAL VALUE-                           
                                        Unterschrift    