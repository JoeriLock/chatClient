Om het programma te testen start je als eerst de Server op in een terminal window

`python3 server.py`

Deze print vervolgens 3 waards
```
priv:6031
pub:1507
mod:6557
```
De `pub` en `mod` moeten mee geven worden aan de client

Draai in een andere terminal:

`python3 client.py 1507 6557` (`pub` `mod`)

Je kan de client ook aanroepen zonder parameters, in did geval zal de client aan de server om de `pub` key en `mod` vragen.

## Werking
Na het opzetten van de verbinding kan de er in de client terminal getyped worden. Als er enter wordt gedrukt veranderd de text in encrypted decimalen waarden (te zien in de terminal) en worden naar de server gestuurd.
De server decrypt de getallen met de private key en veranderd deze weer is ascii

## Configuratie
Boven aan `encryption.py` kan je `p` en `q` wijzigen naar twee andere priem getallen naar keuzen.

In `client.py` & `server.py` kan je de port en ip wijzigen. De basis instelling moeten werken voor local host 
