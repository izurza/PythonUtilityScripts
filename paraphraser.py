from paraphraser_utils import paraphrase
import argparse
parser = argparse.ArgumentParser(description='Paraphrase text using Quillbot.')
parser.add_argument('--data', required=True, help='The text to paraphrase.')
parser.add_argument('--configMode', default='Firefox', choices=['Firefox', 'Chrome'], help='Browser configuration mode.')
parser.add_argument('--limit', type=int, default=125, help='Word limit for each paraphrasing block.')
args = parser.parse_args()
    
paraphrase(data=args.data, configMode=args.configMode, limitWords=args.limit)

# data="""
# El oeste de Texas divide la frontera entre Mexico y Nuevo México. 
# Es muy bella pero aspera, llena de cactus, en esta region se encuentran las Davis Mountains.
# Todo el terreno esta lleno de piedra caliza,
# torcidos arboles de mezquite y espinosos nopales. 
# Para admirar la verdadera belleza desertica, visite el Parque Nacional de Big Bend, cerca de Brownsville.
# Es el lugar favorito para los excurcionistas, acampadores y entusiastas de las rocas.
# Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta region. 
# El area solo tiene dos estaciones, tibia y realmente caliente.
# La mejor epoca para visitarla es de Diciembre a Marzo cuando los dias son tibios,
# las noches son frescas y florecen las plantas del desierto con"""
# paraphrase(data=data,configMode="Firefox")