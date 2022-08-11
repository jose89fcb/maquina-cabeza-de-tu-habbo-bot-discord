import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
import random


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def maquina(ctx,   keko):
    await ctx.message.delete()
    await ctx.send("Generando expositor de habbo...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
   
   
    
    habbo = response.json()['figureString']
   
   

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=m&figure="+ habbo +"&action=none&direction=2&head_direction=4&gesture=std&size=m&headonly=1"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((54,62), Image.Resampling.LANCZOS)#tamaño del keko 1

 
    
    
    


    
    


    

   

    

    
    
    



    img2 = img1.copy()
    
    
    ###

    


    cristalverde = Image.open(r"imagenes/cristalverde.png").convert("RGBA") #imagen
    img1 = cristalverde.resize((64,149), Image.Resampling.LANCZOS)#tamaño de la cristal verde


    ###
  
    ###
    maquina = Image.open(r"imagenes/maquina.png").convert("RGBA") #imagen
    img1 = maquina.resize((64,149), Image.Resampling.LANCZOS)#tamaño de la maquina

    ###
    trozo = Image.open(r"imagenes/trozo.png").convert("RGBA") #imagen
    img1 = trozo.resize((64,149), Image.Resampling.LANCZOS)#tamaño del trozo
    ##
   
   
    
    

 
   
    
    
    
    
    
    
    img1.paste(maquina,(0,0), mask = maquina) #Posicion de la almo
    
   

    
    img1.paste(img2,(5,38), mask = img2) #Posicion del keko 1
    img1.paste(cristalverde,(0,0), mask = cristalverde) #Posicion de la cristal verde

    
    img1.paste(trozo,(0,0), mask = trozo) #Posicion de la cristal verde

    
    
   
    
    ### 

    
    
   
    
   ###
   
    
   
    ###
    
   
 
    
    
  ####
   
  ###
    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   