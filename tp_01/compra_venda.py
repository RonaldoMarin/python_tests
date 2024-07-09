class DAOCompra:
    def __init__ (self) :
        self._placa = None
        self._compra = False
        self._dataCompra = None

#     def getUltimaData(self, placa):
#         return None
    
#     def setDataCompra(self, data):
#         self._dataCompra = data

#     def setPlacaCompra(self, placa):
#         self._placa = placa
#         self._compra = True

#     def save(self, placa, data ):
#         self.setPlacaCompra(placa)
#         self.setDataCompra(data)

# class DAOVenda:
#     def getUltimaData(self, placa) :
#         return None

# class ServicoVeiculo:
#     def __init__(self):
#         self.daoCompra = DAOCompra( )
#         self.daoVenda = DAOVenda( )

#     def isEmPosseDaLoja(self, placa):

#         ultima_compra = self.daoCompra.getUltimaData(placa)

#         # Teste de Software Lista 2: Mock - Testes com Objetos Simulados.
#         ultima_venda = self.daoVenda.getUltimaData(placa)
#             if ultima_comprais None andultima_vendaisNone:
#             return Fal s e
# e l i f ultima_compra i s not None and ultima_venda i s None : return True
# return ultima_venda < ultima_compra
# def compra ( s e l f , placa , data ) :
# i f isEmPosseDaLoja ( pla ca ) == Fal s e :
# s e l f . daoCompra . sa ve ( placa , data )
# return True
# e l s e :
# return Fal s e