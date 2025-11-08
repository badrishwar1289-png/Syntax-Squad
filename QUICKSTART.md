# Quick Start Guide - EchoMind

## 🚀 Installation & Setup

### Step 1: Install Frontend Dependencies
```bash
npm install
```

### Step 2: Install Python Backend Dependencies
```bash
cd server
pip install -r requirements.txt
cd ..
```

### Step 3: Start Python Backend (Terminal 1)
```bash
cd server
python run.py
```
Backend will run on `http://localhost:5000`

### Step 4: Start Next.js Frontend (Terminal 2)
```bash
npm run dev
```

### Step 5: Open in Browser
Navigate to: `http://localhost:3000`

> **Note**: The app works without the Python backend, but the backend provides enhanced features.

## 📱 Using EchoMind

### Journal Tab
1. **Text Input**: Type your thoughts and feelings
2. **Voice Input**: Click "Record Voice Message" to speak
3. **AI Response**: Receive empathetic, context-aware responses
4. **Emotion Tags**: See detected emotions in your messages

### Dashboard Tab
1. **Select Time Period**: Choose 7d, 30d, or 90d view
2. **View Mood Trends**: See your emotional patterns over time
3. **Explore Insights**: Read personalized insights about your mood patterns
4. **Calendar View**: Check daily mood patterns in calendar format

### Analysis Tab
1. **Text Analysis**: Enter text to analyze emotions
2. **Vocal Analysis**: Record voice sample for biomarker analysis
3. **View Breakdown**: See detailed emotion breakdown with charts

## 🎨 Features Overview

### ✨ Beautiful Animations
- Smooth page transitions
- Animated message bubbles
- Floating elements
- Loading animations

### 🧠 Emotion Detection
- 6 emotion types: Joy, Sadness, Anger, Fear, Anxiety, Optimism
- Real-time emotion analysis
- Confidence scoring
- Intensity tracking

### 📊 Visualizations
- Interactive mood charts
- Emotion heatmaps
- Calendar views
- Pie charts for emotion breakdown

## 🔧 Troubleshooting

### Voice Input Not Working?
- Use Chrome or Edge browser
- Allow microphone permissions
- Requires HTTPS in production

### Charts Not Showing?
- Clear browser cache
- Check console for errors
- Ensure all dependencies are installed

### Build Issues?
```bash
# Clean install
rm -rf node_modules .next
npm install
npm run dev
```

## 💡 Tips

1. **Regular Journaling**: Use the journal daily for best insights
2. **Voice vs Text**: Try both input methods for different experiences
3. **Check Dashboard**: Review your mood patterns weekly
4. **Explore Insights**: Read AI-generated insights for self-awareness

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Customize colors in `tailwind.config.js`
- Integrate with external LLM APIs for production use
- Add more emotion detection algorithms

## 🆘 Need Help?

- Check the README for detailed information
- Review component files for implementation details
- Open an issue on GitHub for bugs or questions

Happy journaling! 🌟

