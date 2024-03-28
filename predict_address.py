from eth_utils import keccak, to_checksum_address, encode_hex

def rlp_encode(address, nonce):
    # Ceci est une implémentation simplifiée et pourrait avoir besoin d'être adaptée
    # pour gérer correctement l'encodage RLP en fonction des valeurs.
    # L'encodage RLP varie en fonction de la taille et du type de données.
    if nonce == 0:
        nonce = b'\x80'
    elif nonce < 0x80:
        nonce = nonce.to_bytes(1, byteorder='big')
    elif nonce <= 0xff:
        nonce = b'\x81' + nonce.to_bytes(1, byteorder='big')
    return b'\xd6' + b'\x94' + address + nonce

def predict_contract_address(creator_address, nonce):
    # Convertir l'adresse en bytes et retirer le préfixe "0x"
    address_bytes = bytes.fromhex(creator_address[2:])
    # RLP encode de l'adresse et du nonce
    rlp_encoded = rlp_encode(address_bytes, nonce)
    # Hachage keccak256 de l'encodage RLP
    contract_address_hash = keccak(rlp_encoded)
    # Prendre les 20 derniers octets et convertir en adresse Ethereum
    contract_address = to_checksum_address(contract_address_hash[-20:])
    return contract_address

# Exemple d'utilisation
creator_address = "0x6c5F31631fC7d98438a0124aeFF128620355b2ec"
nonce = 6  # Le nonce du compte créateur au moment de la création du contrat
predicted_address = predict_contract_address(creator_address, nonce)
print("L'adresse prévue du contrat est:", predicted_address)
