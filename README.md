# Discord VPS Creator (Admin-only)

This is a fork/scaffold inspired by PowerEdgeR710/discord-vps-creator but configured to be admin-only.

## Features
- Slash commands restricted to administrators / whitelist
- Commands implemented (stubs):
  - `/create`
  - `/node`
  - `/deploy` (admin only)
  - `/sendvps`
  - `/regen-ssh`
  - `/stop`
  - `/start`
  - `/restart`
  - `/resources`
  - `/sharedipv4`
  - `/tunnel`

## Quick start
1. Copy `.env.example` to `.env` and fill values.
2. Build Docker image:
   ```bash
   docker build -t discord-vps-bot -f Dockerfile1 .
