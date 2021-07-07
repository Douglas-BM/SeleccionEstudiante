from src.seleccionestudiante.modelo.Asignatura import Asignatura, AsignaturaEstudiante
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.logica.Sorteo import Sorteo
from src.seleccionestudiante.modelo.declarative_base import Session, engine, Base
from datetime import datetime

def añadeRegistos():
   #Crea la BD
   Base.metadata.create_all(engine)

   #Abre la sesion
   session = Session()

   # crear estudiantes
   estudiante1 = Estudiante ( apellidoPaterno = "Vilchez" , apellidoMaterno = "Barsola" , nombres = "Luis" ,
                              elegible = True )

   session.add ( estudiante1 )
   session.commit ( )

   # crear asignatura
   asignatura1 = Asignatura ( nombreAsignatura = "Hello" )
   session.add ( asignatura1 )
   session.commit ( )

   # crear equipo de trabajo
   equipo1 = Equipo( denominacionEquipo = "Equipo09" )
   session.add ( equipo1 )
   session.commit ( )

   # crear actividad
   actividad1 = Actividad ( denominacionActividad = "Ayudar",fecha=datetime(2020, 9, 28, 00, 00, 00, 00000) )
   session.add ( actividad1 )
   session.commit ( )

   # Relacionar Asignatura con estudiantes
   asignatura1.estudiantes = [ estudiante1 ]
   session.commit()

   # Relacionar equipo con estudiantes
   equipo1.estudiantes = [ estudiante1 ]
   session.commit()

   # Relacionar Equipo de trabajo con actividad
   equipo1.actividades = [ actividad1 ]
   session.commit ( )

   session.close()

def eliminarRegistros():
   session = Session ( )

   estudiantes = session.query(Estudiante).all()
   for estudiante in estudiantes:
      session.delete(estudiante)
   session.commit()
   session.close()

   asignaturas=session.query(Asignatura).all()
   for asignatura in asignaturas:
      session.delete(asignatura)
   session.commit()
   session.close()

   actividades = session.query ( Actividad ).all()
   for actividad in actividades :
      session.delete ( actividad )
   session.commit ( )
   session.close ( )

   equipos = session.query ( Equipo ).all()
   for equipo in equipos :
      session.delete ( equipo )
   session.commit ( )
   session.close ( )

if __name__ == '__main__':
   sorteo=Sorteo()
   #sorteo.agregar_asignatura ( "Matemática discreta")
   while True:
      print ( "0 Salir" )
      print ( "1 Añadir registros" )
      print ( "2 Eliminar registros" )
      opcion = int ( input ( "Opción: " ) )
      if opcion == 0 :
         print ( "Fin..." )
         break
      elif opcion == 1 :
         añadeRegistos ( )
         print ( "Registros añadidos" )
      elif opcion == 2 :
         #eliminarRegistros ( )
         print ( "Registros eliminados" )
      else:
         print ( "Opción incorrecta" )
      print("\n\n\n")

