from src.seleccionestudiante.modelo.Asignatura import Asignatura, AsignaturaEstudiante
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.logica.Sorteo import Sorteo
from src.seleccionestudiante.modelo.declarative_base import Session, engine, Base
from datetime import datetime

if __name__ == '__main__':
   sorteo=Sorteo()
   #sorteo.agregar_asignatura ( "Gestion pro")
   sorteo.agregar_actividad ( denominacionActividad = "ley" , fecha = datetime ( 2021 , 9 , 25 , 00 , 00 , 00 , 00000 ))
   #sorteo.agregar_equipo ( "EquipoZ")
   #sorteo.agregar_estudiante ( "Cristobal","Mamani","Antonela",elegible = False)