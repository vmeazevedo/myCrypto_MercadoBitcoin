import unittest
from unittest.mock import patch, MagicMock
from rich.table import Table
from myCripto_Monitor import monitorar_criptomoeda, criar_tabela  # Ajuste 'myCripto_Monitor' para o nome do seu arquivo .py
from utils.alerta import verificar_alerta

class TestMonitorarCriptomoeda(unittest.TestCase):
    @patch("myCripto_Monitor.loop")
    @patch("myCripto_Monitor.calc_porc")
    @patch("locale.currency")
    def test_monitorar_criptomoeda_valor_maior(self, mock_currency, mock_calc_porc, mock_loop):
        mock_loop.return_value = 105.0
        mock_calc_porc.return_value = "5.0%"
        mock_currency.return_value = "R$ 105,00"
        
        lista = [100.0]
        valor, porc, style = monitorar_criptomoeda("btc", lista)
        
        self.assertEqual(valor, "R$ 105,00")
        self.assertEqual(porc, "5.0%")
        self.assertEqual(style, "green")
        self.assertEqual(lista[-1], 105.0)

    @patch("myCripto_Monitor.loop")
    @patch("myCripto_Monitor.calc_porc")
    @patch("locale.currency")
    def test_monitorar_criptomoeda_valor_menor(self, mock_currency, mock_calc_porc, mock_loop):
        mock_loop.return_value = 95.0
        mock_calc_porc.return_value = "-5.0%"
        mock_currency.return_value = "R$ 95,00"
        
        lista = [100.0]
        valor, porc, style = monitorar_criptomoeda("btc", lista)
        
        self.assertEqual(style, "red")
        self.assertEqual(porc, "-5.0%")
        self.assertEqual(lista[-1], 95.0)

    @patch("myCripto_Monitor.loop")
    @patch("myCripto_Monitor.calc_porc")
    @patch("locale.currency")
    def test_monitorar_criptomoeda_valor_igual(self, mock_currency, mock_calc_porc, mock_loop):
        mock_loop.return_value = 100.0
        mock_calc_porc.return_value = "0%"
        mock_currency.return_value = "R$ 100,00"
        
        lista = [100.0]
        valor, porc, style = monitorar_criptomoeda("btc", lista)
        
        self.assertEqual(style, "yellow")
        self.assertEqual(porc, "0%")
        self.assertEqual(lista[-1], 100.0)

    @patch("myCripto_Monitor.loop", side_effect=Exception("Erro na requisição"))
    def test_monitorar_criptomoeda_erro(self, mock_loop):
        lista = [100.0]
        valor, porc, style = monitorar_criptomoeda("btc", lista)
        self.assertEqual(valor, "")
        self.assertEqual(porc, "")
        self.assertEqual(style, "")

class TestCriarTabela(unittest.TestCase):
    def test_criar_tabela(self):
        table = criar_tabela()
        self.assertIsInstance(table, Table)
        self.assertEqual(len(table.columns), 5)
        self.assertEqual([c.header for c in table.columns], ["Criptomoeda", "Valor", "Data/Hora", "Status", "Porcentagem"])

class TestVerificarAlerta(unittest.TestCase):
    def test_alerta_com_variação(self):
        lista = [1.0, 1.0, 1.02]
        limite = 1.0
        self.assertTrue(verificar_alerta(lista, limite))

    def test_alerta_sem_variação(self):
        lista = [1.0, 1.0, 1.001]
        limite = 1.0
        self.assertFalse(verificar_alerta(lista, limite))

    def test_alerta_primeira_execucao(self):
        lista = [1.0]
        limite = 1.0
        self.assertFalse(verificar_alerta(lista, limite))

if __name__ == "__main__":
    unittest.main()
