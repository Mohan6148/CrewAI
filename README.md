# Gemini AI Chat Application

A beautiful, modern web application that integrates with Google's Gemini API to provide intelligent chat responses. Built with Flask, HTML5, CSS3, and JavaScript.

## Features

- 🤖 **AI-Powered Chat**: Powered by Google's Gemini models
- 🎨 **Modern UI**: Beautiful, responsive design with gradient backgrounds and smooth animations
- 📱 **Mobile Responsive**: Works perfectly on desktop, tablet, and mobile devices
- ⚡ **Real-time Chat**: Instant responses with loading indicators
- 🔒 **Secure**: API key protection and input validation
- 📝 **Character Counter**: Real-time character count with visual feedback
- ⌨️ **Keyboard Shortcuts**: Enter to send, Shift+Enter for new lines
- 📋 **Copy to Clipboard**: Click on AI responses to copy them
- 🎯 **Error Handling**: User-friendly error messages and modal dialogs

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Google AI Studio API key**:
   - Add `GOOGLE_API_KEY=your_key_here` to `.env`
   - The app reads the key from environment variables at startup
   - If you hit a quota error, change `GEMINI_MODEL` in `.env` to another Gemini flash model

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Start chatting** with the AI!

## Project Structure

```
AI/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── css/
    │   └── style.css     # Styling and animations
    └── js/
        └── app.js        # JavaScript functionality
```

## API Configuration

The application uses Google's Gemini API with the following configuration:
- **Model**: `gemini/gemini-1.5-flash` by default
- **Temperature**: 0.3 (balanced creativity and accuracy)
- **Max Tokens**: 1000 per response

## Customization

### Changing the API Key
Set `GOOGLE_API_KEY` in `.env` or your system environment variables.

### Modifying the Model
Change the model string in `app.py` inside `build_gemini_llm()`.

### Styling
- Edit `static/css/style.css` to customize colors, fonts, and layout
- The design uses CSS custom properties for easy theming

### Functionality
- Modify `static/js/app.js` to add new features or change behavior
- Update `app.py` to add new API endpoints or modify the chat logic

## Keyboard Shortcuts

- **Enter**: Send message
- **Shift + Enter**: Add new line
- **Escape**: Close modal dialogs
- **Ctrl + /**: Focus on input field

## Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Security Notes

- API keys are included in the code for demonstration purposes
- For production deployment, use environment variables or secure key management
- Input validation is implemented to prevent malicious requests
- Rate limiting should be considered for production use

## Known Issues

### System Problems

1. **API Key Dependency**: 
   - The system requires a valid Perplexity API key to function
   - If the API key is missing or invalid, the LLM initialization fails silently
   - No graceful degradation when API is unavailable

2. **Memory Management**:
   - ConversationBufferMemory is initialized but not properly utilized across requests
   - Memory state is not persisted between application restarts
   - Potential memory leaks with long-running sessions

3. **Threading Issues**:
   - Global `crew_status` variable creates race conditions in multi-user scenarios
   - No thread safety mechanisms for concurrent requests
   - Background threads may not clean up properly on application shutdown

4. **Database Limitations**:
   - SQLite database (`crewai_history.db`) is not thread-safe for concurrent writes
   - No database connection pooling or proper connection management
   - Database file can become corrupted with concurrent access

5. **Error Handling**:
   - Limited error recovery mechanisms
   - Crew execution errors may leave the system in an inconsistent state
   - No retry logic for failed API calls

6. **Resource Management**:
   - No rate limiting for API calls
   - No timeout handling for long-running crew operations
   - Potential resource exhaustion with multiple concurrent crews

7. **Configuration Issues**:
   - Hard-coded configuration values mixed with environment variables
   - No validation of environment variable values
   - Missing fallback configurations

8. **Security Concerns**:
   - API key stored in environment variables without encryption
   - No input sanitization beyond basic validation
   - No authentication or authorization mechanisms

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your Google AI Studio API key is valid and `GOOGLE_API_KEY` is set correctly
2. **Quota Error**: If Gemini returns `429 RESOURCE_EXHAUSTED`, switch `GEMINI_MODEL` to another flash model or enable billing on the Google project
2. **Network Issues**: Check your internet connection and firewall settings
3. **Port Already in Use**: Change the port in `app.py` if port 5000 is occupied
4. **Database Locked**: Restart the application if you encounter SQLite locking errors
5. **Crew Stuck**: Use the reset endpoint or restart the application if crew execution hangs

### Debug Mode

The application runs in debug mode by default. To disable:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

## License

This project is open source and available under the MIT License.

---

**Enjoy chatting with AI! 🤖✨**