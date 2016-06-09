from django.db import models


class Componentes(models.Model):
    TiPO_COMPONENTE_COMBO = (
        ("H", "Hamburger"),
        ("Be", "Bebida"),
        ("A", "Acompanhamento"),
        ("Br", "Brinde"),
    )    

    nome = models.CharField(max_length=20)
    tipo = models.CharField(max_length=15, choices=TiPO_COMPONENTE_COMBO, default="H")

    def __str__(self):
        return self.nome


class Combo(models.Model):
    COM_SUCO = "Combo com Suco"
    COM_REFRI = "Combo com Refrigerante"
    SUCO_BATATA = "Combo com Suco e batata"
    REFRI_BATATA = "Combo com Refrigerante e batata"
    SUCO_BATATA_BRINDE = "Combo com Suco, batata e brinde"
    REFRI_BATATA_BRINDE = "Combo com Refrigerante, batata e brinde"

    NOME_COMBO = (
        (COM_REFRI, "Simples com refrigerante"),
        (COM_SUCO, "Simples com suco"),
        (SUCO_BATATA, "Completo com suco"),
        (REFRI_BATATA, "Completo com refrigerante"),
        (SUCO_BATATA_BRINDE, "Completo com suco e brinde"),
        (REFRI_BATATA_BRINDE, "Completo com refrigerante e brinde"),
    )    

    nome = models.CharField(max_length=50, choices=NOME_COMBO, default=COM_REFRI)
    componentes = models.ManyToManyField(Componentes)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=20, default="Cliente");
    combo = models.ForeignKey(Combo)
