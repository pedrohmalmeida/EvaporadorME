import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

df=pd.read_csv("Tabela_agua_saturacao.txt")

def calculo_vazao_app(n_efeitos, lista_entalpia_solucao, lista_entalpia_vapor, lista_entalpia_liquido, hs, hf, F,xf,xn):
    teste = True
    end = False
    X = 0
    A = []
    B = []
    C = []
    D = []
    E = []

    Ln = F * xf/xn

    if n_efeitos >= 1:
        #Equação A
        #V1*(HL1-hG1) + S*hs =F*(HL1-hF)
        if teste:
            st.write(f'Equação A:')
            st.write(f'V1*({lista_entalpia_solucao[0]}-{lista_entalpia_vapor[0]}) + S*{hs} = {F}*({lista_entalpia_solucao[0]}-{hf})')
            st.write(f'V1*({lista_entalpia_solucao[0]}-{lista_entalpia_vapor[0]}) + S*{hs} = {F}*({lista_entalpia_solucao[0]}-{hf})')
        A1 = lista_entalpia_solucao[0]-lista_entalpia_vapor[0]
        B1 = 0
        C1 = 0
        D1 = 0
        E1 = 0
        S1 = hs
        R1 = F*(lista_entalpia_solucao[0]-hf)

    if n_efeitos > 2:
        #Equação B
        #V1*(hG1-hL1+HL2-HL1) + V2*(HL2 - hG2) = F*(HL2-HL1)
        if teste:
            st.write(f'Equação B:')
            st.write(f'V1*({lista_entalpia_vapor[0]}-{lista_entalpia_liquido[0]}+{lista_entalpia_solucao[1]}-{lista_entalpia_solucao[0]}) + V2*({lista_entalpia_solucao[1]} - {lista_entalpia_vapor[1]}) = {F}*({lista_entalpia_solucao[1]}-{lista_entalpia_solucao[0]})')
        A2 = lista_entalpia_vapor[0]-lista_entalpia_liquido[0]+lista_entalpia_solucao[1]-lista_entalpia_solucao[0]
        B2 = lista_entalpia_solucao[1] - lista_entalpia_vapor[1]
        C2 = 0
        D2 = 0
        E2 = 0
        S2 = 0
        R2 = F*(lista_entalpia_solucao[1]-lista_entalpia_solucao[0])

    if n_efeitos > 3:
        #Equação C
        #V1*(HL3 - HL2) + V2*(hG2 - hL2 + HL3 - HL2)  + V3*(HL3-hG3)= F*(HL3 - HL2)
        if teste:
            st.write(f'Equação C:')
            st.write(f'V1*({lista_entalpia_solucao[2]} - {lista_entalpia_solucao[1]}) + V2*({lista_entalpia_vapor[1]} - {lista_entalpia_liquido[1]} + {lista_entalpia_solucao[2]} - {lista_entalpia_solucao[1]})  + V3*({lista_entalpia_solucao[2]}-{lista_entalpia_vapor[2]})= F*({lista_entalpia_solucao[2]} - {lista_entalpia_solucao[1]})')
        A2 = lista_entalpia_solucao[2] - lista_entalpia_solucao[1]
        B2 = lista_entalpia_vapor[1] - lista_entalpia_liquido[1] + lista_entalpia_solucao[2] - lista_entalpia_solucao[1]
        C2 = lista_entalpia_solucao[2]-lista_entalpia_vapor[2]
        D2 = 0
        E2 = 0
        S2 = 0
        R2 = F*(lista_entalpia_solucao[2] - lista_entalpia_solucao[1])

    if n_efeitos > 4:
        #Equação D
        #V1*(HL4 - HL3) + V2*(HL4 - HL3) + V3*(hG3-hL3+HL4-HL3) +V4*(HL4-hG4) = F*(HL4-HL3)
        if teste:
            st.write(f'Equação D:')
            st.write(f'V1*({lista_entalpia_solucao[3]} - {lista_entalpia_solucao[2]}) + V2*({lista_entalpia_solucao[3]} - {lista_entalpia_solucao[2]})  + V3*({lista_entalpia_vapor[2]} - {lista_entalpia_liquido[2]} + {lista_entalpia_solucao[3]} - {lista_entalpia_solucao[2]}) + V4*({lista_entalpia_solucao[3]}-{lista_entalpia_vapor[3]})= F*({lista_entalpia_solucao[3]} - {lista_entalpia_solucao[2]})')
        A3 = lista_entalpia_solucao[3] - lista_entalpia_solucao[2]
        B3 = lista_entalpia_solucao[3] - lista_entalpia_solucao[2]
        C3 = lista_entalpia_vapor[2] - lista_entalpia_liquido[2] + lista_entalpia_solucao[3] - lista_entalpia_solucao[2]
        D3 = lista_entalpia_solucao[3]-lista_entalpia_vapor[3]
        E3 = 0
        S3 = 0
        R3 = F*(lista_entalpia_solucao[3] - lista_entalpia_solucao[2])

    if n_efeitos == 1:
        L1 = Ln
        Vsoma = F - L1
        
        #Equação Auxiliar
        #V1 = F - L1
        #S*hs= F*(hG-hf) + L1(HL1 - hv)
        if teste:
            st.write(f'Equação 1° Efeito:')
            st.write(f'V1*({0}) + S*({hs}) = {F}*({lista_entalpia_vapor[0] - hf}-L1*{lista_entalpia_solucao[0]} - {lista_entalpia_vapor[0]})')
       
        A2 = 0
        B2 = 0
        C2 = 0
        D2 = 0
        E2 = 0
        S2 = hs
        R2 = F*(lista_entalpia_vapor[0]-hf)  + L1*(lista_entalpia_solucao[0] - lista_entalpia_vapor[0])

        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        B.append([R1])
        B.append([R2])

        A = np.array(A)
        B = np.array(B)

        end = True


    if n_efeitos == 2:
        L2 = Ln
        Vsoma = F - L2
        #Equação 2° Efeit
        #V1*(hG1-hL1 + hG2 -  HL1) = F*(-HL1) + L2*HL2 + Vsoma* hG2
        if teste:
            st.write(f'Equação 2° Efeito:')
            st.write(f'V1*({lista_entalpia_vapor[0]} - {lista_entalpia_liquido[0]} + {lista_entalpia_vapor[1]} - {lista_entalpia_solucao[1]} = {F}*({-lista_entalpia_solucao[1]})  + {L2}*{lista_entalpia_solucao[1]} + {Vsoma} * {lista_entalpia_vapor[1]}')

        A2 = lista_entalpia_vapor[0] - lista_entalpia_liquido[0] + lista_entalpia_vapor[1] - lista_entalpia_solucao[1]
        B2 = 0
        C2 = 0
        D2 = 0
        E2 = 0
        S2 = 0
        R2 = F*(-lista_entalpia_solucao[1])  + L2*lista_entalpia_solucao[1] + Vsoma * lista_entalpia_vapor[1]

        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        B.append([R1])
        B.append([R2])

        A = np.array(A)
        B = np.array(B)
    
        end = True
   
    if n_efeitos == 3:
        L3 = Ln
        Vsoma = F - L3
        #Equação 3°Efeito
        #V1*(hG3 - HL2) + V2*(hG2 - hL2 + hG3 - HL2)  = F*(-HL2)  + L3*HL3 + Vsoma * hG3
        st.write(f'Equação 3° Efeito:')
        st.write(f'V1*({lista_entalpia_vapor[2]} - {lista_entalpia_solucao[1]}) + V2*({lista_entalpia_vapor[1]}-{lista_entalpia_liquido[1]}+{lista_entalpia_vapor[2]}-{lista_entalpia_solucao[1]}) = {F}*({-lista_entalpia_solucao[1]})  + {L3}*{lista_entalpia_solucao[2]} + {Vsoma} * {lista_entalpia_vapor[2]}')

        A3 = lista_entalpia_vapor[2] - lista_entalpia_solucao[1]
        B3 = lista_entalpia_vapor[1] - lista_entalpia_liquido[1] + lista_entalpia_vapor[2] - lista_entalpia_solucao[1]
        C3 = 0
        D3 = 0
        E3 = 0
        S3 = 0
        R3 = F*(-lista_entalpia_solucao[1])  + L3*lista_entalpia_solucao[2] + Vsoma * lista_entalpia_vapor[2]
        
        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        A.append([A3,B3,C3,D3,E3,S3])
        B.append([R1])
        B.append([R2])
        B.append([R3])

        st.write(A)
        end = True


    if n_efeitos == 4:
        L4 = Ln
        Vsoma = F - L4
        #Equação 4° Efeito
        #V1*( hG4 - HL3) + V2*(hG4 - HL3) + V3*(hG3 - hL3 + hG4 - HL3) = F*(-HL3)  + L4*HL4 + Vsoma * hG4

        st.write(f'Equação 4° Efeito:')
        st.write(f'V1*({lista_entalpia_vapor[3]} - {lista_entalpia_solucao[2]}) + V2*({lista_entalpia_vapor[3]} - {lista_entalpia_solucao[2]}) + V3*({lista_entalpia_vapor[2]}-{lista_entalpia_liquido[2]}+{lista_entalpia_vapor[3]}-{lista_entalpia_solucao[2]}) = {F}*({-lista_entalpia_solucao[2]})  + {L2}*{lista_entalpia_solucao[3]} + {Vsoma} * {lista_entalpia_vapor[3]}')

        A4 = lista_entalpia_vapor[3] - lista_entalpia_solucao[2]
        B4 = lista_entalpia_vapor[3] - lista_entalpia_solucao[2]
        C4 = lista_entalpia_vapor[2] - lista_entalpia_liquido[2] + lista_entalpia_vapor[3] - lista_entalpia_solucao[2]
        D4 = 0
        E4 = 0
        S4 = 0
        R4 = F*(-lista_entalpia_solucao[2])  + L4*lista_entalpia_solucao[3] + Vsoma * lista_entalpia_vapor[3]
        
        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        A.append([A3,B3,C3,D3,E3,S3])
        A.append([A4,B4,C4,D4,E4,S4])
        B.append([R1])
        B.append([R2])
        B.append([R3])
        B.append([R4])

        A = np.array(A)
        B = np.array(B)
        end = True


    if n_efeitos == 5:
        L5 = Ln
        Vsoma = F - L5
        #Equação 5° Efeito
        #V1*( hG5 - HL4) + V2*(hG5 - HL4) + V3*(hG5 - HL4) + V4* (hG4 - hL4 + hG5 - HL4)= F*(-HL4)  + L5*HL5 + Vsoma * hG5

        A5 = lista_entalpia_vapor[4] - lista_entalpia_solucao[3]
        B5 = lista_entalpia_vapor[4] - lista_entalpia_solucao[3]
        C5 = lista_entalpia_vapor[4] - lista_entalpia_solucao[3]
        D5 = lista_entalpia_vapor[3] - lista_entalpia_liquido[3] + lista_entalpia_vapor[3] - lista_entalpia_solucao[3]
        E5 = 0
        S5 = 0
        R5 = F*(-lista_entalpia_solucao[3])  + L5*lista_entalpia_solucao[4] + Vsoma * lista_entalpia_vapor[4]
                
        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        A.append([A3,B3,C3,D3,E3,S3])
        A.append([A4,B4,C4,D4,E4,S4])
        A.append([A5,B5,C5,D5,E5,S5])
        B.append([R1])
        B.append([R2])
        B.append([R3])
        B.append([R4])
        B.append([R5])

        A = np.array(A)
        B = np.array(B)
        end = True

    if end:
        #To simplify the code we ended up with collums with only zeros that distort the solution
        # Create a boolean index for columns that are not all zeros
        columns_not_zero = ~np.all(A == 0, axis=0)
        # Use the boolean index to filter out the columns that are all zeros
        A = A[:, columns_not_zero] 
        
        if teste:
            st.write(A)
            st.write(B)
        
        A = np.array(A)
        B = np.array(B)

        X = np.linalg.solve(A,B)
        X = X.tolist()
        return(X)

def calculo_vazao_completo(n_efeitos, lista_entalpia_solucao, lista_entalpia_vapor, lista_entalpia_liquido, hs, hf, F,xf,xl):
    A = []
    B = []
    C = []
    D = []
    E = []

    Ln = F * xf/xl

    if n_efeitos >= 1:
        #Equação A
        #V1*(HL1-hG1) + S*hs =F*(HL1-hF)
        print(f'Equação A:')
        print(f'V1*({lista_entalpia_solucao[0]}-{lista_entalpia_vapor[0]}) + S*{hs} = {F}*({lista_entalpia_solucao[0]}-{hf})')
        A1 = lista_entalpia_solucao[0]-lista_entalpia_vapor[0]
        B1 = 0
        C1 = 0
        D1 = 0
        E1 = 0
        S1 = hs
        R1 = F*(lista_entalpia_solucao[0]-hf)

    if n_efeitos > 2:
        #Equação B
        #V1*(hG1-hL1+HL2-HL1) + V2*(HL2 - hG2) = F*(HL2-HL1)
        print(f'Equação B:')
        print(f'V1*({lista_entalpia_vapor[0]}-{lista_entalpia_liquido[0]}+{lista_entalpia_solucao[1]}-{lista_entalpia_solucao[0]}) + V2*({lista_entalpia_solucao[1]} - {lista_entalpia_vapor[1]}) = {F}*({lista_entalpia_solucao[1]}-{lista_entalpia_solucao[0]})')
        
        A2 = lista_entalpia_vapor[0]-lista_entalpia_liquido[0]+lista_entalpia_solucao[1]-lista_entalpia_solucao[0]
        B2 = lista_entalpia_solucao[1] - lista_entalpia_vapor[1]
        C2 = 0
        D2 = 0
        E2 = 0
        S2 = 0
        R2 = F*(lista_entalpia_solucao[1]-lista_entalpia_solucao[0])

    if n_efeitos > 3:
        #Equação C
        #V1*(HL3 - HL2) + V2*(hG2 - hL2 + HL3 - HL2)  + V3*(HL3-hG3)= F*(HL3 - HL2)
        print(f'Equação C:')
        print(f'V1*({lista_entalpia_solucao[2]} - {lista_entalpia_solucao[1]}) + V2*({lista_entalpia_vapor[1]} - {lista_entalpia_liquido[1]} + {lista_entalpia_solucao[2]} - {lista_entalpia_solucao[1]})  + V3*({lista_entalpia_solucao[2]}-{lista_entalpia_vapor[2]})= F*({lista_entalpia_solucao[2]} - {lista_entalpia_solucao[1]})')
        A3 = lista_entalpia_solucao[2] - lista_entalpia_solucao[1]
        B3 = lista_entalpia_vapor[1] - lista_entalpia_liquido[1] + lista_entalpia_solucao[2] - lista_entalpia_solucao[1]
        C3 = lista_entalpia_solucao[2]-lista_entalpia_vapor[2]
        D3 = 0
        E3 = 0
        S3 = 0
        R3 = F*(lista_entalpia_solucao[2] - lista_entalpia_solucao[1])

    if n_efeitos > 4:
        #Equação D
        #V1*(HL4 - HL3) + V2*(HL4 - HL3) + V3*(hG3-hL3+HL4-HL3) +V4*(HL4-hG4) = F*(HL4-HL3)
        print(f'Equação D:')
        A4 = lista_entalpia_solucao[3] - lista_entalpia_solucao[2]
        B4 = lista_entalpia_solucao[3] - lista_entalpia_solucao[2]
        C4 = lista_entalpia_vapor[2] - lista_entalpia_liquido[2] + lista_entalpia_solucao[3] - lista_entalpia_solucao[2]
        D4 = lista_entalpia_solucao[3]-lista_entalpia_vapor[3]
        E4 = 0
        S4 = 0
        R4 = F*(lista_entalpia_solucao[3] - lista_entalpia_solucao[2])

    if n_efeitos == 1:
        L1 = Ln
        Vsoma = F - L1
        
        #Equação Auxiliar
        #V1 = F - L1
        #S*hs= F*(hG-hf) + L1(HL1 - hv)
        print(f'Equação 1° Efeito:')
        print(f'V1*({0}) + S*({hs}) = {F}*({lista_entalpia_vapor[0] - hf}-L1*{lista_entalpia_solucao[0]} - {lista_entalpia_vapor[0]})')
       
        A2 = 0
        B2 = 0
        C2 = 0
        D2 = 0
        E2 = 0
        S2 = hs
        R2 = F*(lista_entalpia_vapor[0]-hf)  + L1*(lista_entalpia_solucao[0] - lista_entalpia_vapor[0])

        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        B.append([R1])
        B.append([R2])

        A = np.array(A)
        B = np.array(B)
        # Create a boolean index for columns that are not all zeros
        columns_not_zero = ~np.all(A == 0, axis=0)
        print(columns_not_zero)
        # Use the boolean index to filter out the columns that are all zeros
        A = A[:, columns_not_zero]   

    if n_efeitos == 2:
        L2 = Ln
        Vsoma = F - L2
        #Equação 2° Efeit
        #V1*(hG1-hL1 + hG2 -  HL1) = F*(-HL1) + L2*HL2 + Vsoma* hG2
        print(f'Equação C:')
        print(f'V1*({lista_entalpia_vapor[0]} - {lista_entalpia_liquido[0]} + {lista_entalpia_vapor[1]} - {lista_entalpia_solucao[1]} = {F}*({-lista_entalpia_solucao[1]})  + {L2}*{lista_entalpia_solucao[1]} + {Vsoma} * {lista_entalpia_vapor[1]}')

        A2 = lista_entalpia_vapor[0] - lista_entalpia_liquido[0] + lista_entalpia_vapor[1] - lista_entalpia_solucao[1]
        B2 = 0
        C2 = 0
        D2 = 0
        E2 = 0
        S2 = 0
        R2 = F*(-lista_entalpia_solucao[1])  + L2*lista_entalpia_solucao[1] + Vsoma * lista_entalpia_vapor[1]

        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        B.append([R1])
        B.append([R2])

        A = np.array(A)
        B = np.array(B)
        # Create a boolean index for columns that are not all zeros
        columns_not_zero = ~np.all(A == 0, axis=0)
        print(columns_not_zero)
        # Use the boolean index to filter out the columns that are all zeros
        A = A[:, columns_not_zero]      
    
    if n_efeitos == 3:
        L3 = Ln
        Vsoma = F - L3
        #Equação 3°Efeito
        #V1*(hG3 - HL2) + V2*(hG2 - hL2 + hG3 - HL2)  = F*(-HL2)  + L3*HL3 + Vsoma * hG3
        print(f'Equação C:')
        print(f'V1*({lista_entalpia_vapor[2]} - {lista_entalpia_solucao[1]}) + V2*({lista_entalpia_vapor[1]}-{lista_entalpia_liquido[1]}+{lista_entalpia_vapor[2]}-{lista_entalpia_solucao[1]}) = {F}*({-lista_entalpia_solucao[1]})  + {L3}*{lista_entalpia_solucao[2]} + {Vsoma} * {lista_entalpia_vapor[2]}')

        A3 = lista_entalpia_vapor[2] - lista_entalpia_solucao[1]
        B3 = lista_entalpia_vapor[1] - lista_entalpia_liquido[1] + lista_entalpia_vapor[2] - lista_entalpia_solucao[1]
        C3 = 0
        D3 = 0
        E3 = 0
        S3 = 0
        R3 = F*(-lista_entalpia_solucao[1])  + L3*lista_entalpia_solucao[2] + Vsoma * lista_entalpia_vapor[2]
        
        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        A.append([A3,B3,C3,D3,E3,S3])
        B.append([R1])
        B.append([R2])
        B.append([R3])

        A = np.array(A)
        B = np.array(B)


    if n_efeitos == 4:
        L4 = Ln
        Vsoma = F - L4
        #Equação 4° Efeito
        #V1*( hG4 - HL3) + V2*(hG4 - HL3) + V3*(hG3 - hL3 + hG4 - HL3) = F*(-HL3)  + L4*HL4 + Vsoma * hG4

        print(f'Equação 4° Efeito:')
        print(f'V1*({lista_entalpia_vapor[3]} - {lista_entalpia_solucao[2]}) + V2*({lista_entalpia_vapor[3]} - {lista_entalpia_solucao[2]}) + V3*({lista_entalpia_vapor[2]}-{lista_entalpia_liquido[2]}+{lista_entalpia_vapor[3]}-{lista_entalpia_solucao[2]}) = {F}*({-lista_entalpia_solucao[2]})  + {L2}*{lista_entalpia_solucao[3]} + {Vsoma} * {lista_entalpia_vapor[3]}')

        A4 = lista_entalpia_vapor[3] - lista_entalpia_solucao[2]
        B4 = lista_entalpia_vapor[3] - lista_entalpia_solucao[2]
        C4 = lista_entalpia_vapor[2] - lista_entalpia_liquido[2] + lista_entalpia_vapor[3] - lista_entalpia_solucao[2]
        D4 = 0
        E4 = 0
        S4 = 0
        R4 = F*(-lista_entalpia_solucao[2])  + L4*lista_entalpia_solucao[3] + Vsoma * lista_entalpia_vapor[3]
        
        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        A.append([A3,B3,C3,D3,E3,S3])
        A.append([A4,B4,C4,D4,E4,S4])
        B.append([R1])
        B.append([R2])
        B.append([R3])
        B.append([R4])

        A = np.array(A)
        B = np.array(B)
        # Create a boolean index for columns that are not all zeros
        columns_not_zero = ~np.all(A == 0, axis=0)
        print(columns_not_zero)
        # Use the boolean index to filter out the columns that are all zeros
        A = A[:, columns_not_zero]

    if n_efeitos == 5:
        L5 = Ln
        Vsoma = F - L5
        #Equação 5° Efeito
        #V1*( hG5 - HL4) + V2*(hG5 - HL4) + V3*(hG5 - HL4) + V4* (hG4 - hL4 + hG5 - HL4)= F*(-HL4)  + L5*HL5 + Vsoma * hG5

        A5 = lista_entalpia_vapor[4] - lista_entalpia_solucao[3]
        B5 = lista_entalpia_vapor[4] - lista_entalpia_solucao[3]
        C5 = lista_entalpia_vapor[4] - lista_entalpia_solucao[3]
        D5 = lista_entalpia_vapor[3] - lista_entalpia_liquido[3] + lista_entalpia_vapor[3] - lista_entalpia_solucao[3]
        E5 = 0
        S5 = 0
        R5 = F*(-lista_entalpia_solucao[3])  + L5*lista_entalpia_solucao[4] + Vsoma * lista_entalpia_vapor[4]
        
        A.append([A1,B1,C1,D1,E1,S1])
        A.append([A2,B2,C2,D2,E2,S2])
        A.append([A3,B3,C3,D3,E3,S3])
        A.append([A4,B4,C4,D4,E4,S4])
        A.append([A5,B5,C5,D5,E5,S5])
        B.append([R1])
        B.append([R2])
        B.append([R3])
        B.append([R4])
        B.append([R5])

        A = np.array(A)
        B = np.array(B)
        # Create a boolean index for columns that are not all zeros
        columns_not_zero = ~np.all(A == 0, axis=0)
        print(columns_not_zero)
        # Use the boolean index to filter out the columns that are all zeros
        A = A[:, columns_not_zero]


    # Create a boolean index for columns that are not all zeros
    columns_not_zero = ~np.all(A == 0, axis=0)
    print(columns_not_zero)
    # Use the boolean index to filter out the columns that are all zeros
    A = A[:, columns_not_zero]
    print(A)
    print(B)
    print(f'A shape: {A.shape}')
    print(f'B shape: {B.shape}')
    
    X = np.linalg.solve(A,B)
    X = X.tolist()
    return(X)

def Tabela_Vapor_Sat_app(X, column_from, column_get):
    df=pd.read_csv("Tabela_agua_saturacao.txt")
    debug = False
    def number_up(x,plus,rd):
        x = x + plus
        x = round(x, rd)
        return x
    def number_down(x,plus,rd):
        x = x - plus
        x = round(x, rd)
        return x

    def interpolate(x1: float, x2: float, y1: float, y2: float, x: float):
        """Perform linear interpolation for x between (x1,y1) and (x2,y2) """

        return ((y2 - y1) * x + x2 * y1 - x1 * y2) / (x2 - x1)
    
    if column_from == 'P (MPa)':
        plus = 0.0001
        rd = 4
    elif column_from == 'T (°C)':
        plus = 0.001
        rd = 3
    elif  column_from == 'Enthalpy Liquid (kJ/kg)' or 'Enthalpy Vapor (kJ/kg)' or 'Enthalpy of Vaporization (kJ/kg)':
        plus = 0.01
        rd = 2

    if debug: 
        st.write(f'{X=}')
        st.write(f'{column_from=}')
        st.write(f'{column_get=}')
        st.write(f'{plus=}, {rd=}')
    Xinicial = X
    series = df[column_from]
    x = series.isin([X]) #creates something with a lot of Falses
    x = x.values #X = list of false/True
    test_up = True
    test_down = True
    value_in_table = True in x
    if debug:
        st.write(f'{X=}')
        st.write(f'{series=}')
        st.write(f'{value_in_table=}')
    #print('Pesquisando na Tabela...')
    if value_in_table:
        row = df.loc[lambda df: df[column_from] == X]
        Y = row[column_get].values[0]
        if debug:
            st.write(f'Value from straight from table: {Y=}')       
        
    else:
        if debug:
            st.write(f'Searching values to interpolate: {test_up=} {test_down=}')       
        if test_up:
            if debug:
                st.write(f'Searching for next value: {test_up=}')       
            i = 0
            while test_up:
                X = number_up(X,plus,rd)
                X_up = X
                x = series.isin([X])
                x = x.values #X = list of false/True
                value_in_table = True in x
                if debug:
                    print(X_up) #Linha para debugar
                i+=1
                if i == 10000:
                    st.write('Error cant find number')
                    break
                if value_in_table:
                    #print(f'Found {X_up=}')
                    row = df.loc[lambda df: df[column_from] == X_up]
                    Y_up = row[column_get].values[0]
                    test_up = False
                    if debug:
                        st.write(f'Next value found: {Y_up=}')
                    continue
                
        if test_down:
            if debug:
                st.write(f'Searching for last value: {test_down=}')       
            i = 0
            while test_down:
                X = number_down(X, plus, rd)
                X_down = X
                x = series.isin([X])
                x = x.values #X = list of false/True
                value_in_table = True in x
                if debug:
                    print(X_down) #Linha para debugar
                i+=1
                if i == 10000:
                    st.write('Error cant find number')
                    break
                if value_in_table:
                    #print(f'Found {X_down=}')
                    row = df.loc[lambda df: df[column_from] == X_down]
                    Y_down = row[column_get].values[0]
                    test_down = False
                    if debug:
                        st.write(f'Last value found: {Y_up=}')
                    continue
    if debug:
        st.write(f'{Y_up=}\n{Y_down=}')
    if not test_down:
        #print('\nRealizando interpolação de {Y_up} e {Y_down}')
        Y = interpolate(X_up,X_down,Y_up,Y_down,Xinicial)
    #print(f'\n\nPara {column_from} {Xinicial} temos uma {column_get} de {Y}')
    if debug:
        st.write(Y)
    Y = round(Y,4)
    return Y.item()

if 'modo' not in st.session_state:
        st.session_state['modo'] = 'Apresentacao'
if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 'Introducao'
if 'lista_novo_delta_T' not in st.session_state:
    st.session_state.lista_novo_delta_T = []
def find_zero_keys(d):
    zero_keys = []
    for key, value in d.items():
        if isinstance(value, list):  # Check if any value in the list is 0
            if 0 in value:
                zero_keys.append(key)
        else:  # Direct check if not a list
            if value == 0:
                zero_keys.append(key)
    return zero_keys

modo = ['Tutorial', 'Educacional', 'Calculo','Instrucao']
#Página Inical
def blue_line():
    st.markdown("""
    <hr style="border: 2px solid blue;">
    """, unsafe_allow_html=True)

if __name__ == "__main__":

    if st.session_state.modo == 'Apresentacao':
        st.subheader('S.Pr.E.M.E.: Solucionador de Projetos de Evaporador de Múltiplos Efeitos')
        st.image(Image.open(f'img_evaporadores/Img_evaporador_me.png'))
        st.write('O evaporador de múltiplos efeitos é crucial na indústria, especialmente na concentração de soluções no setor alimentício. Devido à sua complexidade e aos extensos cálculos, a versão de múltiplos efeitos é frequentemente subestimada no ensino de engenharia, que se foca mais nos evaporadores de efeito único.')    
        st.write('Este programa foi desenvolvido para suprir essa lacuna, apresentando de forma clara e objetiva todos os conceitos e equações. Com esta ferramenta, o futuro engenheiro pode se concentrar na compreensão do funcionamento, otimização e limitações do equipamento.')    
        st.divider()
        st.write('_Desenvolvido por Pedro Almeida (TCC: [link]), com a orientação de Lívia Chaguri ([link]) e apoio de Luiz Eleno ([link])._')
        blue_line()

        col1, col2 = st.columns(2)

        with col1:
            if st.button('Instrução'):
                st.session_state.modo = 'Instrucao'
                st.rerun()
            st.write('Selecione o botão acima para ver as instruções deste programa')

        with col2:
            if st.button('Cálculo'):
                st.session_state.modo = 'Calculo'
                st.session_state.etapa = 'Efeitos'
                st.rerun()
            st.write('Selecione o botão acima para avançar para o desenvolvimento de cálculos')

        blue_line()

    if st.session_state.modo == 'Tutorial':
        st.header('Tutorial')
        st.write('Este programa possui 3 tipos de interação com o usuário: **botões**, **toogles** e **inputs**:')
        blue_line()
        st.write('Um **toogle** possui o formato de uma barra arredondada com uma bola dentro.')
        st.write('Ao ser acionado ele revela uma seção escondida, empurrando o resto da página para baixo.')
        st.write('Acione o toogle abaixo para ver a informação escondida.')
        if st.toggle('Ativar'):
            st.write('Veja que o toogle mudou de cor, indicando estar ativado.')
            st.divider()
            st.write('Esta ferramenta é utilizada quando um conjunto extenso de informação esta associado ao tema discutido na seção, mas sua implementação extende muito a página de modo a atrapalhar a compreenção do usuário.')
            st.divider()
            st.write('Acione novamente para esta informação sumir')

        blue_line()
        
        st.write('Um **input** possui diversos formatos e tem como objetivo coletar alguma informação, com um texto acompanhando para informar o tipo de informação que deve ser detalhada.')
        st.write('Um conjunto de inputs podem ser combinados a fim de se obter uma interação complexa')
        st.divider()
        mes = st.number_input('Este é um **input número**, digite o número do mês atual',min_value=1,)
        nome = st.text_input('Este é um **input texto**, escreva seu nome abaixo',placeholder='Qual é o seu nome?')
        lista_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']    
        
        if mes >12:
            st.warning('Parabéns você encontrou o primeiro bug! Este bug indica que que o programa foi construído para atuar dentro de um limite. (max range = 12 (meses))')

        if mes and nome:
            st.write(f'{nome}, você gosta de {lista_mes[mes-1]}?')
            resposta_sim = st.checkbox('Eu gosto')
            resposta_nao = st.checkbox('Eu não gosto')
            if resposta_sim:
                st.success(f'{nome} gosta de {lista_mes[mes-1]}')
            elif resposta_nao:
                st.error(f'{nome} não gosta de {lista_mes[mes-1]}')
            if resposta_sim and resposta_nao:
                st.warning('Parabéns você encontrou o segundo bug! Este bug não quebra o programa, mas pode gerar confusão quanto aos dados usados pelo programa')
            elif resposta_sim or resposta_nao:
                st.warning('Este programa foi testado multiplas vezes, entretando Bugs são sempre possíveis, não deixe de anotar em papel os dados com o caminhar do programa.')
                st.warning('Tente bugar as caixas acima (existem 2 maneiras)')
        blue_line()
        
        st.write('Um **botão** possui o formato de uma caixa com um texto interno.')
        st.write('Ao ser acionado ele pode abrir uma nova página e, a depender da sequencia do cálculo, seu acesso à páginas anteriores será limitada.')
        st.write('Você utilizou um botão para chegar aqui, use o abaixo para retornar.')
        if st.button('Retornar'):
            st.session_state.modo = 'Apresentacao'
            st.rerun()        

    if st.session_state.modo == 'Instrucao':
        st.write("## 📘 Instruções")
        st.write("""
    1. Selecione o botão **“Cálculo”** para iniciar o cálculo de um projeto

    2. Selecione o modelo de evaporador na página de **Número de Efeitos**:
    - Verifique os dados necessários e as páginas de cálculo através da imagem
    - Clique no botão **“Avançar”**

    3. Para cada conjunto de dados na página de **Coleta de Dados**:
    - Informe os dados disponíveis
    - Selecione as unidades adequadas
    - Verifique os dados inseridos através das tabelas disponibilizadas
    - Verifique a presença da tarja verde **“Dados completos”** e avance com o botão **“Avançar”**

    5. Avance por cada página de cálculo usando o *toogle* para verificar as fórmulas usadas em cada página  
    _Não há necessidade de input de dados nas seguintes páginas:_
    - Cálculo de Frações
    - Cálculo de Temperatura
    - Cálculo de Entalpia da água
    - Cálculo de nova Temperatura
    - Cálculo de Vazão e Área
    - Cálculo de Economia

    6. Na página de **Cálculo de Entalpia de Solução**:
    - Informe as entalpias para as frações e temperaturas informadas:
        - Utilize as fórmulas apresentadas pelo exercício
        - ou
        - Selecione uma das ferramentas disponíveis no final da página
    - Verifique a presença da tarja verde **“Dados completos”** e avance com o botão **“Avançar”**

    7. Na página de **Cálculo de Vazão e Área** *(Avaliação)*, verifique a tarja no final dos cálculos:
    - Se a tarja for **vermelha**, clique em **“Avançar”** para reacalcular a temperatura
    - Se a tarja for **verde**, clique em **“Avançar”** para ir para a última página
                
    8. Os dados principais obtidos do exercício são disponibilizados em tabelas na página **Economia**.
    """)
        st.divider()
        st.subheader('Sequência de Páginas')
        image = Image.open(f'img_diagrama/Guia_paginas.png')
        st.image(image)
        if st.button('Retornar'):
            st.session_state.modo = 'Apresentacao'
            st.rerun()   
    #Início dos cálculo
    if st.session_state.modo == 'Calculo':
        st.write('### Etapas de Projeto:')
        if st.session_state.etapa == 'Efeitos': number = '1'
        elif st.session_state.etapa == 'Dados': number = '2'
        elif st.session_state.etapa == 'Vazao': number = '4'
        elif st.session_state.etapa == 'Economia': number = '5'
        else: number = '3'
        image_path = f'img_diagrama/Guia_paginas{number}.png'

        image = Image.open(image_path)
        st.image(image)
        st.divider()
        if st.session_state.etapa == 'Efeitos':
            st.subheader('Etapa 1 - Definindo o Evaporador')
            st.session_state.n_efeitos = st.selectbox("Qual é o número de efeitos?", ("2", "3", "4", "5"))
            
            st.divider()
            
            st.write('### Características do Evaporador:')
            st.write(f'Verifique se todos os dados necessários para o cálculo estão disponíveis :green[(**verde**)]:')
            effect_number = st.session_state.n_efeitos
            image = Image.open(f'img_evaporadores/evaporador{st.session_state.n_efeitos}.png')
            st.image(image)

            st.divider()
            if st.button('Avançar'):
                st.session_state.etapa = 'Dados'
                st.rerun()

        #Coleta de Dados
        if st.session_state.etapa == 'Dados':
            st.subheader('Dados de Solução')
            if st.checkbox('Autopreencher - Teste'):
                st.session_state.n_efeitos = '3'
                st.session_state.vazao_F = 46000
                st.session_state.Tf = 40
                st.session_state.xf = 0.1
                st.session_state.xsaida = 0.5
                st.session_state.xn = 0.5
                st.session_state.P_vapor_aquecimento_kgf = 2.0
                st.session_state.P_saida_kgf = 0.068
                st.session_state.P_saida_MPa = round((st.session_state.P_saida_kgf) * 0.0981, 4)
                st.session_state.P_vapor_aquecimento_MPa = round(st.session_state.P_vapor_aquecimento_kgf * 0.0981, 4)
                st.session_state.lista_EPE = [5, 9, 39]
                st.session_state.lista_coef_TC = [5400, 2950, 1950]
                st.write("Número de efeitos = 3")
                st.write("Vazão inicial em [kg/h] = 46000")
                st.write("Temperatura Inicial [°C] = 40")
                st.write("Fração na entrada e saída = 0.1 - 0.5")
                st.write("Pressão no vapor de aquecimento [kgf] = 2")
                st.write(f"Pressão no último efeito [kgf] = 0.068, {st.session_state.P_saida_MPa} [MPa]")
                st.write("Elevação do ponto de ebulição [°C] = [5, 9, 39]")
                st.write("Coeficiente de troca de calor [W/(m^2 * °C)] = [5400,2950,1950]")

                col = ['Alimentação']
                for n in range(int(st.session_state.n_efeitos)):
                    col.append(f'{n+1}° efeito')

                vazao_sol = [st.session_state.vazao_F,'?','?','?']
                temp = [st.session_state.Tf,'?','?','?']
                fracao = [st.session_state.xf,'?','?',st.session_state.xsaida]
                pressao = [st.session_state.P_vapor_aquecimento_kgf,'-','-',st.session_state.P_saida_kgf]
                epe = ['-'] + st.session_state.lista_EPE
                U = ['-'] + st.session_state.lista_coef_TC
                st.session_state.df_dados_iniciais = pd.DataFrame([vazao_sol,temp,fracao,pressao,epe,U],['Vazão Solução [kg/h]','Temperatura [°C]','Fração [adm]','Pressão [kgf/cm^2]','EPE [°C]','U [kcal/hm2°C]'],columns=col).style.format(precision=2)
                st.table(st.session_state.df_dados_iniciais)

                if st.button('Avançar'):
                    st.session_state.etapa = 'Fracao'
                    st.rerun()

            else:        
                st.session_state.vazao_F = st.number_input("Qual é a vazão inicial da solução em [kg/h]?",0)
                st.session_state.Tf = st.number_input('Qual é a Temperatura de entrada em [°C]?\n')
                st.session_state.xf = st.number_input('Qual é a fração de sólidos na entrada [adm]?\n',min_value=0.0)
                st.session_state.xsaida = st.number_input('Qual é a fração de sólidos na saída [adm]?\n',min_value=0.0)
                st.session_state.xn = st.session_state.xsaida
                dados1 = {'F [kg/h]':[st.session_state.vazao_F],
                        'Tf [°C]':[st.session_state.Tf],
                        'xf [adm]':[st.session_state.xf],
                        'xn':[st.session_state.xsaida]
                        }
                st.table(dados1)


                st.divider()
                st.subheader("Dados de pressão")
                Unidades = ['kg/cm2','Pa','kPa','MPa']
                unidade = st.radio('Escolha que unidade você quer trabalhar com a Pressão abaixo:',Unidades)
                if unidade == 'kg/cm2':
                    st.session_state.P_vapor_aquecimento_kgf = st.number_input('Qual é a pressão do vapor de aquecimento no primeiro efeito [kgf/cm^2]?\n')
                    st.session_state.P_saida_kgf = st.number_input('Qual é a pressão na saída do último efeito [kgf/cm^2]?\n')
                    st.session_state.P_vapor_aquecimento_MPa = round(st.session_state.P_vapor_aquecimento_kgf * 0.0981, 4)
                    st.session_state.P_saida_MPa = round(st.session_state.P_saida_kgf * 0.0981, 4)
                elif unidade == 'Pa':
                    st.session_state.P_vapor_aquecimento_kgf = st.number_input('Qual é a pressão do vapor de aquecimento no primeiro efeito [Pa]?\n')
                    st.session_state.P_saida_kgf = st.number_input('Qual é a pressão na saída do último efeito [MPa]?\n')
                    st.session_state.P_vapor_aquecimento_MPa = round(st.session_state.P_vapor_aquecimento_kgf /1000000, 4)
                    st.session_state.P_saida_MPa = round(st.session_state.P_saida_kgf /1000000, 4)
                elif unidade == 'kPa':
                    st.session_state.P_vapor_aquecimento_kgf = st.number_input('Qual é a pressão do vapor de aquecimento no primeiro efeito [kPa]?\n')
                    st.session_state.P_saida_kgf = st.number_input('Qual é a pressão na saída do último efeito [kPa]?\n')
                    st.session_state.P_vapor_aquecimento_MPa = round(st.session_state.P_vapor_aquecimento_kgf /1000, 4)
                    st.session_state.P_saida_MPa = round(st.session_state.P_saida_kgf /1000, 4)
                elif unidade == 'MPa':
                    st.session_state.P_vapor_aquecimento_MPa = st.number_input('Qual é a pressão do vapor de aquecimento no primeiro efeito [MPa]?\n')
                    st.session_state.P_saida_MPa = st.number_input('Qual é a pressão na saída do último efeito [MPa]?\n')

                if st.checkbox('Vácuo aplicado no último efeito?'):
                    st.session_state.P_saida_MPa = round((0.1013 - st.session_state.P_saida_MPa), 4)
                    if st.checkbox('Verificar fórmulas de conversão?'):
                        st.write(f'A transformação para pressão de vácuo se dá pelas seguintes formulas')
                        st.latex(r'''Pressão_{absoluta} = Pressão_{atmosférica} + Pressão_{manométrica}''')
                        st.latex(r'''Pressão_{absoluta} = Pressão_{atmosférica} - Pressão_{vácuo}''')
                    #Imagem: https://www.fem.unicamp.br/~instrumentacao/pressao/figuras/intro5.jpg
                    st.divider()

                dados2 = {
                        'Pressão do vapor de aq. [MPa]':[st.session_state.P_vapor_aquecimento_MPa],
                        'Pressão no último efeito [MPa]':[st.session_state.P_saida_MPa],
                        }



                st.table(dados2)     

    

                st.divider()
                st.subheader("Elevação do ponto de ebulição - EPE")
                #Inicializando listas
                st.session_state.lista_EPE = []
                st.session_state.lista_coef_TC = []
                for n in range(int(st.session_state.n_efeitos)):
                    epe = st.number_input(f"Qual a elevação de temperatura do efeito {n+1} [K ou °C]")
                    st.session_state.lista_EPE.append(epe)

                st.divider()
                st.subheader("Coeficiente de troca de calor")
                Unidades = ['kcal/hm2°C','W/m^2°C','Btu/ft^2h°F']
                unidade = st.radio('Escolha que unidade você quer trabalhar com o CTC abaixo:',Unidades)
                for n in range(int(st.session_state.n_efeitos)):
                    coef = st.number_input(f'\nQual o coeficiente de troca de calor para o efeito {n+1} [{unidade}]?')
                    if unidade == 'W/m^2°C':
                        coef = coef*0.86             
                    elif unidade == 'Btu/ft^2h°F':
                        coef = coef*4.882                
                    st.session_state.lista_coef_TC.append(coef)
                dados3 = {'EPE em cada efeito [°C]':st.session_state.lista_EPE,
                        'Coeficiente de troca de calor [kcal/hm2°C]]':st.session_state.lista_coef_TC,
                        }
                st.table(dados3)      


                st.subheader('Resumo dos Dados Iniciais')
                #st.warning('Os dados foram convertidos para as unidades abaixo.')
                st.write(f'A tabela abaixo reúne os :green[valores conhecidos] e os :red[valores à calcular], onde:')
                st.write(f'- (?) indica os valores que serão calculados nas próximas etapa. ')
                st.write(f'- (-) indica os valores que não serão cálculados ')
                
                vazao_sol = [st.session_state.vazao_F]
                fracao = [st.session_state.xf]
                temp = [st.session_state.Tf]
                pressao = [st.session_state.P_vapor_aquecimento_kgf]
                col = ['Alimentação']
                for n in range(int(st.session_state.n_efeitos)):
                    col.append(f'{n+1}° efeito')
                    vazao_sol.append('?')
                    fracao.append('?')
                    temp.append('?')
                    pressao.append('-')
                pressao.pop()
                pressao.append(st.session_state.P_saida_kgf)
                fracao.pop()
                fracao.append(st.session_state.xsaida)

                epe = ['-'] + st.session_state.lista_EPE
                U = ['-'] + st.session_state.lista_coef_TC
                st.session_state.df_dados_iniciais = pd.DataFrame([vazao_sol,temp,fracao,pressao,epe,U],['Vazão Solução [kg/h]','Temperatura [°C]','Fração [adm]','Pressão [kgf/cm^2]','EPE [°C]','U [kcal/hm2°C]'],columns=col).style.format(precision=2)
                st.table(st.session_state.df_dados_iniciais)


                dados1.update(dados2)
                dados1.update(dados3)
                st.session_state.dados_iniciais = dados1

                zero_keys = find_zero_keys(dados1)      
                dados1_flatenned = [item for sublist in dados1.values() for item in sublist]
                
    
                if 0 in dados1_flatenned:
                    st.divider()
                    st.error('**Dados incompletos**, verifique os dados abaixo') 
                    # Definir número de colunas
                    num_colunas = 3
                    colunas = st.columns(num_colunas)
                    st.divider()

                    # Distribuir os itens entre as colunas
                    for i, item in enumerate(zero_keys):
                        coluna_index = i % num_colunas  # Distribui de forma cíclica
                        with colunas[coluna_index]:  # Adiciona item à coluna correspondente
                            st.write(item)
                else:
                    st.success('**Dados Completos**') 
                    


                if st.button('Avançar'):
                    st.session_state.etapa = 'Fracao'
                    st.rerun()
                if st.button('Retornar'):
                    st.session_state.etapa = 'Efeitos'
                    st.rerun()

        #Cálculo das frações
        if st.session_state.etapa == 'Fracao':
            st.subheader('Cálculo das frações mássicas')

            #Tabela Inicial
            col = []
            vazao_sol = []
            lista_fracao = []
            for n in range(int(st.session_state.n_efeitos)+1):
                if n == 0:
                    col.append(f'Entrada')
                    vazao_sol.append(st.session_state.vazao_F)
                    lista_fracao.append(st.session_state.xf)
                elif n == int(st.session_state.n_efeitos):
                    col.append(f'{n}° efeito (Saída)')
                    lista_fracao.append(st.session_state.xn)
                    vazao_sol.append('?')
                else:
                    col.append(f'{n}° efeito - Chute')
                    vazao_sol.append('?')
                    lista_fracao.append('?')
            st.session_state.dados_fracao = pd.DataFrame([vazao_sol,lista_fracao],['Vazão Solução[kg/h]','Fração [adm]'],columns=col).style.format(precision=2)
            st.table(st.session_state.dados_fracao)
            #Cálculos
            st.session_state.lista_fracao = []
            st.session_state.n_efeito = float(st.session_state.n_efeitos)
            st.session_state.xn = float(st.session_state.xsaida)
            st.session_state.Lsaida = (st.session_state.vazao_F* st.session_state.xf/st.session_state.xn)
            st.session_state.Vn = (st.session_state.vazao_F - st.session_state.Lsaida)/(st.session_state.n_efeito)

            st.session_state.lista_fracao = []
            while st.session_state.n_efeito >= 0:
                xn = st.session_state.xf * st.session_state.vazao_F/(st.session_state.vazao_F-st.session_state.n_efeito*st.session_state.Vn)
                st.session_state.lista_fracao.append(xn)
                st.session_state.n_efeito -= 1
            st.session_state.lista_fracao.reverse()

            #Fórmulas e resoluções
            st.divider()
            if st.toggle('Equações empregadas:'):
                st.write('**1° Passo**: Determinar vazão de solução na saída')            
                st.latex(r'''\boldsymbol{Ln} = F * \frac{xf}{xn}''')
                st.write('**2° Passo**: Determinar a vazão média')
                st.latex(r'''\boldsymbol{V_{médio}} = (F - Lsaida)/n''')
                st.write('**3° Passo**: Calcular as frações em cada etapa')
                st.latex(r'''\boldsymbol{x_i} = xf * \frac{F}{F - V_{médio} * i}''')
                st.divider()
            if st.toggle('Solução detalhada'):
                st.write('**1° Passo**: Determinar vazão de solução na saída')
                st.latex(fr'''\boldsymbol{{Ln}} = {st.session_state.Lsaida} = {st.session_state.vazao_F} * \frac{{{st.session_state.xf}}}{{{st.session_state.xn}}}''')
                st.write('**2° Passo**: Determinar a vazão média')
                st.latex(fr'''\boldsymbol{{V_{{médio}}}} = {st.session_state.Vn:.2f} = ({st.session_state.vazao_F} - {st.session_state.Lsaida})/{st.session_state.n_efeitos}''')
                st.write('**3° Passo**: Calcular as frações em cada etapa')
                for n in range(int(st.session_state.n_efeitos)+1):
                    st.latex(fr'''\boldsymbol{{x_{n}}} = {st.session_state.lista_fracao[n]:.3f} = {st.session_state.xf} * \frac{{{st.session_state.vazao_F}}}{{{st.session_state.vazao_F} - {st.session_state.Vn:.2f} * {n}}}''')
                st.warning('O arredondamento é realizado apenas na apresentação dos dados, os valores usados em cálculos nunca são arredondados')
            st.divider()
            #Tabela completa
            col = []
            vazao_sol = []
            for n in range(int(st.session_state.n_efeitos)+1):
                if n == 0:
                    col.append(f'Entrada')
                elif n == int(st.session_state.n_efeitos):
                    col.append(f'{n}° efeito (Saída)')
                else:
                    col.append(f'{n}° efeito - (Chute)')
                vazao_sol.append(round(st.session_state.vazao_F - n* st.session_state.Vn,2))
            st.session_state.dados_fracao = pd.DataFrame([vazao_sol,st.session_state.lista_fracao],['Vazão Solução[kg/h]','Fração [adm]'],columns=col).style.format(precision=2)
            st.table(st.session_state.dados_fracao)
            
            image = Image.open(f'img_evaporadores/evaporador{st.session_state.n_efeitos}.png')
            st.image(image)
            if st.button('Avançar'):
                st.session_state.etapa = 'Temperatura'
                st.rerun()
            if st.button('Retornar'):
                st.session_state.etapa = 'Dados'
                st.rerun()

        if st.session_state.etapa == 'Temperatura':
            st.header('Cálculo das Temperatura')
            if st.session_state.lista_novo_delta_T:
                st.write('Dado que ja temos uma lista de variação existente, vamos pular a primeira etapa de contas.')

                col=[] 
                for n in range(int(st.session_state.n_efeitos)):
                    col.append(f'{n+1}° efeito')
                
                df = pd.DataFrame([st.session_state.lista_delta_T,st.session_state.lista_novo_delta_T], index=['Variação Antiga', 'Nova Variação'], columns=col)
                df.index.name = 'Temperatura [°C]'  # Define o nome do índice
                st.dataframe(df.style.format(precision=2))

                st.session_state.lista_delta_T = st.session_state.lista_novo_delta_T  
            else:
                col = []
                pressao = []
                temperatura = ['?']
                d_temperatura = ['-']
                epe = ['-']
                for n in range(int(st.session_state.n_efeitos)+2):
                    if n == 0:
                        col.append(f'Vapor de aq.')
                        pressao.append(st.session_state.P_vapor_aquecimento_kgf)
                        epe = epe + st.session_state.lista_EPE
                    elif n == int(st.session_state.n_efeitos)+1:
                        col.append(f'Vapor Saída')
                        pressao.append(st.session_state.P_saida_kgf)
                        temperatura.append('?')
                        epe.append('-')
                        d_temperatura.append('-')
                    else:
                        col.append(f'{n}° efeito')
                        pressao.append('-')
                        d_temperatura.append('?')
                        temperatura.append('?')
                
                st.session_state.dados_temp = pd.DataFrame([pressao,epe,d_temperatura,temperatura],['Pressão [kgf/cm^2]','EPE [°C]','Variação T [°C]','Temperatura [°C]'],columns=col).style.format(precision=2) 
                st.table(st.session_state.dados_temp)


                st.subheader('Cálculo Temperatura no primeiro e último efeito')
                st.write('A temperatura do vapor de aquecimento inicial e do vapor de saída no último efeito podem ser encontradas na a tabela de propriedades da água.')
                #1° Efeito
                #st.write(f'Obtendo temperatura do vapor de aquecimento inicial a partir da tabela de propriedades termodinâmicas da água.')
                #st.session_state.Ts = calc.Tabela_Vapor_Sat_app(st.session_state.P_vapor_aquecimento_MPa,'P (MPa)','T (°C)')
                st.session_state.Ts = Tabela_Vapor_Sat_app(st.session_state.P_vapor_aquecimento_MPa,'P (MPa)','T (°C)')
                #N° Efeito
                #st.write(f'Obtendo temperatura no último efeito a partir da tabela de propriedades termodinâmicas da água.')
                                
                if st.session_state.P_saida_MPa != 0:
                    #st.session_state.Tsaida = calc.Tabela_Vapor_Sat_app(st.session_state.P_saida_MPa,'P (MPa)','T (°C)')
                    st.session_state.Tsaida = Tabela_Vapor_Sat_app(st.session_state.P_saida_MPa,'P (MPa)','T (°C)')
                    st.write(f'Pressão de entrada: **{st.session_state.P_vapor_aquecimento_kgf:.2f} kgf/cm^2** ({st.session_state.P_vapor_aquecimento_MPa:.4f} Mpa) -> **{st.session_state.Ts:.1f} °C**')
                    st.write(f'Pressão de saída: **{st.session_state.P_saida_kgf:.2f} kgf/cm^2** ({st.session_state.P_saida_MPa:.4f} Mpa) -> **{st.session_state.Tsaida:.1f} °C**')
                else:
                    st.error('Pressão de saída não informada, Temperatura de saída indisponível')
                    st.write('Informe a temperatura em cada efeito:')
                    st.write('Temperatura de vapor de aquecimento inicial - **Ts**:',st.session_state.Ts)
                    st.session_state.lista_T = []
                    for i in range(int(st.session_state.n_efeitos)):
                        T = st.number_input(f'Temperatura no efeito {i+1}')
                        st.session_state.lista_T.append(T)
                    st.write('Temperatura dos efeitos:',st.session_state.lista_T)
                    if st.button('Avançar'):
                        st.session_state.etapa = 'Entalpia agua'
                        st.session_state.recalcular_temp = False
                        st.session_state.lista_novo_delta_T = False
                        st.rerun()

                #Elevação individual de tempetatura
                i = 0
                #Variação total temperatura
                st.divider()
                st.subheader('Cálculo Variação de Temperatura Total')
                st.session_state.delta_T_total = st.session_state.Ts - (st.session_state.Tsaida + sum(st.session_state.lista_EPE))
                st.latex(r'''\Delta T_{total} = T_s - (T_{saída}+ {\sum(EPEs)})''')
                if st.toggle('Cálculo aplicado'):
                    st.latex(fr'''\Delta T_{{total}} = {st.session_state.Ts:.2f} - ({st.session_state.Tsaida:.2f}+ {sum(st.session_state.lista_EPE)})''')
                    st.latex(fr'''\Delta T_{{total}} = {round(st.session_state.delta_T_total,2)}°C''')

                st.divider()
                st.subheader('Cálculo Variação de Temperatura Individual')
                st.session_state.lista_delta_T = []
                while i < int(st.session_state.n_efeitos):
                    delta_Ti = st.session_state.delta_T_total/(st.session_state.lista_coef_TC[i]*(sum(1/u for u in st.session_state.lista_coef_TC)))
                    st.session_state.lista_delta_T.append(delta_Ti)
                    i += 1
                st.write('A variação da temperatura em cada efeito é obtida relacionando a **variação total da temperatura** com o **coeficiente de troca de calor do efeito**')
                st.latex(r'''\Delta T_i = \frac{\Delta T_{total}}{U_i * \sum{\frac{1}{u}}}''')

                if st.toggle('Equação aplicada1'):
                    i = 0
                    while i < int(st.session_state.n_efeitos):
                        st.latex(fr'''\Delta T_{i+1} = \frac{{{st.session_state.delta_T_total:.2f}}}{{{st.session_state.lista_coef_TC[i]} * {sum(1/u for u in st.session_state.lista_coef_TC):.5f}}} = {st.session_state.lista_delta_T[i]:.1f} °C''')
                        i += 1


            st.divider()
            st.subheader('Cálculo Temperatura nos efeitos')
            st.session_state.lista_T = []
            i = 0
            while i < int(st.session_state.n_efeitos):
                if i == 0:
                    T1 = st.session_state.Ts - st.session_state.lista_delta_T[i]
                    st.session_state.lista_T.append(T1)
                    #st.write(f'Temperatura no efeito {i+1}: {T1:.1f} °C')    
                else:
                    Tn = (st.session_state.lista_T[i-1] - st.session_state.lista_EPE[i-1]) - st.session_state.lista_delta_T[i]
                    st.session_state.lista_T.append(Tn)
                    #st.write(f'Temperatura no efeito {i+1}: {Tn:.1f} °C')    
                i += 1

            st.write('A temperatura no primeiro efeito é calculada por:')
            st.latex(r''' T_1 = T_s - \Delta T_1''')
            st.write('As demais temperaturas são calculadas por:')
            st.latex(r''' T_i = T_{i-1} - EPE_{i-1} - \Delta T_i''')
            if st.toggle('Equação aplicada2'):
                i = 0
                while i < int(st.session_state.n_efeitos):
                    if i == 0:
                        st.latex(fr''' T_1 = {st.session_state.Ts:.2f} - {st.session_state.lista_delta_T[i]:.2f} = {T1:.2f} °C''')
                    else:
                        st.latex(fr''' T_{i+1} = {st.session_state.lista_T[i-1]:.2f} - {st.session_state.lista_EPE[i-1]:.2f} - {st.session_state.lista_delta_T[i]:.2f} = {st.session_state.lista_T[i]:.2f} °C''')
                    i += 1
                
                
            #Variação total temperatura
            #linha abaixo repetida
            st.session_state.delta_T_total = st.session_state.Ts - (st.session_state.Tsaida + sum(st.session_state.lista_EPE))
                
            
            col = []
            pressao = []
            temperatura = []
            d_temperatura = ['-']
            epe = ['-']
            for n in range(int(st.session_state.n_efeitos)+2):
                if n == 0:
                    col.append(f'Vapor de aq.')
                    pressao.append(st.session_state.P_vapor_aquecimento_kgf)
                    temperatura.append(st.session_state.Ts)
                    epe = epe + st.session_state.lista_EPE
                elif n == int(st.session_state.n_efeitos)+1:
                    col.append(f'Vapor Saída')
                    pressao.append(st.session_state.P_saida_kgf)
                    temperatura = temperatura + st.session_state.lista_T + [st.session_state.Tsaida]

                else:
                    col.append(f'{n}° efeito')
                    pressao.append('-')

            st.divider()
            st.subheader('Resumo dos dados')
            d_temperatura = d_temperatura + st.session_state.lista_delta_T + ['-']
            epe = epe + ['-']
            st.session_state.dados_temp = pd.DataFrame([pressao,epe,d_temperatura,temperatura],['Pressão [kgf/cm^2]','EPE [°C]','Variação T [°C]','Temperatura [°C]'],columns=col).style.format(precision=2) 
            st.table(st.session_state.dados_temp)

            
            st.write('Para o futuro cálculo das entalpias necessitamos encontrar a temperatura de saturação através da seguinte fórmula:')
            st.latex(r'''Tsat = T - EPE''')
            temperatura_sat = []
            for n in range(int(st.session_state.n_efeitos)):
                t_sat = temperatura[n]-st.session_state.lista_EPE[n]
                temperatura_sat.append(t_sat)
            st.session_state.dados_temp2 = pd.DataFrame([temperatura,epe,temperatura_sat],['Temperatura [°C]','EPE [°C]','Temperatura Saturação[°C]'],columns=col).style.format(precision=2) 
            st.table(st.session_state.dados_temp2)


            if st.button('Avançar'):
                st.session_state.etapa = 'Entalpia agua'
                st.session_state.recalcular_temp = False
                st.session_state.lista_novo_delta_T = False
                st.rerun()
            if st.button('Retornar'):
                st.session_state.etapa = 'Fracao'
                st.rerun()

        if st.session_state.etapa == 'Entalpia agua':
            st.subheader('Cálculo das entalpias: vapor de aquecimento e saída dos efeitos')
            st.write('As entalpias para água saturada são obtidas diretamente através da tabela de propriedades da água saturada.')
            st.link_button(
                label="Acesse a Tabela de Vapor (Universidade Federal de Pelotas)",
                url="https://wp.ufpel.edu.br/ciceroescobar/files/2022/04/Tabelas-e-diagramas-de-propriedades-Cengel-Mec-Flu.pdf"
            )            
            st.divider()
            st.subheader('Entalpia vaporização do vapor inicial')
            #st.session_state.hs = calc.Tabela_Vapor_Sat_app(st.session_state.P_vapor_aquecimento_MPa,'P (MPa)','Enthalpy of Vaporization (kJ/kg)') * 0.239006
            st.session_state.hs = Tabela_Vapor_Sat_app(st.session_state.P_vapor_aquecimento_MPa,'P (MPa)','Enthalpy of Vaporization (kJ/kg)') * 0.239006
            st.write(f"Para o vapor de aquecimento inicial (P = {st.session_state.P_vapor_aquecimento_kgf} kgf/cm^2) -> {st.session_state.hs:.2f} kcal/kg")
            st.divider()          
            
            st.session_state.lista_entalpia_vapor = []
            st.session_state.lista_entalpia_liquido = []

            i = 0
            while i < int(st.session_state.n_efeitos):  
                #Vapor saturado
                #Entrada: Tn
                #Saída:  hVn (vapor saturado)
                T = st.session_state.lista_T[i]
                #h = calc.Tabela_Vapor_Sat_app(round(T,3), 'T (°C)', 'Enthalpy Vapor (kJ/kg)')
                h = Tabela_Vapor_Sat_app(round(T,3), 'T (°C)', 'Enthalpy Vapor (kJ/kg)')
                hv = h / 4.184
                st.session_state.lista_entalpia_vapor.append(hv)
                #st.write(f'Entalpia Vapor (T = {round(T,2)}°C): {hv:.2f} kcal/kg')
                
                #Liquido saturado
                #Entrada: Tsat,n
                #Saída: hLn (líquido saturado)
                Tsat = st.session_state.lista_T[i] - st.session_state.lista_EPE[i]
                #h = calc.Tabela_Vapor_Sat_app(round(Tsat,3), 'T (°C)', 'Enthalpy Liquid (kJ/kg)')
                h = Tabela_Vapor_Sat_app(round(Tsat,3), 'T (°C)', 'Enthalpy Liquid (kJ/kg)')
                hl = h / 4.184
                st.session_state.lista_entalpia_liquido.append(hl)
                #st.write(f'Entalpia Liquido (Tsat = {round(Tsat,2)}°C): {hl:.2f} kcal/kg')
                i += 1


            st.subheader('Entalpias nos efeitos')
            col = []
            H = []
            hl = []
            hv = []
            Tsat = []
            T = []
            for n in range(int(st.session_state.n_efeitos)):
                col.append(f'{n+1}° efeito')
                hv .append(st.session_state.lista_entalpia_vapor[n])
                hl.append(st.session_state.lista_entalpia_liquido[n])
                H.append(st.session_state.lista_entalpia_vapor[n] - st.session_state.lista_entalpia_liquido[n])
                T.append(st.session_state.lista_T[n])
                Tsat.append(st.session_state.lista_T[n] - st.session_state.lista_EPE[n])

           
            st.write('A **entalpia do vapor saturado** lida na tabela de vapor, usando a temperatura de operação (temperatura do efeito).')
            st.warning('Valores para vazão composta por apenas vapor saturado.')
            df = pd.DataFrame([T,hv], index=['Temperatura [°C]', 'Entalpia Vapor [kcal/kg]'], columns=col)
            st.dataframe(df.style.format(precision=2))
            st.divider()
            st.write('A **entalpia do vapor de aquecimento** na saída do evaporador.')
            st.warning('Valores para vazão composta por apenas líquido saturado.')
            df = pd.DataFrame([Tsat,hl,], index=['Temperatura Sat [°C]', 'Entalpia Líquido [kcal/kg]'], columns=col)
            st.dataframe(df.style.format(precision=2))
            st.divider()
            st.write('A **energia** conferida para o sistema pelo trocador de calor é a diferença entre as duas temperaturas')
            df = pd.DataFrame([hv,hl, H], index=[ 'Entalpia Vapor [kcal/kg]', 'Entalpia Líquido [kcal/kg]','Entalpia Vaporização [kcal/kg]'], columns=col)
            st.dataframe(df.style.format(precision=2))
            st.divider()

            #Tabelas para apresentação no final do programa
            st.session_state.dados_entalpia_v=df
            
            if st.button('Avançar'):
                st.session_state.etapa = 'Entalpia solucao'
                st.rerun()
            if st.button('Retornar'):
                st.session_state.etapa = 'Temperatura'
                st.rerun()

        if st.session_state.etapa == 'Entalpia solucao':
            st.subheader('Cálculo das entalpias de solução')

            if st.checkbox('Autopreencher'):
                st.session_state.hf = 37
                st.write(f'Entalpia da solução inicial: {st.session_state.hf} Kcal/kg')
                st.session_state.lista_entalpia_solucao = [102,86,113]
                i = 0
                for x in st.session_state.lista_entalpia_solucao:
                    i += 1
                    st.write(f'Entalpia da solução saindo do efeito {i}: {x} Kcal/kg')
            else:
                st.write('Para a entalpia de solução podemos usar gráficos termodinâmicos ou fórmulas específicas a depender da solução estudada.')

                col = ['Alimentação']
                hs = ['?']
                Temp = [round(st.session_state.Tf,2)]
                for n in range(int(st.session_state.n_efeitos)):
                    col.append(f'{n+1}° efeito')
                    hs.append('?')
                    Temp.append(round(st.session_state.lista_T[n],2))

                df = pd.DataFrame([Temp,hs], index=['Temperatura [°C]',' Ent. Sol. [Kcal/kg]'], columns=col)
                df

                modo = st.pills('Escolha uma ferramenta de auxílio',['Auxilio gráfico NaOH','Auxílio gráfico H2SO4','Esconder'],)
                if modo == 'Auxilio gráfico NaOH':
                    rotated_image = Image.open(f'img_evaporadores/Diagrama_NaOH_entalpia.png').rotate(90, expand= True)
                    st.image(rotated_image)
                elif modo == 'Auxílio gráfico H2SO4':
                    #st.write('4.6 - enthalpy-composition phase diagram for water+sulfuric acid mixtures at 1 atm.')                    
                    image = Image.open(r"C:\Users\pedro\Desktop\Projetos\TCC\img_evaporadores\Diagrama_H2SO4_entalpia.jpg")
                    st.image(image)
                    st.link_button("Chemical Engineering Design and Analysis: An Introduction", "https://duncan.cbe.cornell.edu/Graphs/Chp4graphs/4-36.pdf")

                st.divider()
                st.subheader(f'Entalpia solução original')
                st.session_state.hf = st.number_input(f'Qual a entalpia [kcal/kg] para solução inicial, fração {round(st.session_state.xf,2)} e temperatura {round(st.session_state.Tf,2)}°C ({round((st.session_state.Tf*1.8+32),2)}°F)')
                #st.session_state.hf = st.number_input(f"Digite a Entalpia para a Vazão de entrada, {round(st.session_state.Tf,0)} °C e {round(st.session_state.xf,3)}:", step=1)
                st.write(f'Para a solução na alimentação, teremos uma entalpia de {st.session_state.hf} Kcal/kg.')

                st.session_state.lista_entalpia_solucao = []
                i = 0
                while i < int(st.session_state.n_efeitos):
                    st.divider()
                    st.subheader(f'Entalpia solução saindo do efeito {i+1}')
                    Entalpia_NaOH = st.number_input(f'Qual a entalpia [kcal/kg] de uma solução {round(st.session_state.lista_fracao[i+1],2)} e temperatura {round(st.session_state.lista_T[i],2)}°C ({round((st.session_state.lista_T[i]*1.8+32),0)}°F)')
                    st.write(f'Para o {i+1}° efeito, teremos entalpia de {Entalpia_NaOH} cal/kg')
                
                    st.session_state.lista_entalpia_solucao.append(Entalpia_NaOH) 
                    i += 1          

            st.divider()
            st.subheader('Resumo dos dados')      

            col = ['Alimentação']
            hs = [st.session_state.hf]
            Temp = ['-']
            for n in range(int(st.session_state.n_efeitos)):
                col.append(f'{n+1}° efeito')
                hs.append(st.session_state.lista_entalpia_solucao[n])

            df = pd.DataFrame([[st.session_state.Tf]+st.session_state.lista_T,hs], index=['Temperatura [°C]',' Ent. Sol. [Kcal/kg]'], columns=col)
            st.session_state.dados_entalpia_sol = df
            st.dataframe(st.session_state.dados_entalpia_sol.style.format(precision=2))
    
            
            if 0 in hs:
                st.divider()
                st.error('**Dados incompletos**, verifique os dados abaixo')
                for idx, x in enumerate(hs):
                    if x == 0:
                        st.warning(f'⚠ Preencher dados do efeito {idx}')
            else:
                st.success('**Dados Completos**') 

            if st.button('Avançar'):
                st.session_state.etapa = 'Vazao'
                st.rerun()
            if st.button('Retornar'):
                st.session_state.etapa = 'Entalpia agua'
                st.rerun()

        if st.session_state.etapa == 'Vazao':
            st.subheader('Cálculo das Vazões')
            st.write('Para obter as vazões precisamos contruir uma matriz com base nas equações termodinâmicas que regem o EME.')
            st.write('Na tabela abaixo está reunida todos os dados calculados até aqui e necessários para montar esta matriz:')
            H = [st.session_state.hs]
            hl = ['Não calc']
            hv = ['Não calc']
            hsol = [st.session_state.hf]
            l_v = ['?']
            x = st.session_state.lista_fracao
            col= ['Alimentação']
            for n in range(int(st.session_state.n_efeitos)):
                col.append(f'{n+1}° efeito')
                hv .append(st.session_state.lista_entalpia_vapor[n])
                hl.append(st.session_state.lista_entalpia_liquido[n])
                H.append(st.session_state.lista_entalpia_vapor[n] - st.session_state.lista_entalpia_liquido[n])
                hsol.append(st.session_state.lista_entalpia_solucao[n])
                l_v.append('?')

            df = pd.DataFrame([l_v,x,hv,hl,H,hsol], index=['Vazão de Vapor [kg/h]', 'Fração Mássica [adm]','Entalpia do Vapor de saída[kcal/kg]','Entalpia do Liquido [kcal/kg]','Entalpia de vaporização [kcal/kg]','Entalpia da Solução na saída[kcal/kg]'], columns=col)
            st.dataframe(df.style.format(precision=2))
            st.divider()

            if st.toggle('Desenvolvimento das equações de matriz'):    
                st.write('Exemplo de construção de matriz para evaporador de 2 Efeito)')
                st.write('Um passo a passo mais detalhado pode ser encontrado no meu TCC')
                st.write('**Balanço de Energia**')
                st.latex(r'''1° Efeito: F \cdot h_F + S \cdot h_s = V_1 \cdot h_{G1} + L_1 \cdot H_{L1}''')
                st.latex(r'''2° Efeito: L_1 \cdot H_{L1} + V_1 \cdot (h_{G1}-h_{L1}) = V_1 \cdot h_{G1} + V_2 \cdot h_{G2} + L_2 \cdot H_{L2}''')
                st.latex(r'''Global: F \cdot h_F + S \cdot h_s = V_1 \cdot h_{G1} + V_2 \cdot h_{G2} + L_2 \cdot H_{L2}''')

                st.write('**Balanço de massa solvente**')
                st.latex(r'''1° Efeito: F = L_1 + V_1''')
                st.latex(r'''2° Efeito: L_1 = L_2 + V_2 ''')
                st.latex(r'''Global: F = L_2 + V_2 +V_1''')
                st.latex(r'''V_2 +V_1  = F - L_2 = \boldsymbol{V_{soma}}''')
                st.write('**Balanço de massa soluto**')
                st.latex(r'''1° Efeito: F*x_f= L_1*x_{L1} + \cancel{V_1*x_{v1}}''')
                st.latex(r'''2° Efeito: L_1*x_{L1}= L_2*x_{L2} + \cancel{V_2*x_{v2}}''')
                st.latex(r'''Global: F*x_f= L_2*x_{L2} + \cancel{V_2*x_{v2}} + \cancel{V_1*x_{v1}}''')
                
                st.write('**Equação desenvolvida**')
                st.latex(r'''\boldsymbol{V_1}*(H_{L1}-h_{G1}) + \boldsymbol{S}*h_s = F*(H_{L1}-h_F)''')
                st.latex(r'''\boldsymbol{V_1}*(h_{G1}-h_{L1}+h_{G2}-H_{L1}) = F*(-H_{L1})+ L_2*H_{L2} + V_{soma}* h_{G2}''')
                st.write('**Última Incógnita**')
                st.latex(r'''\boldsymbol{V_2} = F - (V_2 +V_1)''')


            st.divider()
            #lista_vazao_incompleta = calc.calculo_vazao_completo(int(st.session_state.n_efeitos), st.session_state.lista_entalpia_solucao, st.session_state.lista_entalpia_vapor, st.session_state.lista_entalpia_liquido, st.session_state.hs, st.session_state.hf, st.session_state.vazao_F,st.session_state.xf, st.session_state.xsaida)
            lista_vazao_incompleta = calculo_vazao_completo(int(st.session_state.n_efeitos), st.session_state.lista_entalpia_solucao, st.session_state.lista_entalpia_vapor, st.session_state.lista_entalpia_liquido, st.session_state.hs, st.session_state.hf, st.session_state.vazao_F,st.session_state.xf, st.session_state.xsaida)
            st.session_state.vazao_S = lista_vazao_incompleta.pop().pop()
            st.session_state.lista_vazao = []
            for x in lista_vazao_incompleta:
                for y in x:
                    st.session_state.lista_vazao.append(y)
            Vfinal = st.session_state.vazao_F - st.session_state.Lsaida - (sum(st.session_state.lista_vazao))
            st.session_state.lista_vazao.append(Vfinal)

            st.write(f'Aplicando os valores acima na matriz, Nós obtemos a tabela abaixo:')
            
            l_v = st.session_state.lista_vazao
            col.pop(0)
            df = pd.DataFrame([l_v], index=['Vazão de vapor de saída[kg/h]'], columns=col)
            st.dataframe(df.style.format(precision=2))
            st.divider()        

            #desvio_padrao_vazao = np.std(st.session_state.lista_vazao)
            #erro_vazao = desvio_padrao_vazao*100/np.mean(st.session_state.lista_vazao)
            
            st.subheader(f'Cálculo Área')
            i = 0
            st.session_state.lista_area = []
            while i < int(st.session_state.n_efeitos):
                if i == 0:
                    Area = st.session_state.vazao_S * st.session_state.hs /(st.session_state.lista_coef_TC[i] * st.session_state.lista_delta_T[i])
                    st.session_state.lista_area.append(Area)
                else:
                    Area = st.session_state.lista_vazao[i-1]*(st.session_state.lista_entalpia_vapor[i-1] - st.session_state.lista_entalpia_liquido[i-1])/((st.session_state.lista_coef_TC[i] * st.session_state.lista_delta_T[i]))
                    st.session_state.lista_area.append(Area)
                i += 1  
            desvio_padrao_area = np.std(st.session_state.lista_area)
            st.session_state.erro_area = desvio_padrao_area*100/np.mean(st.session_state.lista_area)
            if st.toggle('Visualizar equações'):
                st.write('Utilizando as vazões obtidas acima e partindo da equação de:')
                st.latex(r'''Q = U*A*\Delta T''')
                st.latex(r'''Area_i = Vazão_{vapor_{i-1}} * \frac{(H_{vapor_{i-1}} - H_{líquido_{i-1}})}{Coef_i * \Delta T_i}''')
                st.latex(r'''Area_i = Vazão_{vapor_{i-1}} * \frac{H_{vaporizacao_{i-1}}}{U_i * \Delta T_i}''')
            if st.toggle('Visualização Cálculos'):
                for i in range(int(st.session_state.n_efeitos)):
                    if i == 0:
                        st.latex(fr'''Area_{i+1} = {st.session_state.vazao_S:.2f} * \frac{{{st.session_state.hs:.2f}}}{{{st.session_state.lista_coef_TC[i]:.2f} * {st.session_state.lista_delta_T[i]:.2f}}} = {st.session_state.lista_area[i]:.2f} m^2''')
                    else:
                        st.latex(fr'''Area_{i+1} = {st.session_state.lista_vazao[i-1]:.2f} * \frac{{{st.session_state.lista_entalpia_vapor[i-1]:.2f}-{st.session_state.lista_entalpia_liquido[i-1]}}}{{{st.session_state.lista_coef_TC[i]:.2f} * {st.session_state.lista_delta_T[i]:.2f}}} = {st.session_state.lista_area[i]:.2f} m^2''')

                


            st.subheader(f'Avaliação das Áreas')
            col= []
            for n in range(int(st.session_state.n_efeitos)):
                col.append(f'{n+1}° efeito')
            col.append('Dp')
            col.append('Erro (%)')
            st.session_state.dados_v_a = pd.DataFrame([st.session_state.lista_area+[desvio_padrao_area]+[st.session_state.erro_area]], index=['Area (m^2)'], columns=col).style.format(precision=2)
            st.dataframe(st.session_state.dados_v_a)

            erro_limite = 5
            if st.session_state.erro_area < erro_limite: 
                st.success(f'Area dentro do aceitável: {round(st.session_state.erro_area,2)}% < {erro_limite}%')
                st.write('Iremos agorafinalizar o programa calculando a economia do evaporador')
                if st.button('Calcular Economia'): st.session_state.etapa = 'Economia'

            else:
                st.error(f'Area fora do aceitável: {round(st.session_state.erro_area,2)}% > {erro_limite}%')
                st.write('Iremos agora calcular uma nova Temperatura')
                if st.button('Avançar para novo T'):
                    st.session_state.etapa = 'Novo T'
                    st.rerun()

            if st.button('Retornar'):
                st.session_state.etapa = 'Entalpia solucao'
                st.rerun()

        if st.session_state.etapa == 'Economia':
            economia = sum(st.session_state.lista_vazao)/st.session_state.vazao_S
            #st.latex(fr'''Economia = \frac{{{round(st.session_state.lista_vazao[0],2)}+{round(st.session_state.lista_vazao[1],2)}+{round(st.session_state.lista_vazao[2],2)}}}{{{round(st.session_state.vazao_S,2)}}}''')

            st.latex(r'''\text{economia} = \frac{\sum{vazão_{vapor}}}{vazao_{aq.}}''')
            
            if st.toggle('Visualização dos cálculos'):
                rounded_vazoes = [f"{v:.2f}" for v in st.session_state.lista_vazao]
                vazoes_str = ", ".join(rounded_vazoes)

                st.latex(fr'''\text{{economia}} = \frac{{\sum[{vazoes_str}]}}{{{st.session_state.vazao_S:.2f}}} = {economia:.2f}''')

            
            st.write(f'Para o evaporador com os parâmetros informados teremos uma economia de {round(economia,2)}')
            

            #st.table(st.session_state.dados_iniciais)
            #st.table(st.session_state.dados_fracao)
            #st.table(st.session_state.dados_temp)
            #st.dataframe(st.session_state.dados_entalpia_v)
            #st.dataframe(st.session_state.dados_entalpia_sol)        
            #st.dataframe(st.session_state.dados_v_a)
            st.subheader('Resumo de dados')
            vazao_sol = [st.session_state.vazao_F]
            vazao_vap = [st.session_state.vazao_S] + st.session_state.lista_vazao
            pressao = [st.session_state.P_vapor_aquecimento_kgf]
            fracao = st.session_state.lista_fracao
            temp = [st.session_state.Tf] + st.session_state.lista_T #+ [st.session_state.Tsaida]
            epe = ['-'] + st.session_state.lista_EPE
            U = ['-'] + st.session_state.lista_coef_TC
            area = ['-'] + st.session_state.lista_area
            col = ['Alimentação']
            for n in range(int(st.session_state.n_efeitos)):
                col.append(f'{n+1}° efeito')
                pressao.append('-')
                if n == 0:
                    sol = st.session_state.vazao_F - st.session_state.lista_vazao[0]
                    vazao_sol.append(sol)
                else:
                    sol = sol - st.session_state.lista_vazao[n]
                    vazao_sol.append(sol)
            pressao.pop()
            pressao.append(st.session_state.P_saida_kgf)       
            st.session_state.df_dados_iniciais_completos = pd.DataFrame([vazao_sol,vazao_vap,temp,fracao,pressao,epe,U,area],['Vazão Solução [kg/h]','Vazão Vapor [kg/h]','Temperatura [°C]','Fração [adm]','Pressão [kgf/cm^2]','EPE [°C]','U [kcal/hm2°C]','Area [m^2]'],columns=col).style.format(precision=2)
            
            st.write('A partir dos dados iniciais disponíveis na tabela abaixo:')
            st.table(st.session_state.df_dados_iniciais)
            st.write(f'Podemos realizar a modelagem de um reator de {st.session_state.n_efeitos} efeitos obtendo os seguintes dados:')
            st.table(st.session_state.df_dados_iniciais_completos)
            st.write('Este programa forneceu os dados tabelados de entalpia no seguinte formato:')
            st.dataframe(st.session_state.dados_entalpia_v.style.format(precision=2))
            st.dataframe(st.session_state.dados_entalpia_sol.style.format(precision=2))
            st.dataframe(df.style.format(precision=2))
            if st.button('Retornar.'):
                st.session_state.etapa = 'Vazao'
                st.rerun()
        
        if st.session_state.etapa == 'Novo T':
            st.subheader(f'Cálculo Nova Variação de Temperatura')
            lista_area_arit = []
            for i in range(len(st.session_state.lista_delta_T)):
                area_arit = st.session_state.lista_area[i] * st.session_state.lista_delta_T[i]
                lista_area_arit.append(area_arit)
            area_media = sum(lista_area_arit)/sum(st.session_state.lista_delta_T)
            
            st.session_state.lista_novo_delta_T = []
            for i in range(len(st.session_state.lista_delta_T)):
                novo_delta_T = st.session_state.lista_area[i] * st.session_state.lista_delta_T[i]/area_media
                st.session_state.lista_novo_delta_T.append(novo_delta_T)

            col= []
            for n in range(int(st.session_state.n_efeitos)):
                col.append(f'{n+1}° efeito')
            col.append('Média / Soma')
            df = pd.DataFrame([lista_area_arit + [area_media],st.session_state.lista_novo_delta_T+[sum(st.session_state.lista_novo_delta_T)]], index=['Area (m^2)','Variação T (°C)'], columns=col)
            st.dataframe(df.style.format(precision=2))

            if st.toggle('Fórmulas empregadas'):
                st.latex(r'''Area_{art} = Area*\Delta T_{antigo}''')
                st.divider()
                st.latex(r'''Area_{média} = \frac{\sum{Area_{art}}}{\Delta T_{antigo}}''')
                st.divider()
                st.latex(r'''\Delta T_{novo} = Area* \frac{\Delta T_{antigo}}{area_{média}}''')
            if st.toggle('Visualização dos cálculos'):
                for i in range(len(st.session_state.lista_delta_T)):
                    st.latex(fr'''Area_{{art{i+1}}} = {st.session_state.lista_area[i]:.2f}*{st.session_state.lista_delta_T[i]:.2f} = {st.session_state.lista_area[i]*st.session_state.lista_delta_T[i]:.2f}''')
                st.divider()
                rounded_areas = [f"{area:.2f}" for area in st.session_state.lista_area]
                areas_str = ", ".join(rounded_areas)

                st.latex(fr'''Area_{{média}} = \frac{{\sum[{areas_str}]}}{{{st.session_state.lista_delta_T[i]:.2f}}} = {area_media:.2f}''')
                st.divider()
                for i in range(len(st.session_state.lista_delta_T)):
                    st.latex(fr'''\Delta T_{{novo{i+1}}} = {st.session_state.lista_area[i]:.2f}* \frac{{{st.session_state.lista_delta_T[i]:.2f}}}{{{area_media:.2f}}} = {st.session_state.lista_area[i]*st.session_state.lista_delta_T[i]/area_media:.2f}''')
                st.divider()


            if st.button('Avançar'):
                st.session_state.etapa = 'Temperatura'
                st.rerun()
            if st.button('Retornar'):
                st.session_state.etapa = 'Vazao'
                st.rerun()
