# 📢 MikesLaptopsAds

# Fully synchronized, time based digital signage system powered by GitHub Pages

# MikesLaptopsAds is a lightweight, zero maintenance, cloud hosted advertising display system designed for laptops on display.
# All devices instantly sync slide timing based on GitHub server time, ensuring every laptop shows the same image at the same moment.

This solves the biggest problem with local slideshow systems:
🎯 every machine stays perfectly aligned with no setup or local configuration.

# ✨ Features
# 🔄 Perfect Cross Device Synchronization

All devices fetch the GitHub server time and calculate slides based on that.
No internet time APIs, no CORS issues, no drift.

# 🖼️ Ultra Simple Image Management

Just drop PNG or JPG files into the ads folder:

ads/
   ad1.png
   ad2.png
   ad3.png


Your slideshow updates instantly when the repo is published.

# ⚡ Zero Software Installation Required

Runs in any modern browser:

Windows laptops

Desktop PCs

Tablets

Smart TVs with browser support

# 🌐 Hosted Entirely on GitHub Pages

No backend, no server maintenance, no costs.

# 📱 Responsively Scales to Any Screen

Images resize cleanly using CSS object fitting.

# 🟢 Live Sync Status Indicator

Shows whether the system is:

Synced

Syncing

Offline fallback

# 🚀 Live Demo

Open the deployed ad display:

👉 https://noahtollysmells.github.io/MikesLaptopsAds/

This link is used by all display machines.

You can also launch it using a .bat file in fullscreen mode on Windows.

# 📁 Project Structure
MikesLaptopsAds/
│  index.html
│  README.md
│
└── ads/
       ad1.png
       ad2.png
       ad3.png


The website code automatically cycles through all entries defined in index.html.

# 💻 How the Synchronization Works

GitHub Pages returns a universal timestamp in every response header:

Date: Tue, 21 Jan 2025 19:51:03 GMT


This timestamp is always:

Accurate

Universal

Identical for every device

Not blocked by CORS

Your script reads this header, compares it to local time, and computes:

serverTime minus localTime equal timeOffset


Every slide change is based on:

(timeNow plus timeOffset)


This ensures all devices show the same slide at the same second.

# 🧠 Core Logic Summary

Sync with GitHub server time using a HEAD request

Calculate the current slide based on a fixed interval

Automatically update once per second

Re sync every 60 seconds

Fall back to local time if offline

Stay aligned forever

# 🖥️ Using the System on Display Machines

Open the synced ad URL

Press F11 to fullscreen

Or run the provided BAT launcher:

@echo off

set "URL=https://noahtollysmells.github.io/MikesLaptopsAds/"

set "EDGE1=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
set "EDGE2=C:\Program Files\Microsoft\Edge\Application\msedge.exe"

if exist "%EDGE1%" (
    start "" "%EDGE1%" --start-fullscreen "%URL%"
    exit /b
)

if exist "%EDGE2%" (
    start "" "%EDGE2%" --start-fullscreen "%URL%"
    exit /b
)

start "" "%URL%"


This script opens the website in fullscreen mode on all Windows systems.

🔧 Customization
Change Slide Duration

Open index.html and edit:

const slideDurationMs = 10000;


Value is in milliseconds.

Add or Remove Ads

Add more files into /ads/ and update the array:

const images = [
  "ads/ad1.png",
  "ads/ad2.png",
  "ads/ad3.png"
];

Hide Sync Indicator

Tell me and I can provide an auto fade version.

Add Video Support

Also possible; just ask.

# ❤️ Credits

Built specifically for the Mike's Laptops showroom system to simplify advertising across multiple demo laptops.
