# Server PyWhats 

## V1

### Objectifs de cas d'utilisation
- recevoir des messages
    - voir le message sur le serveur V
    - acquitter la réception

- Authentifier un utilisateur V
- Authentifier les messages reçus

### Remarques

identifier un message : concatenation nom utilisateur + timestamp
 --------------  -------------- -------------- -------------- 
| message_type |    content   |  identifier  ||    token     |
 --------------  -------------- -------------- --------------
#### Message d'authentification 
 -----------  --------------------------------------- -------------- -------------
| "connect" |   {"username" : "", "password", ""}   |  identifier  ||  token      |
 -----------  --------------------------------------- -------------- -------------



#
## V2 

### Objectifs

- Créer une conversation entre deux utilisateurs 
    - Créer un thread pour traiter chaque message reçu sans bloquer le serveur
- Créer un compte dans la BD

### Remarques
