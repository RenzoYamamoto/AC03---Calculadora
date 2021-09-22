import abc
from unittest import TestCase, main

class Calculadora(object):

    def calcular(self, valor1, valor2, operador):
        result = 0
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
       
        if(operacao != None):
            result = operacao.executar(valor1, valor2)

        return result

class OperacaoFabrica(object):

    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        if (operador == 'subtracao'):
            return Subtracao()
        if (operador == 'divisao'):
            return Divisao()
        if (operador == 'multiplicacao'):
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        if (valor2 == 0):
           return 'valor2 nao pode ser 0' 

        return valor1 / valor2


class Teste(TestCase):

    def test_soma(self):
        calculador = Calculadora()
        self.assertEqual(calculador.calcular(5,3, 'soma'), 8)
        self.assertEqual(calculador.calcular(5,-3, 'soma'), 2)
        self.assertEqual(calculador.calcular(-5,-3, 'soma'), -8)
        self.assertEqual(calculador.calcular(-5,2, 'soma'), -3)
        

    def test_multiplicacao(self):
        calculadorM = Calculadora()
        self.assertEqual(calculadorM.calcular(5,5, 'multiplicacao'), 25)
        self.assertEqual(calculadorM.calcular(5,-5, 'multiplicacao'), -25)

    def test_divisao(self):
        calculadorD = Calculadora()
        self.assertEqual(calculadorD.calcular(100,10, 'divisao'), 10)
        self.assertEqual(calculadorD.calcular(2,0, 'divisao'), 'valor2 nao pode ser 0')

    def test_subtracao(self):
        calculadorS = Calculadora()
        self.assertEqual(calculadorS.calcular(10,20, 'subtracao'), -10)
        

    def test_operadorErrado(self):
        calculadorE = Calculadora()
        self.assertEqual(calculadorE.calcular(2,4, ''), 0)

if __name__ == '__main__':

    main()
