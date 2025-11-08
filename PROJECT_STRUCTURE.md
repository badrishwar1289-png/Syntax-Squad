# EchoMind Project Structure

## 📁 Complete File Structure

```
EchoMind/
├── app/                          # Next.js App Router
│   ├── globals.css              # Global styles, animations, custom scrollbar
│   ├── layout.tsx               # Root layout with metadata
│   └── page.tsx                 # Main page with tab navigation
│
├── components/                   # React Components (Modular Structure)
│   ├── Navigation/
│   │   └── Navigation.tsx       # Main navigation with animated tabs
│   │
│   ├── ConversationalJournal/   # Module 1: Conversational Journal
│   │   ├── ConversationalJournal.tsx  # Main journal container
│   │   ├── ChatInterface.tsx          # Text input with emoji support
│   │   ├── VoiceInput.tsx             # Voice recording interface
│   │   ├── MessageList.tsx            # Message display with animations
│   │   ├── MessageBubble.tsx          # Individual message component
│   │   └── EmotionBadge.tsx           # Emotion indicator badge
│   │
│   ├── MoodDashboard/           # Module 2: Mood Dashboard
│   │   ├── MoodDashboard.tsx          # Main dashboard container
│   │   ├── MoodChart.tsx              # Area chart for mood trends
│   │   ├── EmotionHeatmap.tsx         # Bar chart for emotion distribution
│   │   ├── MoodCalendar.tsx           # Calendar view with mood indicators
│   │   └── MoodInsights.tsx           # AI-generated insights component
│   │
│   └── EmotionAnalysis/         # Module 3: Emotion Analysis
│       ├── EmotionAnalysis.tsx        # Main analysis container
│       ├── EmotionDetector.tsx        # Text emotion detection
│       ├── VocalAnalysis.tsx          # Voice biomarker analysis
│       └── EmotionBreakdown.tsx       # Detailed emotion breakdown
│
├── types/                        # TypeScript Type Definitions
│   ├── emotion.ts               # Emotion types and interfaces
│   └── speech.d.ts              # Web Speech API type definitions
│
├── utils/                        # Utility Functions
│   ├── emotionDetection.ts      # Emotion detection algorithms
│   └── aiService.ts             # AI response generation
│
├── Configuration Files
│   ├── package.json             # Dependencies and scripts
│   ├── tsconfig.json            # TypeScript configuration
│   ├── tailwind.config.js       # Tailwind CSS configuration
│   ├── next.config.js           # Next.js configuration
│   ├── postcss.config.js        # PostCSS configuration
│   └── .gitignore               # Git ignore patterns
│
└── Documentation
    ├── README.md                # Comprehensive documentation
    ├── QUICKSTART.md            # Quick start guide
    └── PROJECT_STRUCTURE.md     # This file
```

## 🎯 Module Breakdown

### 1. Conversational Journal Module
**Purpose**: Provide a safe space for users to express emotions through text or voice.

**Files**:
- `ConversationalJournal.tsx`: Main container managing state and message flow
- `ChatInterface.tsx`: Text input with send functionality
- `VoiceInput.tsx`: Voice recording using Web Speech API
- `MessageList.tsx`: Displays conversation with animations
- `MessageBubble.tsx`: Individual message with emotion badges
- `EmotionBadge.tsx`: Visual emotion indicators

**Key Features**:
- Real-time emotion detection
- Voice and text input
- Animated message bubbles
- Emotion tagging

### 2. Mood Dashboard Module
**Purpose**: Visualize emotional patterns and provide insights.

**Files**:
- `MoodDashboard.tsx`: Main container with time period filtering
- `MoodChart.tsx`: Area chart showing mood trends over time
- `EmotionHeatmap.tsx`: Bar chart showing emotion distribution
- `MoodCalendar.tsx`: Calendar view with color-coded moods
- `MoodInsights.tsx`: AI-generated personalized insights

**Key Features**:
- Interactive charts (Recharts)
- Time period filtering (7d, 30d, 90d)
- Pattern recognition
- Personalized insights

### 3. Emotion Analysis Module
**Purpose**: Deep analysis of emotions from text and voice.

**Files**:
- `EmotionAnalysis.tsx`: Main container for analysis tools
- `EmotionDetector.tsx`: Text-based emotion detection
- `VocalAnalysis.tsx`: Voice biomarker analysis (pitch, pace, tone)
- `EmotionBreakdown.tsx`: Detailed visualization with pie charts

**Key Features**:
- Nuanced emotion detection (6 emotions)
- Vocal biomarker analysis
- Detailed emotion breakdown
- Confidence scoring

## 🛠️ Utility Files

### `utils/emotionDetection.ts`
- `detectEmotions()`: Analyzes text for emotional content
- `analyzeVocalBiomarkers()`: Processes voice characteristics

### `utils/aiService.ts`
- `generateAIResponse()`: Generates empathetic AI responses
- Context-aware responses based on emotions
- Conversation history integration

## 🎨 Styling & Animations

### `app/globals.css`
- Tailwind CSS base styles
- Custom animations (float, gradient)
- Custom scrollbar styling

### `tailwind.config.js`
- Emotion color palette
- Custom animation keyframes
- Extended theme configuration

## 📊 Data Flow

1. **User Input** → `ChatInterface` or `VoiceInput`
2. **Emotion Detection** → `emotionDetection.ts`
3. **AI Response** → `aiService.ts`
4. **Message Storage** → Local state → LocalStorage
5. **Dashboard Visualization** → Load from LocalStorage → Charts
6. **Analysis** → Real-time processing → Visual breakdown

## 🔄 State Management

- **Local State**: React hooks (useState, useRef)
- **Persistence**: LocalStorage for mood entries
- **Real-time**: Component-level state for conversations

## 🚀 Key Technologies

- **Next.js 14**: App Router, Server Components
- **TypeScript**: Type safety
- **Tailwind CSS**: Utility-first styling
- **Framer Motion**: Smooth animations
- **Recharts**: Data visualization
- **Lucide React**: Icon library
- **date-fns**: Date manipulation

## 📝 Notes

- All components are client-side (`'use client'`)
- Voice input requires browser support (Chrome, Edge, Safari)
- Emotion detection uses keyword-based algorithm (can be replaced with ML models)
- AI responses are simulated (can integrate with LLM APIs)
- Data persists in LocalStorage (can be migrated to database)

## 🔮 Extension Points

1. **LLM Integration**: Replace `aiService.ts` with actual API calls
2. **Database**: Replace LocalStorage with database
3. **Authentication**: Add user accounts
4. **Mobile App**: Create React Native version
5. **Advanced ML**: Integrate fine-tuned emotion models
6. **TTS**: Add text-to-speech for AI responses

