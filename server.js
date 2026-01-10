const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

// Store emergency broadcast message in memory
let emergencyMessage = null;
let emergencyActive = false;

// GET current emergency message
app.get('/api/emergency', (req, res) => {
  res.json({
    active: emergencyActive,
    message: emergencyMessage
  });
});

// POST new emergency message (sent by one device, broadcast to all)
app.post('/api/emergency', (req, res) => {
  const { message, active } = req.body;
  
  if (active && message && message.trim()) {
    emergencyMessage = message;
    emergencyActive = true;
    console.log('[' + new Date().toLocaleTimeString() + '] EMERGENCY BROADCAST ACTIVATED:', message);
  } else {
    emergencyMessage = null;
    emergencyActive = false;
    console.log('[' + new Date().toLocaleTimeString() + '] Emergency broadcast ended');
  }
  
  res.json({ 
    success: true, 
    active: emergencyActive, 
    message: emergencyMessage 
  });
});

// GET system status
app.get('/api/status', (req, res) => {
  res.json({
    serverTime: Date.now(),
    emergency: {
      active: emergencyActive,
      message: emergencyMessage
    }
  });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log('🚀 Emergency Broadcast Server running on http://localhost:' + PORT);
  console.log('📡 API endpoints:');
  console.log('  GET  /api/emergency - Get current emergency status');
  console.log('  POST /api/emergency - Set emergency broadcast');
  console.log('  GET  /api/status   - Get server status');
});
