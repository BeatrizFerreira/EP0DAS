from django import forms


class PedidoForm(forms.Form):
    COM_SUCO = "Combo com Suco"
    COM_REFRI = "Combo com Refrigerante"
    SUCO_BATATA = "Combo com Suco e batata"
    REFRI_BATATA = "Combo com Refrigerante e batata"
    SUCO_BATATA_BRINDE = "Combo com Suco, batata e brinde"
    REFRI_BATATA_BRINDE = "Combo com Refrigerante, batata e brinde"

    NOME_COMBO = (
        (COM_REFRI, "Combo simples com refrigerante"),
        (COM_SUCO, "Combo simples com suco"),
        (SUCO_BATATA, "Combo completo com suco"),
        (REFRI_BATATA, "Combo completo com refrigerante"),
        (SUCO_BATATA_BRINDE, "Combo completo com suco e brinde"),
        (REFRI_BATATA_BRINDE, "Combo completo com refrigerante e brinde"),
    )

    nome_cliente = forms.CharField(max_length=20)
    combo = forms.ChoiceField(choices=NOME_COMBO)

   
