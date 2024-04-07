import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
from myCripto_Monitor import monitorar_criptomoeda, criar_tabela, main

class TestMyCriptoMonitor(unittest.TestCase):

    @patch('myCripto_Monitor.loop')
    @patch('myCripto_Monitor.locale.currency')
    @patch('myCripto_Monitor.calc_porc')
    def test_monitorar_criptomoeda(self, mock_calc_porc, mock_currency, mock_loop):
        # Configurando mocks
        mock_loop.return_value = 100  # Simula valores retornados pela função loop
        mock_currency.return_value = "R$100,00"  # Simula o valor retornado pela função locale.currency
        mock_calc_porc.return_value = "10%"  # Simula o valor retornado pela função calc_porc

        # Testando monitorar_criptomoeda
        valor, porcentagem, estilo = monitorar_criptomoeda('btc', [1.00])
        self.assertEqual(valor, "R$100,00")
        self.assertEqual(porcentagem, "10%")
        self.assertEqual(estilo, "green")

    def test_criar_tabela(self):
        # Testando criar_tabela
        tabela = criar_tabela()
        self.assertEqual(len(tabela.columns), 5)
        self.assertEqual(tabela.columns[0].name, "Criptomoeda")
        self.assertEqual(tabela.columns[1].name, "Valor")
        self.assertEqual(tabela.columns[2].name, "Data/Hora")
        self.assertEqual(tabela.columns[3].name, "Status")
        self.assertEqual(tabela.columns[4].name, "Porcentagem")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('time.sleep', side_effect=KeyboardInterrupt)
    def test_main(self, mock_sleep, mock_stdout):
        # Simulando a interrupção do usuário (Ctrl+C)
        with self.assertRaises(KeyboardInterrupt):
            main()

        # Verificando se a mensagem de encerramento foi impressa
        self.assertIn("Programa encerrado pelo usuário.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
