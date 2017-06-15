# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
from prettytable import PrettyTable
# url that we are scraping

url_nba_ficha = "http://www.espn.com.mx/basquetbol/nba/ficha?juegoId=40095451"
lista_url = [url_nba_ficha+"0" , url_nba_ficha+"1", url_nba_ficha+"2", url_nba_ficha+"3", url_nba_ficha+"4" ]
Lebron_J_a_J = [] 
Irving_J_J = []
Love_J_a_J = []
Durant_J_a_J = []
Curry_J_J = []
Thompson_J_a_J = []
for url in lista_url:
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, "lxml")
        name_box = soup.find('div', attrs={'class': 'row-wrapper'})  
        results = []
        for row in name_box:
                 table_headers = row.find_all('th')
                 if table_headers:
                     results.append([headers.get_text() for headers in table_headers])
                 table_data = row.find_all('td')
                 if table_data:
         	    results.append([data.get_text() for data in table_data])
        contador = 0
        lista_visita = []
        lista_casa= []
        for jugadores in results:
            if contador != 0 or contador != 2:
                nro_tips = len(jugadores)
        
            if contador == 1:
                    lista_visita.append(jugadores)
            if  contador == 3:
                    lista_casa.append(jugadores)
            contador += 1 
        lista_equipos = [lista_visita,lista_casa ]
        for equipo in lista_equipos:
            equipo = equipo[0]
            cuantos_items_por_titulares = len(equipo)
            hacer_cuantas_veces = (cuantos_items_por_titulares*1.000)/ 15
            hacer_cuantas_veces = int(hacer_cuantas_veces+1)
            numero_iteracion = 1
            principio_lista = 0
            fin_lista = 15
            lista_nueva = []
            lista_total = []
            equipo_completo = []
            for lista in range(1,hacer_cuantas_veces):
                    diccionario_pedidos = {}
                    lista_nueva = equipo[principio_lista:fin_lista]
                    principio_lista +=15
                    fin_lista += 15
                    if "DEL ENTRENADOR" in lista_nueva[1]:
                        print "No hacer nada 1"
                    elif "TEAM" in lista_nueva[0]:
                        print "No hacer nada 8"
                    elif "%" in lista_nueva[4]:
                        print "No hacer nada 4"
                    elif "%" in lista_nueva[8]:
                        print "No hacer nada 8"
                    elif "%" in lista_nueva[10]:
                        print "No hacer nada 10"
                    else:
                        equipo_completo.append(lista_nueva)
            table = PrettyTable([u'Titulares', u'Min', u'TC A-I', u'% TC3', u'TL A-I', u'OREB', u'DREB', u'REB', u'AST', u'STL', u'BLK', u'P\xe9r', u'PF', u'+/-', u'PTS'])
            for jugador in equipo_completo:
                    table.add_row([jugador[0].strip(),
                                   jugador[1].strip(),
                                   jugador[2].strip(),
                                   jugador[3].strip(), 
                                   jugador[4].strip(),
                                   jugador[5].strip(),
                                   jugador[6].strip(), 
                                   jugador[7].strip(), 
                                   jugador[8].strip(),
                                   jugador[9].strip(), 
                                   jugador[10].strip(), 
                                   jugador[11].strip(), 
                                   jugador[12].strip(),
                                   jugador[13].strip(),
                                   jugador[14].strip()
                                   ])
                    if 'L. James' in jugador[0]:
                        Lebron_J_a_J.append(jugador)   
                    elif 'Curry' in jugador[0]:
                        Curry_J_J.append(jugador)       
                    elif 'K. Durant' in jugador[0]:
                        Durant_J_a_J.append(jugador)   
                    elif 'K. Thompson' in jugador[0]:
                        Thompson_J_a_J.append(jugador)       
                    elif 'K. Love' in jugador[0]:
                        Love_J_a_J.append(jugador)   
                    elif 'K. Irving' in jugador[0]:
                        Irving_J_J.append(jugador)       
            print table
            
            print " "
            print " "
            print " "
lista_Lebron = []

for juego in Lebron_J_a_J:
    diccionario_1 = {}
    cestas_2 = juego[2]
    antes_de_guion = cestas_2.find("-")
    cestas = cestas_2[0:antes_de_guion]
    fallos = cestas_2[antes_de_guion+1:]
    
    diccionario_1["TC"] = cestas
    diccionario_1["F-TC"] = fallos
    diccionario_1["Min"] = juego[1]
    lista_Lebron.append(diccionario_1)
    
lista_Irving = []
for juego in Irving_J_J:
    diccionario_1 = {}
    cestas_2 = juego[2]
    antes_de_guion = cestas_2.find("-")
    cestas = cestas_2[0:antes_de_guion]
    fallos = cestas_2[antes_de_guion+1:]
    
    diccionario_1["TC"] = cestas
    diccionario_1["F-TC"] = fallos
    diccionario_1["Min"] = juego[1]
    lista_Irving.append(diccionario_1) 
    
    
Lista_Love = []
for juego in Love_J_a_J:
    diccionario_1 = {}
    print juego
    cestas_2 = juego[2]
    antes_de_guion = cestas_2.find("-")
    cestas = cestas_2[0:antes_de_guion]
    fallos = cestas_2[antes_de_guion+1:]
    
    diccionario_1["TC"] = cestas
    diccionario_1["F-TC"] = fallos
    diccionario_1["Min"] = juego[1]
    Love_J_a_J.append(diccionario_1)   
    
lista_Durant = []

for juego in Durant_J_a_J:
    diccionario_1 = {}
    cestas_2 = juego[2]
    antes_de_guion = cestas_2.find("-")
    cestas = cestas_2[0:antes_de_guion]
    fallos = cestas_2[antes_de_guion+1:]
    
    diccionario_1["TC"] = cestas
    diccionario_1["F-TC"] = fallos
    diccionario_1["Min"] = juego[1]
    lista_Durant.append(diccionario_1)   
     
lista_Curry = []

for juego in Curry_J_J:
    diccionario_1 = {}
    cestas_2 = juego[2]
    antes_de_guion = cestas_2.find("-")
    cestas = cestas_2[0:antes_de_guion]
    fallos = cestas_2[antes_de_guion+1:]
    
    diccionario_1["TC"] = cestas
    diccionario_1["F-TC"] = fallos
    diccionario_1["Min"] = juego[1]
    lista_Curry.append(diccionario_1)   
     
lista_Thompson = []

for juego in Thompson_J_a_J:
    diccionario_1 = {}
    cestas_2 = juego[2]
    antes_de_guion = cestas_2.find("-")
    cestas = cestas_2[0:antes_de_guion]
    fallos = cestas_2[antes_de_guion+1:]
    
    diccionario_1["TC"] = cestas
    diccionario_1["F-TC"] = fallos
    diccionario_1["Min"] = juego[1]
    lista_Thompson.append(diccionario_1)   
    
lista_Lista_Total = [lista_Lebron, lista_Irving, Lista_Love,lista_Durant, lista_Curry, lista_Thompson]
print lista_Lista_Total 
  
table_total = PrettyTable([u'Jugador', u'J1 Min', u'J1 TC', u'J2 Min', u'J2 TC', u'J3 Min', u'J3 TC', u'J4 Min', u'J4 TC', u'J5 Min', u'J5 TC'])
nombre_jugador = ["L. James","K. Irving","K. Love", "K. Durant" , "S. Curry", "S. Curry", 'K. Thompson' ]
jj = 0
for jugador in lista_Lista_Total:
                    table_total.add_row([nombre_jugador[jj].strip(),
                                   jugador[0]['J1 Min'].strip(),
                                   jugador[0]['J1 TC'].strip(),
                                   jugador[1]['J2 Min'].strip(),
                                   jugador[1]['J2 TC'].strip(),
                                   jugador[2]['J3 Min'].strip(),
                                   jugador[2]['J3 TC'].strip(),
                                   jugador[3]['J4 Min'].strip(),
                                   jugador[3]['J4 TC'].strip(),
                                   jugador[4]['J5 Min'].strip(),
                                   jugador[4]['J5 TC'].strip(),
                                   ])
                    jj += 1
                    
print table_total
    