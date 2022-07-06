from random import random

class Alumno:
    def __init__(self,nomb="",cod_alum=0,cod_curso="",prom=0):
        self.nomb=nomb
        self.cod_alum=cod_alum
        self.cod_curso=cod_curso
        self.prom=prom

    def random(self):
        self.nomb=(chr)((int)(random()*(90-65)+65))
        self.cod_alum=(int)(random()*(900-100)+100)
        self.cod_curso=(chr)((int)(random()*(90-87)+87))
        self.prom=(random()*(20-0)+0)

class ListaAlumno:
    def __init__(self):
        self.ListE=[]
        
    def insertar(self,objE):
        self.ListE.append(objE)
        
    def Mostrar(self):
        for i in range (0,len(self.ListE)):
            print("Nombre Alumno: ",self.ListE[i].nomb," Código Alumno: ",self.ListE[i].cod_alum," Código Curso: ",self.ListE[i].cod_curso," Promedio Final: ",self.ListE[i].prom)

    def Num_Curso(self):
        count=0
        count_1=0
        count_2=0
        for i in range (0,len(self.ListE)):
            if(self.ListE[i].cod_curso=="X"):
                count+=1
            elif(self.ListE[i].cod_curso=="Y"):
                count_1+=1
            elif(self.ListE[i].cod_curso=="W"):
                count_2+=1
        print("Número de Alumnos del curso X: ",count)
        print("Número de Alumnos del curso Y: ",count_1)
        print("Número de Alumnos del curso W: ",count_2)
                    
            
                
                
    
def main():
    objLista=ListaAlumno() 
    for i in range(1,11):
        objE=Alumno()
        objE.random()
        objLista.insertar(objE)
        
    objLista.Mostrar()
    objLista.Num_Curso()

 
main()
