# Wildborn – Releases

Downloads for **Wildborn**, a cozy 2D pixel-art survival game for Windows (in development).
This repository only holds published builds and update information. The game's source code
lives in a separate, private repository.

## Install

1. Open [Releases](https://github.com/AuroraSkylines/Wildborn-Releases/releases/latest) and download
   `Wildborn-<version>-Setup.exe`.
2. Run it. It installs for your Windows user (no administrator rights needed) to
   `%LOCALAPPDATA%\Programs\Wildborn` and creates a Start menu shortcut (desktop shortcut optional).
3. Start **Wildborn** from the shortcut. It opens the Wildborn Launcher, which checks for updates
   and starts the game.

The installer is not code-signed yet, so Windows SmartScreen may show a warning
("More info" → "Run anyway").

## Updates

The launcher checks this repository for a newer version each time it starts (you can switch that
off) and shows what changed. Updates are verified with SHA-256 before anything is replaced; if a
download or installation fails, your installed version stays as it was.

No GitHub account is needed: release downloads from this public repository are anonymous.

**Your saves and settings** are stored in `%APPDATA%\Wildborn`. Updates, reinstalling and
uninstalling never delete them (the uninstaller only removes them if you explicitly say so).

**Steam:** the Steam version of Wildborn is updated by Steam. The launcher from this repository is
not used there and never changes a Steam installation.

## Files in each release

| File | Purpose |
| --- | --- |
| `Wildborn-<version>-Setup.exe` | Installer for new installs (also repairs an install) |
| `Wildborn-<version>-win64.zip` | Game package that the launcher downloads for updates |
| `latest.json` | Update manifest: version, change notes, download URLs, sizes, SHA-256 |
| `latest.json.sig` | Signature of `latest.json` (when release signing is enabled) |
| `SHA256SUMS.txt` | Checksums of all files |

Stable versions are normal releases. Beta versions are marked as pre-releases and only reach
players who enabled "Include beta versions" in the launcher.

## For maintainers

Releases are built by the `Release` workflow of the game repository and arrive here as **drafts**.
A draft is invisible to players and to the launcher. Review it, then click **Publish release**.
Publishing runs `verify-release.yml` here, which downloads the published files anonymously and
checks them against `latest.json`. Never edit or replace files of a published release; publish a
new version instead. Details: `docs/RELEASES_AND_UPDATES.md` in the game repository.
