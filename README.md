# RProxy2

# Introduction

A simple magisk module to achive local reverse proxy,so you can accsess discord&steamcommunity etc.It use [caddy2](https://github.com/caddyserver/caddy/releases) as a local reverse proxy  transfer data to specified server

### Requirements
* [TrustmeAlready](https://github.com/ViRb3/TrustMeAlready)

## Install

This module is still on developmentm,You can install by follow this steps

**make sure you have installed** **[edxposed](disable SSL verification) and [magisk](https://github.com/topjohnwu/Magisk/releases)**

1.install [TrustmeAlready](https://github.com/ViRb3/TrustMeAlready)  to disable SSL verification 

2.flash this mod via magisk

3.add follow hosts to `/system/etc/hosts`

```
223.119.248.19 steamuserimages-a.akamaihd.net #UHE_
223.119.248.19 steamcdn-a.akamaihd.net #UHE_
223.119.248.19 steamstore-a.akamaihd.net #UHE_
223.119.248.19 steamcommunity-a.akamaihd.net #UHE_
223.119.248.19 steampipe.akamaized.net #UHE_
223.119.248.19 eaassets-a.akamaihd.net #UHE_
223.119.248.19 humblebundle-a.akamaihd.net #UHE_
223.119.248.19 steamcommunity-a.akamaihd.net #UHE_
127.0.0.1 steamcommunity.com #S302
127.0.0.1 www.steamcommunity.com #S302
127.0.0.1 discordapp.com #S302
127.0.0.1 dl.discordapp.net #S302
127.0.0.1 status.discordapp.com #S302
127.0.0.1 cdn.discordapp.com #S302
127.0.0.1 media.discordapp.net #S302
127.0.0.1 images-ext-2.discordapp.net #S302
127.0.0.1 images-ext-1.discordapp.net #S302
127.0.0.1 support.discordapp.com #S302
127.0.0.1 url7195.discordapp.com #S302
127.0.0.1 www.google.com #S302
```

4.reboot

Normally you can access [steam](steamcommunity.com)now,for some roms you should add additional steps

```
cd /data/local/caddy2
./start.sh
```

## Credits

[Dogfight360](https://www.dogfight360.com/blog/):he's  steamcommunity 302 tool make this possible!

[magisk](https://github.com/topjohnwu/Magisk/releases):make this a module

[TrustmeAlready](https://github.com/ViRb3/TrustMeAlready):solve SSL verification 

[Caddy2](https://github.com/caddyserver/caddy/releases) :Best Server!!!

## Thanks

[@Royz](https://github.com/RoyZ-CSGO):for add additional featuresf