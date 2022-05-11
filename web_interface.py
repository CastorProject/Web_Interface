#! /usr/bin/env python
import time
import rospy
import subprocess

from flask import Flask, render_template, request
import threading

from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Bool

######################################
################ ROS #################
######################################
threading.Thread(target=lambda: rospy.init_node('mainMenuHTML', disable_signals=True)).start()
######################################
############# PUBLISHERS #############
######################################
pubEmotions = rospy.Publisher('/emotions', String, queue_size = 10)
pubSpeaker = rospy.Publisher('/speaker', String, queue_size = 10)
pubSpeakerAction = rospy.Publisher('/speakerAction', String, queue_size = 15)
pubMovements = rospy.Publisher('/movements', String, queue_size = 5)
pubCastorSystem = rospy.Publisher('/castor_system', String, queue_size = 5)
######################################
############# MAIN MENU ##############
######################################
app = Flask(__name__)
@app.route("/")
def mainMenu():
    templateData = {
        'title' : 'Main Menu',
    }
    return render_template('mainMenu.html', **templateData)

@app.route("/<action>")
def actionMainMenu(action):
    template = "mainMenu.html"
    if action == "greet":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("hola")

    elif action == "greetPN":
        template = "mainGreet.html"

    elif action == "bye":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("chao_amigo")

    elif action == "bye2":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("chao_amiga")

    elif action == "byeNP":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Nos_vemos_pronto")
        
    elif action == "happyday":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Ten_un_lindo_dia")

    elif action == "byePN":
        template = "mainBye.html" 
      
    elif action == "lets_go":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_jugar")

    elif action == "AC":
        template = "mainActivities.html"

    elif action == "hifiveinstruction":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("choca_los_cinco")
        
    elif action == "highfive":
    	pubEmotions.publish("talk")
        pubMovements.publish("highfive")
        
    elif action == "bajar_brazo":
        pubMovements.publish("neutral")

    elif action == "shutdown":
        template = "shutdown.html"
        
    elif action == "reboot":
        template = "reboot.html"
    templateData = {
        'title' : 'Main Menu',
    }
    return render_template(template, **templateData)

###############################################
################ Greet per Name ###############
###############################################
@app.route("/main/<action>")
def actionGreetMenu(action):
    template = "mainGreet.html"
    if action == "name1":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Hola_Jose_emilio")
    elif action == "name2":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Hola_Belen")
    elif action == "name3":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Hola_Italo")
    elif action == "name4":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Hola_Gregor")
    elif action == "name5":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Hola_Yamir")
    elif action == "name6":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Hola_Padma")
    elif action == "name7":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Hola_Rafel")
    elif action == "name8":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Hola_Arturo")


    templateData = {
        'title' : 'Greet Menu',
    }
    return render_template(template, **templateData)

#################################################
################ Bye Bye per Name ###############
#################################################
@app.route("/mainBye/<action>")
def actionByeMenu(action):
    if action == "name1":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Chao_Jose_emilio")
    elif action == "name2":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Chao_Belen")
    elif action == "name3":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Chao_Italo")
    elif action == "name4":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Chao_Gregor")
    elif action == "name5":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Chao_Yamir")
    elif action == "name6":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Chao_Padma")
    elif action == "name7":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Chao_Rafel")
    elif action == "name8":
        pubMovements.publish("wave")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Chao_Arturo")


    templateData = {
        'title' : 'Bye Menu',
    }
    return render_template('mainBye.html', **templateData)

#########################################
################ Shutdown ###############
#########################################
@app.route("/shutdown/<action>")
def action1(action):
    if action == "yes":
        pubCastorSystem.publish("shutdown")
        time.sleep(0.5)
        subprocess.call(['sudo', 'shutdown', 'now'], shell=False)
        template = "shutdown.html"

    elif action == "no":
        print("no")
        template = "mainMenu.html"

    templateData = {
        'title' : 'Shutdown',
    }
    return render_template(template, **templateData)

#########################################
################ Reboot #################
#########################################
@app.route("/reboot/<action>")
def action2(action):
    if action == "yes":
        pubCastorSystem.publish("reboot")
        time.sleep(0.5)
        subprocess.call(['sudo', 'reboot', 'now'], shell=False)
        template = "reboot.html"
    elif action == "no":
        template = "mainMenu.html"
    templateData = {
        'title' : 'Reboot',
    }
    return render_template(template, **templateData)


######################################
############### Aditionals Activities ################
######################################

##############################################
################ Actions ###############
##############################################
@app.route("/AC/<action>")
def AC(action):
    
    if action == "hug":
        template = 'ActivitiesHug.html'
    elif action == "Conversation":
        template = 'mainConversation.html'
    elif action == "BodyParts":
        template = 'Bodyparts.html' 
    elif action == "emotions":
        template = 'mainEmotions.html' 
    elif action == "maths":
        template = 'mainMaths.html' 

    templateData = {
        'title' : 'Actividades Adicionales',
    }
    return render_template(template, **templateData)

##############################################
################ Action_Hug ###############
##############################################
@app.route("/AC/hug/<action>")
def Hug(action):
    template = "ActivitiesHug.html"
    if action == "sayHug":        #Abrazos
        pubEmotions.publish("talk")
        pubSpeaker.publish("Dame_un_abrazo")
    elif action == "hugOpen":
        pubMovements.publish("hugOpen1")
    elif action == "hugClose":
        pubMovements.publish("hugClose")
    elif action == "hugEnd":
        pubMovements.publish("neutral")
    elif action == "thanks":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Gracias")


    templateData = {
        'title' : 'Abrazos',
    }
    return render_template(template, **templateData)
##############################################
################ Conversation ###############
###############################################
@app.route("/AC/conv/<action>")
def Conversation(action):
    template = "mainConversation.html"
    if action == "howRU":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Como_estas")
    elif action == "dad":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Como_papa")
    elif action == "mom":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Como_mama")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("como_te_llamas")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("recuerdas_nombre")
    elif action == "dotoday":
        pubEmotions.publish("talk")
        pubSpeaker.publish("que_has_hecho")
    elif action == "breakfast":
        pubEmotions.publish("talk")
        pubSpeaker.publish("que_desayunaste")
    elif action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Como_me_llamo")
    elif action == "color":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Que_color_te_gusta")
    elif action == "animalFav":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cual_animal") 
    elif action == "edad":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cuantos_anos_tienes")
    elif action == "imGood":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yo_muy_bien")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Mi_nombre")
    elif action == "liketoplay":
        pubEmotions.publish("talk")
        pubSpeaker.publish("gusta_jugar")
    elif action == "fav_meal":
        pubEmotions.publish("talk")
        pubSpeaker.publish("fav_comida")
    elif action == "cookies":
        pubEmotions.publish("talk")
        pubSpeaker.publish("galletas_regalo")
    elif action == "who":
        pubEmotions.publish("talk")
        pubSpeaker.publish("quien")
    elif action == "cumple":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cumple")






    elif action == "yourwelcome":
        pubEmotions.publish("talk")
        pubSpeaker.publish("de_nada")
    elif action == "age":
        pubEmotions.publish("talk")
        pubSpeaker.publish("10_anos")
    elif action == "ilove":
        pubEmotions.publish("talk")
        pubSpeaker.publish("te_quiero")
    elif action == "Metoo":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yo_tambien")
    elif action == "Likewise":
        pubEmotions.publish("talk")
        pubSpeaker.publish("El_mio_tambien")
    elif action == "ColorGreen":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Mi_color_favorito")
    elif action == "MianimalFav":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Mi_animal_favorito")
    elif action == "DogSound":
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("El_perro_hace")
    elif action == "Cookiesgift":
        pubEmotions.publish("talk")
        pubSpeaker.publish("galletas_regalo2")
    elif action == "Hearthat":
        pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action == "Favthings":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Me_gusta_jugar_contigo")
    elif action == "si":
        pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action == "no":
        pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action == "thanks":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action == "deli":
        pubEmotions.publish("talk")
        pubSpeaker.publish("delicioso")
    elif action == "aloneplay":
        pubEmotions.publish("sad")
        pubSpeaker.publish("solo_sin_jugar")
    elif action == "likeit":
        pubEmotions.publish("sad")
        pubSpeaker.publish("te_gusta")
    elif action == "pawsong":
        pubEmotions.publish("sad")
        pubSpeaker.publish("tengo_cancion_paw_patrol")
    elif action == "sonicsong":
        pubEmotions.publish("sad")
        pubSpeaker.publish("tengo_cancion_sonic")
    elif action == "dulce":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Dulce")
    elif action == "nose":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Como_papa")






    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_te_escucho")
    elif action == "gj9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action == "gj10":
        pubEmotions.publish("angry")
        pubSpeaker.publish("eso_no_se_hace")
    elif action == "gj11":
        pubEmotions.publish("angry")
        pubSpeaker.publish("no_hagas_eso")
    elif action == "gj12":
        pubEmotions.publish("happy")
        pubSpeaker.publish("tu_puedes")




    templateData = {
        'title' : 'Conversation Menu',
    }
    return render_template(template, **templateData)

##############################################
################ Emotions ###############
##############################################
@app.route("/AC/emotions/<action>")
def emotions(action):
    template = "mainEmotions.html"
    if action == "howifeel":        #Abrazos
        pubEmotions.publish("talk")
        pubSpeaker.publish("como_me_siento")
    elif action == "emotion":
        pubEmotions.publish("talk")
        pubSpeaker.publish("emociones")
    elif action == "andnow":
        pubEmotions.publish("talk")
        pubSpeaker.publish("ahora_como_me_siento")
    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")


    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")
    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")






    templateData = {
        'title' : 'Emociones',
    }
    return render_template(template, **templateData)

##############################################
################ Operaciones ###############
##############################################
@app.route("/AC/maths/<action>")
def maths(action):
    template = "mainMaths.html"
    if action == "count":
        pubEmotions.publish("talk")
        pubSpeaker.publish("contar")
    elif action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cuenta_conmigo")
    elif action == "one":
        pubEmotions.publish("talk")
        pubSpeaker.publish("uno")
    elif action == "two":
        pubEmotions.publish("talk")
        pubSpeaker.publish("dos")
    elif action == "tree":
        pubEmotions.publish("talk")
        pubSpeaker.publish("tres")
    elif action == "four":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cuatro")
    elif action == "five":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cinco")
    elif action == "six":
        pubEmotions.publish("talk")
        pubSpeaker.publish("seis")
    elif action == "seven":
        pubEmotions.publish("talk")
        pubSpeaker.publish("siete")
    elif action == "eight":
        pubEmotions.publish("talk")
        pubSpeaker.publish("ocho")
    elif action == "nine":
        pubEmotions.publish("talk")
        pubSpeaker.publish("nueve")
    elif action == "ten":
        pubEmotions.publish("talk")
        pubSpeaker.publish("diez")
    elif action == "sum":
        pubEmotions.publish("talk")
        pubSpeaker.publish("sabes_sumar")
    elif action == "substraction":
        pubEmotions.publish("talk")
        pubSpeaker.publish("sabes_restar")
    elif action == "howmuch":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cuanto_es")
    elif action == "plus":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mas")
    elif action == "less":
        pubEmotions.publish("talk")
        pubSpeaker.publish("menos")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")


    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")
    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")





    templateData = {
        'title' : 'Operaciones',
    }
    return render_template(template, **templateData)

##############################################
################ BodyParts ###############
###############################################
@app.route("/AC/BodyParts/<action>")
def Body(action):
    template = "Bodyparts.html"

    if action == "sayBody":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Actividad_Partes_del_Cuerpo")
    elif action == "pointHead":
        pubMovements.publish("pointHead")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Mi_cabeza")
    elif action == "pointEyes":
        pubMovements.publish("pointEyes")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Mis_ojos")
    elif action == "pointNose":
        pubMovements.publish("pointNose")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Mi_nariz")
    elif action == "pointMouth":
        pubMovements.publish("pointMouth")
        time.sleep(0.5)
        pubEmotions.publish("talk")
        pubSpeaker.publish("Mi_boca")

    elif action == "askHead":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_mi_cabeza")
    elif action == "askEyes":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_mis_ojos")
    elif action == "askNose":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_mi_nariz")
    elif action == "askMouth":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_mi_boca")
    elif action == "askFeet":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_mis_pies")
    elif action == "askArms":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_mis_brazos")
    elif action == "askStomatch":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_mi_barriga")
    elif action == "askShoulders":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_mis_hombros")

    elif action == "asktheirHead":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_tu_cabeza")
    elif action == "asktheirEyes":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_tu_ojos")
    elif action == "asktheirNose":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_tu_nariz")
    elif action == "asktheirMouth":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_tu_boca")
    elif action == "asktheirFeet":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_tu_pies")
    elif action == "asktheirArms":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_tu_brazos")
    elif action == "asktheirStomatch":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_tu_barriga")
    elif action == "asktheirShoulders":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_tu_hombros")
    elif action == "asktheirKnees":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_estan_tu_rodillas")
    elif action == "asktheireyebrows":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cejas")
    elif action == "asktheirhair":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cabello")
    elif action == "asktheirneck":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cuello")
    elif action == "asktheirfingers":
        pubEmotions.publish("talk")
        pubSpeaker.publish("dedos")
    elif action == "asktheirback":
        pubEmotions.publish("talk")
        pubSpeaker.publish("espalda")
    elif action == "asktheirears":
        pubEmotions.publish("talk")
        pubSpeaker.publish("orejas")




    elif action == "names":
        template = 'BodyNames.html'


    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")

    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")


    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")


    templateData = {
        'title' : 'BodyParts Menu',
    }
    return render_template(template, **templateData)
############################################################
################ Body parts Names ###############
############################################################
@app.route("/AC/BodyParts/names/<action>")
def actionBody_names(action):
    template = 'BodyNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Daniel")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Dayana")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Julian_Camilo")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Juan_Esteban")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Martin")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Oscar")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Santiago")
    elif action == "name9":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Valery")
    elif action == "name10":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yovan")
    elif action == "name11":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Nicolas")
    elif action == "name12":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Juliana")


    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)


######################################
############### LVL 1 ################
######################################

@app.route("/L1")
def L1():
    templateData = {
        'title' : 'Nivel 1',
    }
    return render_template('level1.html', **templateData)

##############################################
################ LVL 1 Actions ###############
##############################################
@app.route("/L1/<action>")
def actionL1(action):
    if action == "FA":
        template = 'level1Attention.html'
    elif action == "FI":
        template = 'level1Instructions.html'
    elif action == "WMP":
        template = 'level1Memory.html'
    elif action == "PI":
        template = 'level1Physical.html'
    elif action == "VI":
        template = 'level1Verbal.html'
    elif action == "pinpon":
        pubSpeaker.publish("Pinpon")
        template = 'level1.html'

    templateData = {
        'title' : 'Nivel 1',
    }
    return render_template(template, **templateData)

######################################################
################ LVL 1 Focal Attention ###############
######################################################
@app.route("/L1/FA/<action>")
def actionL1_FA(action):
    template = 'level1Attention.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("explicacion_n1_af")
    elif action == "traer":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Traelo")
    elif action == "songBattle":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_batalla_del_calentamiento")
    elif action == "cow":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_vaca")
    elif action == "horse":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_caballo")
    elif action == "table":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_mesa")
    elif action == "chair":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_silla")
    elif action == "plane":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_avion")
    elif action == "helicopter":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_helicoptero")
    elif action == "car":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_carro")
    elif action == "ball":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_pelota")
    elif action == "apple":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_manzana")
    elif action == "sombrero":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Sombrero")
    elif action == "banana":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_banano")

    elif action == "pera":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_pera")
    elif action == "frutilla":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_frutilla")
    elif action == "limon":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_limon")
    elif action == "naranja":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_naranja")
    elif action == "zanahoria":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_zanahoria")
    elif action == "perro":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_perro")
    elif action == "conejo":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_conejo")
    elif action == "mono":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_mono")
    elif action == "tigre":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_tigre")
    elif action == "jirafa":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_jirafa")
    elif action == "leon":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_leon")
    elif action == "canguro":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_canguro")
    elif action == "gato":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_gato")
    elif action == "oso":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_oso")



        

    elif action == "vaso":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vaso")
    elif action == "cepillo":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cepillo")
    elif action == "cepillo_dientes":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cepillo_dientes")
    elif action == "plato":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Plato")
    elif action == "tenedor":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Tenedor")
    elif action == "cuchara":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cuchara")
    elif action == "basura":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Basura")
    elif action == "camisa":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Camisa")
    elif action == "ojos":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Ojos")
    elif action == "zapatos":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Zapatos")
    elif action == "botones":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Botones")

    elif action == "underwear":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_calzoncillos")
    elif action == "shirt":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_camisa")
    elif action == "scrap":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_correa")
    elif action == "socks":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_medias")
    elif action == "pants":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_pantalon")
    elif action == "toiletpaper":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_papel")
    elif action == "sack":
        pubEmotions.publish("talk")
        pubSpeaker.publish("donde_esta_saco")




    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")


    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "lookAtMe":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")

    elif action == "names":
        template = 'level1AttentionNames.html'

    templateData = {
        'title' : 'Focal Attention',
    }
    return render_template(template, **templateData)

############################################################
################ LVL 1 Focal Attention Names ###############
############################################################
@app.route("/L1/FA/names/<action>")
def actionL1_FA_names(action):
    template = 'level1AttentionNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")


    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)

##########################################################
################ LVL 1 Follow Instructions ###############
##########################################################
@app.route("/L1/FI/<action>")
def actionL1_FI(action):
    template = 'level1Instructions.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("explicacion_n1_si")
    elif action == "traer":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Traelo")
    elif action == "trae":
        pubEmotions.publish("talk")
        pubSpeaker.publish("trae")

    elif action == "one":
        pubEmotions.publish("talk")
        pubSpeaker.publish("uno")
    elif action == "two":
        pubEmotions.publish("talk")
        pubSpeaker.publish("dos")
    elif action == "tree":
        pubEmotions.publish("talk")
        pubSpeaker.publish("tres")
    elif action == "four":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cuatro")
    elif action == "five":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cinco")
    elif action == "six":
        pubEmotions.publish("talk")
        pubSpeaker.publish("seis")
    elif action == "seven":
        pubEmotions.publish("talk")
        pubSpeaker.publish("siete")
    elif action == "eight":
        pubEmotions.publish("talk")
        pubSpeaker.publish("ocho")


    elif action == "animals":
        pubEmotions.publish("talk")
        pubSpeaker.publish("animales")
    elif action == "rings":
        pubEmotions.publish("talk")
        pubSpeaker.publish("aros")
    elif action == "fruits":
        pubEmotions.publish("talk")
        pubSpeaker.publish("frutas")
    elif action == "balls":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pelotas")
    elif action == "transport":
        pubEmotions.publish("talk")
        pubSpeaker.publish("transporte")

    elif action == "please":
        pubEmotions.publish("talk")
        pubSpeaker.publish("porfavor")




    elif action == "lcow":
        pubEmotions.publish("talk")
        pubSpeaker.publish("levanta_vaca")
    elif action == "lhorse":
        pubEmotions.publish("talk")
        pubSpeaker.publish("levanta_caballo")
    elif action == "lplane":
        pubEmotions.publish("talk")
        pubSpeaker.publish("levanta_avion")
    elif action == "lhelicopter":
        pubEmotions.publish("talk")
        pubSpeaker.publish("levanta_helicoptero")
    elif action == "lcar":
        pubEmotions.publish("talk")
        pubSpeaker.publish("levanta_carro")
    elif action == "lball":
        pubEmotions.publish("talk")
        pubSpeaker.publish("levanta_pelota")
    elif action == "lapple":
        pubEmotions.publish("talk")
        pubSpeaker.publish("levanta_manzana")

    elif action == "mcow":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mueve_vaca")
    elif action == "mhorse":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mueve_caballo")
    elif action == "mplane":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mueve_avion")
    elif action == "mhelicopter":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mueve_helicoptero")
    elif action == "mcar":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mueve_carro")
    elif action == "mball":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mueve_pelota")
    elif action == "mapple":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mueve_manzana")

    elif action == "pcow":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_vaca")
    elif action == "phorse":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_caballo")
    elif action == "ptable":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_mesa")
    elif action == "pchair":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_silla")
    elif action == "pplane":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_avion")
    elif action == "phelicopter":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_helicoptero")
    elif action == "pcar":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_carro")
    elif action == "pball":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_pelota")
    elif action == "papple":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_manzana")
    elif action == "pred":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_rojo")
    elif action == "pgreen":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_verde")
    elif action == "pblue":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_azul")
    elif action == "pgray":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_gris")
    elif action == "porange":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_naranja")
    elif action == "ppink":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_rosado")
    elif action == "pviolet":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_morado")
    elif action == "pwhite":
        pubEmotions.publish("talk")
        pubSpeaker.publish("senala_blanco")


    elif action == "p1Cow":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cual_animal_hace_mu")
    elif action == "p1Dog":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cual_animal_hace_guau")
    elif action == "p1Cat":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cual_animal_hace_miau")
    elif action == "p1Duck":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cual_animal_hace_cuac")
    elif action == "p1Sheep":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cual_animal_hace_veee")
    elif action == "p1Pig":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Cual_animal_hace_oing")

    elif action == "phrase17":
        pubEmotions.publish("talk")
        pubSpeaker.publish("como_hace_vaca")
    elif action == "phrase18":
        pubEmotions.publish("talk")
        pubSpeaker.publish("como_hace_perro")
    elif action == "phrase19":
        pubEmotions.publish("talk")
        pubSpeaker.publish("como_hace_gato")
    elif action == "phrase20":
        pubEmotions.publish("talk")
        pubSpeaker.publish("como_hace_oveja")
    elif action == "phrase21":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Como_hace_pato")
    elif action == "phrase22":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Como_hace_tren")
    elif action == "phrase26":
        pubEmotions.publish("talk")
        pubSpeaker.publish("ambulancia")
    elif action == "phrase27":
        pubEmotions.publish("talk")
        pubSpeaker.publish("carros")
    elif action == "phrase28":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pollo")
    elif action == "phrase29":
        pubEmotions.publish("talk")
        pubSpeaker.publish("caballo")


    elif action == "phrase23":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Camina_como_cangrejo")
    elif action == "phrase24":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Has_como_gorila")
    elif action == "phrase25":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Salta_como_sapo")



    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level1FollowNames.html'

    templateData = {
        'title' : 'Follow Instructions',
    }
    return render_template(template, **templateData)


############################################################
################ LVL 1 Follow Instructions Names ###############
############################################################
@app.route("/L1/FI/names/<action>")
def actionL1_FI_names(action):
    template = 'level1FollowNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")
    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)


###################################################################
################ LVL 1 Working Memory and Procedure ###############
###################################################################
@app.route("/L1/WMP/<action>")
def actionL1_WMP(action):
    template = 'level1Memory.html'
    if action == "cow":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_vaca")
    elif action == "llevar":
        pubEmotions.publish("talk")
        pubSpeaker.publish("llevalo")
    elif action == "horse":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_caballo")
    elif action == "plane":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_avion")
    elif action == "helicopter":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_helicoptero")
    elif action == "car":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_carro")
    elif action == "ball":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_pelota")
    elif action == "apple":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_manzana")
    elif action == "banana":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_banano")
    elif action == "pera":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_pera")
    elif action == "frutilla":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_frutilla")
    elif action == "limon":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_limon")
    elif action == "naranja":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_naranja")
    elif action == "zanahoria":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_zanahoria")
    elif action == "perro":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_perro")
    elif action == "conejo":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_conejo")
    elif action == "mono":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_mono")
    elif action == "tigre":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_tigre")
    elif action == "leon":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_leon")
    elif action == "jirafa":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_jirafa")
    elif action == "canguro":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_canguro")
    elif action == "gato":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_gato")
    elif action == "oso":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_oso")



    elif action == "cepillo_dientes":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_cepillo_dientes")
    elif action == "cepillo":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_cepillo")
    elif action == "cuchara":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_cuchara")
    elif action == "tenedor":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_tenedor")
    elif action == "vaso":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_vaso")
    elif action == "plato":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Donde_encontraste_plato")


    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level1MemoryNames.html'

    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

############################################################
################ LVL 1 Working Memory and Procedure Names ###############
############################################################
@app.route("/L1/WMP/names/<action>")
def actionL1_WMP_names(action):
    template = 'level1MemoryNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")


    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)



#########################################################
################ LVL 1 Physical Imitation ###############
#########################################################
@app.route("/L1/PI/<action>")
def actionL1_PI(action):
    template = 'level1Physical.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("explicacion_nv1_if")

    elif action == "rArm1":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl1Movement1")
    elif action == "rArm2":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl1Movement2")
    elif action == "rArm3":
        pubEmotions.publish("happy")
        pubMovements.publish("rightShoulderP")
    elif action == "lArm1":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl1Movement3")
    elif action == "lArm2":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl1Movement4")
    elif action == "lArm3":
        pubEmotions.publish("happy")
        pubMovements.publish("leftShoulderP")
    elif action == "head1":
        pubEmotions.publish("happy")
        pubMovements.publish("rightHead")
    elif action == "head2":
        pubEmotions.publish("happy")
        pubMovements.publish("leftHead")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level1PhysicalNames.html'

    
    templateData = {
        'title' : 'Physical Imitation',
    }
    return render_template(template, **templateData)

############################################################
################ LVL 1 Physical Imitation Names ###############
############################################################
@app.route("/L1/PI/names/<action>")
def actionL1_PI_names(action):
    template = 'level1PhysicalNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")


    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)


#######################################################
################ LVL 1 Verbal Imitation ###############
#######################################################
@app.route("/L1/VI/<action>")
def actionL1_VI(action):
    template = 'level1Verbal.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("repite_despues_de_mi")
    elif action == "escribem":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mayuscula")
    elif action == "escribem2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("minuscula")

    elif action == "phrase1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action == "phrase2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("rojo")
    elif action == "phrase3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("azul")
    elif action == "phrase4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("amarillo")
    elif action == "phrase5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("verde")
    elif action == "phrase6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("naranja")
    elif action == "phrase7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("morado")
    elif action == "phrase8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mama")
    elif action == "phrase9":
        pubEmotions.publish("talk")
        pubSpeaker.publish("papa")
    elif action == "phrase10":
        pubEmotions.publish("talk")
        pubSpeaker.publish("casa")
    elif action == "phrase11":
        pubEmotions.publish("talk")
        pubSpeaker.publish("libro")
    elif action == "phrase12":
        pubEmotions.publish("talk")
        pubSpeaker.publish("lapiz")
    elif action == "phrase13":
        pubEmotions.publish("talk")
        pubSpeaker.publish("plato")
    elif action == "phrase14":
        pubEmotions.publish("talk")
        pubSpeaker.publish("avion")
    elif action == "phrase15":
        pubEmotions.publish("talk")
        pubSpeaker.publish("tren")
    elif action == "phrase16":
        pubEmotions.publish("talk")
        pubSpeaker.publish("carro")
    elif action == "phrase17":
        pubEmotions.publish("talk")
        pubSpeaker.publish("agua")
    elif action == "phrase18":
        pubEmotions.publish("talk")
        pubSpeaker.publish("camisa")
    elif action == "phrase19":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cepillo")
    elif action == "phrase20":
        pubEmotions.publish("talk")
        pubSpeaker.publish("chaqueta")
    elif action == "phrase21":
        pubEmotions.publish("talk")
        pubSpeaker.publish("elefante")
    elif action == "phrase22":
        pubEmotions.publish("talk")
        pubSpeaker.publish("galleta")
    elif action == "phrase23":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jabon")
    elif action == "phrase24":
        pubEmotions.publish("talk")
        pubSpeaker.publish("limon")
    elif action == "phrase25":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mango")
    elif action == "phrase26":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pantalon")
    elif action == "phrase27":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pescado")
    elif action == "phrase28":
        pubEmotions.publish("talk")
        pubSpeaker.publish("shampoo")
    elif action == "phrase29":
        pubEmotions.publish("talk")
        pubSpeaker.publish("sopa")



    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")

    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level1VerbalNames.html'

    templateData = {
        'title' : 'Verbal Imitation',
    }
    return render_template(template, **templateData)

############################################################
################ LVL 1 Verbal Imitation Names ###############
############################################################
@app.route("/L1/VI/names/<action>")
def actionL1_VI_names(action):
    template = 'level1VerbalNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")

    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)


######################################
############### LVL 2 ################
######################################

@app.route("/L2")
def L2():
    templateData = {
        'title' : 'Nivel 2',
    }
    return render_template('level2.html', **templateData)

##############################################
################ LVL 2 Actions ###############
##############################################
@app.route("/L2/<action>")
def actionL2(action):
    print action
    if action == "FI_FA":
        template = 'level2IaA.html'
    elif action == "WMP":
        template = 'level2Memory.html'
    elif action == "PI":
        template = 'level2Physical.html'
    elif action == "VI":
        template = 'level2Verbal.html'

    templateData = {
        'title' : 'Nivel 2',
    }
    return render_template(template, **templateData)

##############################################################################
################ LVL 2 Follow Instructions and Focal Attention ###############
##############################################################################
@app.route("/L2/FI_FA/<action>")
def actionL2_FI_FA(action):
    template = 'level2IaA.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Sigue_indicaciones_cancion")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "round1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cabeza_hombros_rodillas_pies")
    elif action == "round2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("partes_del_cuerpo")
    elif action == "round3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("si_estas_feliz_y_lo_sabes")
    elif action == "round4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Chuchuwa")
    elif action == "round5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Brinca_y_para")
    elif action == "round6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baile_animales")
    elif action == "round7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Mueve_cuerpo")
    elif action == "round8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baile_gorila")
    elif action == "round9":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Soy_una_taza")




    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level2AttentionNames.html'

    
    templateData = {
        'title' : 'Follow Instrucction and Focal Attention',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 2 Focal Attention and Follow Instructions Names ########
############################################################
@app.route("/L2/FI_FA/names/<action>")
def actionL2_FI_FA_names(action):
    template = 'level2AttentionNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")


    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)


###########################################################################
################ LVL 2 Working Memory and Procedure #######################
###########################################################################
@app.route("/L2/WMP/<action>")
def actionL2_WMP(action):
    if action == "explain1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_escuchar_cancion")
        template = 'level2Memory.html'

    elif action == "explain2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_responder_preguntas")
        template = 'level2Memory.html'

    elif action == "round1":
        template = 'level2Memory1.html'
    elif action == "round2":
        template = 'level2Memory2.html'
    elif action == "round3":
        template = 'level2Memory3.html'
    elif action == "round4":
        template = 'level2Memory4.html'
    elif action == "round5":
        template = 'level2Memory5.html'
    elif action == "round6":
        template = 'level2Memory6.html'
    elif action == "round7":
        template = 'level2Memory7.html'
    elif action == "round8":
        template = 'level2Memory8.html'
    elif action == "round9":
        template = 'level2Memory9.html'
    elif action == "round10":
        template = 'level2Memory10.html'
    elif action == "round11":
        template = 'level2Memory11.html'
    elif action == "names":
        template = 'level2MemoryNames.html'

    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 2 Working Memory and Procedure ########
############################################################
@app.route("/L2/WMP/names/<action>")
def actionL2_WMP_names(action):
    template = 'level2MemoryNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")


    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)


###########################################################################
################ LVL 2 Working Memory and Procedure Round 1 ###############
###########################################################################
@app.route("/L2/WMP/round1/<action>")
def actionL2_WMP1(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vocales")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_vocales_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_vocales_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vocales_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")

    template = 'level2Memory1.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 1',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 2 Working Memory and Procedure Round 2 ###############
###########################################################################
@app.route("/L2/WMP/round2/<action>")
def actionL2_WMP2(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("los_colores_voy_a_decir")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_colores_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_colores_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_colores_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")
    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level2Memory2.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 2',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 2 Working Memory and Procedure Round 3 ###############
###########################################################################
@app.route("/L2/WMP/round3/<action>")
def actionL2_WMP3(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("los_medios_de_transporte")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_transporte_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_transporte_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_transporte_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    template = 'level2Memory3.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 3',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 2 Working Memory and Procedure Round 4 ###############
###########################################################################

@app.route("/L2/WMP/round4/<action>")
def actionL2_WMP4(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Un_elefante")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Elefante_1")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Elefante_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")

    template = 'level2Memory4.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 4',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 2 Working Memory and Procedure Round 5 ###############
###########################################################################

@app.route("/L2/WMP/round5/<action>")
def actionL2_WMP5(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("A_mi_burro")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Burro_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Burro_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Burro_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")

    template = 'level2Memory5.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 5',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 2 Working Memory and Procedure Round 6 ###############
###########################################################################

@app.route("/L2/WMP/round6/<action>")
def actionL2_WMP6(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("La_vaca_Lola")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vaca_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vaca_2")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")

    template = 'level2Memory6.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 6',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 2 Working Memory and Procedure Round 7 ###############
###########################################################################

@app.route("/L2/WMP/round7/<action>")
def actionL2_WMP7(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Dias_semana")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Semana_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Semana_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Semana_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")

    template = 'level2Memory7.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 7',
    }
    return render_template(template, **templateData)
###########################################################################
################ LVL 2 Working Memory and Procedure Round 8 ###############
###########################################################################
@app.route("/L2/WMP/round8/<action>")
def actionL2_WMP8(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Colores_2")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_colores2_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_colores2_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_colores2_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")

    template = 'level2Memory8.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 8',
    }
    return render_template(template, **templateData)
###########################################################################
################ LVL 2 Working Memory and Procedure Round 9 ###############
###########################################################################
@app.route("/L2/WMP/round9/<action>")
def actionL2_WMP9(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Numeros")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_numeros_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_numeros_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_numeros_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")

    template = 'level2Memory9.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 9',
    }
    return render_template(template, **templateData)
###########################################################################
################ LVL 2 Working Memory and Procedure Round 10 ###############
###########################################################################
@app.route("/L2/WMP/round10/<action>")
def actionL2_WMP10(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Meses")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pregunta_meses_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pregunta_meses_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pregunta_meses_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")

    template = 'level2Memory10.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 10',
    }
    return render_template(template, **templateData)


###########################################################################
################ LVL 2 Working Memory and Procedure Round 11 ###############
###########################################################################
@app.route("/L2/WMP/round11/<action>")
def actionL2_WMP11(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Sammy_heladero")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pregunta_sammy_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pregunta_sammy_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pregunta_sammy_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")

    template = 'level2Memory11.html'
    templateData = {
        'title' : 'Working Memory and Procedure Round 11',
    }
    return render_template(template, **templateData)


#########################################################
################ LVL 2 Physical Imitation ###############
#########################################################
@app.route("/L2/PI/<action>")
def actionL2_PI(action):
    template = 'level2Physical.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("explicacion_nv2_if")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")

    elif action == "explain2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Aerobicos")


    elif action == "song1":
        pubMovements.publish("dance")
        pubSpeaker.publish("Pista_pop")
    elif action == "song2":
        pubMovements.publish("dance")
        pubSpeaker.publish("Pista_electronica")
    elif action == "song3":
        pubMovements.publish("dance2")
        pubSpeaker.publish("pista_mapale")
    elif action == "song4":
        pubMovements.publish("dance")
        pubSpeaker.publish("pista_de_salsa")
    elif action == "song5":
        pubMovements.publish("dance")
        pubSpeaker.publish("pista_de_merengue")
    elif action == "song6":
        pubMovements.publish("dance")
        pubSpeaker.publish("Pista_reggaeton")
    elif action == "song7":
        pubMovements.publish("dance")
        pubSpeaker.publish("Pista_llanera")
    elif action == "song8":
        pubMovements.publish("dance")
        pubSpeaker.publish("Pista_aerobicos")
    elif action == "song9":
        pubMovements.publish("dance")
        pubSpeaker.publish("Cancion_paw_patrol")
    elif action == "song10":
        pubMovements.publish("dance")
        pubSpeaker.publish("Cancion_sonic")




    elif action == "movement1":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl2Movement1")
    elif action == "movement2":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl2Movement2")
    elif action == "movement3":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl2Movement3")
    elif action == "movement4":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl2Movement4")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("no")
    elif action=="t4":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("mirame")
    elif action=="t5":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_grites")
    elif action=="t6":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("No_llores")
    elif action=="t7":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("si")
    elif action=="t8":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Gracias")
    elif action=="t9":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
    	pubEmotions.publish("talk")
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level2PhysicalNames.html'

   
    templateData = {
        'title' : 'Physical Imitation',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 2 Physical Imitation Names ########
############################################################
@app.route("/L2/PI/names/<action>")
def actionL2_PI_names(action):
    template = 'level2PhysicalNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")


    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)


###########################################################################
################ LVL 2 Verbal Imitation #######################
###########################################################################
@app.route("/L2/VI/<action>")
def actionL2_VI(action):
    if action == "explain1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_escuchar_cancion")
        template = 'level2Verbal.html'
    elif action == "explain2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_responder_preguntas")
        template = 'level2Verbal.html'
    elif action == "round1":
        template = 'level2Verbal1.html'
    elif action == "round2":
        template = 'level2Verbal2.html'
    elif action == "round3":
        template = 'level2Verbal3.html'
    elif action == "round4":
        template = 'level2Verbal4.html'
    elif action == "names":
        template = 'level2VerbalNames.html'

    templateData = {
        'title' : 'Verbal Imitation 2',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 2 Verbal Imitation Names ########
############################################################
@app.route("/L2/VI/names/<action>")
def actionL2_VI_names(action):
    template = 'level2VerbalNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")

    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)


###########################################################################
################ LVL 2 Verbal Imitation Round 1 ###########################
###########################################################################
@app.route("/L2/VI/round1/<action>")
def actionL2_VI1(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_marcha_de_mi_tia_clementina")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_tia_clementina_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_tia_clementina_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_tia_clementina_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")
    elif action=="t7":
        pubSpeaker.publish("si")
    elif action=="t8":
        pubSpeaker.publish("Gracias")
    elif action=="t9":
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level2Verbal1.html'
    templateData = {
        'title' : 'Verbal Imitation Round 1',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 2 Verbal Imitation Round 2 ###########################
###########################################################################
@app.route("/L2/VI/round2/<action>")
def actionL2_VI2(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_sonido_de_los_animales")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_animales_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_animales_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_animales_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")
    elif action=="t7":
        pubSpeaker.publish("si")
    elif action=="t8":
        pubSpeaker.publish("Gracias")
    elif action=="t9":
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level2Verbal2.html'
    templateData = {
        'title' : 'Verbal Imitation Round 2',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 2 Verbal Imitation Round 3 ###########################
###########################################################################
@app.route("/L2/VI/round3/<action>")
def actionL2_VI3(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Los_pollitos")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_los_pollitos_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_los_pollitos_2")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")
    elif action=="t7":
        pubSpeaker.publish("si")
    elif action=="t8":
        pubSpeaker.publish("Gracias")
    elif action=="t9":
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level2Verbal3.html'
    templateData = {
        'title' : 'Verbal Imitation Round 3',
    }
    return render_template(template, **templateData)
###########################################################################
################ LVL 2 Verbal Imitation Round 4 ###########################
###########################################################################
@app.route("/L2/VI/round4/<action>")
def actionL2_VI4(action):
    if action == "start":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pollito_pio")
    elif action == "dance1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Baila_conmigo")
    elif action == "dance":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_bailar")


    elif action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pregunta_pollitopio_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pregunta_pollitopio_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Pregunta_pollitopio_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
    elif action == "gj9":
        pubEmotions.publish("happy")
        pubSpeaker.publish("bailaste_bien")



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")
    elif action=="t7":
        pubSpeaker.publish("si")
    elif action=="t8":
        pubSpeaker.publish("Gracias")
    elif action=="t9":
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
        pubSpeaker.publish("Se_dice_porfavor")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level2Verbal4.html'
    templateData = {
        'title' : 'Verbal Imitation Round 4',
    }
    return render_template(template, **templateData)


######################################
############### LVL 3 ################
######################################

@app.route("/L3")
def L3():
    templateData = {
        'title' : 'Nivel 3',
    }
    return render_template('level3.html', **templateData)

##############################################
################ LVL 3 Actions ###############
##############################################
@app.route("/L3/<action>")
def actionL3(action):
    print action
    if action == "FI_FA":
        template = 'level3IaA.html'
    elif action == "WMP":
        template = 'level3Memory.html'
    elif action == "PI":
        template = 'level3Physical.html'
    elif action == "VI":
        template = 'level3Verbal.html'

    templateData = {
        'title' : 'Nivel 3',
    }
    return render_template(template, **templateData)

##############################################################################
################ LVL 3 Follow Instructions and Focal Attention ###############
##############################################################################
@app.route("/L3/FI_FA/<action>")
def actionL3_FI_FA(action):
    template = 'level3IaA.html'
    if action == "songBattle":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_batalla_del_calentamiento")
    elif action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Seguir_indicaciones_sargento")


    elif action == "indication2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("dame_la_mano")
    elif action == "indication3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("salta")
    elif action == "indication4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("toca_mi_cabeza")
    elif action == "indication5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("toca_mis_pies")
    elif action == "indication6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("trae_el_carro")
    elif action == "indication7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("trae_la_oveja")
    elif action == "indication8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("trae_la_vaca")
    elif action == "indication14a":
        pubMovements.publish("talk_")
        pubSpeaker.publish("choca_los_cinco")
    elif action == "indication13a":
        pubMovements.publish("neutral")


    elif action == "indication9":
        pubMovements.publish("highfive")
    elif action == "indication10":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Aplaude_2")
    elif action == "indication11":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Una_vuelta")
    elif action == "indication12":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Tocar_botones")
    elif action == "indication13":
        pubEmotions.publish("talk")
        pubSpeaker.publish("agachar")
    elif action == "indication14":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cara_asombro")
    elif action == "indication15":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cara_enojo")
    elif action == "indication16":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cara_felicidad")
    elif action == "indication17":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cara_miedo")
    elif action == "indication18":
        pubEmotions.publish("talk")
        pubSpeaker.publish("cara_tristeza")
    elif action == "indication19":
        pubEmotions.publish("talk")
        pubSpeaker.publish("toca_boca")
    elif action == "indication20":
        pubEmotions.publish("talk")
        pubSpeaker.publish("toca_codos")
    elif action == "indication21":
        pubEmotions.publish("talk")
        pubSpeaker.publish("toca_cola")
    elif action == "indication22":
        pubEmotions.publish("talk")
        pubSpeaker.publish("toca_nariz")
    elif action == "indication23":
        pubEmotions.publish("talk")
        pubSpeaker.publish("toca_pies")
    elif action == "indication24":
        pubEmotions.publish("talk")
        pubSpeaker.publish("avion_izquierda")
    elif action == "indication25":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mano_derecha")
    elif action == "indication26":
        pubEmotions.publish("talk")
        pubSpeaker.publish("mano_izquierda")
    elif action == "indication27":
        pubEmotions.publish("talk")
        pubSpeaker.publish("manzana_derecha")
    elif action == "indication28":
        pubEmotions.publish("talk")
        pubSpeaker.publish("nariz_derecha")
    elif action == "indication29":
        pubEmotions.publish("talk")
        pubSpeaker.publish("nariz_izquierda")
    elif action == "indication30":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pie_derecho_robot")
    elif action == "indication31":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pie_izquierdo_robot")
    elif action == "indication33":
        pubEmotions.publish("talk")
        pubSpeaker.publish("vaca_izquierda")



    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")
    elif action=="t7":
        pubSpeaker.publish("si")
    elif action=="t8":
        pubSpeaker.publish("Gracias")
    elif action=="t9":
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
        pubSpeaker.publish("Se_dice_porfavor")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level3AttentionNames.html'
    

    
    templateData = {
        'title' : 'Follow Instrucction and Focal Attention',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 3 Focal Attention and Follow Instructions Names ########
############################################################
@app.route("/L3/FI_FA/names/<action>")
def actionL3_FI_FA_names(action):
    template = 'level3AttentionNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")
    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)


###################################################################
################ LVL 3 Working Memory and Procedure ###############
###################################################################
@app.route("/L3/WMP/<action>")
def actionL3_WMP(action):
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Completar_frase")
        template = 'level3Memory.html'
    elif action == "songBattle":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_batalla_del_calentamiento")
        template = 'level3Memory.html'

    elif action == "phrase1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_cielo_es_de_color")
        template = 'level3Memory.html'
    elif action == "phrase2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("El_tren_hace")
        template = 'level3Memory.html'
    elif action == "phrase3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Redondo_pelota")
        template = 'level3Memory.html'
    elif action == "phrase4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("hay_columpios_en_el")
        template = 'level3Memory.html'
    elif action == "phrase5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("los_zapatos_van_en_los")
        template = 'level3Memory.html'
    elif action == "explain2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Vamos_a_ver_pictograma")
        template = 'level3Memory.html'
    elif action == "explain3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Responder_pictogramas")
        template = 'level3Memory.html'
    elif action == "explain4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Escribir")
        template = 'level3Memory.html'


    elif action == "jose1":
        template = 'level3Memory1.html'
    elif action == "jose2":
        template = 'level3Memory2.html'
    elif action == "jose3":
        template = 'level3Memory3.html'
    elif action == "jose4":
        template = 'level3Memory4.html'
    elif action == "jose5":
        template = 'level3Memory5.html'
    elif action == "jose6":
        template = 'level3Memory6.html'
    elif action == "jose7":
        template = 'level3Memory7.html'
    elif action == "jose8":
        template = 'level3Memory8.html'
    elif action == "jose9":
        template = 'level3Memory9.html'
    elif action == "jose10":
        template = 'level3Memory10.html'

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
        template = 'level3Memory.html'
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
        template = 'level3Memory.html'
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
        template = 'level3Memory.html'
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
        template = 'level3Memory.html'
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
        template = 'level3Memory.html'
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
        template = 'level3Memory.html'
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
        template = 'level3Memory.html'
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")
	template = 'level3Memory.html'



    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
        template = 'level3Memory.html'
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
        template = 'level3Memory.html'
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
        template = 'level3Memory.html'
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
        template = 'level3Memory.html'
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
        template = 'level3Memory.html'
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
        template = 'level3Memory.html'
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
        template = 'level3Memory.html'
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
        template = 'level3Memory.html'
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
        template = 'level3Memory.html'
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
        template = 'level3Memory.html'
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
        template = 'level3Memory.html'
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
        template = 'level3Memory.html'
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
        template = 'level3Memory.html'
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
        template = 'level3Memory.html'
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")
        template = 'level3Memory.html'

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")
    elif action=="t7":
        pubSpeaker.publish("si")
    elif action=="t8":
        pubSpeaker.publish("Gracias")
    elif action=="t9":
        pubSpeaker.publish("alegra_escuchar")
    elif action=="t10":
        pubSpeaker.publish("Se_dice_porfavor")


    elif action == "happy":
        pubEmotions.publish("happy")
        template = 'level3Memory.html'
    elif action == "sad":
        pubEmotions.publish("sad")
        template = 'level3Memory.html'
    elif action == "angry":
        pubEmotions.publish("angry")
        template = 'level3Memory.html'
    elif action == "surprise":
        pubEmotions.publish("surprise")
        template = 'level3Memory.html'
    elif action == "neutral":
        pubEmotions.publish("neutral")
        template = 'level3Memory.html'
    elif action == "names":
        template = 'level3MemoryNames.html'

    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 3 Working Memory and Procedure Names ########
############################################################
@app.route("/L3/WMP/names/<action>")
def actionL3_WMP_names(action):
    template = 'level3MemoryNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")

    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 1 ###############
#############################################################################
@app.route("/L3/WMP/history1/<action>")
def actionL3_WMP1(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_calle_1")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_calle_2")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_calle_3")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_calle_4")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_calle_5")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_calle_6")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("jose_calle_p1")
    elif action == "question2":
        pubSpeaker.publish("jose_calle_p2")
    elif action == "question3":
        pubSpeaker.publish("jose_calle_p3")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level3Memory1.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 1',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 2 ###############
#############################################################################
@app.route("/L3/WMP/history2/<action>")
def actionL3_WMP2(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_cumpleanios_1")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_cumpleanios_2")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_cumpleanios_3")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_cumpleanios_4")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_5_cumpleanos")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_6_cumpleanos")
    elif action == "segment7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_7_cumpleanos")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("jose_cumpleanios_p1")
    elif action == "question2":
        pubSpeaker.publish("jose_cumpleanios_p2")
    elif action == "question3":
        pubSpeaker.publish("jose_cumpleanios_p3")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level3Memory2.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 2',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 3 ###############
#############################################################################
@app.route("/L3/WMP/history3/<action>")
def actionL3_WMP3(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_dientes_1")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_dientes_2")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_dientes_3")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_dientes_4")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_dientes_5")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_dientes_6")
    elif action == "segment7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_dientes_7")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("jose_dientes_p1")
    elif action == "question2":
        pubSpeaker.publish("jose_dientes_p2")
    elif action == "question3":
        pubSpeaker.publish("jose_dientes_p3")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level3Memory3.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 3',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 4 ###############
#############################################################################
@app.route("/L3/WMP/history4/<action>")
def actionL3_WMP4(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_1_banera")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_banera_2")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_banera_3")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_banera_4")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_banera_5")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_6_banera")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("jose_banera_p1")
    elif action == "question2":
        pubSpeaker.publish("jose_banera_p2")
    elif action == "question3":
        pubSpeaker.publish("jose_banera_p3")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    template = 'level3Memory4.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 4',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 5 ###############
#############################################################################
@app.route("/L3/WMP/history5/<action>")
def actionL3_WMP5(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_asustado_1")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_asustado_2")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_3_asustado")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_4_asustado")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_5_asustado")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_asustado_6")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("jose_asustado_p1")
    elif action == "question2":
        pubSpeaker.publish("Pregunta_2_asustado")
    elif action == "question3":
        pubSpeaker.publish("jose_asustado_p3")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level3Memory5.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 5',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 6 ###############
#############################################################################
@app.route("/L3/WMP/history6/<action>")
def actionL3_WMP6(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_enfadado_1")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_2_enfadado")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_enfadado_3")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_enfadado_4")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_5_enfadado")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_enfadado_6")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("jose_enfadado_p1")
    elif action == "question2":
        pubSpeaker.publish("jose_enfadado_p2")
    elif action == "question3":
        pubSpeaker.publish("jose_enfadado_p3")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level3Memory6.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 6',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 7 ###############
#############################################################################
@app.route("/L3/WMP/history7/<action>")
def actionL3_WMP7(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_sorprendido_1")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_sorprendido_2")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_3_sorprendido")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_4_sorprendido")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_sorprendido_5")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_sorprendido_6")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("Pregunta_1_asombrado")
    elif action == "question2":
        pubSpeaker.publish("jose_sorprendido_p2")
    elif action == "question3":
        pubSpeaker.publish("jose_sorprendido_p3")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level3Memory7.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 7',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 8 ###############
#############################################################################
@app.route("/L3/WMP/history8/<action>")
def actionL3_WMP8(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_triste_1")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_triste_2")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_triste_3")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_4_triste")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_triste_5")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_triste_6")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("jose_triste_p1")
    elif action == "question2":
        pubSpeaker.publish("jose_triste_p2")
    elif action == "question3":
        pubSpeaker.publish("Pregunta_3_triste")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level3Memory8.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 8',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 9 ###############
#############################################################################
@app.route("/L3/WMP/history9/<action>")
def actionL3_WMP9(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_contento_1")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Segmento_2_contento")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_contento_3")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_contento_4")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_contento_5")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_contento_6")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("jose_contento_p1")
    elif action == "question2":
        pubSpeaker.publish("jose_contento_p2")
    elif action == "question3":
        pubSpeaker.publish("jose_contento_p3")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level3Memory9.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 9',
    }
    return render_template(template, **templateData)

#############################################################################
################ LVL 3 Working Memory and Procedure History 10 ##############
#############################################################################
@app.route("/L3/WMP/history10/<action>")
def actionL3_WMP10(action):
    if action == "segment1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_manos_1")
    elif action == "segment2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_manos_2")
    elif action == "segment3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_manos_3")
    elif action == "segment4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_manos_4")
    elif action == "segment5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_manos_5")
    elif action == "segment6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("jose_manos_6")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "question1":
        pubSpeaker.publish("jose_manos_p1")
    elif action == "question2":
        pubSpeaker.publish("jose_manos_p2")
    elif action == "question3":
        pubSpeaker.publish("jose_manos_p3")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level3Memory10.html'
    templateData = {
        'title' : 'Working Memory and Procedure History 10',
    }
    return render_template(template, **templateData)

#########################################################
################ LVL 3 Physical Imitation ###############
#########################################################
@app.route("/L3/PI/<action>")
def actionL3_PI(action):
    template = 'level3Physical.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("explicacion_n3_if")
    elif action == "songBattle":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_batalla_del_calentamiento")

    elif action == "movement1":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl3Movement1")
    elif action == "movement2":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl3Movement2")
    elif action == "movement3":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl3Movement3")
    elif action == "movement4":
        pubEmotions.publish("happy")
        pubMovements.publish("lvl3Movement4")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level3PhysicalNames.html'
    
    templateData = {
        'title' : 'Physical Imitation',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 3 Physical Imitation Names ########
############################################################
@app.route("/L3/PI/names/<action>")
def actionL3_PI_names(action):
    template = 'level3PhysicalNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")

    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)

#########################################################
################ LVL 3 Verbal Imitation ###############
#########################################################
@app.route("/L3/VI/<action>")
def actionL3_VI(action):
    template = 'level3Verbal.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("explicacion_nv3_iv")
    elif action == "songBattle":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_batalla_del_calentamiento")

    elif action == "phrase1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_hielo_es_muy_frio")
    elif action == "phrase2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("en_el_parque_se_juega")
    elif action == "phrase3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("las_bicicletas_tienen_dos_llantas")
    elif action == "phrase4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("los_pinguinos_son_lindos")
    elif action == "phrase5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("me_gustan_los_perros")
    elif action == "phrase6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("frase6")
    elif action == "phrase7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("frase7")
    elif action == "phrase8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("frase8")
    elif action == "phrase9":
        pubEmotions.publish("talk")
        pubSpeaker.publish("frase9")
    elif action == "phrase10":
        pubEmotions.publish("talk")
        pubSpeaker.publish("frase10")

    elif action == "explain2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("canta_conmigo")


    elif action == "song1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("iguana")
    elif action == "song2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("ranita")
    elif action == "song3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("sammy")
    elif action == "song4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("serpiente")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level3VerbalNames.html'

    
    templateData = {
        'title' : 'Verbal Imitation',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 3 Verbal Imitation Names ########
############################################################
@app.route("/L3/VI/names/<action>")
def actionL3_VI_names(action):
    template = 'level3VerbalNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")

    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)

######################################
############### LVL 4 ################
######################################

@app.route("/L4")
def L4():
    templateData = {
        'title' : 'Nivel 4',
    }
    return render_template('level4.html', **templateData)

##############################################
################ LVL 4 Actions ###############
##############################################
@app.route("/L4/<action>")
def actionL4(action):
    print action
    if action == "FA":
        template = 'level4Attention.html'
    elif action == "WMP":
        template = 'level4Memory.html'
    elif action == "PI":
        template = 'level4Physical.html'
    elif action == "VI":
        template = 'level4Verbal.html'
    elif action == "FI":
        template = 'level4Instructions.html'

    templateData = {
        'title' : 'Nivel 4',
    }
    return render_template(template, **templateData)

######################################################
################ LVL 4 Focal Attention ###############
######################################################
@app.route("/L4/FA/<action>")
def actionL4_FA(action):
    template = 'level4Attention.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("explicacion_nv4_a")

    elif action == "story1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("aladdin")
    elif action == "story2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_aguila_y_la_zorra")
    elif action == "story3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_arbol_magico")
    elif action == "story4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_burro_magico")
    elif action == "story6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_gato_con_botas")
    elif action == "story7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_leon_y_el_raton")
    elif action == "story8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_nino_y_el_cohete")
    elif action == "story9":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_oro_y_las_ratas")
    elif action == "story10":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_patito_feo")
    elif action == "story12":
        pubEmotions.publish("talk")
        pubSpeaker.publish("hansel_y_gretel")
    elif action == "story13":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_casita_de_chocolate")
    elif action == "story14":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_gallinita_roja")
    elif action == "story16":
        pubEmotions.publish("talk")
        pubSpeaker.publish("simbad_el_marino")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")

    elif action=="t1":
        pubSpeaker.publish("todo_esta_bien")
    elif action=="t2":
        pubSpeaker.publish("no_pasa_nada")
    elif action=="t3":
        pubSpeaker.publish("no")
    elif action=="t4":
        pubSpeaker.publish("mirame")
    elif action=="t5":
        pubSpeaker.publish("No_grites")
    elif action=="t6":
        pubSpeaker.publish("No_llores")


    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level4AttentionNames.html'

    
    templateData = {
        'title' : 'Focal Attention',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 4 Focal Attention Names ########
############################################################
@app.route("/L4/FA/names/<action>")
def actionL4_FA_names(action):
    template = 'level4AttentionNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")

    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)

###################################################################
################ LVL 4 Working Memory and Procedure ###############
###################################################################
@app.route("/L4/WMP/<action>")
def actionL4_WMP(action):
    if action == "story1":
        template = 'level4Memory1.html'
    elif action == "story2":
        template = 'level4Memory2.html'
    elif action == "story3":
        template = 'level4Memory3.html'
    elif action == "story4":
        template = 'level4Memory4.html'
    elif action == "story5":
        template = 'level4Memory5.html'
    elif action == "story6":
        template = 'level4Memory6.html'
    elif action == "story7":
        template = 'level4Memory7.html'
    elif action == "story8":
        template = 'level4Memory8.html'
    elif action == "story9":
        template = 'level4Memory9.html'
    elif action == "story10":
        template = 'level4Memory10.html'
    elif action == "story12":
        template = 'level4Memory12.html'
    elif action == "story13":
        template = 'level4Memory13.html'
    elif action == "story14":
        template = 'level4Memory14.html'
    elif action == "story15":
        template = 'level4Memory15.html'
    elif action == "story16":
        template = 'level4Memory16.html'
    elif action == "names":
        template = 'level4MemoryNames.html'

    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 4 Working Memory and Procedure Names ########
############################################################
@app.route("/L4/WMP/names/<action>")
def actionL4_WMP_names(action):
    template = 'level4MemoryNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")

    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 4 Working Memory and Procedure Story 1 ###############
###########################################################################
@app.route("/L4/WMP/story1/<action>")
def actionL4_WMP1(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_aladdin_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_aladdin_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_aladdin_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory1.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 4 Working Memory and Procedure Story 2 ###############
###########################################################################
@app.route("/L4/WMP/story2/<action>")
def actionL4_WMP2(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_aguila_y_zorra_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_aguila_y_zorra_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_aguila_y_zorra_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory2.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 4 Working Memory and Procedure Story 3 ###############
###########################################################################
@app.route("/L4/WMP/story3/<action>")
def actionL4_WMP3(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_arbol_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_arbol_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_arbol_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    template = 'level4Memory3.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 4 Working Memory and Procedure Story 4 ###############
###########################################################################
@app.route("/L4/WMP/story4/<action>")
def actionL4_WMP4(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_burro_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_burro_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_burro_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory4.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 4 Working Memory and Procedure Story 6 ###############
###########################################################################
@app.route("/L4/WMP/story6/<action>")
def actionL4_WMP6(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_gato_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_gato_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_gato_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory6.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 4 Working Memory and Procedure Story 7 ###############
###########################################################################
@app.route("/L4/WMP/story7/<action>")
def actionL4_WMP7(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_leon_y_raton_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_leon_y_raton_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_leon_y_raton_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory7.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 4 Working Memory and Procedure Story 8 ###############
###########################################################################
@app.route("/L4/WMP/story8/<action>")
def actionL4_WMP8(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_ninio_y_cohete_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_ninio_y_cohete_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_ninio_y_cohete_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory8.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

###########################################################################
################ LVL 4 Working Memory and Procedure Story 9 ###############
###########################################################################
@app.route("/L4/WMP/story9/<action>")
def actionL4_WMP9(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_oro_y_ratas_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_oro_y_ratas_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_oro_y_ratas_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    template = 'level4Memory9.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

############################################################################
################ LVL 4 Working Memory and Procedure Story 10 ###############
############################################################################
@app.route("/L4/WMP/story10/<action>")
def actionL4_WMP10(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_patito_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_patito_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_patito_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory10.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

############################################################################
################ LVL 4 Working Memory and Procedure Story 12 ###############
############################################################################
@app.route("/L4/WMP/story12/<action>")
def actionL4_WMP12(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_hansel_y_gretel_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_hansel_y_gretel_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_hansel_y_gretel_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory12.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

############################################################################
################ LVL 4 Working Memory and Procedure Story 13 ###############
############################################################################
@app.route("/L4/WMP/story13/<action>")
def actionL4_WMP13(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_casa_chocolate1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_casa_chocolate2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_casa_chocolate3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory13.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

############################################################################
################ LVL 4 Working Memory and Procedure Story 14 ###############
############################################################################
@app.route("/L4/WMP/story14/<action>")
def actionL4_WMP14(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_gallinita_roja_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_gallinita_roja_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_gallinita_roja_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory14.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

############################################################################
################ LVL 4 Working Memory and Procedure Story 16 ###############
############################################################################
@app.route("/L4/WMP/story16/<action>")
def actionL4_WMP16(action):
    if action == "question1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_simbad_1")
    elif action == "question2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_simbad_2")
    elif action == "question3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("pregunta_simbad_3")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")

    template = 'level4Memory16.html'
    templateData = {
        'title' : 'Working Memory and Procedure',
    }
    return render_template(template, **templateData)

#########################################################
################ LVL 4 Physical Imitation ###############
#########################################################
@app.route("/L4/PI/<action>")
def actionL4_PI(action):
    template = 'level4Physical.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("explicacion_n4_if")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level4PhysicalNames.html'

    
    templateData = {
        'title' : 'Physical Imitation',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 4 Physical Imitation Names ########
############################################################
@app.route("/L4/PI/names/<action>")
def actionL4_PI_names(action):
    template = 'level4PhysicalNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")

    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)

######################################################
################ LVL 4 Verbal Imitation ###############
######################################################
@app.route("/L4/VI/<action>")
def actionL4_VI(action):
    template = 'level4Verbal.html'
    if action == "symphony":
        pubEmotions.publish("talk")
        pubSpeaker.publish("sinfonia_inconclusa_en_el_mar")
    elif action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Identificar_sinfonia")
    elif action == "story1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("aladdin")
    elif action == "story2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_aguila_y_la_zorra")
    elif action == "story3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_arbol_magico")
    elif action == "story4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_burro_magico")
    elif action == "story6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_gato_con_botas")
    elif action == "story7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_leon_y_el_raton")
    elif action == "story8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_nino_y_el_cohete")
    elif action == "story9":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_oro_y_las_ratas")
    elif action == "story10":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_patito_feo")
    elif action == "story11":
        pubEmotions.publish("talk")
        pubSpeaker.publish("el_sapito")
    elif action == "story12":
        pubEmotions.publish("talk")
        pubSpeaker.publish("hansel_y_gretel")
    elif action == "story13":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_casita_de_chocolate")
    elif action == "story14":
        pubEmotions.publish("talk")
        pubSpeaker.publish("la_gallinita_roja")
    elif action == "story16":
        pubEmotions.publish("talk")
        pubSpeaker.publish("simbad_el_marino")

    elif action == "stop":
        pubSpeakerAction.publish("stop")
    elif action == "pause":
        pubSpeakerAction.publish("pause")
    elif action == "play":
        pubSpeakerAction.publish("unpause")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level4VerbalNames.html'

    
    templateData = {
        'title' : 'Verbal Imitation',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 4 Verbal Imitation Names ########
############################################################
@app.route("/L4/VI/names/<action>")
def actionL4_VI_names(action):
    template = 'level4VerbalNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")
    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)

##########################################################
################ LVL 4 Follow Instructions ###############
##########################################################
@app.route("/L4/FI/<action>")
def actionL4_FI(action):
    template = 'level4Instructions.html'
    if action == "explain":
        pubEmotions.publish("talk")
        pubSpeaker.publish("explicacion_nv4_si")

    elif action == "place1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("nv_4_playa")
    elif action == "place2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("nv_4_cueva")
    elif action == "place3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("nv_4_parque_de_diversiones")
    elif action == "object1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("nv_4_balon")
    elif action == "object2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("nv_4_lapiz")
    elif action == "object3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Maleta")

    elif action == "gj1":
        pubEmotions.publish("happy")
        pubSpeaker.publish("muy_bien")
    elif action == "gj2":
        pubEmotions.publish("happy")
        pubSpeaker.publish("te_felicito")
    elif action == "gj3":
        pubEmotions.publish("happy")
        pubSpeaker.publish("que_bien")
    elif action == "gj4":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_lograste")
    elif action == "gj5":
        pubEmotions.publish("happy")
        pubSpeaker.publish("lo_hiciste_bien")
    elif action == "gj6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("felicitaciones")
    elif action == "gj7":
        pubEmotions.publish("happy")
        pubSpeaker.publish("excelente")
    elif action == "gj8":
        pubEmotions.publish("happy")
        pubSpeaker.publish("Sigamos_jugando")


    elif action == "nt1":
        pubEmotions.publish("sad")
        pubSpeaker.publish("intenta_otra_vez")
    elif action == "nt2":
        pubEmotions.publish("sad")
        pubSpeaker.publish("estuvo_cerca")
    elif action == "nt3":
        pubEmotions.publish("sad")
        pubSpeaker.publish("casi_lo_logras")
    elif action == "nt4":
        pubEmotions.publish("sad")
        pubSpeaker.publish("sigue_asi")
    elif action == "nt5":
        pubEmotions.publish("sad")
        pubSpeaker.publish("asi_es")
    elif action == "nt6":
        pubEmotions.publish("happy")
        pubSpeaker.publish("sigue_bailando")
    elif action=="nt7":
	pubEmotions.publish("sad")
        pubSpeaker.publish("no_te_escucho")
    elif action=="nt8":
	pubEmotions.publish("sad")
        pubSpeaker.publish("puedes_hablar_fuerte")
    elif action=="nt9":
	pubEmotions.publish("sad")
        pubSpeaker.publish("de_nada")
    elif action=="nt10":
	pubEmotions.publish("sad")
        pubSpeaker.publish("sientate")
    elif action=="nt11":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ven")
    elif action=="nt12":
	pubEmotions.publish("sad")
        pubSpeaker.publish("ponme_atencion")
    elif action == "me_duele":
        pubSpeaker.publish("Me_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "no_pegar":
        pubSpeaker.publish("No_me_pegues_duele")
        time.sleep(0.5)
        pubEmotions.publish("angry")
    elif action == "lastimar":
        pubSpeaker.publish("Me_estas_lastimando")
        time.sleep(0.5)
        pubEmotions.publish("sad")



    elif action == "happy":
        pubEmotions.publish("happy")
    elif action == "sad":
        pubEmotions.publish("sad")
    elif action == "angry":
        pubEmotions.publish("angry")
    elif action == "surprise":
        pubEmotions.publish("surprise")
    elif action == "neutral":
        pubEmotions.publish("neutral")
    elif action == "names":
        template = 'level4FollowNames.html'

    
    templateData = {
        'title' : 'Follow Instructions',
    }
    return render_template(template, **templateData)

############################################################
#### LVL 4 Follow Instructions Names ########
############################################################
@app.route("/L4/FI/names/<action>")
def actionL4_FI_names(action):
    template = 'level4FollowNames.html'
    if action == "name1":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Jose_emilio")
    elif action == "name2":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Belen")
    elif action == "name3":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Italo")
    elif action == "name4":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Gregor")
    elif action == "name5":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Yamir")
    elif action == "name6":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Padma")
    elif action == "name7":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Rafel")
    elif action == "name8":
        pubEmotions.publish("talk")
        pubSpeaker.publish("Arturo")

    templateData = {
        'title' : 'Names',
    }
    return render_template(template, **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
