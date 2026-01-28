# BTC-Jackpot-Hunter
💰 BTC Range Hunter: High-speed Python scanner for Bitcoin private keys. Checks Balance &amp; History (Active/Used) for Compressed/Uncompressed addresses. Features a premium Matrix UI, auto-save to found.txt, and anti-ban protection. Supports Hex/Dec ranges. Educational use only. 🚀
```bash
pip install bitcoinaddress requests rich fake-useragent
```
```bash
python CGT.py
```
The script marks a Private Key as "FOUND" if it detects ANY ONE of the following three conditions on the Blockchain:

Final Balance: The address currently holds Bitcoin (Money is available now).

Total Received: The address has received Bitcoin in the past (Even if the balance is currently 0).

Total Sent: The address has sent Bitcoin in the past (It has transaction history).

In short: It finds any address that is active or has ever been used, not just the ones that have money right now.


Created By: Sisu / CRYPTOGRAPHYTUBE
