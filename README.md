# Prédiction d'Adresses de Contrats

Les adresses de contrat sont déterministes et sont calculées en utilisant `keccak256(adresse, nonce)`, où :
- `adresse` est l'adresse du contrat (ou l'adresse Ethereum qui a créé la transaction),
- `nonce` est le nombre de contrats que le contrat source a créé (ou le nonce de la transaction, pour les transactions régulières).

Grâce à cela, il est possible d'envoyer de l'ether à une adresse prédéterminée (qui n'a pas de clé privée) et de créer plus tard un contrat à cette adresse qui récupère l'ether. C'est une manière non intuitive et quelque peu secrète de stocker (dangereusement) de l'ether sans détenir de clé privée.

## Script de Prédiction

Dans ce dépôt, je vous ai écrit un script qui montre la prochaine adresse de Smart Contract que vous déploierez.

Vous avez seulement besoin de changer les variables suivantes :
- `creator_address = "0xYourAddress"` par votre adresse,
- `nonce = 6` par votre `nonce + 1`. Vous pouvez voir votre nonce actuel en cliquant sur votre dernière transaction sur MetaMask, où il sera indiqué.
