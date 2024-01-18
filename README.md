# Server PyWhats 

## V1

### Objectifs de cas d'utilisation
- recevoir des messages
    - acquitter la réception

- Authentifier un utilisateur
- Authentifier les messages reçus

### Remarques

identifier un message : concatenation nom utilisateur + timestamp
 --------------  -------------- -------------- 
| message_type |    content   |  identifier  ||
 --------------  -------------- --------------
## V2 

### Objectifs

- Créer une conversation entre deux utilisateurs 
    - Créer un thread pour traiter chaque message reçu sans bloquer le serveur
- Créer un compte dans la BD

### Remarques
