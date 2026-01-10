# Firebase Instant Broadcast Setup

## Step 1: Create Firebase Project (2 minutes)
1. Go to https://console.firebase.google.com
2. Click "Add project" → Name it `MikesLaptopsAds`
3. Uncheck "Enable Google Analytics" → Create project
4. Wait for setup to complete

## Step 2: Enable Realtime Database
1. Left sidebar → "Realtime Database"
2. Click "Create Database"
3. Region: `us-central1` (default)
4. Security Rules: **Start in Test Mode** (for now)
5. Create

## Step 3: Get Your Config
1. Left sidebar → Project Settings (⚙️)
2. Copy these values:
   - **API Key** (under "Web API Key")
   - **Database URL** (format: `https://YOUR_PROJECT.firebaseio.com`)

## Step 4: Update index.html
In `index.html`, find this section:
```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  databaseURL: "https://YOUR_PROJECT.firebaseio.com"
};
```

Replace with your actual values:
```javascript
const firebaseConfig = {
  apiKey: "AIzaSyD...",  // Your API Key
  databaseURL: "https://mikes-laptops-ads.firebaseio.com"
};
```

## Step 5: Test Broadcast
1. Go to Firebase Console → Realtime Database
2. Click the "+" button and create new data:
   - Path: `broadcast`
   - Add child: `message` (object)
   - Add to message object:
     - `text` = "HELLO ALL DEVICES"
     - `color` = "#ff0000" (optional, for background color)

3. Refresh your pages - all 5 devices show the message **instantly**!

## How to Send Messages
From Firebase Console → Realtime Database:
- Edit `broadcast/message/text` to update message
- All devices see it in < 100ms

Or via simple web form (I can add this too).

## Security (Later)
Once tested, update security rules in Firebase Console → Rules:
```json
{
  "rules": {
    "broadcast": {
      ".read": true,
      ".write": false
    }
  }
}
```
This lets devices read, but prevents external writes.
