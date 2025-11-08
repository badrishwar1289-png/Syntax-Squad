# EchoMind - Your AI-Powered Emotional Co-Pilot

## Overview

EchoMind is an empathetic AI companion that helps users reflect on their feelings, track mood patterns, and receive supportive, context-aware responses. The project combines a Next.js frontend (TypeScript + Tailwind) with a small Python backend (Flask) that provides emotion analysis and a lightweight "mini-LM" service which can use remote providers (DeepSeek,OpenAI) or a local template-based fallback.

Key goals: privacy-first local-first UX, multimodal input (text + voice), and extensible AI backends for production integration.

![EchoMind](https://img.shields.io/badge/EchoMind-AI%20Emotional%20Co--Pilot-blue)
![Next.js](https://img.shields.io/badge/Next.js-14-black)
![TypeScript](https://img.shields.io/badge/TypeScript-5.3-blue)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.3-38bdf8)

EchoMind is an intelligent and empathetic AI companion designed to be more than just a chatbot. It's an emotional co-pilot that actively listens, helps users understand their emotional patterns, and provides a personalized toolkit for mental well-being.

## 🌟 Features

### 1. Conversational Journal
- **Clean, Calming UI**: A private, safe space for emotional expression
- **Dynamic AI Responses**: Context-aware, empathetic dialogue that adapts to user tone
- **Multi-Modal Expression**: Support for both text and voice input
- **Real-time Emotion Detection**: Automatic emotion analysis from conversations

### 2. Deep Emotion Analysis Engine
- **Nuanced Emotion Detection**: Identifies joy, sadness, anger, fear, anxiety, and optimism
- **Vocal Biomarkers**: Analyzes pitch, pace, and tone from voice inputs
- **Emotion Intensity Tracking**: Quantifies emotional states with confidence scores
- **Pattern Recognition**: Identifies emotional trends and patterns

### 3. Dynamic Mood Dashboard
- **Interactive Visualizations**: Beautiful charts and graphs for mood trends
- **Emotion Heatmap**: Visual representation of emotion distribution
- **Mood Calendar**: Calendar view showing daily mood patterns
- **Personalized Insights**: AI-generated insights based on emotional patterns
- **Pattern Discovery**: Identifies correlations (e.g., "Your stress levels tend to spike on Wednesdays")

## 🚀 Getting Started

### Prerequisites

- **Node.js 18+** installed
- **Python 3.8+** installed
- **npm or yarn** package manager
- **pip** (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

#### Step 1: Clone the repository
```bash
git clone <repository-url>
cd EchoMind
```

#### Step 2: Install Frontend Dependencies
```bash
npm install
# or
yarn install
```

#### Step 3: Install Python Backend Dependencies
```bash
cd server
pip install -r requirements.txt
# or
python -m pip install -r requirements.txt
```

#### Step 4: Set up Environment Variables (Optional)
Create a `.env.local` file in the root directory:
```env
NEXT_PUBLIC_API_URL=http://localhost:5000
```

#### Step 5: Run the Application

**Terminal 1 - Start Python Backend:**
```bash
cd server
python run.py
# or
python app.py
```

The Python API server will start on `http://localhost:5000`

**Terminal 2 - Start Next.js Frontend:**
```bash
npm run dev
# or
yarn dev
```

The frontend will start on `http://localhost:3000`

#### Step 6: Open your browser
Navigate to [http://localhost:3000](http://localhost:3000)

> **Note**: The application works without the Python backend using local fallback functions. However, the Python backend provides enhanced emotion detection and AI responses.

## 📁 Project Structure

```
EchoMind/
├── app/
│   ├── globals.css          # Global styles and animations
│   ├── layout.tsx           # Root layout component
│   └── page.tsx             # Main page with tab navigation
├── components/
│   ├── Navigation/
│   │   └── Navigation.tsx   # Main navigation component
│   ├── ConversationalJournal/
│   │   ├── ConversationalJournal.tsx  # Main journal component
│   │   ├── ChatInterface.tsx          # Text input interface
│   │   ├── VoiceInput.tsx             # Voice recording interface
│   │   ├── MessageList.tsx            # Message display list
│   │   ├── MessageBubble.tsx          # Individual message component
│   │   └── EmotionBadge.tsx           # Emotion indicator badge
│   ├── MoodDashboard/
│   │   ├── MoodDashboard.tsx          # Main dashboard component
│   │   ├── MoodChart.tsx              # Line/area chart for mood trends
│   │   ├── EmotionHeatmap.tsx         # Emotion distribution chart
│   │   ├── MoodCalendar.tsx           # Calendar view of moods
│   │   └── MoodInsights.tsx           # Personalized insights component
│   └── EmotionAnalysis/
│       ├── EmotionAnalysis.tsx        # Main analysis component
│       ├── EmotionDetector.tsx        # Text emotion detection
│       ├── VocalAnalysis.tsx          # Voice biomarker analysis
│       └── EmotionBreakdown.tsx       # Detailed emotion breakdown
├── server/                   # Python Backend
│   ├── app.py               # Flask API server
│   ├── run.py               # Server entry point
│   ├── requirements.txt     # Python dependencies
│   └── .gitignore           # Python gitignore
├── types/
│   ├── emotion.ts            # TypeScript type definitions
│   └── speech.d.ts           # Web Speech API types
├── utils/
│   ├── emotionDetection.ts   # Emotion detection (with backend integration)
│   └── aiService.ts          # AI response generation (with backend integration)
├── package.json              # Frontend dependencies
├── tsconfig.json             # TypeScript configuration
├── tailwind.config.js        # Tailwind CSS configuration
└── README.md                 # This file
```

## 🎨 Key Components Explained

### ConversationalJournal
The main journal interface where users interact with the AI. It includes:
- **ChatInterface**: Text input with emoji support
- **VoiceInput**: Voice recording with Web Speech API
- **MessageList**: Displays conversation history with animations
- **MessageBubble**: Individual message bubbles with emotion badges

### MoodDashboard
Comprehensive dashboard for viewing emotional patterns:
- **MoodChart**: Visualizes mood trends over time using Recharts
- **EmotionHeatmap**: Bar chart showing emotion distribution
- **MoodCalendar**: Interactive calendar with color-coded moods
- **MoodInsights**: AI-generated insights and pattern recognition

### EmotionAnalysis
Deep analysis tools for understanding emotions:
- **EmotionDetector**: Analyzes text input for emotional content
- **VocalAnalysis**: Processes voice recordings for vocal biomarkers
- **EmotionBreakdown**: Detailed breakdown with pie charts and insights

## 🔧 Configuration

### Environment Variables

Create a `.env.local` file in the root directory:

```env
# Python Backend URL (default: http://localhost:5000)
NEXT_PUBLIC_API_URL=http://localhost:5000

# Optional: For production LLM integration
NEXT_PUBLIC_LLM_API_KEY=your_api_key_here
```

### Python Backend Configuration

The Python backend runs on `http://localhost:5000` by default. To change the port, edit `server/app.py`:

```python
app.run(debug=True, port=5000, host='0.0.0.0')
```

### API Endpoints

The Python backend provides the following endpoints:

- `GET /api/health` - Health check endpoint
- `POST /api/analyze-emotions` - Analyze emotions from text
- `POST /api/generate-response` - Generate AI response
- `POST /api/analyze-voice` - Analyze vocal biomarkers

**Example API Request:**
```bash
curl -X POST http://localhost:5000/api/analyze-emotions \
  -H "Content-Type: application/json" \
  -d '{"text": "I feel happy today!"}'
```

### Backend Fallback

The application automatically falls back to local JavaScript implementations if the Python backend is unavailable. This ensures the app works even without the backend running.

### Customization

#### Colors
Edit `tailwind.config.js` to customize the color scheme:
```javascript
emotion: {
  joy: '#fbbf24',
  sadness: '#3b82f6',
  // ... customize colors
}
```

#### Animations
Modify animations in `app/globals.css`:
```css
@keyframes float {
  /* Customize animation */
}
```

## 🎯 Usage Guide

### Starting a Conversation

1. Navigate to the **Journal** tab
2. Type your message in the text input or click "Record Voice Message"
3. The AI will analyze your emotions and respond empathetically
4. Continue the conversation to build context

### Viewing Mood Dashboard

1. Navigate to the **Dashboard** tab
2. Select a time period (7d, 30d, 90d)
3. Explore:
   - Mood trends over time
   - Emotion distribution
   - Calendar view of moods
   - Personalized insights

### Emotion Analysis

1. Navigate to the **Analysis** tab
2. **Text Analysis**: Enter text to analyze emotions
3. **Vocal Analysis**: Record a voice sample for biomarker analysis
4. View detailed breakdowns and insights

## 🛠️ Technology Stack

### Frontend
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Animations**: Framer Motion
- **Charts**: Recharts
- **Icons**: Lucide React
- **Date Handling**: date-fns

### Backend
- **Framework**: Flask (Python)
- **CORS**: flask-cors
- **API**: RESTful API with JSON responses
- **Port**: 5000 (default)

## 🚀 Building for Production

### Frontend
```bash
# Build the application
npm run build

# Start production server
npm start
```

### Backend
```bash
# Install production dependencies
cd server
pip install -r requirements.txt

# Run with production server (e.g., Gunicorn)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Or use Flask's built-in server (development only)
python app.py
```

### Docker (Optional)
Create a `Dockerfile` for containerized deployment:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY server/requirements.txt .
RUN pip install -r requirements.txt
COPY server/ .
CMD ["python", "app.py"]
```

## 🔮 Future Enhancements

### Planned Features
- **Proactive Check-ins**: AI-initiated conversations based on mood trends
- **Long-term Memory**: Context awareness across sessions
- **Emotionally-Aware TTS**: Voice responses matching empathetic tone
- **Export Data**: Export mood data for external analysis
- **Mobile App**: Native mobile application
- **Integration with Health Apps**: Sync with Apple Health, Google Fit

### Advanced AI Integration
- Replace simulated AI with actual LLM API (OpenAI, Anthropic, etc.)
- Fine-tune models on emotional datasets
- Implement RAG (Retrieval-Augmented Generation) for context

## 🐛 Troubleshooting

### Python Backend Not Starting
- Ensure Python 3.8+ is installed: `python --version`
- Install dependencies: `pip install -r server/requirements.txt`
- Check if port 5000 is available: `netstat -an | findstr 5000` (Windows) or `lsof -i :5000` (Mac/Linux)
- Try a different port if 5000 is occupied

### Backend Connection Issues
- Verify backend is running: `curl http://localhost:5000/api/health`
- Check CORS settings in `server/app.py`
- Ensure `NEXT_PUBLIC_API_URL` matches backend URL
- Application will use local fallback if backend is unavailable

### Voice Input Not Working
- Ensure you're using a modern browser (Chrome, Edge, Safari)
- Check browser permissions for microphone access
- Some browsers require HTTPS for voice recognition

### Charts Not Displaying
- Clear browser cache
- Check console for errors
- Ensure Recharts is properly installed

### Build Errors
- Delete `node_modules` and `.next` folders
- Run `npm install` again
- Check Node.js version (should be 18+)
- Check Python version (should be 3.8+)

### Port Already in Use
- Change Python backend port in `server/app.py`
- Update `NEXT_PUBLIC_API_URL` in `.env.local`
- Or stop the process using the port

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- Inspired by the need for accessible mental health tools
- Built with empathy and care for user privacy
- Uses modern web technologies for best user experience

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Remember**: EchoMind is a tool to support your emotional well-being, but it's not a replacement for professional mental health care. If you're experiencing a mental health crisis, please contact a healthcare professional or emergency services.

**Take care of yourself. You matter. ❤️**

