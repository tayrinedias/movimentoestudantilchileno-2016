# Apresentação

Este é um código desenvolvido com propósitos didáticos para o ensino de programação técnicas de de mineração de dados para cientistas políticos. 

# Instruções de Uso

1. Acesse https://apps.twitter.com e registre sua aplicação.
2. Baixe o código fonte utilizando uma das formas a seguir:
   * Fazendo um clone local do repositório. 
     * git clone git@github.com:code4pol/movimentoestudantilchileno-2016.git
   * Se o passo anterior não fizer sentido para você:
     * Clique [aqui](https://raw.githubusercontent.com/code4pol/movimentoestudantilchileno-2016/master/collect_movimentoestudantilchileno.py).
     * Copie (Ctrl+C) todo o código que vai abrir na sequência.
     * Utilizando seu editor de *textos* preferido (e.g. Sublime ou Notepad) (pelamordedeus, pelosmeusfilhos, porfarofassemuvapassa, não usem o Word!!!), crie um arquivo vazio e cole nele o código copiado (Ctrl+V).
     * Salve este novo arquivo (Ctrl+S) com o nome collect_movimentoestudantilchileno.py (só para padronizarmos a comunicação) em alguma pasta de sua máquina.
     * Vamos agora fazer as alternações necessárias no código fonte que acabamos de copiar.
3. Copie as chaves geradas no passo 1 e informe-as nas linhas equivalentes do código fonte baixado no passo 2 (láaaa no final do arquivo).
   * O código
```python
consumer_key="sua consumer_key"
consumer_secret="sua consumer_secret"
access_token="seu access_token"
access_token_secret="seu access_token_secret" 
```
   * deve se tornar algo como:
```python
consumer_key="dxDCq1vknttfPYn4"
consumer_secret="6Lq9ElMZbnO8RFGuruK1Qfoy5jAqlC2UZPCdWOQJ"
access_token="14147108-TX4p6DxzFJO9K1LjXk17bsayOiZiF06VDcUFXa"
access_token_secret="YcGN6NLnAXJ45AURlqzIl9yDV28LksWYtdrLKfnTo"
```
4. Ajustes as contas cujos tweets deseja capturar, por volta da linha 118, 
```python
accounts = ['Feuls','Feupla','feusach','FEUSAM','feusmjmc','FeustSantiago','FEUTEM','feutfsm','feuv','feuvsantiago','la_fech','FEL_Stgo','FedFEMAE','FECUdeC','FEUDMVina','FEDEUNAP','FEUFRO','feummagallanes','FEDEPUDP','FepPedagogico','confech','creceruc','Estafados_CORFO','infestudiantes','Izquierda_Tuit','izqautonoma','u_informado','privmovilizadas','FELUCHILE','naupuc','jjcc_chile','mesup_Chile','SolidaridadUC','UNE_CHILE','Rdemocratica']
```
   * Cada um dos elementos deste array(?!?) corresponde a uma conta do tweet, exemplo @Feuls, @Feupla... Sacou? ;-)
