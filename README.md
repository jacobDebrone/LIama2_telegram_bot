<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Telegram Chatbot with HugChat</title>

    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 20px;
        }

        h1, h2 {
            color: #333;
        }

        ol, ul {
            margin-bottom: 20px;
        }

        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    </style>
</head>
<body>

    <h1>Telegram Chatbot with HugChat</h1>

    <h2>Overview</h2>
    <p>This project demonstrates the creation of a Telegram chatbot using the HugChat library to facilitate AI conversations. The chatbot interacts with users in real-time, sending and receiving messages through the Telegram platform.</p>

    <h2>Table of Contents</h2>
    <ol>
        <li>Prerequisites</li>
        <li>Getting Started</li>
        <li>Usage</li>
        <li>Customization</li>
        <li>Contributing</li>
        <li>License</li>
    </ol>

    <h2>Prerequisites</h2>
    <p>To run the Telegram chatbot with HugChat, you'll need the following prerequisites:</p>
    <ul>
        <li>Python 3.6 or higher</li>
        <li>Telegram Bot API Token</li>
        <li>HugChat credentials (email and password)</li>
        <li>telebot and hugchat Python libraries</li>
    </ul>
    <p>You can install the required libraries using:</p>
    <code>pip install telebot</code><br>
    <code>pip install hugchat</code>
    <p>You can then clone the repo and edit the code to set up your Telegram bot token and HugChat credentials. Replace the following placeholders in the code:</p>
    <ul>
        <li>"YOUR_BOT_TOKEN" with your Telegram bot token</li>
        <li>"Your Email" with your email registered on huggingface</li>
        <li>"Your password from Huggingface" with your Huggingface password</li>
    </ul>
    <p>You can then run the main file:</p>
    <code>python Telehug.py</code>
    <p>The bot code gives access to Llama by default. For more info, look at the Hugchat library documentation <a href="https://pypi.org/project/hugchat/">here</a>.</p>

</body>
</html>
