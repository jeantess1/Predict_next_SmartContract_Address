Contract addresses are deterministic and are calculated by keccak256(address, nonce) where the address is the address of the contract (or ethereum address that created the transaction) and nonce is the number of contracts the spawning contract has created (or the transaction nonce, for regular transactions).

Because of this, one can send ether to a pre-determined address (which has no private key) and later create a contract at that address which recovers the ether. This is a non-intuitive and somewhat secretive way to (dangerously) store ether without holding a private key.

In this repo I wrote you a script that show the next SmartContract Address that you will deploy.

You only need to change 
creator_address = "0xYourAddress"
nonce = 6 // By your nounce+1. You can see your actual nounce by clicking on your last transaction on Metamask it will be written. 
