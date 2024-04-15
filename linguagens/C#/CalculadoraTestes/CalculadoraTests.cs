/*using Calculadora.Services;
namespace CalculadoraTestes;

public class CalculadoraTests
{
    private CalculadoraImp _calc;

    public CalculadoraTests()
    {
        _calc = new CalculadoraImp();
    }
    
    [Fact]
    public void DeveSomar5Com10ERetornar15()
    {
    //Arrange :montar cenário
    int num1 = 5;
    int num2 = 10;
    //Act :chamar executar
    int resultado = _calc.Somar(num1, num2);
    //Assert :validar resultado esperado
    Assert.Equal(15, resultado);
    }
    
    [Fact]
    public void DeveSomar10Com10ERetornar20()
    {
        //Arrange :montar cenário
        int num1 = 10;
        int num2 = 10;
        //Act :chamar executar
        int resultado = _calc.Somar(num1, num2);
        //Assert :validar resultado esperado soma> .Equal
        Assert.Equal(20, resultado);
    }

    [Fact]
    public void Numero4EhParERetornarVerdadeiro()
    {
        //arrange
        int numeros = 4;
        //Act
        bool resultado = _calc.EhPar(numeros);
        //Assert bool> .True
        Assert.True(resultado);
    }
    // 2, 4, 6, 8, 10
    [Theory]
    [InlineData(new int[] {2, 4})]
    [InlineData(new int[] {6, 8, 10})]
    public void DeveVerificarSeOsNumerosSaoParesEVerdadeiro(int[] numeros)
    {

        //Act //Assert
        //exemplo: foreach (var item in num){
        //Assert.True(_calc.EhPar(item) }
        Assert.All(numeros, x => Assert.True(_calc.EhPar(x)));
    }
}

*/