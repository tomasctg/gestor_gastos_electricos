import streamlit as st
import pandas as pd

def detectar_tipo_residencial(consumo_kwh):
    if consumo_kwh <= 149:
        return 1  
    elif 150 <= consumo_kwh <= 299:
        return 2  
    else:
        return 3  

def extraer_tarifas(df,R):
    R1=["Residencial 1","Residencial 2"]
    R2=["Residencial 2","Residencial 3"]
    R3=["Residencial 3","Residencial 3"]
    
    if R == 1:
       tarifas = {
            "nivel_1": {},
            "nivel_2": {},
            "nivel_3": {},
            "electrodependientes": {}
        } 
    elif R==2 or R==3:
        tarifas = {
            "nivel_1": {},
            "nivel_2": {},
            "nivel_3_base": {},
            "nivel_3_excedente": {},
            "electrodependientes": {}
        }
    else:
        raise Exception
    
    stop = False
    column_num_2 = 0
    column_num_3 = 0 
    nivel_1 = 0
    nivel_2 = 0
    nivel_3 = 0
    nivel_3_base = 0
    nivel_3_excedente = 0
    electrodependientes = 0

    if R ==1:
        for i, row in df.iterrows():
            if stop:
                break
            for index, column in enumerate(row):
                if isinstance(column, str) and "Tarifa 2" in column:
                    stop = True
                    break
                if isinstance(column, str) and R1[0] in column:
                    column_num_2 = index
                if isinstance(column, str) and R1[1] in column:
                    column_num_3 = index
                if isinstance(column, str) and "Nivel 1" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_1 = index
                if isinstance(column, str) and "Nivel 2" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_2 = index
                if isinstance(column, str) and "Nivel 3" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_3 = index
                if isinstance(column, str) and "Electrodependientes" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        electrodependientes = index
                if isinstance(column, str) and "ALUMBRADO PUBLICO (ALP)" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        ALP =  float(df.iloc[i+2][index+2])
                        tarifas["nivel_1"]["ALP"] = ALP
                        tarifas["nivel_2"]["ALP"] = ALP
                        tarifas["nivel_3"]["ALP"] = ALP
                        tarifas["electrodependientes"]["ALP"] = ALP
                        stop = True
                        break
                if isinstance(column, str) and "Cargo Fijo" in column:
                    if index >= column_num_2 and index < column_num_3:
                        tarifas["nivel_1"]["cargo_fijo"] = float(df.iloc[i][index+3])
                        tarifas["nivel_2"]["cargo_fijo"] = float(df.iloc[i][index+4])
                        tarifas["nivel_3"]["cargo_fijo"] = float(df.iloc[i][index+5])
                        tarifas["electrodependientes"]["cargo_fijo"] = float(df.iloc[i][index+6])
                if isinstance(column, str) and "Cargo Variable " in column:
                    if index >= column_num_2 and index < column_num_3:
                        tarifas["nivel_1"]["cargo_variable"] = float(df.iloc[i][index+3])
                        tarifas["nivel_2"]["cargo_variable"] = float(df.iloc[i][index+4])
                        tarifas["nivel_3"]["cargo_variable"] = float(df.iloc[i][index+5])
                        tarifas["electrodependientes"]["cargo_variable"] = float(df.iloc[i][index+6])
    
    elif R==2:  
        for i, row in df.iterrows():
            if stop:
                break
            for index, column in enumerate(row):
                if isinstance(column, str) and "Tarifa 2" in column:
                    stop = True
                    break
                if isinstance(column, str) and R2[0] in column:
                    column_num_2 = index
                if isinstance(column, str) and R2[1] in column:
                    column_num_3 = index
                if isinstance(column, str) and "Nivel 1" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_1 = index
                if isinstance(column, str) and "Nivel 2" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_2 = index
                if isinstance(column, str) and "Nivel 3 base" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_3_base = index
                if isinstance(column, str) and "Nivel 3 Excedente" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_3_excedente = index
                if isinstance(column, str) and "Electrodependientes" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        electrodependientes = index
                if isinstance(column, str) and "ALUMBRADO PUBLICO (ALP)" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        ALP =  float(df.iloc[i+2][index+2])
                        tarifas["nivel_1"]["ALP"] = ALP
                        tarifas["nivel_2"]["ALP"] = ALP
                        tarifas["nivel_3_base"]["ALP"] = ALP
                        tarifas["nivel_3_excedente"]["ALP"] = ALP
                        tarifas["electrodependientes"]["ALP"] = ALP
                        stop = True
                        break
                if isinstance(column, str) and "Cargo Fijo" in column:
                    if index >= column_num_2 and index < column_num_3:
                        tarifas["nivel_1"]["cargo_fijo"] = float(df.iloc[i][index+2])
                        tarifas["nivel_2"]["cargo_fijo"] = float(df.iloc[i][index+3])
                        tarifas["nivel_3_base"]["cargo_fijo"] = float(df.iloc[i][index+4])
                        tarifas["nivel_3_excedente"]["cargo_fijo"] = float(df.iloc[i][index+5])
                        tarifas["electrodependientes"]["cargo_fijo"] = float(df.iloc[i][index+6])
                if isinstance(column, str) and "Cargo Variable " in column:
                    if index >= column_num_2 and index < column_num_3:
                        tarifas["nivel_1"]["cargo_variable"] = float(df.iloc[i][index+2])
                        tarifas["nivel_2"]["cargo_variable"] = float(df.iloc[i][index+3])
                        tarifas["nivel_3_base"]["cargo_variable"] = float(df.iloc[i][index+4])
                        tarifas["nivel_3_excedente"]["cargo_variable"] = float(df.iloc[i][index+5])
                        tarifas["electrodependientes"]["cargo_variable"] = float(df.iloc[i][index+6])
    elif R==3:  
        for i, row in df.iterrows():
            if stop:
                break
            for index, column in enumerate(row):
                if isinstance(column, str) and "Tarifa 2" in column:
                    stop = True
                    break
                if isinstance(column, str) and R3[0] in column:
                    column_num_2 = index
                    column_num_3 = column_num_2 + 8
                    
                if isinstance(column, str) and "Nivel 1" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_1 = index
                if isinstance(column, str) and "Nivel 2" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_2 = index
                if isinstance(column, str) and "Nivel 3 base" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_3_base = index
                if isinstance(column, str) and "Nivel 3 Excedente" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        nivel_3_excedente = index
                if isinstance(column, str) and "Electrodependientes" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        electrodependientes = index
                if isinstance(column, str) and "ALUMBRADO PUBLICO (ALP)" in column:
                    if index >= column_num_2 and index <= column_num_3:
                        ALP =  float(df.iloc[i+2][index+2])
                        tarifas["nivel_1"]["ALP"] = ALP
                        tarifas["nivel_2"]["ALP"] = ALP
                        tarifas["nivel_3_base"]["ALP"] = ALP
                        tarifas["nivel_3_excedente"]["ALP"] = ALP
                        tarifas["electrodependientes"]["ALP"] = ALP
                        stop = True
                        break
                if isinstance(column, str) and "Cargo Fijo" in column:
                    if index >= column_num_2 and index < column_num_3:
                        tarifas["nivel_1"]["cargo_fijo"] = float(df.iloc[i][index+2])
                        tarifas["nivel_2"]["cargo_fijo"] = float(df.iloc[i][index+3])
                        tarifas["nivel_3_base"]["cargo_fijo"] = float(df.iloc[i][index+4])
                        tarifas["nivel_3_excedente"]["cargo_fijo"] = float(df.iloc[i][index+5])
                        tarifas["electrodependientes"]["cargo_fijo"] = float(df.iloc[i][index+6])
                if isinstance(column, str) and "Cargo Variable " in column:
                    if index >= column_num_2 and index < column_num_3:
                        tarifas["nivel_1"]["cargo_variable"] = float(df.iloc[i][index+2])
                        tarifas["nivel_2"]["cargo_variable"] = float(df.iloc[i][index+3])
                        tarifas["nivel_3_base"]["cargo_variable"] = float(df.iloc[i][index+4])
                        tarifas["nivel_3_excedente"]["cargo_variable"] = float(df.iloc[i][index+5])
                        tarifas["electrodependientes"]["cargo_variable"] = float(df.iloc[i][index+6])
    
    return tarifas

def calcular_factura_completa(tarifas_dict, nivel, kwh_mes):

    if nivel not in tarifas_dict:
        raise ValueError(f"Nivel no válido. Usá uno de estos: {list(tarifas_dict.keys())}")
    
    datos = tarifas_dict[nivel]
    cargo_fijo = datos["cargo_fijo"]/2.0
    cargo_variable_unit = datos["cargo_variable"]
    alp = datos.get("ALP", 0.0)
    imp_ley_6922 = 582.20  

    cargo_variable = kwh_mes * cargo_variable_unit
    conceptos_electricos = cargo_fijo + cargo_variable + imp_ley_6922 + alp

    iva = conceptos_electricos * 0.21
    sobre_tasa_prov = conceptos_electricos * 0.03
    tasa_control = conceptos_electricos * 0.015
    ccce = conceptos_electricos * 0.09
    municipales = 34.78 + 4955.56

    total_impuestos = iva + sobre_tasa_prov + tasa_control + ccce + municipales
    total_final = conceptos_electricos + total_impuestos

    return {
        "Cargo Fijo": round(cargo_fijo, 2),
        "Cargo Variable": round(cargo_variable, 2),
        "ALP": round(alp, 2),
        "Impuesto Ley 6922": round(imp_ley_6922, 2),
        "Subtotal Conceptos Eléctricos": round(conceptos_electricos, 2),
        "IVA (21%)": round(iva, 2),
        "Sobretasa Provincial (3%)": round(sobre_tasa_prov, 2),
        "Tasa de Control (1.5%)": round(tasa_control, 2),
        "CCCE (9%)": round(ccce, 2),
        "Municipales (fijo)": round(municipales, 2),
        "Total Impuestos": round(total_impuestos, 2),
        "TOTAL A PAGAR": round(total_final, 2)
    }

def calcular_factura_detectando_R(df, consumo_kwh, nivel_manual):
    tipo_residencial = detectar_tipo_residencial(consumo_kwh)
    tarifas = extraer_tarifas(df, tipo_residencial)
    resultado = calcular_factura_completa(tarifas, nivel_manual, consumo_kwh)
    
    resultado["Tipo Residencial Detectado"] = f"R{tipo_residencial}"
    resultado["Nivel Seleccionado"] = nivel_manual
    return resultado

st.set_page_config(
    page_title="Calculadora de Factura Eléctrica",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #121212;
        color: #E0E0E0;
        font-family: 'Fira Code', monospace;
    }
    .stButton>button {
        background-color: #1f1f1f;
        color: white;
        border: 1px solid #555;
        border-radius: 6px;
    }
    .stTextInput>div>div>input {
        background-color: #1f1f1f;
        color: #fff;
    }
    .stSelectbox>div>div>div>div {
        background-color: #1f1f1f;
        color: #fff;
    }
    .stFileUploader>div>div {
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)


st.title("Calculadora de Factura Eléctrica")
st.markdown("Subí el archivo Excel de tarifas y completá tu consumo mensual para calcular la factura.")

uploaded_file = st.file_uploader("Archivo Excel de tarifas", type=["xlsx"])

if uploaded_file:
    consumo_kwh = st.number_input("Consumo mensual (kWh)", min_value=0.0, value=150.0)

    nivel_manual = st.selectbox(
        "Nivel de tarifa",
        ["nivel_1", "nivel_2", "nivel_3", "nivel_3_base", "nivel_3_excedente", "electrodependientes"]
    )

    if st.button("Calcular factura"):
        try:
            df_excel = pd.read_excel(uploaded_file, sheet_name="Anexo III", header=None)
            resultado = calcular_factura_detectando_R(df_excel, consumo_kwh, nivel_manual)

            st.subheader("Resultado")
            for k, v in resultado.items():
                if isinstance(v, (int, float)):
                    st.markdown(f"`{k}`: **${v:.2f}**")
                else:
                    st.markdown(f"`{k}`: **{v}**")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")