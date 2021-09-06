import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import lasio
st.title("Aplicación para Registro de Pozos")
st.sidebar.title("Menu")
archivo_las=lasio.read("LGAE-040.las")
df=archivo_las.df()
archivo_las2 = st.sidebar.file_uploader("Cargar archivo LAS" , type=['.las', '.LAS'], key=None)


opciones_inicio=st.sidebar.radio("Seleccione una opción",["Inicio","Datos","Cálculos"])
if opciones_inicio=="Inicio":
	st.write("Sección Inicio")
	barra_deslizadora=st.slider("Seleccione un Valor",1000,10000,2000)
	st.write(barra_deslizadora)
	ingreso_numero=st.number_input("Ingrese un valor",min_value=0.00,max_value=11000.00,value=100.00)
	st.write(ingreso_numero)
	seleccion_columnas=df.columns
	st.write(len(seleccion_columnas))
	numero_de_graficas=int(st.number_input("Ingrese Numero de Graficas ",min_value=1,max_value=len(seleccion_columnas),value=2))
	lista=[0,0,0,0]
	st.write(lista)
	#for i in range(numero_de_graficas):
	#	st.write(i)
	#	lista[i]=st.selectbox("Seleccione curva",,seleccion_columnas)

	seleccion1=st.selectbox("Seleccione curva 1",seleccion_columnas)
	seleccion2=st.selectbox("Seleccione curva 2",seleccion_columnas)
	seleccion3=st.selectbox("Seleccione curva 3",seleccion_columnas)
	seleccion4=st.selectbox("Seleccione curva 4",seleccion_columnas)
	s=[seleccion1,seleccion2,seleccion3,seleccion4]
	st.write(s)
	df_limites=df[barra_deslizadora:ingreso_numero]
	df_filtrado=df_limites[s]
	#df_filtrado["DEPTH"]=df_filtrado.index
	st.write(df_filtrado)

	f,ax=plt.subplots(nrows=1,ncols=1,figsize=(16,100))
	ax.plot(df_filtrado["GR"],df_filtrado.index,color="brown")
	ax.invert_yaxis()
	ax.set_xlabel("TT3F")
	ax.set_ylabel("Profundidad")
	ax.grid()



	#def ploter():
	#	colors=["black","red","green","blue"]
	#	f,ax=plt.subplots(nrows=1,ncols=4,figsize=(16,100))
	#	for i,log,color in zip(range(4),s,colors):
	#		ax[i].plot(df_filtrado[log],df_filtrado.index,color=color)
	#		ax[i].invert_yaxis()
	#		ax[i].set_xlabel(log)
	#		ax[i].set_ylabel("Profundidad")
	#		ax[i].grid()

	#ploter()


if opciones_inicio=="Datos":
	st.write("Sección Datos")
	st.write(df)
	st.write("Prueba")

if opciones_inicio=="Cálculos":
	st.write("Sección Cálculos")