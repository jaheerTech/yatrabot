from __future__ import annotations

from datetime import datetime
from typing import Dict

from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

def generate_bot_reply(user_message: str) -> str:
    """Return a simple, helpful reply for a given user message.

    The logic is intentionally lightweight and rule-based to keep the app self-contained.
    """
    if not user_message:
        return "I didn't catch that. Could you please type something?"

    normalized = user_message.strip().lower()

    greetings = {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"}
    farewells = {"bye", "goodbye", "see you", "see ya", "later"}

    if any(word in normalized for word in greetings):
        return "Hello! How can I help you today? I can tell you about Indian tourism, time, date, or just chat!"

    if any(word in normalized for word in farewells):
        return "Goodbye! If you need anything else, just say hi."

    if "your name" in normalized or normalized == "who are you" or normalized.startswith("who are you"):
        return "I'm a simple Python chatbot with knowledge about Indian tourism! Nice to meet you!"

    if "time" in normalized:
        now_str = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now_str}."

    if "date" in normalized or "day" in normalized:
        today_str = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today_str}."

    # Indian Tourism Responses - Check for specific places first
    if "taj mahal" in normalized or "agra" in normalized:
        return ("The Taj Mahal in Agra is one of the Seven Wonders of the World! "
               "Built by Emperor Shah Jahan in memory of his wife Mumtaz Mahal. "
               "Best time to visit: October to March. Don't miss the sunrise view! "
               "Top hotels: The Oberoi Amarvilas, ITC Mughal, Taj Hotel & Convention Centre. "
               "Airports: Agra Airport (AGR) - 12km from city center, Delhi Airport (DEL) - 200km. "
               "Railway: Agra Cantt Railway Station, Agra Fort Railway Station, Raja Ki Mandi. "
               "Bus: Agra ISBT, Idgah Bus Stand, Taj Depot. "
               "Book via: Booking.com, Agoda, or direct hotel websites.")
    
    if "goa" in normalized:
        return ("Goa is famous for its beautiful beaches, Portuguese architecture, and vibrant nightlife! "
               "Must-visit: Calangute Beach, Basilica of Bom Jesus, Fort Aguada. "
               "Best time: November to March (avoid monsoon). Try the seafood! "
               "Top hotels: Taj Exotica Resort & Spa, The Leela Goa, Park Hyatt Goa. "
               "Airports: Goa International Airport (GOI) - 29km from Panaji, Mumbai Airport (BOM) - 600km. "
               "Railway: Madgaon Junction, Vasco da Gama Railway Station, Thivim Railway Station. "
               "Bus: Kadamba Bus Terminal Panaji, Mapusa Bus Stand, Margao Bus Stand. "
               "Book via: Booking.com, Airbnb, or direct hotel websites.")
    
    if "kerala" in normalized or "god's own country" in normalized:
        return ("Kerala is called 'God's Own Country' for its backwaters, Ayurveda, and lush greenery! "
               "Highlights: Houseboat in Alleppey, tea gardens in Munnar, beaches in Kovalam. "
               "Best time: September to March. Don't miss the Kathakali dance! "
               "Top hotels: Kumarakom Lake Resort, Spice Village Thekkady, Niraamaya Retreats. "
               "Airports: Cochin International Airport (COK) - 25km from Kochi, Trivandrum Airport (TRV) - 6km from city. "
               "Railway: Ernakulam Junction, Trivandrum Central, Kottayam Railway Station. "
               "Bus: Ernakulam KSRTC Bus Station, Trivandrum Central Bus Station, Kottayam Bus Stand. "
               "Book via: Booking.com, Kerala Tourism, or direct hotel websites.")
    
    if "rajasthan" in normalized or "jaipur" in normalized or "udaipur" in normalized:
        return ("Rajasthan is the land of palaces, forts, and vibrant culture! "
               "Must-visit: Jaipur (Pink City), Udaipur (City of Lakes), Jaisalmer Fort. "
               "Best time: October to March. Experience the desert safari! "
               "Top hotels: Rambagh Palace Jaipur, Taj Lake Palace Udaipur, The Oberoi Udaivilas. "
               "Airports: Jaipur Airport (JAI) - 13km from city, Udaipur Airport (UDR) - 22km from city. "
               "Railway: Jaipur Junction, Udaipur City Railway Station, Jaisalmer Railway Station. "
               "Bus: Jaipur Sindhi Camp Bus Stand, Udaipur Bus Stand, Jaisalmer Bus Depot. "
               "Book via: Booking.com, MakeMyTrip, or direct hotel websites.")
    
    if "varanasi" in normalized or "banaras" in normalized or "kashi" in normalized:
        return ("Varanasi is the spiritual capital of India, located on the banks of the Ganges! "
               "Highlights: Ganga Aarti, boat ride on Ganges, ancient temples, ghats. "
               "Best time: October to March. Experience the spiritual atmosphere! "
               "Top hotels: Taj Nadesar Palace, BrijRama Palace, Hotel Surya. "
               "Airports: Lal Bahadur Shastri International Airport (VNS) - 26km from city center. "
               "Railway: Varanasi Junction, Varanasi Cantt Railway Station, Manduadih Railway Station. "
               "Bus: Varanasi Bus Station, Lanka Bus Stand, Godowlia Bus Depot. "
               "Book via: Booking.com, Yatra, or direct hotel websites.")
    
    if "delhi" in normalized or "new delhi" in normalized:
        return ("Delhi is India's capital with rich history and modern culture! "
               "Must-visit: Red Fort, Qutub Minar, India Gate, Humayun's Tomb. "
               "Best time: October to March. Try the street food in Old Delhi! "
               "Top hotels: The Leela Palace New Delhi, Taj Palace New Delhi, The Oberoi New Delhi. "
               "Airports: Indira Gandhi International Airport (DEL) - 16km from city center. "
               "Railway: New Delhi Railway Station, Old Delhi Railway Station, Hazrat Nizamuddin. "
               "Bus: Inter State Bus Terminal (ISBT) Kashmere Gate, Anand Vihar, Sarai Kale Khan. "
               "Book via: Booking.com, MakeMyTrip, or direct hotel websites.")
    
    if "mumbai" in normalized or "bombay" in normalized:
        return ("Mumbai is the financial capital and city of dreams! "
               "Highlights: Gateway of India, Marine Drive, Juhu Beach, Bollywood tours. "
               "Best time: October to February. Don't miss the local train experience! "
               "Top hotels: Taj Mahal Palace Mumbai, The Oberoi Mumbai, Four Seasons Hotel Mumbai. "
               "Airports: Chhatrapati Shivaji Maharaj International Airport (BOM) - 28km from city center. "
               "Railway: Chhatrapati Shivaji Terminus (CST), Mumbai Central, Bandra Terminus. "
               "Bus: Mumbai Central Bus Terminal, Dadar Bus Terminal, Borivali Bus Depot. "
               "Book via: Booking.com, Yatra, or direct hotel websites.")
    
    if "bangalore" in normalized or "bengaluru" in normalized:
        return ("Bangalore is India's IT hub with pleasant weather year-round! "
               "Highlights: Lalbagh Botanical Garden, Cubbon Park, Bangalore Palace. "
               "Best time: Throughout the year. Famous for its coffee culture! "
               "Top hotels: The Oberoi Bengaluru, Taj West End Bengaluru, The Leela Palace Bengaluru. "
               "Airports: Kempegowda International Airport (BLR) - 40km from city center. "
               "Railway: Bangalore City Junction, Yesvantpur Junction, Bangalore Cantonment. "
               "Bus: Kempegowda Bus Station (Majestic), Shantinagar Bus Station, Satellite Bus Station. "
               "Book via: Booking.com, Goibibo, or direct hotel websites.")
    
    if "hyderabad" in normalized:
        return ("Hyderabad is famous for its biryani, pearls, and historic monuments! "
               "Must-visit: Charminar, Golconda Fort, Hussain Sagar Lake. "
               "Best time: October to February. Try the famous Hyderabadi biryani! "
               "Top hotels: Taj Falaknuma Palace, The Park Hyderabad, Novotel Hyderabad Airport. "
               "Airports: Rajiv Gandhi International Airport (HYD) - 22km from city center. "
               "Railway: Secunderabad Junction, Hyderabad Deccan, Kacheguda Railway Station. "
               "Bus: Mahatma Gandhi Bus Station (MGBS), Jubilee Bus Station, Dilsukhnagar Bus Depot. "
               "Book via: Booking.com, Yatra, or direct hotel websites.")
    
    if "chennai" in normalized or "madras" in normalized:
        return ("Chennai is the gateway to South India with rich culture and beaches! "
               "Highlights: Marina Beach, Kapaleeshwarar Temple, Fort St. George. "
               "Best time: November to February. Experience classical music and dance! "
               "Top hotels: The Leela Palace Chennai, Taj Coromandel Chennai, ITC Grand Chola. "
               "Airports: Chennai International Airport (MAA) - 7km from city center. "
               "Railway: Chennai Central, Chennai Egmore, Tambaram Railway Station. "
               "Bus: Chennai Mofussil Bus Terminus (CMBT), Koyambedu Bus Terminal, T Nagar Bus Stand. "
               "Book via: Booking.com, Yatra, or direct hotel websites.")
    
    if "kolkata" in normalized or "calcutta" in normalized:
        return ("Kolkata is the cultural capital of India with colonial heritage! "
               "Highlights: Victoria Memorial, Howrah Bridge, Park Street. "
               "Best time: October to March. Famous for its literature and arts! "
               "Top hotels: The Oberoi Grand Kolkata, Taj Bengal Kolkata, ITC Royal Bengal. "
               "Airports: Netaji Subhas Chandra Bose International Airport (CCU) - 17km from city center. "
               "Railway: Howrah Junction, Sealdah Railway Station, Kolkata Terminal. "
               "Bus: Esplanade Bus Terminus, Howrah Bus Terminal, Salt Lake Bus Depot. "
               "Book via: Booking.com, Yatra, or direct hotel websites.")
    
    # Hotel and Booking Specific Queries
    if "hotel" in normalized or "accommodation" in normalized or "stay" in normalized:
        return ("Top hotel booking sites for India: "
               "• Booking.com - International platform with wide selection "
               "• MakeMyTrip - Popular Indian travel portal "
               "• Yatra - Good for domestic bookings "
               "• Goibibo - Competitive prices "
               "• Airbnb - For homestays and unique experiences "
               "• Direct hotel websites - Often best rates and loyalty programs "
               "Ask me about specific cities for hotel recommendations!")
    
    if "book" in normalized or "booking" in normalized or "reserve" in normalized:
        return ("Popular booking platforms for India travel: "
               "Hotels: Booking.com, MakeMyTrip, Yatra, Goibibo "
               "Flights: Skyscanner, Google Flights, MakeMyTrip, Yatra "
               "Trains: IRCTC (official), MakeMyTrip, Yatra "
               "Buses: RedBus, MakeMyTrip, Yatra "
               "Activities: Viator, GetYourGuide, local tour operators "
               "Best to compare prices across multiple platforms!")
    
    if "best time" in normalized or "when to visit" in normalized:
        return ("Best time to visit India: October to March (winter season). "
               "Avoid monsoon (June-September) and peak summer (April-June). "
               "Festival season (October-November) is magical with Diwali and other celebrations! "
               "Book hotels 2-3 months in advance for peak season.")
    
    if "food" in normalized or "cuisine" in normalized or "eat" in normalized:
        return ("Indian cuisine is diverse and delicious! Must-try: "
               "North: Butter Chicken, Naan, Biryani | "
               "South: Dosa, Idli, Sambar | "
               "West: Vada Pav, Pav Bhaji | "
               "East: Fish Curry, Litti Chokha | "
               "Street food: Pani Puri, Chaat, Samosa! "
               "Book food tours via Viator or local operators.")
    
    if "culture" in normalized or "festival" in normalized:
        return ("India has rich cultural diversity! Major festivals: "
               "Diwali (Festival of Lights), Holi (Festival of Colors), "
               "Eid, Christmas, Pongal, Onam. "
               "Each state has unique traditions, dance forms, and art! "
               "Book festival tours via local operators or travel agencies.")
    
    if "transport" in normalized or "how to travel" in normalized:
        return ("India has excellent transport options! "
               "Trains: Indian Railways (book via IRCTC) | "
               "Flights: Domestic airlines connect major cities | "
               "Buses: State transport and private operators | "
               "Metro: Available in Delhi, Mumbai, Bangalore, Chennai | "
               "Auto-rickshaws and taxis for local travel! "
               "Book via: IRCTC, MakeMyTrip, Yatra, or airline websites.")
    
    if "airport" in normalized or "flight" in normalized:
        return ("Major airports in India: "
               "Delhi: Indira Gandhi International (DEL) | "
               "Mumbai: Chhatrapati Shivaji Maharaj (BOM) | "
               "Bangalore: Kempegowda International (BLR) | "
               "Hyderabad: Rajiv Gandhi International (HYD) | "
               "Chennai: Chennai International (MAA) | "
               "Kolkata: Netaji Subhas Chandra Bose (CCU) | "
               "Goa: Goa International (GOI) | "
               "Agra: Agra Airport (AGR) | "
               "Varanasi: Lal Bahadur Shastri (VNS) | "
               "Jaipur: Jaipur Airport (JAI) | "
               "Kochi: Cochin International (COK) | "
               "Trivandrum: Trivandrum International (TRV). "
               "Ask about specific cities for detailed airport information!")
    
    if "railway" in normalized or "train" in normalized or "station" in normalized:
        return ("Major railway stations in India: "
               "Delhi: New Delhi, Old Delhi, Hazrat Nizamuddin | "
               "Mumbai: Chhatrapati Shivaji Terminus (CST), Mumbai Central | "
               "Bangalore: Bangalore City Junction, Yesvantpur | "
               "Hyderabad: Secunderabad, Hyderabad Deccan, Kacheguda | "
               "Chennai: Chennai Central, Chennai Egmore | "
               "Kolkata: Howrah Junction, Sealdah | "
               "Agra: Agra Cantt, Agra Fort | "
               "Goa: Madgaon Junction, Vasco da Gama | "
               "Varanasi: Varanasi Junction, Varanasi Cantt | "
               "Jaipur: Jaipur Junction | "
               "Kerala: Ernakulam Junction, Trivandrum Central. "
               "Book trains via IRCTC, MakeMyTrip, or Yatra!")
    
    if "bus" in normalized or "bus station" in normalized or "bus terminal" in normalized:
        return ("Major bus terminals in India: "
               "Delhi: ISBT Kashmere Gate, Anand Vihar, Sarai Kale Khan | "
               "Mumbai: Mumbai Central, Dadar, Borivali | "
               "Bangalore: Kempegowda (Majestic), Shantinagar, Satellite | "
               "Hyderabad: MGBS, Jubilee, Dilsukhnagar | "
               "Chennai: CMBT, Koyambedu, T Nagar | "
               "Kolkata: Esplanade, Howrah, Salt Lake | "
               "Agra: Agra ISBT, Idgah, Taj Depot | "
               "Goa: Kadamba Panaji, Mapusa, Margao | "
               "Varanasi: Varanasi Bus Station, Lanka, Godowlia | "
               "Jaipur: Sindhi Camp | "
               "Kerala: Ernakulam KSRTC, Trivandrum Central, Kottayam. "
               "Book buses via RedBus, MakeMyTrip, or Yatra!")
    
    if "budget" in normalized or "cost" in normalized or "expensive" in normalized:
        return ("India offers options for all budgets! "
               "Budget: ₹1000-2000/day (hostels, street food) | "
               "Mid-range: ₹3000-5000/day (hotels, restaurants) | "
               "Luxury: ₹8000+/day (5-star hotels, fine dining) | "
               "Transport and accommodation costs vary by city! "
               "Book budget hotels via Hostelworld, Booking.com, or Airbnb.")
    
    # General India/Tourism queries
    if any(word in normalized for word in {"india", "indian", "tourism", "travel", "visit"}):
        return ("India is a diverse country with rich culture, history, and landscapes! "
               "Popular destinations: Taj Mahal (Agra), Goa beaches, Kerala backwaters, "
               "Rajasthan palaces, Varanasi spirituality, Delhi monuments. "
               "Ask me about specific places, hotels, booking sites, food, culture, or travel tips!")

    if "help" in normalized:
        return (
            "I can help you with: "
            "• Indian tourism (places, food, culture, travel tips) "
            "• Hotels and accommodation recommendations "
            "• Airports, railway stations, and bus terminals "
            "• Booking sites and travel platforms "
            "• Time and date "
            "• General chat "
            "Try: 'Tell me about Taj Mahal', 'Hotels in Delhi', 'Airports in Mumbai', 'Railway stations in Bangalore', 'Bus terminals in Chennai', or 'help with travel'!"
        )
    if "thank you" in normalized or "thanks" or "great" or "good"in normalized:
        return "You're welcome! If you need anything else, just say hi."
    if "sorry" in normalized:
        return "No problem! If you need anything else, just say hi."

    if "joke" in normalized:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    if "weather" in normalized:
        return (
            "I can't check live weather yet, but you can try a weather site or app. "
            "For India travel, October to March is generally the best weather!"
        )

    return (
        "I'm not sure about that yet, but I'm learning! "
        "I can help with Indian tourism, time, date, or general chat. "
        "Try asking about 'Taj Mahal', 'Goa beaches', 'Indian food', or say 'help' for more options."
    )


@app.get("/")
def index():
    html = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Simple Python Chatbot</title>
        <style>
            :root {
                --bg: #0f172a;       /* slate-900 */
                --panel: #111827;    /* gray-900 */
                --panel-2: #1f2937;  /* gray-800 */
                --text: #e5e7eb;     /* gray-200 */
                --muted: #9ca3af;    /* gray-400 */
                --accent: #22d3ee;   /* cyan-400 */
                --accent-2: #38bdf8; /* sky-400 */
                --error: #f87171;    /* red-400 */
            }
            * { box-sizing: border-box; }
            body {
                margin: 0;
                background: radial-gradient(1200px 600px at 20% -10%, rgba(56,189,248,0.15), transparent),
                            radial-gradient(1000px 500px at 120% -10%, rgba(34,211,238,0.12), transparent),
                            var(--bg);
                font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
                color: var(--text);
                min-height: 100vh;
                display: grid;
                place-items: center;
            }
            .card {
                width: min(100%, 820px);
                margin: 24px;
                background: linear-gradient(180deg, rgba(31,41,55,0.8), rgba(17,24,39,0.9));
                border: 1px solid rgba(148,163,184,0.2);
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.4);
                overflow: hidden;
                backdrop-filter: blur(8px);
            }
            .header {
                padding: 16px 20px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                border-bottom: 1px solid rgba(148,163,184,0.18);
                background: linear-gradient(180deg, rgba(31,41,55,0.6), rgba(17,24,39,0.6));
            }
            .brand {
                display: flex;
                align-items: center;
                gap: 12px;
                font-weight: 700;
                letter-spacing: 0.3px;
            }
            .brand .dot {
                width: 10px;
                height: 10px;
                border-radius: 50%;
                background: radial-gradient(circle at 30% 30%, var(--accent), var(--accent-2));
                box-shadow: 0 0 18px rgba(56,189,248,0.6);
            }
            .indian-flag {
                display: flex;
                align-items: center;
                gap: 8px;
                font-size: 16px;
            }
            .flag-container {
                display: flex;
                align-items: center;
                gap: 12px;
            }
            .tourism-icons {
                display: flex;
                align-items: center;
                gap: 6px;
                font-size: 14px;
            }
            .subtitle {
                font-size: 12px;
                color: var(--muted);
                display: flex;
                align-items: center;
            }
            .subtitle .flag-container {
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .subtitle .indian-flag {
                font-size: 14px;
            }
            .subtitle .tourism-icons {
                font-size: 12px;
            }
            .chat {
                height: 60vh;
                min-height: 360px;
                max-height: 600px;
                overflow: auto;
                padding: 18px;
                display: flex;
                flex-direction: column;
                gap: 10px;
                background:
                    radial-gradient(800px 200px at 30% -10%, rgba(34,211,238,0.08), transparent),
                    radial-gradient(800px 300px at 80% -10%, rgba(56,189,248,0.08), transparent);
            }
            .msg {
                display: grid;
                grid-template-columns: 32px 1fr;
                gap: 10px;
                align-items: start;
            }
            .avatar {
                width: 32px;
                height: 32px;
                border-radius: 50%;
                display: grid;
                place-items: center;
                color: #081019;
                font-weight: 800;
                background: radial-gradient(circle at 30% 30%, var(--accent), var(--accent-2));
                box-shadow: 0 4px 12px rgba(56,189,248,0.35);
            }
            .bubble {
                padding: 12px 14px;
                background: linear-gradient(180deg, rgba(17,24,39,0.85), rgba(15,23,42,0.9));
                border: 1px solid rgba(148,163,184,0.18);
                border-radius: 12px;
                line-height: 1.5;
                word-wrap: break-word;
                white-space: pre-wrap;
            }
            .user .bubble {
                background: linear-gradient(180deg, rgba(2,6,23,0.9), rgba(15,23,42,0.9));
            }
            .footer {
                border-top: 1px solid rgba(148,163,184,0.18);
                background: linear-gradient(180deg, rgba(31,41,55,0.6), rgba(17,24,39,0.6));
                padding: 12px;
                display: grid;
                grid-template-columns: 1fr 90px;
                gap: 10px;
            }
            input[type="text"] {
                width: 100%;
                background: rgba(2,6,23,0.65);
                color: var(--text);
                border: 1px solid rgba(148,163,184,0.25);
                border-radius: 10px;
                padding: 12px 14px;
                outline: none;
            }
            input[type="text"]:focus {
                border-color: rgba(56,189,248,0.55);
                box-shadow: 0 0 0 3px rgba(56,189,248,0.15);
            }
            button {
                background: linear-gradient(180deg, var(--accent-2), var(--accent));
                color: #06202b;
                font-weight: 700;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: transform .05s ease, filter .2s ease;
            }
            button:active { transform: scale(0.98); }
            .muted { color: var(--muted); font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="header">
                <div class="brand">
                    <div class="dot"></div>
                    <div>YatraBot</div>
                </div>
                <div class="subtitle">
                    <div class="flag-container">
                        <div class="indian-flag">🇮🇳</div>
                        <div class="tourism-icons">🏛️ 🏖️ 🏔️ 🕌</div>
                        <span>YatraBot • Your Travel Assistant</span>
                    </div>
                </div>
            </div>
            <div id="chat" class="chat">
                <div class="msg bot">
                    <div class="avatar">B</div>
                    <div class="bubble">🇮🇳 Namaste! I'm YatraBot, your Indian travel assistant! 🏛️🏖️🏔️ Ask me about Indian destinations, culture, food, or travel tips. Try: "Tell me about Taj Mahal" or "help" for more options.</div>
                </div>
            </div>
            <div class="footer">
                <input id="input" type="text" placeholder="Type a message and press Enter..." autocomplete="off" />
                <button id="send">Send</button>
            </div>
        </div>

        <script>
            const chat = document.getElementById('chat');
            const input = document.getElementById('input');
            const send = document.getElementById('send');

            function appendMessage(role, text) {
                const wrapper = document.createElement('div');
                wrapper.className = `msg ${role}`;
                const avatar = document.createElement('div');
                avatar.className = 'avatar';
                avatar.textContent = role === 'user' ? 'U' : 'B';
                const bubble = document.createElement('div');
                bubble.className = 'bubble';
                bubble.textContent = text;
                wrapper.appendChild(avatar);
                wrapper.appendChild(bubble);
                chat.appendChild(wrapper);
                chat.scrollTop = chat.scrollHeight;
            }

            async function sendMessage() {
                const message = input.value.trim();
                if (!message) return;
                input.value = '';
                appendMessage('user', message);

                try {
                    const res = await fetch('/chat', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ message })
                    });
                    if (!res.ok) {
                        throw new Error('Network error');
                    }
                    const data = await res.json();
                    appendMessage('bot', data.reply || 'Sorry, I had trouble replying.');
                } catch (err) {
                    appendMessage('bot', 'Oops, something went wrong. Please try again.');
                }
            }

            input.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });
            send.addEventListener('click', sendMessage);
        </script>
    </body>
    </html>
    """
    return render_template_string(html)


@app.post("/chat")
def chat() -> Dict[str, str]:
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", ""))
    reply = generate_bot_reply(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    # Run the development server
    app.run(host="0.0.0.0", port=5000, debug=True)


