import discord
import discord.ext
import os

bot = discord.Bot()
cwd = os.getcwd()

@bot.event
async def on_ready():
    print(f"{bot.user} is online.")

@bot.slash_command(name = "archivechannel", description = "Archives a channel")
async def archivechannel(ctx, channelname):
    guildID = 0 #server ID goes here
    await ctx.send("Archiving channel...")
    try: 
        guild = bot.get_guild(guildID)
        print(guildID)
        channelID = 0
        for channel in guild.channels:
            if channel.name == channelname:
                channelID = channel.id
        print("Archiving channel...")
        channeltoarchive = bot.get_channel(channelID)
        with open(cwd + "\\" + channelname + ".html" ,"w+") as f:
            f.write("<!doctype html>\n<html>\n<head>\n <style> @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@500&display=swap'); body { width: 95%; background-color:#36393e; } p { color: #DBDEE1; font-family: 'Open Sans'; padding: 10px; } h1 { color: #DBDEE1; font-family: 'Open Sans'; padding: 10px; text-align: center; } img { max-width: 99%; max-height: 400px; border-radius: 5px; border: 2px solid #7289da; } .messageContainer { width: 100%; background-color: #7289da; border-radius: 10px; padding: 10px; } .nameContainer { width: fit-content; border: #7289da; border-radius: 10px; background-color: #36393e; } .contentContainer { width: 100%; background-color: #424549; border-radius: 10px; } .attachmentContainer { height: fit-content ; margin: 5px; } </style>\n<title>" + channelname + "</title> </head>\n")
            f.write("<body>\n")
            async for msg in channeltoarchive.history(limit=None):
                try:
                    f.write(f'<div class="messageContainer"><div class="nameContainer"><h1>{msg.author.display_name}</h1> \n </div>\n <div class="contentContainer"> <p>{msg.clean_content}</p>')
                    if len(msg.attachments) > 0:
                        attachments = msg.attachments
                        for element in attachments:
                            f.write('\n <div class="attachmentContainer">')
                            f.write('<a href="' + element.url + '">')
                            f.write('<img src="' + element.url + '" onerror="this.src=' + "'https://cdn3.emoji.gg/emojis/5068-file.png'" + '"' + '></a>')
                            f.write('</div>\n</div>\n</div>\n</div>\n<hr>')
                    else:
                        f.write("\n</div>\n</div>\n<hr>")
                except:
                    pass
                f.write("</body>\n</html>")
        await ctx.send("The channel has been saved. Download it to view it.")
        await ctx.send(file=discord.File(cwd + "\\" + channelname + ".html"))
    except:
        await ctx.send("Channel does not exist.")

bot.run("") #token goes here