# 🇮🇳 YatraBot - Indian Travel Assistant

A beautiful, intelligent chatbot designed to help travelers explore India with comprehensive information about destinations, culture, food, and travel tips.

![YatraBot Demo](https://img.shields.io/badge/YatraBot-Indian%20Travel%20Assistant-blue?style=for-the-badge&logo=python)

## ✨ Features

- 🏛️ **Comprehensive Indian Tourism Knowledge**: Detailed information about major Indian cities and tourist destinations
- 🏖️ **Travel Planning Assistance**: Hotels, airports, railway stations, and bus terminals information
- 🏔️ **Cultural Insights**: Food, festivals, and cultural experiences across India
- 🕌 **Booking Guidance**: Recommendations for travel booking platforms
- 💬 **Interactive Chat Interface**: Modern, responsive web interface
- 🎨 **Beautiful UI**: Dark theme with Indian flag and tourism symbols
- ⚡ **Fast & Lightweight**: No external dependencies, runs locally

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/yatrabot.git
   cd yatrabot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 📋 Requirements

The project uses minimal dependencies:

- **Flask**: Web framework for the chat interface
- **Python 3.7+**: Modern Python features and type hints

## 🎯 What You Can Ask

### Destinations
- "Tell me about Taj Mahal"
- "What to do in Goa?"
- "Kerala tourism information"
- "Rajasthan travel guide"

### Travel Planning
- "Hotels in Delhi"
- "Airports in Mumbai"
- "Railway stations in Bangalore"
- "Bus terminals in Chennai"

### Culture & Food
- "Indian food recommendations"
- "Festivals in India"
- "Best time to visit India"

### General
- "Help" - Get a list of available features
- "Time" - Current time
- "Date" - Current date

## 🏗️ Project Structure

```
yatrabot/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── Dockerfile         # Docker configuration
└── .gitignore         # Git ignore rules
```

## 🐳 Docker Deployment

### Build and run with Docker

```bash
# Build the Docker image
docker build -t yatrabot .

# Run the container
docker run -p 5000:5000 yatrabot
```

### Using Docker Compose

```bash
# Run with docker-compose
docker-compose up -d
```

## 🌐 Deployment Options

### Local Development
```bash
python app.py
```

### Production (Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Cloud Platforms
- **Heroku**: Add `Procfile` with `web: gunicorn app:app`
- **Railway**: Direct deployment from GitHub
- **Render**: Connect repository and deploy
- **Vercel**: Python runtime support

## 🎨 Customization

### Adding New Destinations
Edit the `generate_bot_reply()` function in `app.py` to add more Indian cities and tourist spots.

### Modifying UI
The HTML template and CSS styles are embedded in the `index()` function. Customize colors, layout, and styling as needed.

### Extending Features
- Add weather API integration
- Include image galleries for destinations
- Add booking links
- Implement user authentication

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git checkout -b feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Ideas
- Add more Indian destinations
- Improve response accuracy
- Add multilingual support
- Enhance UI/UX
- Add more travel categories

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Indian tourism information sources
- Flask web framework
- Emoji support for visual elements
- Open source community

## 📞 Support

If you have any questions or need help:

- Create an [Issue](https://github.com/yourusername/yatrabot/issues)
- Star the repository if you find it useful
- Share with fellow travelers!

## 🔄 Updates

Stay updated with the latest features and improvements by:
- Watching the repository
- Following releases
- Checking the changelog

---

**Made with ❤️ for Indian Tourism**

*YatraBot - Your Gateway to Incredible India* 🇮🇳

